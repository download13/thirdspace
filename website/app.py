from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/findaspace', methods = ['GET'])
def findaspace():
	return render_template('findaspace.html')

if __name__ == '__main__':
    app.run(debug = True)
