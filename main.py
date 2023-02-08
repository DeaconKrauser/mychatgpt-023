from flask import Flask, request, render_template
from dotenv import load_dotenv
import openai, os

load_dotenv()

key_ = os.getenv('KEY_')
print('TESTEEEEEEE:', key_)
app = Flask(__name__)
openai.api_key = key_

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    prompt = request.form['prompt']
    payload = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return payload['choices'][0]['text']

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080
    )