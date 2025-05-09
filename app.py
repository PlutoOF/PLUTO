from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query_model():
    # Get the user's input from the POST request
    user_input = request.json.get("input", "")

    # Call Ollama CLI to run LLaMA 3 with the user input
    result = subprocess.run(
        ["ollama", "run", "llama3", user_input],
        capture_output=True,
        text=True
    )

    # The model's output is in result.stdout
    return jsonify({"response": result.stdout.strip()})

if __name__ == "__main__":
    app.run(debug=True)





