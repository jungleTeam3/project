import os #세션에서 디렉토리 경로 호출용
from flask import Flask, render_template, request, jsonify, make_response, session, redirect, url_for, flash, Response
#버전이 많아서 이것도 받았는데 안 쓰게된듯..?
# #jwt 토큰 발급용
# import jwt 
#암호 만들기 위한 함수용
import hashlib
#만료 시간 설정하기 위해 임포트.
from datetime import datetime, timedelta
#CORS 에러 방ㅣ용
from flask_cors import CORS
from functools import wraps

from flask_login import login_required

from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
app = Flask(__name__)
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError





app = Flask(__name__)

CORS(app)
app.config['SECRET_KEY'] = 'dsfdsafdsafdsafdsagdsdgdsafasdf'
SECRET_KEY = "dsfdsafdsafdsafdsagdsdgdsafasdf"
# 토큰 생성에 사용될 Secret Key를 flask 환경 변수에 등록
# app.config.update(
# 			DEBUG = True,
# 			JWT_SECRET_KEY = "I'M IML"
# 		)

# JWT 확장 모듈을 flask 어플리케이션에 등록, 이것도 안쓰게 된듯..
jwt = JWTManager(app)

import requests

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.team_3
restaurant = db['restaurant']
user = db['user']

# token을 decode하여 반환함, decode에 실패하는 경우 payload = None으로 반환
@jwt_required()
def check_access_token(access_token):
    try:
        payload = get_jwt_identity()
      #   payload = jwt.decode(access_token, app.config['SECRET_KEY'], algorithm= ["HS256"])
      #   if payload['exp'] < datetime.utcnow():  # 토큰이 만료된 경우
      #       payload = None
    except InvalidTokenError:
        payload = None
    
    return payload

# decorator 함수
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwagrs):
        access_token = request.headers.get('Authorization') # 요청의 토큰 정보를 받아옴
        if access_token is not None: # 토큰이 있는 경우
            payload = check_access_token(access_token) # 토큰 유효성 확인
            if payload is None: # 토큰 decode 실패 시 401 반환
                return Response(status=401)
        else: # 토큰이 없는 경우 401 반환
            return Response(status=402)

        return f(*args, **kwagrs)

    return decorated_function

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/api/comment', methods=['POST'])
@login_required
def review():
   if 'id_give' in session:
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
            'comment': comment
         })
         return jsonify({'result': 'success'})
      except Exception as e:
         return jsonify({'result': 'failure', 'error': str(e)})
   else:
      flash("로그인이 필요합니다!")
      return render_template('index.html')

@app.route('/api/comment/list', methods=['GET'])
def comment_list():
   # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
   # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
   comment = list(db.comment.find({}, {'_id': False}).sort('name', -1))
   # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
   return jsonify({'result': 'success', 'comment': comment})

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



# API #2 : 계정을 생성합니다.
@app.route('/register', methods = ['POST', 'GET'])
def register():
   if request.method == 'POST' :
      #받은 값으로 닉네임, 아이디, 패스워드, 이메일 설정
      nickname_receive = request.form['nickname_give']
      id_receive =request.form['id_give']
      password_receive = request.form['password_give']
      email_receive = request.form['email_give']
      # 패스워드 암호화. sha256방법으로 단방향 암호화.
      pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
      # 받은 값들은 session으로 세션 형태로 저장되는데, 객체 DB로 접근시 암호화되어 보임(실제 값이 암호화된건 아님).
      # 추가로 암호화시키는 함수를 더할 수는 있음. 대조할때도 암호화값과 대조하면 됨.
      session['password_give'] = pw_hash
      session['email_give'] = email_receive
      session['id_give'] = id_receive
      session['nickname_give'] = nickname_receive
      # db에 account 형식으로 추가.
      account = {'ID' : id_receive, 'password' : pw_hash, 'email' : email_receive, 'nickname' : nickname_receive}
      db.user.insert_one(account)
       # 쿠키로 저장해두는 과정. 세션은 서버 메모리에, 쿠키는 클라이언트 PC에 생성됨. 
      #근데 사실 session으로 호출해도 되기때문에 필요하진 않는데, 실제 서비스라면 둘을 분담하긴 해야할 것. 세션만 쓰면 서버에 부하가 가니까.
      resp = make_response(jsonify({'result' :'success'}))
      resp.set_cookie('password',pw_hash)
      resp.set_cookie('email', email_receive)
      resp.set_cookie('ID', id_receive)

      return resp
   else :
      return render_template('register.html')


# API #3 : 로그인 페이지를 띄우고 결과를 반환합니다.
@app.route('/login', methods = ['POST', 'GET'])
def login():
   # POST 요청시 로그인 여부 확인하기.
   if request.method == 'POST':
      id = request.form['id_give']
      pw = request.form['password_give']
      #비밀번호를 똑같은 방식으로 암호화.
      pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
      #아이디와 비밀번호를 가지고 해당 유저를 db에서 탐색.
      result = db.user.find_one({'ID' : id, 'password' : pw_hash})
      #값이 실제로 있다면 JWT 토큰을 발급하기.
      if result is not None:
         #JWT토큰에는 payload와 시크릿키 필요. 시크릿키로 토큰을 디코딩하여 payload값 확인. exp항목으로 만료 시간, jwt토큰을 풀면 유저아이디 확인가능.
         # payload = {'id' : id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)}
         # token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
         # expires = datetime.utcnow() + timedelta(days=1)
         token = create_access_token(identity='id', expires_delta=timedelta(days=1))
      #세션을 생성하며, html에서 {session['id']} 등으로 호출 가능.
         session['id_give'] = id
         session['password_give'] = pw
         #유저 아이디도 반환하기... 
         return jsonify({'result': 'success', 'token' : token, '': id })
      else:
         return jsonify({'result':'fail'})
   #GET 요청만 받았을때 로그인 페이지 띄우기.
   else:
      return render_template('login.html')


# API #7 : 로그아웃을 합니다
@app.route('/logout')
def logout():
   #저장되어있는 세션 제거.
   session.clear()
   #메인 페이지로 리다이렉트.
   return render_template('index.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)