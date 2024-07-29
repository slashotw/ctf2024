from flask import Flask, redirect, url_for, render_template,request,flash,session,render_template_string
import markdown
import random

app = Flask(__name__)
app.config['SECRET_KEY']= 'meowmeow'
@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read())

@app.route('/render', methods=['POST'])
def render():
    markdown_text = request.json['markdown']
    print(markdown_text)
    html = markdown.markdown(markdown_text)
    print(html)
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)