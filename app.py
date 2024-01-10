from flask import Flask, render_template, jsonify, request
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

# # 음식점 추가 노가다
# db.restaurant.insert_one({
# 	'name':'음식점 이름',
# 	#경도
# 	'X': 12,
# 	#위도
# 	'Y': 12,
# 	# 카테고리 (한식, 중식, 일식, 양식, 아시안, 분식)
# 	# 추가 사항 있을 경우 팀원들과 공유
# 	'category' : "양식",
# 	# 배달 여부
# 	'delivery': True,
# 	# 주소
# 	'location': "음식점 주소",
# 	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
# 	'price' : 'string'
# 	# 기본 평점은 0으로 하고, 이후 코멘트의 평균을 내서 저장하는 식으로 직행 예정
# 	'rating' : 2.2,
# 	# 안필요 할 수 있음 (코멘트 테이블에서 가져온 lenth만큼 나누는 식으로 해도 될 듯함)
# 	'review_num' : 2,
# 	# 영업 시간 (아래와 같이 기업할 것)
# 	'business_hours' : "AM 00:00 ~ PM 00:00",
# 	#정기 휴무일 ('월', '월,화', 확인 안될시 '-')
# 	'closed_days' : '-',
# 	#전화번호 (string)
# 	'call' : '-'
# })

@app.route('/api/comment', methods=['POST'])
def review():
   try:
      data = request.json
      print(data['name'])
      name = data['name']
      review_num = int(data['review_num'])
      new_review_num = review_num + 1
      rating = float(data['rating'])
      comment = data['comment']
      selectedRating = float(data['selectedRating'])

      new_rating = (float(rating) * int(review_num) + float(selectedRating)) / (int(review_num) + 1)

      db.restaurant.update_one({"name": name}, {'$set': {
         'review_num': new_review_num,
         'rating': new_rating
      }})
      # 유저 닉네임 추가 해야함
      db.comment.insert_one({
         'name': name,
         'rating': selectedRating,
         'description': comment
      })
      return jsonify({'result': 'success'})
   except Exception as e:
      return jsonify({'result': 'failure', 'error': str(e)})

@app.route('/menu/list', methods=['GET'])
def menus_list():
   # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
   # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
   menus = list(db.menu.find({}, {'_id': False}).sort('name', -1))
   # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
   return jsonify({'result': 'success', 'menus_list': menus})

@app.route('/api/list', methods=['GET'])
def stars_list():
   # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
   # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
   restaurant = list(db.restaurant.find({}, {'_id': False}).sort('name', -1))
   # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
   return jsonify({'result': 'success', 'restaurant': restaurant})


#종류 별로 하나씩


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)