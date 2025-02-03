from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aqidah')
def aqidah():
    return render_template('aqidah.html')

@app.route('/matematika')
def matematika():
    return render_template('matematika.html')

@app.route('/sosiologi')
def sosiologi():
    return render_template('sosiologi.html')

if __name__ == '__main__':
    app.run(debug=True)
