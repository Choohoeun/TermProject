from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask import Flask, request, render_template_string

# Flask 애플리케이션
app = Flask(__name__)

# T5 모델 로드
model_name = "paust/pko-t5-base"  # T5 기반 한국어 모델
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text: str) -> str:
    input_text = f"summarize: {text}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    outputs = model.generate(
        inputs.input_ids,
        max_length=100,
        min_length=30,
        do_sample=True,
        temperature=0.9,
        top_p=0.85,
        top_k=50,
        early_stopping=True,
        no_repeat_ngram_size=4,
    )
    
    summarized_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    summarized_text = remove_redundant_phrases(summarized_text)

    return summarized_text

def remove_redundant_phrases(text: str) -> str:
    words = text.split()
    unique_words = []
    for word in words:
        if len(unique_words) == 0 or word != unique_words[-1]:
            unique_words.append(word)
    final_text = ' '.join(unique_words)
    seen_phrases = set()
    result_words = []
    for word in final_text.split():
        if word not in seen_phrases:
            seen_phrases.add(word)
            result_words.append(word)
    return ' '.join(result_words)

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
            output_text = summarize_text(input_text)
    return render_template_string(HTML_TEMPLATE, output_text=output_text)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
