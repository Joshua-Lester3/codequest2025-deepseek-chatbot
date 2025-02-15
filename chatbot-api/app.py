from flask import Flask, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/chat")
def chat():
  isLlama = str(request.args.get('isLlama', 'true')).lower() == 'true'
  message = request.args.get('message', 'hi')
  model = "llama3" if isLlama else "deepseek-r1:1.5b"
  cmd = ["ollama", "run", model, message]
  try:
    response = subprocess.check_output(cmd, text=True)
    return response
  except subprocess.CalledProcessError as e:
    return f"Command failed with return code {e.returncode}"


if __name__ == '__main__':
  app.run()