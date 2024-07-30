from flask import Flask, redirect, url_for, render_template, request, make_response, jsonify
import json
import os
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
flag = r"flag{idor}"


BLOG_FILE = 'blog_posts.json'
DEFAULT_POSTS = [
    {"title": "延邊刺客", "content": """我個人認為
義大利麵就應該拌 42 號混泥土
因為這個螺絲釘的長度很容易直接影響到挖掘機的扭矩

你往裡砸的時候
一瞬間他就會產生大量的高能蛋白
俗稱 UFO，會嚴重影響經濟的發展
以至於對整個太平洋和充電器的核污染

再或者說
透過這勾股定理
很容易推斷出人工飼養的東條英機
他是可以捕獲野生的三角函數

所以說
不管這秦始皇的切面是否具有放射性
川普的 N 次方是否有沈澱物
都不會影響到沃爾瑪跟維爾康在南極匯合

你往裡砸的時候
一瞬間他就會產生大量的高能蛋白
俗稱 UFO，會嚴重影響經濟的發展
以至於對整個太平洋和充電器的核污染

再或者說
透過這勾股定理
很容易推斷出人工飼養的東條英機
他是可以捕獲野生的三角函數"""},
    {"title": "☝️ 😐👇", "content": "雨停滯天空之間 ☝️ 😐👇 像淚在眼眶盤旋👇😐☝️ 這也許是最後一 ✋ 🤚 😐 次見面😐 ✋ 🤚"},
    {"title": "夜店", "content": "我第一次去夜店唯一一次，只進去了3分鐘，我是被同學綁去的 ，剛進去就受不了，那裡沒有書，沒有考卷，沒有老師，太吵雜了，並不適合我，我只想好好學習，考取功名，報效國家！"}
]

def load_posts():
    if os.path.exists(BLOG_FILE):
        with open(BLOG_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_POSTS

def save_posts(posts):
    with open(BLOG_FILE, 'w') as f:
        json.dump(posts, f)


def clear_posts():
    while True:
        time.sleep(300)  # 每分鐘執行一次
        save_posts(DEFAULT_POSTS)
        print("===clear posts===")

# 啟動清理文章的背景任務
threading.Thread(target=clear_posts, daemon=True).start()


@app.route('/')
def index():
    posts = load_posts()
    role = request.cookies.get('role')
    resp = make_response(render_template('index.html', posts=posts, role=role))
    if not request.cookies.get('role'):
        resp.set_cookie(key='role',value= 'guest')
    return resp

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    role = request.cookies.get('role')
    if role == 'admin' :
        if request.headers.get('X-Forwarded-For') =='localhost' or request.headers.get('X-Forwarded-For') == '127.0.0.1' :
            if request.method == 'POST':
                title = request.form['title']
                content = request.form['content']
                if title and content:
                    posts = load_posts()
                    posts.append({"title": title, "content": content})
                    save_posts(posts)
                    print(posts)
                    return redirect(url_for('index'))
            posts = load_posts()
            return render_template('admin.html', posts=posts, role=role,flag=flag)

    return "無權限訪問或非本地訪問" 


if __name__ == "__main__":
    save_posts(DEFAULT_POSTS)
    app.run(debug=False,host="0.0.0.0",port=80)