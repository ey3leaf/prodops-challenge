from flask import Flask, jsonify
from boto3 import resource

app = Flask(__name__)
codename = 'thedoctor'
github_path = 'https://github.com/ey3leaf/prodops-challenge'
container_path = 'https://cloud.docker.com/repository/docker/canichangeit/flask-app'


@app.route('/')
def root_page():
    return 'It\'s Alive!'


@app.route('/secret')
def secret():
    return jsonify(get_secret())


@app.route('/health')
def health():
    res = {'status': 'healthy', 'project': github_path, 'container': container_path}
    return jsonify(res)


def get_secret():
    # Credentials and region are taken from environment variables
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('devops-challenge')
    response = table.get_item(Key={
        'code_name': codename
    })
    return response['Item']


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')