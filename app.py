from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/photos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

START_DATE = datetime(2025, 11, 5)
ANNIVERSARIES = [100, 300, 500, 1000]

@app.route("/", methods=['GET', 'POST'])
def index():
    # 上傳照片
    if request.method == 'POST':
        file = request.files['photo']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
        return redirect(url_for('index'))

    # 計算天數
    today = datetime.now()
    diff = (today - START_DATE).days + 1

    # 紀念日判斷
    is_anniversary = diff in ANNIVERSARIES

    # 取得照片清單
    photos = os.listdir(UPLOAD_FOLDER)

    return render_template("index.html",
                           days=diff,
                           is_anniversary=is_anniversary,
                           anniversary_day=diff,
                           photos=photos)

if __name__ == "__main__":
    app.run(debug=True)