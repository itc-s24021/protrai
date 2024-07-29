#s24021
#

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/himitsu')
def himitsu():
    return "<small>秘密のメッセージ</small>"
@app.route('/msg')
def msg():
    return render_template('msg.html')
@app.route('/submit', methods=['POST'])
def submit():
    content = request.form['content']
    with open('data.txt', 'a') as file:
        file.write(f"\n{datetime.datetime.now()}\n{content}\n")
        return f"書き込みました"
            
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
