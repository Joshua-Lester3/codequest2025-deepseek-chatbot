from flask import Flask, request
from flask_cors import CORS
import subprocess
import requests


app = Flask(__name__)
CORS(app)

# @app.route("/chat")
# def chat():
#   isLlama = str(request.args.get('isLlama', 'true')).lower() == 'true'
#   message = request.args.get('message', 'hi')
#   model = "llama3" if isLlama else "deepseek-r1:1.5b"
#   cmd = ["ollama", "run", model, message]
#   try:
#     response = subprocess.check_output(cmd, text=True)
#     return response
#   except subprocess.CalledProcessError as e:
#     return f"Command failed with return code {e.returncode}"

@app.route("/chat")
def chat():
  isLlama = str(request.args.get('isLlama', 'true')).lower() == 'true'
  message = request.args.get('message', 'hi')
  model = "llama3" if isLlama else "deepseek-r1:1.5b"
  try:
    url = "http://ollama:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {"model": model, "prompt": message, "stream": False}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()["response"]
    return result
  except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
    print(f"Response content:", response.text)

@app.route("/hi")
def hi():
  return 'hi'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)