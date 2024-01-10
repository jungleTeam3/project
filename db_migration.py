import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.team_3

#######################################################################
#                                한 식                                 #
#######################################################################

#1
db.restaurant.insert_one({'name':'드림타워 구내식당',
	'X': 127.0347399,
	'Y': 37.3005585,
	'category' : "한식",
	'delivery': False,
	'location': "경기 수원시 영통구 광교산로 154-42",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '5,000~10,000',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 11:30 ~ PM 01:30",
	'closed_days' : '토,일',
	'call' : '-'
})
db.menu.insert_one({'name' : '드림타워 구내식당',
	'menu' : '학식',
	'price' : 5000,
	'priority' : 1
})
#2
db.restaurant.insert_one({'name':'맑은 주막',
	'X': 127.0452014,
	'Y': 37.3008172,
	'category' : "한식",
	'delivery': False,
	'location': "경기 수원시 영통구 창룡대로256번길 41 1층",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '15,000이상',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 11:30 ~ PM 09:00",
	'closed_days' : '-',
	'call' : '031-214-2783'
})
db.menu.insert_one({'name' : '맑은 주막',
	'menu' : '오삼불고기',
	'price' : 15000,
	'priority' : 1
})
db.menu.insert_one({'name' : '맑은 주막',
	'menu' : '라떼는 통닭',
	'price' : 15000,
	'priority' : 2
})
db.menu.insert_one({'name' : '맑은 주막',
	'menu' : '해물은파전을사랑해',
	'price' : 15000,
	'priority' : 3
})
db.menu.insert_one({'name' : '맑은 주막',
	'menu' : '등갈비에빠진김치찜',
	'price' : 15000,
	'priority' : 4
})
#3
db.restaurant.insert_one({'name': '기달임 돼지곰탕',
    'X': 127.0408421,
    'Y': 37.2961352,
    'category': "한식",
    'delivery': False,
    'location': "경기 수원시 영통구 창룡대로256번길 77 1층 107호",
    'price': '10,000~15,000',
    'rating': 0.0,
    'review_num': 0,
    'business_hours': "AM 11:00 ~ PM 20:00",
    'closed_days': '-',
    'call': '0507-1400-6628'
})
db.menu.insert_one({'name': '기달임 돼지곰탕',
    'menu': '곰탕',
    'price': 10000,
    'priority': 1
})
db.menu.insert_one({'name': '기달임 돼지곰탕',
    'menu': '곰탕특',
    'price': 14000,
    'priority': 2
})


