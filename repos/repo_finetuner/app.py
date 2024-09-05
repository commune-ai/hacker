
from flask import Flask, render_template, request, jsonify
from finetuner import Finetuner

app = Flask(__name__)
finetuner = Finetuner()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/finetune', methods=['POST'])
def finetune():
    model_name = request.form['model_name']
    data_path = request.form['data_path']
    
    task = finetuner.start_finetuning(model_name, data_path)
    return jsonify({"task_id": task.id})

@app.route('/status/<task_id>')
def status(task_id):
    task = finetuner.get_task(task_id)
    return jsonify({"status": task.status, "progress": task.progress})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
