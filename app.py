from flask import Flask, request

app = Flask(__name__)

tasks = ["Learn DevOps", "Deploy on Cloud"]

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
        </style>
    </head>
    <body>
        <h1>🚀 DevOps Pipeline Live</h1>
        <div class="box">
            <p>✅ Flask App Running</p>
            <p>✅ Docker Containerized</p>
            <p>✅ CI/CD Enabled</p>
            <p>☁️ Deployed on AWS EC2</p>
        </div>
        <p style="margin-top:20px;">Try: /tasks</p>
    </body>
    </html>
    """