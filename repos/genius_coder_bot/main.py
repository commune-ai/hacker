
import flask
from genius_coder_bot import GeniusCoderBot

app = flask.Flask(__name__)
bot = GeniusCoderBot()

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Genius Coder Bot!"

@app.route('/code_assist', methods=['POST'])
def code_assist():
    data = flask.request.json
    code = data.get('code', '')
    language = data.get('language', 'python')
    
    result = bot.process_code(code, language)
    
    return flask.jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