############################################################
#                      분  식 8개                            #
############################################################
#1
db.restaurant.insert_one({'name':'동대문엽기떡볶이',
	#경도
	'X': 127.0444142,
	#위도
	'Y': 37.2995223,
	# 카테고리 (한식, 중식, 일식, 양식, 분식, )
	# 추가 사항 있을 경우 팀원들과 공유
	'category' : "분식",
	# 배달 여부
	'delivery': False,
	# 주소
	'location': "경기 수원시 영통구 대학1로 38 1층",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '15,000이상',
	# 기본 평점은 0으로 하고, 이후 코멘트의 평균을 내서 저장하는 식으로 직행 예정
	'rating' : 0,
	# 안필요 할 수 있음 (코멘트 테이블에서 가져온 lenth만큼 나누는 식으로 해도 될 듯함)
	'review_num' : 0,
	# 영업 시간 (아래와 같이 기업할 것)
	'business_hours' : "AM 11:00 ~ PM 11:00",
	#정기 휴무일 ('월', '월,화', 확인 안될시 '-')
	'closed_days' : '-',
	#전화번호 (string)
	'call' : '0507-1370-8594'
})
db.menu.insert_one({'name' : '동대문엽기떡볶이',
	'menu' : '마라떡볶이',
	'price' : 16000,
	'priority' : 1
})
db.menu.insert_one({'name' : '동대문엽기떡볶이',
	'menu' : '엽기떡볶이',
	'price' : 14000,
	'priority' : 2
})
db.menu.insert_one({'name' : '동대문엽기떡볶이',
	'menu' : '로제떡볶이',
	'price' : 16000,
	'priority' : 3
})
db.menu.insert_one({'name' : '동대문엽기떡볶이',
	'menu' : '엽기닭볶음탕',
	'price' : 24000,
	'priority' : 4
})
db.menu.insert_one({'name' : '동대문엽기떡볶이',
	'menu' : '주먹김밥(셀프)',
	'price' : 2000,
	'priority' : 5
})
#2
db.restaurant.insert_one({'name':'좋은 인연 식당',
	'X': 127.0421299,
	'Y': 37.2998203,
	'category' : "분식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학3로 7 1층 105호",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '5,000~10,000',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 00:00 ~ PM 00:00",
	'closed_days' : '-',
	'call' : '070-7700-3227'
})
db.menu.insert_one({'name' : '좋은 인연 식당',
	'menu' : '원조김밥',
	'price' : 3000,
	'priority' : 1
})
db.menu.insert_one({'name' : '좋은 인연 식당',
	'menu' : '치즈김밥',
	'price' : 4000,
	'priority' : 2
})
db.menu.insert_one({'name' : '좋은 인연 식당',
	'menu' : '참치김밥',
	'price' : 4000,
	'priority' : 3
})
db.menu.insert_one({'name' : '좋은 인연 식당',
	'menu' : '떡볶이',
	'price' : 4000,
	'priority' : 4
})
db.menu.insert_one({'name' : '좋은 인연 식당',
	'menu' : '라볶이',
	'price' : 5000,
	'priority' : 5
})
#3
db.restaurant.insert_one({'name':'스퀘어식당',
	'X': 127.0347399,
	'Y': 37.3005585,
	'category' : "분식",
	'delivery': False,
	'location': "경기 수원시 영통구 광교산로 154-42",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '5,000~10,000',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 07:30 ~ PM 07:30",
	'closed_days' : '토, 일',
	'call' : '-'
})
db.menu.insert_one({'name' : '스퀘어식당',
	'menu' : '팝만두',
	'price' : 3000,
	'priority' : 1
})
db.menu.insert_one({'name' : '스퀘어식당',
	'menu' : '소떡소떡',
	'price' : 3200,
	'priority' : 2
})
db.menu.insert_one({'name' : '스퀘어식당',
	'menu' : '쉬림프 샐러드',
	'price' : 7000,
	'priority' : 3
})
db.menu.insert_one({'name' : '스퀘어식당',
	'menu' : '치킨마요덮밥',
	'price' : 8000,
	'priority' : 4
})
db.menu.insert_one({'name' : '스퀘어식당',
	'menu' : '등심돈까스(200g)',
	'price' : 6300,
	'priority' : 5
})
#4
db.restaurant.insert_one({'name':'김밥천국',
	'X': 127.0434998,
	'Y': 37.2999374,
	'category' : "분식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학3로4번길 12 이스턴타워 101호",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '5,000~10,000',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 09:00 ~ PM 09:00",
	'closed_days' : '토',
	'call' : '0507-1495-1478'
})
db.menu.insert_one({'name' : '김밥천국',
	'menu' : '야채김밥',
	'price' : 2000,
	'priority' : 1
})
db.menu.insert_one({'name' : '김밥천국',
	'menu' : '참치마요김밥',
	'price' : 3500,
	'priority' : 2
})
db.menu.insert_one({'name' : '김밥천국',
	'menu' : '참치볶음밥',
	'price' : 6000,
	'priority' : 3
})
db.menu.insert_one({'name' : '김밥천국',
	'menu' : '순두부찌개',
	'price' : 5500,
	'priority' : 4
})
db.menu.insert_one({'name' : '김밥천국',
	'menu' : '등심돈까스',
	'price' : 6000,
	'priority' : 5
})
#5
db.restaurant.insert_one({'name':'떡볶이참잘하는집',
	'X': 127.0443075,
	'Y': 37.2999618,
	'category' : "분식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학로 46 104호",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '5,000~10,000',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 11:00 ~ PM 11:00",
	'closed_days' : '-',
	'call' : '0507-1395-2727'
})
db.menu.insert_one({'name' : '떡볶이참잘하는집',
	'menu' : '떡참떡볶이',
	'price' : 3500,
	'priority' : 1
})
db.menu.insert_one({'name' : '떡볶이참잘하는집',
	'menu' : '떡참로제떡볶이',
	'price' : 5500,
	'priority' : 2
})
db.menu.insert_one({'name' : '떡볶이참잘하는집',
	'menu' : '순살치킨 400g',
	'price' : 7900,
	'priority' : 3
})
db.menu.insert_one({'name' : '떡볶이참잘하는집',
	'menu' : '순살양념치킨 400g',
	'price' : 8900,
	'priority' : 4
})
#6
db.restaurant.insert_one({'name':'고라니김밥',
	'X': 127.0437544,
	'Y': 37.3002484,
	'category' : "분식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학로 43 B동 1층 107호",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '5,000~10,000',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 10:30 ~ PM 08:30",
	'closed_days' : '일',
	'call' : '0507-1356-1446'
})
db.menu.insert_one({'name' : '고라니김밥',
	'menu' : '김밥',
	'price' : 3500,
	'priority' : 1
})
db.menu.insert_one({'name' : '고라니김밥',
	'menu' : '치즈김밥',
	'price' : 4000,
	'priority' : 2
})
db.menu.insert_one({'name' : '고라니김밥',
	'menu' : '떡볶이',
	'price' : 5500,
	'priority' : 3
})
db.menu.insert_one({'name' : '고라니김밥',
	'menu' : '어묵탁',
	'price' : 4000,
	'priority' : 4
})
#7
db.restaurant.insert_one({'name':'신전떡볶이',
	'X': 127.0445158,
	'Y': 37.2982363,
	'category' : "분식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학1로8번길 57 1층 102호",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '5,000~10,000',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 10:00 ~ PM 09:00",
	'closed_days' : '일',
	'call' : '0507-1436-4302'
})
db.menu.insert_one({'name' : '신전떡볶이',
	'menu' : '김밥',
	'price' : 3500,
	'priority' : 1
})
db.menu.insert_one({'name' : '신전떡볶이',
	'menu' : '치즈김밥',
	'price' : 4000,
	'priority' : 2
})
db.menu.insert_one({'name' : '신전떡볶이',
	'menu' : '떡볶이',
	'price' : 5500,
	'priority' : 3
})
db.menu.insert_one({'name' : '신전떡볶이',
	'menu' : '어묵탕',
	'price' : 4000,
	'priority' : 4
})
#8
db.restaurant.insert_one({'name':'배떡',
	'X': 127.0452014,
	'Y': 37.3008172,
	'category' : "분식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학로 56",
	# 평균 식사 가격대 (5,000~10,000, 10,000~15,000, 15,000이상 ))
	'price' : '10,000~15,000',
	'rating' : 0,
	'review_num' : 0,
	'business_hours' : "AM 11:00 ~ PM 10:00",
	'closed_days' : '-',
	'call' : '0507-1436-4302'
})
db.menu.insert_one({'name' : '배떡',
	'menu' : '로제떡볶이세트',
	'price' : 14500,
	'priority' : 1
})
db.menu.insert_one({'name' : '배떡',
	'menu' : '분모자떡볶이세트',
	'price' : 14500,
	'priority' : 2
})
db.menu.insert_one({'name' : '배떡',
	'menu' : '짜장떡볶이세트',
	'price' : 10500,
	'priority' : 3
})
db.menu.insert_one({'name' : '배떡',
	'menu' : '국물떡볶이세트',
	'price' : 10500,
	'priority' : 4
})

