# app.py
from flask import Flask, request, render_template_string
from main import summarize_text  # 요약 모듈 불러오기

# Flask 애플리케이션 설정
app = Flask(__name__)

# 웹 페이지 템플릿
HTML_TEMPLATE = """
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>T5 기반 한글 텍스트 요약 프로그램</title>
  </head>
  <body>
    <h1>T5 기반 한글 텍스트 요약 프로그램</h1>
    <form method="POST">
      <textarea name="input_text" rows="10" cols="50" placeholder="문서를 입력하세요..."></textarea><br>
      <input type="submit" value="요약하기">
    </form>
    {% if output_text %}
      <h2>요약된 문장:</h2>
      <p>{{ output_text }}</p>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    output_text = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        if input_text:
            output_text = summarize_text(input_text)  # 요약 모듈 사용
    return render_template_string(HTML_TEMPLATE, output_text=output_text)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
