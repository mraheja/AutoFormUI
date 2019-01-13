from flask import *
app = Flask(__name__)
import requests

@app.route('/setup',methods = ['POST'])
def login():
	x = requests.get(request.form['link']).text
	return x

if __name__ == '__main__':
   app.run(debug = True)