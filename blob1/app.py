from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS extension
import backend

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/fetch_web_address', methods=['GET'])
def api_fetch_web_address():
    try:
        button_name = request.args.get('button_name')
        web_address = backend.fetch_web_address(button_name)
        return jsonify({'web_address': web_address})
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
