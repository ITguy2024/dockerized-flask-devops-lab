from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Lab</h1>
    <h2>Dockerized Flask Application</h2>
    <p>Deployed successfully by Joseph Nicolas.</p>
    <p>Environment: Ubuntu Server + Docker</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
