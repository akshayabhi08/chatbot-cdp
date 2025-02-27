from flask import Flask, request, jsonify, render_template
from nlp.processor import process_question
from indexer.search import search_docs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    intent, cdp = process_question(user_question)  # NLP processing
    response = search_docs(intent, cdp)           # Search documentation
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)