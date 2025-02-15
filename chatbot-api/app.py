from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/chat/<message>")
def chat(message):
  cmd = ["ollama", "run", "deepseek-r1:1.5b", message]
  try:
    response = subprocess.check_output(cmd, text=True)
    return response
  except subprocess.CalledProcessError as e:
    return f"Command failed with return code {e.returncode}"


if __name__ == '__main__':
  app.run()