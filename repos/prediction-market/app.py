
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prediction_market.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Float, default=100.0)

class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resolved = db.Column(db.Boolean, default=False)
    outcome = db.Column(db.Boolean, nullable=True)

class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    market_id = db.Column(db.Integer, db.ForeignKey('market.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    prediction = db.Column(db.Boolean, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    markets = Market.query.filter_by(resolved=False).all()
    return render_template('index.html', markets=markets)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form['password'])
        new_user = User(username=request.form['username'], password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/create_market', methods=['GET', 'POST'])
@login_required
def create_market():
    if request.method == 'POST':
        new_market = Market(question=request.form['question'], creator_id=current_user.id)
        db.session.add(new_market)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_market.html')

@app.route('/place_bet/<int:market_id>', methods=['GET', 'POST'])
@login_required
def place_bet(market_id):
    market = Market.query.get_or_404(market_id)
    if request.method == 'POST':
        amount = float(request.form['amount'])
        prediction = request.form['prediction'] == 'true'
        if current_user.balance >= amount:
            new_bet = Bet(user_id=current_user.id, market_id=market_id, amount=amount, prediction=prediction)
            current_user.balance -= amount
            db.session.add(new_bet)
            db.session.commit()
            flash('Bet placed successfully')
        else:
            flash('Insufficient balance')
    return render_template('place_bet.html', market=market)

@app.route('/resolve_market/<int:market_id>', methods=['GET', 'POST'])
@login_required
def resolve_market(market_id):
    market = Market.query.get_or_404(market_id)
    if request.method == 'POST':
        outcome = request.form['outcome'] == 'true'
        market.resolved = True
        market.outcome = outcome
        bets = Bet.query.filter_by(market_id=market_id).all()
        for bet in bets:
            if bet.prediction == outcome:
                bet.user.balance += bet.amount * 2
        db.session.commit()
        flash('Market resolved successfully')
        return redirect(url_for('index'))
    return render_template('resolve_market.html', market=market)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)
