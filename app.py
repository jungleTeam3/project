from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/render')
def render():
   return render_template('main.html')

@app.route('/update_content')
def update_content():
   # 실제로는 여기에서 필요한 데이터를 가공하여 반환
   new_content = '<p>Updated content from the server!</p>'
   return new_content

@app.route('/map')
def map():
   return render_template('test.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)