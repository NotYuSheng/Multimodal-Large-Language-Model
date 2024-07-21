from flask import Flask, request, jsonify
import requests
import json
import datetime
import logging

app = Flask(__name__)
OLLAMA_SERVER_URL = "http://127.0.0.1:11434/api/generate"

# Configure logging to log to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("server.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def log_conversation(data):
    with open('conversation_log.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')

@app.route('/api/generate', methods=['POST'])
def generate():
    # Extract the incoming payload
    user_payload = request.json

    # Log the incoming request payload
    logger.info(f"Received request: {user_payload}")

    # Log the incoming request to the conversation log
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

        # Log the response from the Ollama server
        logger.info(f"Response from Ollama server: {ollama_response}")
    except requests.RequestException as e:
        error_message = {'error': str(e)}
        logger.error(f"Error occurred: {error_message}")
        return jsonify(error_message), 500

    # Log the response to the conversation log
    log_conversation({
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'response': ollama_response
    })

    # Return the response to the client
    return jsonify(ollama_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
