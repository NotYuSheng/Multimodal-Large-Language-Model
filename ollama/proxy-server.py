from flask import Flask, request, jsonify
import requests
import json
import datetime

app = Flask(__name__)
OLLAMA_SERVER_URL = "http://127.0.0.1:11434/api/generate"

def log_conversation(data):
    with open('conversation_log.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')

@app.route('/api/generate', methods=['POST'])
def generate():
    # Extract the incoming payload
    user_payload = request.json

    # Print the incoming request payload
    print(f"Received request: {user_payload}")

    # Log the incoming request
    log_data = {
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'model': user_payload.get('model'),
        'prompt': user_payload.get('prompt'),
        'stream': user_payload.get('stream')
    }
    log_conversation({'request': log_data})

    # Forward the request to the Ollama server
    try:
        response = requests.post(OLLAMA_SERVER_URL, json=user_payload)
        ollama_response = response.json()

        # Print the response from the Ollama server
        print(f"Response from Ollama server: {ollama_response}")
    except requests.RequestException as e:
        error_message = {'error': str(e)}
        print(f"Error occurred: {error_message}")
        return jsonify(error_message), 500

    # Log the response from the Ollama server
    log_conversation({
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'response': ollama_response
    })

    # Return the response to the client
    return jsonify(ollama_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
