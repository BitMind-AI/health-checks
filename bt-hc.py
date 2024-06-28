import argparse

import bittensor as bt
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    try:
        if bt.__version__: 
            return jsonify({"status": "success", "detail": "Bittensor is operational"}), 200
        else:
            return jsonify({"status": "failure", "detail": "Bittensor operation failed"}), 500
    except Exception as e:
        return jsonify({"status": "error", "detail": str(e)}), 500

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Bittensor Health Check Service')
    parser.add_argument('--port', type=int, default=8000, help='Port number for the Flask application')
    args = parser.parse_args()
    
    app.run(host='0.0.0.0', port=args.port)