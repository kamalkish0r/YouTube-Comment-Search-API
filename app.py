from flask import Flask, jsonify, request
import requests
from datetime import datetime

app = Flask(__name__)

yltic_url = 'https://app.ylytic.com/ylytic/test'

@app.route('/', methods=['GET'])
def home():
    return "To filter comments use parameters like : /search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&seach_text=economic"

@app.route('/search', methods=['GET'])
def search():
    search_author = request.args.get('search_author')
    search_text = request.args.get('search_text')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')

    response = requests.get(yltic_url)
    filtered_comments = response.json().get('comments', [])

    if at_from:
        at_from_date = datetime.strptime(at_from, '%d-%m-%Y')
        filtered_comments = [
            c for c in filtered_comments 
            if at_from_date <= datetime.strptime(c['at'], '%a, %d %b %Y %H:%M:%S %Z')
        ]
    
    if at_to:
        at_to_date = datetime.strptime(at_to, '%d-%m-%Y')
        filtered_comments = [
            c for c in filtered_comments 
            if datetime.strptime(c['at'], '%a, %d %b %Y %H:%M:%S %Z') <= at_to_date
        ]

    if search_author:
        filtered_comments = [c for c in filtered_comments if search_author.lower() in c['author'].lower()]

    if search_text:
        filtered_comments = [c for c in filtered_comments if search_text.lower() in c['text'].lower()]

    if reply_from:
        filtered_comments = [c for c in filtered_comments if c['reply'] >= int(reply_from)]

    if reply_to:
        filtered_comments = [c for c in filtered_comments if c['reply'] <= int(reply_to)]

    if like_from:
        filtered_comments = [c for c in filtered_comments if c['like'] >= int(like_from)]

    if like_to:
        filtered_comments = [c for c in filtered_comments if c['like'] <= int(like_to)]

    return jsonify(filtered_comments)

if __name__ == '__main__':
    app.run(debug=False)
