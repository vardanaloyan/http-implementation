from flask import Flask, request

app = Flask(__name__)


@app.route('/test/', endpoint='test', methods=["POST", "GET"])
def test(other=None):
    if request.endpoint == 'test':
        msg = 'Your Data here'
    else:
        msg = 'called ' + request.endpoint + ' method --> ' + str(type(other))
    return msg


app.run()
