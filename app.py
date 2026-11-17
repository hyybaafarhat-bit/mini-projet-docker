from flask import Flask
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Mon application Docker")
ENVIRONMENT = os.getenv("ENVIRONMENT", "Development")

@app.route("/")
def home():
    return f"""
    <h1>Bienvenue dans {APP_NAME}</h1>
    <p>Application déployée avec Docker !</p>
    <p>Environnement : {ENVIRONMENT}</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# v1.0.1
