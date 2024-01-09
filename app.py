from flask import Flask, render_template, request, jsonify, make_response, session, redirect, url_for
#버전이 많아서 이것도 받았는데 안 쓰게된듯..?
from flask_jwt_extended import *
#jwt 토큰 발급용
import jwt 
#암호 만들기 위한 함수용
import hashlib
#만료 시간 설정하기 위해 임포트.
import datetime
#CORS 에러 방ㅣ용
from flask_cors import CORS


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
db = client.jungleweekzero
collection = db['user']

@app.route('/')
def home():
   #세션에 아이디값이 있는지 확인, 확인시 닉네임 반영한 홈페이지 렌더링.
   if 'id_give' in session:
      nickname = session['nickname_give']
      # 닉네임을 반영한 로그인된 페이지 렌더링 리턴 필요
   else:
      return render_template('index.html')

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
      resp = make_response(render_template('register.html'))
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
         payload = {'id' : id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)}
         token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
      #세션을 생성하며, html에서 {session['id']} 등으로 호출 가능.
         session['id_give'] = id
         session['password_give'] = pw
         return jsonify({'result': 'success', 'token' : token})
      else:
         return jsonify({'result':'fail'})
   #GET 요청만 받았을때 로그인 페이지 띄우기.
   else:
      return render_template('login.html')

   # cookie_id = request.cookies.get('ID')
   # cookie_password = request.cookies.get('password')
   # cookie_email = request.cookies.get('email')
   # id_receive = request.form['id_give']
   # password_receive = request.form['password_give']

   

   #    return jsonify(
   #       result = "success",
   #       # 검증된 경우 액세스 토큰 반환
   #       access_token = create_access_token(identity= user_id, expires_delta= False)
   #     ) #토큰 고유 식별 정보. 클라이언트에서 유지되는 정보이므로 비밀번호등은 x/토큰 만료일자 
   # else:
   #    return jsonify(result = "Invalid Params")
      


# API #4 : 비밀번호 찾기 페이지를 띄웁니다.

@app.route('/login/password')
def password_searching():
   return render_template('password.html')

# API #5 : 아이디와 이메일을 대조하고 비밀번호를 띄워줍니다.
@app.route('/login/passwordView', methods = ['POST'])
def password_view():
   return

# API #6 : 회원 탈퇴를 합니다.
@app.route('/login/delete', methods=['POST'])
@jwt_required()
def delete_login():
   return redirect(url_for('index'))

# API #7 : 로그아웃을 합니다
def logout():
   #저장되어있는 세션 제거.
   session.clear()
   #메인 페이지로 리다이렉트.
   return redirect(url_for('index'))

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)
