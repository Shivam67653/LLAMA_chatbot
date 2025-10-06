from flask_cors import CORS
from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    print(f">>> USER: {user_input}")
    
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", user_input],
            capture_output=True,
            text=True,
            timeout=120
        )
        print(">>> OLLAMA STDOUT:", result.stdout)   # Output from model
        print(">>> OLLAMA STDERR:", result.stderr)   # Error, if any

        response = result.stdout.strip()
        if not response:
            response = "⚠️ No response received from model."

        print(f"Sending response to frontend: {response}")
        return jsonify({"response": response})
    except Exception as e:
        print(">>> ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
