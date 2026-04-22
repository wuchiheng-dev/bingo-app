from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# ===== 模擬開獎 =====
def draw_numbers():
    return sorted(random.sample(range(1, 81), 20))

# ===== 一鍵選號 =====
@app.route("/pick", methods=["POST"])
def pick():
    count = int(request.json["count"])
    nums = sorted(random.sample(range(1, 81), count))
    return jsonify(nums)

# ===== 模擬開獎 =====
@app.route("/draw", methods=["POST"])
def draw():
    user_nums = request.json["nums"]
    draw = draw_numbers()

    hits = len(set(user_nums) & set(draw))

    return jsonify({
        "draw": draw,
        "hits": hits
    })

# ===== 主頁 =====
@app.route("/")
def index():
    return render_template("index.html")

# ===== PWA manifest =====
@app.route("/manifest.json")
def manifest():
    return app.send_static_file("manifest.json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)