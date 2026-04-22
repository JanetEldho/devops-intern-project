from flask import Flask

app = Flask(__name__)

tasks = ["Learn DevOps", "Build Project"]

@app.route('/')
def home():
    return "Hello, DevOps Journey!"

@app.route('/tasks')
def get_tasks():
    return {"tasks": tasks}

if __name__ == '__main__':
    app.run(debug=True)