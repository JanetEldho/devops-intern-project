from flask import Flask, request

app = Flask(__name__)

tasks = ["Learn DevOps", "Deploy on Cloud"]

@app.route('/')
def home():
    return {"message": "DevOps Project Running"}

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return {"tasks": tasks}

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = data.get("task")
    tasks.append(task)
    return {"message": "Task added", "tasks": tasks}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)