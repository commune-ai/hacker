
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import User, Item
from app.forms import RegistrationForm, LoginForm, ItemForm

@app.route('/')
@app.route('/index')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Add login logic here
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, description=form.description.data, price=form.price.data)
        db.session.add(item)
        db.session.commit()
        flash('Item added successfully!')
        return redirect(url_for('index'))
    return render_template('add_item.html', title='Add Item', form=form)
