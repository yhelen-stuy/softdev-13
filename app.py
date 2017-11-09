from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=H3ydsKtlvNEegALq3daoUIZL5V7QAtOv6K1RALaO')

    d = json.loads(data.read())

    return render_template('index.html',
                           name=d['title'],
                           src=d['url'],
                           hd_src=d['hdurl'],
                           info=d['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
