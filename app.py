from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task list
tasks = ["Learn DevOps", "Deploy on Cloud"]

# ----------------------------
# Home Route (UI)
# ----------------------------
@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>DevOps Project</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: #0f172a;
                color: white;
                padding: 50px;
            }
            h1 { color: #38bdf8; }
            .box {
                background: #1e293b;
                padding: 20px;
                border-radius: 10px;
                display: inline-block;
                margin-top: 20px;
            }
            .endpoint {
                margin-top: 15px;
                color: #94a3b8;
            }
        </style>
    </head>
    <body>
        <h1>🚀 DevOps Pipeline Live</h1>
        <div class="box">
            <p>✅ new project</p>
            <p>✅ Docker Containerized</p>
            <p>✅ CI/CD Enabled</p>
            <p>☁️ Deployed on AWS EC2</p>
        </div>

        <div class="endpoint">
            <p>📌 Try endpoints:</p>
            <p>/tasks (GET)</p>
            <p>/tasks (POST)</p>
        </div>
    </body>
    </html>
    """

# ----------------------------
# Get all tasks
# ----------------------------
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# ----------------------------
# Add a task
# ----------------------------
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get("task")

    if task:
        tasks.append(task)
        return jsonify({"message": "Task added", "tasks": tasks})
    else:
        return jsonify({"error": "No task provided"}), 400

# ----------------------------
# Health Check (DevOps useful)
# ----------------------------
@app.route('/health')
def health():
    return jsonify({"status": "running"})

# ----------------------------
# START APP (CRITICAL)
# ----------------------------
if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host="0.0.0.0", port=5000)