##########################################################################
#                             일  식  5개                                  #
##########################################################################
#1
db.restaurant.insert_one({'name':'겐코쇼쿠도',
	'X': 127.0436433,
	'Y': 37.2992617,
	'category' : "일식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학로 34",
	'price' : '10,000~15,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 10:00 ~ PM 21:00",
	'closed_days' : '-',
	'call' : '0507-1319-5306'
})
db.menu.insert_one({'name' : '겐코쇼쿠도',
	'menu' : '차슈라멘',
	'price' : 9500,
	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
	'priority' : 1
})
db.menu.insert_one({'name' : '겐코쇼쿠도',
	'menu' : '미소라멘',
	'price' : 9000,
	'priority' : 2
})
db.menu.insert_one({'name' : '겐코쇼쿠도',
	'menu' : '연어덮밥',
	'price' : 10000,
	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
	'priority' : 3
})
db.menu.insert_one({'name' : '겐코쇼쿠도',
	'menu' : '새우장동',
	'price' : 8500,
	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
	'priority' : 4
})
#2
db.restaurant.insert_one({'name':'역전우동0410',
	'X': 127.0436433,
	'Y': 37.2992617,
	'category' : "일식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학로 34 경기캠퍼스프라자 105호",
	'price' : '5,000~10,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 10:00 ~ PM 21:00",
    'closed_days' : '-',
    'call' : '031-212-0417'
})
db.menu.insert_one({'name' : '역전우동0410',
	'menu' : '얼큰파닭국수',
	'price' : 6500,
	'priority' : 1
})
db.menu.insert_one({'name' : '역전우동0410',
	'menu' : '역전돈까스',
	'price' : 8500,
	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
	'priority' : 2
})
db.menu.insert_one({'name' : '역전우동0410',
	'menu' : '더블치즈돈까스',
	'price' : 9000,
	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
	'priority' : 3
})
db.menu.insert_one({'name' : '역전우동0410',
  	'menu' : '구운파닭국수',
  	'price' : 6500,
  	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
  	'priority' : 4
})
#3
db.restaurant.insert_one({'name':'회뜨는 킹',
  	'X': 127.0448803,
  	'Y': 37.2986188,
  	'category' : "일식",
  	'delivery': False,
  	'location': "경기 수원시 영통구 대학1로54번길 25 101호",
  	'price' : '10,000~15,000',
  	'rating' : 0.0,
  	'review_num' : 0,
  	'business_hours' : "AM 16:00 ~ PM 22:00",
	'closed_days' : '-',
	'call' : '0507-1388-5561'
})
db.menu.insert_one({'name' : '회뜨는 킹',
	'menu' : '광어(소)',
	'price' : 40000,
	'priority' : 1
})
#4
db.restaurant.insert_one({'name':'동경당',
	'X': 127.0454046,
	'Y': 37.2991796,
	'category' : "일식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학1로54번길 11 1층 동경당",
	'price' : '10,000~15,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 16:00 ~ PM 22:00",
	'closed_days' : '-',
	'call' : '0507-1388-5561'
})
db.menu.insert_one({'name' : '동경당',
	'menu' : '모밀세트',
	'price' : 12000,
	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
	'priority' : 1
})
db.menu.insert_one({'name' : '동경당',
	'menu' : '냉모밀',
	'price' : 9900,
	'priority' : 2
})
db.menu.insert_one({'name' : '동경당',
	'menu' : '비빔모밀',
	'price' : 9900,
	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
	'priority' : 3
})
db.menu.insert_one({'name' : '동경당',
	'menu' : '새우튀김우동',
	'price' : 9900,
	# 우선 순위 (메뉴 소팅을 가격순으로 할 시, 해당 가게의 주력 메뉴가 아닐 수 있기에 우선 순위로 소팅 할 예정)
	'priority' : 4
})
#5
db.restaurant.insert_one({'name':'키무카츠광교점',
	'X': 127.0469684,
	'Y': 37.2963486,
	'category' : "일식",
	'delivery': False,
	'location': "경기 수원시 영통구 광교로 191",
	'price' : '10,000~15,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 10:00 ~ PM 21:00",
	'closed_days' : '-',
	'call' : '031-214-0977'
})
db.menu.insert_one({'name' : '키무카츠광교점',
	'menu' : '새우튀김우동',
	'price' : 13900,
	'priority' : 1
})
db.menu.insert_one({'name' : '키무카츠광교점',
	'menu' : '카레카츠동',
	'price' : 10500,
	'priority' : 2
})
db.menu.insert_one({'name' : '키무카츠광교점',
	'menu' : '김치카츠우동나베',
	'price' : 11500,
	'priority' : 3
})
db.menu.insert_one({'name' : '키무카츠광교점',
	'menu' : '치킨카레동',
	'price' : 10500,
	'priority' : 4
})
##################################################################################
#                            중 식  4개                                           #
##################################################################################
#1
db.restaurant.insert_one({'name': '경기대 수련반점',
    'X': 127.0420618,
    'Y': 37.2975482,
    'category': "중식",
    'delivery': False,
    'location': "경기 수원시 영통구 대학로 10",
    'price': '5,000~10,000',
    'rating': 0.0,
    'review_num': 0,
    'business_hours': "AM 10:30 ~ PM 21:00",
    'closed_days': '-',
    'call': '0507-1332-8256'
})
db.menu.insert_one({'name': '경기대 수련반점',
    'menu': '유니짜장면',
    'price': 7000,
    'priority': 1
})
db.menu.insert_one({'name': '경기대 수련반점',
    'menu': '간짜장',
    'price': 8000,
    'priority': 2
})
db.menu.insert_one({'name': '경기대 수련반점',
    'menu': '짬뽕',
    'price': 8000,
    'priority': 3
})
db.menu.insert_one({'name': '경기대 수련반점',
    'menu': '고추해물짬뽕',
    'price': 10000,
    'priority': 4
})
#2
db.restaurant.insert_one({'name': '호중천',
    'X': 127.0440235,
    'Y': 37.2977283,
    'category': "중식",
    'delivery': False,
    'location': "경기 수원시 영통구 대학1로8번길 54-3 선경빌라1층",
    'price': '5,000~10,000',
    'rating': 0.0,
    'review_num': 0,
    'business_hours': "AM 11:00 ~ PM 21:00",
    'closed_days': '-',
    'call': '0507-1399-0661'
})
db.menu.insert_one({'name': '호중천',
    'menu': '쭈꾸미새우덮밥',
    'price': 12000,
    'priority': 1
})
db.menu.insert_one({'name': '호중천',
    'menu': '유니짜장면',
    'price': 7000,
    'priority': 2
})
db.menu.insert_one({'name': '호중천',
    'menu': '간짜장',
    'price': 8000,
    'priority': 3
})
db.menu.insert_one({'name': '호중천',
    'menu': '해물짬뽕',
    'price': 9000,
    'priority': 4
})
#3
db.restaurant.insert_one({'name': '마라타임마라탕',
    'X': 127.0436433,
    'Y': 37.2992617,
    'category': "중식",
    'delivery': False,
    'location': "경기 수원시 영통구 대학로 34 1층 104호",
    'price': '5,000~10,000',
    'rating': 0.0,
    'review_num': 0,
    'business_hours': "AM 11:00 ~ PM 21:00",
    'closed_days': '-',
    'call': '0507-1311-1074'
})
db.menu.insert_one({'name': '마라타임마라탕',
    'menu': '마라탕100g',
    'price': 1800,
    'priority': 1
})
#4
db.restaurant.insert_one({'name': '조원동 교동반점',
    'X': 127.0448481,
    'Y': 37.2980663,
    'category': "중식",
    'delivery': False,
    'location': "경기 수원시 영통구 대학1로8번길 63",
    'price': '5,000~10,000',
    'rating': 0.0,
    'review_num': 0,
    'business_hours': "AM 10:30 ~ PM 21:00",
    'closed_days': '-',
    'call': '031-212-1128'
})
db.menu.insert_one({'name': '조원동 교동반점',
    'menu': '짬뽕',
    'price': 9000,
    'priority': 1
})
db.menu.insert_one({'name': '조원동 교동반점',
    'menu': '탕수육',
    'price': 19000,
    'priority': 2
})
db.menu.insert_one({'name': '조원동 교동반점',
    'menu': '짜장면',
    'price': 7000,
    'priority': 3
})
####################################################################
#                    아시안 음식 4개                                          
#################################################################
#1
db.restaurant.insert_one({'name':'야마도리',
	'X': 127.0452587,
	'Y': 37.2990384,
	'category' : "일식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학1로54번길 15 1층",
	'price' : '10,000~15,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 11:00 ~ PM 10:00",
	'closed_days' : '일',
	'call' : '0507-1471-3308'
})
db.menu.insert_one({'name' : '야마도리',
	'menu' : '야끼규동',
	'price' : 10900,
	'priority' : 1
})
db.menu.insert_one({'name' : '야마도리',
	'menu' : '야마아게동',
	'price' : 10900,
	'priority' : 2
})
db.menu.insert_one({'name' : '야마도리',
	'menu' : '카이센동',
	'price' : 10900,
	'priority' : 3
})
db.menu.insert_one({'name' : '야마도리',
	'menu' : '해물볶음우동',
	'price' : 10900,
	'priority' : 4
})
#2
db.restaurant.insert_one({'name':'방콕스토리',
	'X': 127.0438701,
	'Y': 37.2989525,
	'category' : "아시안",
	'delivery':False,
	'location': "경기 수원시 영통구 대학1로64번길 55",
	'price' : '5,000~10,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 10:00 ~ PM 08:00",
	'closed_days' : '월',
	'call' : '031-216-1337'
})
db.menu.insert_one({'name' : '방콕스토리',
	'menu' : '소고기쌀국수',
	'price' : 9000,
	'priority' : 1
})
db.menu.insert_one({'name' : '방콕스토리',
	'menu' : '모닝글로리',
	'price' : 7000,
	'priority' : 2
})
db.menu.insert_one({'name' : '방콕스토리',
	'menu' : '팟타이새우',
	'price' : 9000,
	'priority' : 3
})
#3
db.restaurant.insert_one({'name':'전티마이 베트남쌀국수',
	'X': 127.0440183,
	'Y': 37.2996349,
	'category' : "아시안",
	'delivery': False,
	'location': "경기 수원시 영통구 대학로 40",
	'price' : '5,000~10,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 00:00 ~ PM 00:00",
	'closed_days' : '-',
	'call' : '031-212-9933'
})
db.menu.insert_one({'name' : '전티마이 베트남쌀국수',
	'menu' : '소고기쌀국수',
	'price' : 4500,
	'priority' : 1
})
db.menu.insert_one({'name' : '전티마이 베트남쌀국수',
	'menu' : '파인애플 볶음밥',
	'price' : 4900,
	'priority' : 2
})
db.menu.insert_one({'name' : '전티마이 베트남쌀국수',
	'menu' : '해물볶음면',
	'price' : 4900,
	'priority' : 3
})
#4
db.restaurant.insert_one({'name':'홍대쌀국수 이마트광교점',
	'X': 127.0469684,
	'Y': 37.2963486,
	'category' : "아시안",
	'delivery': False,
	'location': "경기 수원시 영통구 광교로 191 1층 홍대쌀국수",
	'price' : '5,000~10,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 00:00 ~ PM 00:00",
	'closed_days' : '-',
	'call' : '-'
})
db.menu.insert_one({'name' : '홍대쌀국수 이마트광교점',
	'menu' : '홍대 쌀국수',
	'price' : 6900,
	'priority' : 1
})
db.menu.insert_one({'name' : '홍대쌀국수 이마트광교점',
	'menu' : '닭고기쌀국수',
	'price' : 7900,
	'priority' : 2,
})
db.menu.insert_one({'name' : '홍대쌀국수 이마트광교점',
	'menu' : '얼큰쇠고기쌀국수',
	'price' : 8900,
	'priority' : 3
})
db.menu.insert_one({'name' : '홍대쌀국수 이마트광교점',
	'menu' : '베트남새우볶음밥',
	'price' : 8900,
	'priority' : 4
})
#################################################################################################
#                           양 식                                      
################################################################################
#1
db.restaurant.insert_one({'name':'키친 토리노',
	'X': 127.0420618,
	'Y': 37.2975482,
	'category' : "양식",
	'delivery': True,
	'location': "경기 수원시 영통구 대학로 10 1층 키친토리노",
	'price' : '10,000~15,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 11:00 ~ PM 09:00",
	'closed_days' : '1, 3, 5주차 일',
	'call' : '0507-1415-2216'
})
db.menu.insert_one({'name' : '키친 토리노',
	'menu' : '알리오 올리오',
	'price' : 10000,
	'priority' : 1
})
db.menu.insert_one({'name' : '키친 토리노',
	'menu' : '해산물 토마토',
	'price' : 12000,
	'priority' : 2
})
db.menu.insert_one({'name' : '키친 토리노',
	'menu' : '까르보 떡볶이 파스타',
	'price' : 11000,
	'priority' : 3
})
#2
db.restaurant.insert_one({'name':'부리또 정거장',
	'X': 127.0425411,
	'Y': 37.2973203,
	'category' : "양식",
	'delivery': True,
	'location': "경기 수원시 영통구 대학1로8번길 5 101호",
	'price' : '5,000~10,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 10:30 ~ PM 09:30",
    'closed_days' : '일',
    'call' : '0507-1431-0689'
})
db.menu.insert_one({'name' : '부리또 정거장',
	'menu' : '프리미엄 정거장 부리또',
	'price' : 8000,
	'priority' : 1
})
db.menu.insert_one({'name' : '부리또 정거장',
	'menu' : '치킨라이스',
	'price' : 5000,
	'priority' : 2
})
db.menu.insert_one({'name' : '부리또 정거장',
	'menu' : '소고기라이스',
	'price' : 5500,
	'priority' : 3
})
db.menu.insert_one({'name' : '부리또 정거장',
	'menu' : '치킨감자',
	'price' : 5500,
	'priority' : 4
})
#3
db.restaurant.insert_one({'name':'서브웨이 광교경기대후문',
	'X': 127.0436433,
	'Y': 37.2992617,
	'category' : "양식",
	'delivery': True,
	'location': "경기 수원시 영통구 대학로 34",
	'price' : '5,000~10,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 08:00 ~ PM 10:00",
	'closed_days' : '-',
	'call' : '-'
})
db.menu.insert_one({'name' : '서브웨이 광교경기대후문',
	'menu' : '에그마요',
	'price' : 5500,
	'priority' : 1
})
db.menu.insert_one({'name' : '서브웨이 광교경기대후문',
	'menu' : '이탈리안 비엠티',
	'price' : 6700,
	'priority' : 2
})
db.menu.insert_one({'name' : '서브웨이 광교경기대후문',
	'menu' : '비엘티',
	'price' : 6600,
	'priority' : 3
})
#4
db.restaurant.insert_one({'name':'언락',
	'X': 127.0453278,
	'Y': 37.2988398,
	'category' : "양식",
	'delivery': False,
	'location': "경기 수원시 영통구 대학1로58번길 16 1층",
	'price' : '10,000~15,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 11:00 ~ PM 11:00",
	'closed_days' : '일',
	'call' : '0507-1367-5816'
	})
