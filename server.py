from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello2'

@app.route('/post', methods=['POST'])
def post():
    messages = []
    messages.append('Got POST!')
    if request.json.get('type'):
        messages.append(request.json['type'])
        if request.json['type'] == 'wall_post_new':
            messages.append('New post!')
            res = requests.post(
                f"https://api.telegram.org/bot6646276001:AAH4q6HZM2n_-m4mscDBgEuVhIBhYTiMJBw/sendMessage?chat_id=159529075&text={request.json['text']}",
            )
            messages.append(f'Response status: {res.status_code}')
    messages.append(json.dumps(request.json))

    response = Response('\n'.join(messages))
    response.headers['Content-Type'] = 'text/plain'
    return response