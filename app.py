from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f'Unhandled Exception: {str(e)}')
    return jsonify({'error': str(e)}), 500

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided for analysis'}), 400
    # Placeholder for analysis logic
    result = {'text': data['text'], 'sentiment': 'neutral'}  # Replace with actual analysis logic
    return jsonify(result)

@app.route('/analyze/batch', methods=['POST'])
def analyze_batch():
    data = request.get_json()
    if 'texts' not in data:
        return jsonify({'error': 'No texts provided for batch analysis'}), 400
    results = []
    for text in data['texts']:
        # Placeholder for analysis logic
        result = {'text': text, 'sentiment': 'neutral'}  # Replace with actual analysis logic
        results.append(result)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
