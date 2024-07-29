from flask import Flask, render_template, request, jsonify , send_from_directory
import json

app = Flask(__name__)

articles = [
    {"id": 1, "title": "選舉的最大秘密", "content": "票多的贏票少的輸！"},
    {"id": 2, "title": "鮭魚", "content": "我愛吃鮭魚:D"},
    {"id": 3, "title": "php", "content": "php是世界上最棒的語言！ 沒有之一！"}
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/my_secret_flag_page', methods=['GET', 'POST'])
def secret_flag():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        with open('secret.json') as f:
            secrets = json.load(f)
        
        if username in secrets and secrets[username] == password:
            with open('flag') as f:
                flag = f.read().strip()
            return render_template('login.html', flag=flag)
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

@app.route('/robots.txt')
def robotstxt():
    return "User-agent: *\nDisallow: /my_secret_flag_page"

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)