db.menu.insert_one({'name' : '언락',
	'menu' : '마르게리따 피자',
	'price' : 12000,
	'priority' : 1
})
db.menu.insert_one({'name' : '언락',
	'menu' : '하몽과루꼴라피자',
	'price' : 14000,
	'priority' : 2
})
db.menu.insert_one({'name' : '언락',
	'menu' : '고르곤졸라 피자',
	'price' : 12000,
	'priority' : 3
})
db.menu.insert_one({'name' : '언락',
	'menu' : '볼로네제 깔조네',
	'price' : 13000,
	'priority' : 4
})
db.menu.insert_one({'name' : '언락',
	'menu' : '새우오일파스타',
	'price' : 11000,
	'priority' : 5
})
#5
db.restaurant.insert_one({'name':'올리베떼',
	'X': 127.0452014,
	'Y': 37.3008172,
	'category' : "양식",
	'delivery': True,
	'location': "경기 수원시 영통구 대학로 56",
	'price' : '10,000~15,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 11:00 ~ PM 08:00",
	'closed_days' : '-',
	'call' : '031-214-5284'
	})
db.menu.insert_one({'name' : '올리베떼',
	'menu' : '게살크림',
	'price' : 9500,
	'priority' : 1
})
db.menu.insert_one({'name' : '올리베떼',
	'menu' : '쉬림프 스노잉 피자',
	'price' : 14000,
	'priority' : 2
})
db.menu.insert_one({'name' : '올리베떼',
	'menu' : '씨푸드 바질 라이스',
	'price' : 8500,
	'priority' : 3
})
db.menu.insert_one({'name' : '올리베떼',
	'menu' : '리코타 치즈 샐러드',
	'price' : 8000,
	'priority' : 4
})
#6
db.restaurant.insert_one({'name':'마리나그란데',
	'X': 127.0456866,
	'Y': 37.2987973,
	'category' : "양식",
	'delivery': True,
	'location': "경기 수원시 영통구 대학1로58번길 13 . 1층 101호",
	'price' : '10,000~15,000',
	'rating' : 0.0,
	'review_num' : 0,
	'business_hours' : "AM 11:00 ~ PM 09:00",
	'closed_days' : '일',
	'call' : '031-212-3902'
})
db.menu.insert_one({'name' : '마리나그란데',
	'menu' : '안심 샐러드',
	'price' : 17000,
	'priority' : 1
})
db.menu.insert_one({'name' : '마리나그란데',
	'menu' : '시저 샐러드',
	'price' : 14000,
	'priority' : 2
})
db.menu.insert_one({'name' : '마리나그란데',
	'menu' : '펜네 아라비아따 파스터',
	'price' : 13000,
	'priority' : 5
})
db.menu.insert_one({'name' : '마리나그란데',
	'menu' : '상하이 파스타',
	'price' : 14000,
	'priority' : 3
})
db.menu.insert_one({'name' : '마리나그란데',
	'menu' : '미트소스 파스타',
	'price' : 14000,
	'priority' : 4
})
