from flask import Flask, request, jsonify
from chatbot import get_chatbot_response
from flask_cors import CORS

app = Flask(__name__)
cors=CORS(app, origins='*')  # This will enable CORS for all routes

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('input')
    response = get_chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
