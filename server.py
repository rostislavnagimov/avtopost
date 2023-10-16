from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Server is running'

@app.route('/post', methods=['POST'])
def post():
    if request.json.get('type'):
        if request.json['type'] == 'wall_post_new':
            requests.post(
                f"https://api.telegram.org/bot6646276001:AAH4q6HZM2n_-m4mscDBgEuVhIBhYTiMJBw/sendMessage?chat_id=159529075&text={request.json['object']['text']}",
            )

            return 'ok', 200

        if request.json['type'] == 'confirmation':
            return '92a043a8'

    return 'Invalid data'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)