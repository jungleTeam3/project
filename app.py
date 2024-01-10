from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['team_3']
collection = db['restaurant']  # 컬렉션 이름을 정확히 맞춥니다.

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/map')
def map():
   return render_template('test.html')

@app.route('/layout')
def layout():
   return render_template('layout.html')

@app.route('/api/list', methods=['GET'])
def stars_list():
   # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
   # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
   stars = list(db.restaurant.find({}, {'_id': False}).sort('name', -1))
   # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
   return jsonify({'result': 'success', 'stars_list': stars})


#종류 별로 하나씩


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)