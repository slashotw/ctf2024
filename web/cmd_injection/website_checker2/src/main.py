import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "very_secret_key_for_ctf_challenge"

def ping_url(url):
    command = f"ping -c 4 {url}"
    result = os.popen(command)
    output = result.read()
    result.close()
    return output

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            blocklist = [" ","&",";","@","%","^","~","`","<",">",",","ls","cat","less","tail","more","whoami","pwd","echo"]
            for item in blocklist:
                if item in url:
                    return render_template('index.html',result=f"you hacker !!! dont put these inside: {blocklist}  ")
            result = ping_url(url)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)