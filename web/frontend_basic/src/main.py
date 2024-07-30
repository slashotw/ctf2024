from flask import Flask, jsonify, render_template, request, make_response
import base64

app = Flask(__name__)

FLAG1 = r"flag{call_value_in_console}"
FLAG2 = r"flag{disable_javascript}"
FLAG3 = r"flag{header}"
FLAG4 = r"flag{dev_tools_network}"
FLAG5 = r"flag{burp_suite}"
FLAG6 = r"flag{kali_linux}"

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.headers['CTF_Flag'] = FLAG3
    return response


@app.route('/form', methods=["POST", "GET"])
def form():
    if request.method == "POST":
        return FLAG2
    return render_template('form.html')

@app.route('/abc' )
def abc():
    return render_template('abc.html',flag="Flag")

@app.route('/bang1234')
def bang():
    return "dont blink ;)"

@app.route('/flag.json')
def flag_json():
    return jsonify({"flag": FLAG4})

@app.route('/api/flag')
def api_flag():
    return base64.b64encode(FLAG1.encode()).decode()

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    if request.method == 'POST':
        money = request.json.get('money', 0)
        if money >= 1000000:
            return jsonify({
                "message": f"🥳{FLAG5}🥳",
                "received": money,
                "success": True
            })
        else:
            return jsonify({
                "message": f"你只有 {money} $$ :(",
                "received": money,
                "success": False
            })
    return render_template('shop.html')

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)