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

@app.route('/yelp', methods=['GET'])
def yelp():
    s = open(".secret").read()
    data = json.loads(s)
    token = data['access_token']
    api_url = 'https://api.yelp.com/v3/businesses/search'
    query = "?location=TriBeCa&term=dirty+bird"

    req = urllib2.Request(api_url + query)
    req.add_header('Authorization', 'Bearer ' + token)
    try:
        resp = urllib2.urlopen(req)
        d = json.loads(resp.read())
        bs = d['businesses']
    except HTTPError:
        return "Gateway error :("

    return render_template('yelp.html',
            businesses=bs)

if __name__ == "__main__":
    app.debug = True
    app.run()
