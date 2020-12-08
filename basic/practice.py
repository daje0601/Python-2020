# # 1. 자료형
# # 1-1. int, float 
# print(5)
# print(-10)
# print(3.14)

# # 1-2. str
# print("나비")
# print('나비')
# print("zzzzzzzz")
# print("z" * 9)

# # 2. Boolean(True, flase)
# print(5 > 10)
# print( not (5>10))
# print(10 > 5)
# print(not True)
# print(not False)

# # 3. 변수(variable)
# # 변수란? 어떤 값을 저장하는 공간이며, 
# #print(" 우리집 강아지의 이름은 또또입니다. 또또는 10살이며, 산책을 싫어해요")
# # 위와 같은 구문에서 강아지이름을 갑자기 예쁜이라고 변경되었다면 모두 바꿔줘야하니까 이를 간결하게 수정하기
# # 위해서 변수를 사용한다. 
# anminal = "강아지"
# name = "또또"
# age = 10
# is_adult = age >= 3
# #문자열 포맷팅1
# print(f"우리집 {anminal}의 이름은 {name}입니다. 또또는 {age}살이며, {is_adult}이에요, 산책을 싫어해요")
# #문자열 포맷팅2
# print("우리집" + anminal + "의 이름은 " + name + "예요" + name + "는" + str(age) + "살이며 산책을 아주 좋아해요")
# #문자열 포맷팅3
# print("우리집",anminal,"의 이름은 ",name,"예요", name,"는",age,"살이며 산책을 아주 좋아해요")
# #위처럼 변수를 이용하면 문장 전체를 수정하지 않고 우리가 원하는 문자열 얻을 수 있다 

# 4. 주석 
# 주석이란? 코드 내에 포함은 되어 있지만 실행은 되지 않는 문장
# 프로그램에 대한 설명이나, 다른 개발자와의 소통을 위해서 사용된다 
# 주석처리 방법 1: '''작은 따운표를 쓰면 된다 ''' 
# 주석처리 방법 2: # 
# 주석처리 방법 3: 컨트롤 + / 

# Quiz 변수명을 이용하여 다음 문장을 출력하시오 
# 문제 : 변수명 station으로 "사당", "신도림", "인천공항"을 순서대로 출력하십시오 
# stations = ["사당", "신도림", "인천공항"]
# for station in stations:
#     print(f"{station}행 열차가 들어오고 있습니다." )


# 5. 연산자
# 덥셈 print(1+1)
# number = 3 
# number = number + 4 이렇게 간단하게 쓸 수 있음 number += 4 

# 뺄셈 print(3-2)
# number = 3 
# number = number - 4 이렇게 간단하게 쓸 수 있음 number -= 4 

# 곱셈 print(5*2)
# number = 3 
# number = number * 4 이렇게 간단하게 쓸 수 있음 number *= 4 

# 나눗셈 print(6/3)
# number = 3 
# number = number / 4 이렇게 간단하게 쓸 수 있음 number /= 4 

# 나머지 print(10%3)
# 제곱 print(2**3)
# 몫구하기 print(10//3)
# 비교1 print(10 > 3), print(10 >= 3), print(5 <= 7), pritn(3 == 3)
# 비교2 print(1 != 3), print(not(1 != 3))
# 비교3 
# print((3 > 0) and ( 4 < 10)), print((3 > 0) & ( 4 < 10))
# print((3 > 0) or ( 4 < 10)), print((3 > 0) | ( 4 < 10))
# 비교4(3중 연산)
# print(5 > 4 > 3)
# print(5 > 4 > 7)

# 6. 숫자처리 함수 
# 절대값
# print(abs(-5))
# # 제곱 (4의 2승)
# print(pow(4, 2))
# #최대값 
# print(max(5, 12))
# #최소값
# print(min(5, 12))
# #반올림
# print(round(3.14))
# print(round(4.99))
# #내림 (math를 import해야 사용가능)
# print(floor(4.99))
# #올림 (math를 import해야 사용가능)
# print(ceil(3.14))
# #제곱근 (math를 import해야 사용가능)
# print(sqrt(16))

# 7. 랜덤함수 
# from random import *
# #0.0 ~ 1.0 미만의 임의 값 생성 
# print(random())
# #0.0 ~ 10.0 미만의 임의 값 생성 
# print(random() * 10 ) 
# #0 ~ 10 미만의 임의 값 생성 
# print(int(random() * 10)) 
# #1 ~ 10 이하의 임의 값 생성 
# print(int(random() * 10) + 1)
# #로또 번호 출력 ( 1부터 45 사이의 수를 출력하는 방법 )
# #방법1
# print(int(random() * 45) + 1)
# #방법2
# print(randrange(1, 46))
# #방법3
# print(randint(1, 45))

# Quiz 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다. 
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 
# #아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오
# 조건1: 랜덤으로 날짜를 뽑아야 함  
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함 
# 조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외 
# 출력문 예제 : 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다. 
# from random import *
# off__day = int(random() * 28) + 4
# print(f"오프라인 스터디 모임 날짜는 매월 {off__day}일로 선정되었습니다.")

# #8. 문자열 
# sentence1 = "나는 소년입니다."
# sentence2 = '이렇게 따옴표를 바꾸어도 잘 출력이 되요'
# sentence3 = """이렇게 해도 출력이 되네요
# 심지어 줄을 바꾸었는데도 되죠?
# 신기하죠? """
# print(sentence3)

# 9. 슬라이싱 : 문자열에서 필요한 정보만 잘라오는 것 
# jumin = "990120-1234567"
# #성별을 가져오기 
# print(f"성별: {jumin[7]}")
# #연도
# print(f"연:{jumin[0:2]}")
# print(f"연:{jumin[:2]}")
# #월
# print(f"연:{jumin[2:4]}")
# #일 
# print(f"연:{jumin[4:6]}")
# print(f"생년월일:{jumin[:6]}")
# print(f"뒷7자리:{jumin[7:]}")
# print(f"뒷7자리(뒤에서 부터):{jumin[-7:]}")

# # 10. 문자열 처리 함수
# python = "Python is Amazing"
# #모두 소문자로 변경
# print(python.lower())
# #모두 대문자로 변경 
# print(python.upper())
# #특정 인덱스가 대문자인지 확인 
# print(python[0].isupper())
# #문자열의 길이
# print(len(python))
# #문자열 교체 
# print(python.replace("Python", "Java"))
# # 파이썬에서 인덱스 찾기 
# index = python.index("n")
# #인덱스를 검색한 후 그 다음 위치부터 찾기 
# index = python.index("n", index+1)
# #위와 비슷한 기능을 가진 find
# # find의 경우 내가 원하는 값이 없는 경우, -1을 반환하고 
# # index에서 내가 원하는 값이 없는 경우, 오류를 내면서 프로그램을 종료함 
# print(python.find("n"))
# print(python.find("Java"))
# #내가 원하는 문자가 몇개 있는지 찾을 수 있는 count 
# print(python.count("n"))

# # 11. 문자열포맷팅 
# print("a", "b")
# print("a" + "b")
# #d는 숫자 
# print("나는 %d살입니다." % 20)
# #c는 한글자 
# print("Apple은 %c로 시작해요" % "A")
# #s는 문자
# print("나는 %s을 좋아해요" % "파이썬")
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨강"))
# #.format
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨강"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강"))
# #.format 변수 
# print("나는 {age}살이며 {color}색을 좋아해요".format(age=20, color="빨강"))
# #.f
# age = 20
# color = "파란"
# print(f"나는 {age}살이며 {color}색을 좋아해요") 

# # 12. 탈출문자 
# #\n 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")
# #\"" 문장 내에 큰 따옴표를 넣고 싶을 때 
# print("저는 \"나도코딩\"입니다.")
# #\\는 문장 내에서 한개의 \로 인식된다 
# print("C:\\user\\Desktop\\worksapce")
# # \r : 커서를 맨 앞으로 이동 
# print("Red Apple\rPine")
# #\b: 백스페이스 역할(한글자 삭제)
# print("Redd\bApple")
# #\t : 탭 
# print("Red\tApple")

# Quiz 사이트별 비밀번호 만들어 주는 프로그램 작성하기
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 갯수 + "!"로 구성 하시오  
# website = "http://naver.com"
# my_str = website.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(f"{website}의 비밀번호는 {password}입니다.")

# # 13. 리스트 : 순서를 가지는 객체의 집합 
# # 지하철에 1번칸에 10명, 2번칸에 20명, 3번칸에 30명이 타고 있다는 걸 표현하기 위해서는 
# # 기존에 배운 개념으로는 각각의 변수를 생성해야한다. sub1=10, sub2=20, sub3=30
# # 이렇게 변수가 많이 지고 코드가 길어지는 것을 막기 위하여 리스트라는 개념이 나왔다 
# #sub = [10, 20, 30]
# subway = ["유재석", "조세호", "박명수"]
# #조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))
# #하하씨가 다음 정류장에서 탔어 ( append는 리스트 맨 뒤에 붙힘 )
# subway.append("하하")
# #정현돈씨가 유재석과 조세호씨 사이에 넣기 ( insert는 원하는 위치에 넣을 수 있음 )
# subway.insert(1, "정형돈")
# # 뒤에서 부터 하나씩 꺼내기 
# print(subway.pop())
# 리스트에 있는 모든 값 지우기 
# subway.clear()
# # 리스트 카운트 
# print(subway.count("유재석"))
# 정렬 ( 정방향, 역방향 )
# num_list = [5, 4, 3, 6, 7, 8, 9]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# # #리스트 내에 다양한 타입을 함께 기재할 수 있으며, 리스트끼리 합치는 것도 가능하다 
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# # 결과값 : [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# # 14. dict(사전) : key와 value가 존재함 / key에 대한 중복이 허용되지 않음 
# cabinet = {3: "kang", 100: "kim"}
# # dict에서 value 확인방법 1( 값이 있을 때 )
# print(cabinet[3])
# print(cabinet[100])
# # dict에서 value를 확인방법 2( 값이 있을 때 )
# print(cabinet.get(3))
# # 방법1과 방법2의 차이 : 방법1은 값이 없는 경우 프로그램 종료, 방법2는 None출력 
# # dict에서 value를 확인방법 3( 값이 없을 때 )
# # 만약 없는 값을 가져올때 None말고 내가 지정한 값이 나오게 하고 싶다면 !
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능"))
# # dict에서 key, value를 확인방법 4
# # key 
# print(3 in cabinet)
# print(cabinet.keys()) # 꼭 복수형으로 기재할 것 
# #value
# print(cabinet.values())  # 꼭 복수형으로 기재할 것 
# # key & value 동시 출력 
# print(cabinet.items())

# # dict에서 새로운 값 추가 및 기존값 변경 
# cabinet[3] = "jung"
# cabinet[5] = "hong"

# # dict에서 삭제하는 방법 
# # key별로 삭제 
# del cabinet[3]
# # 전체 삭제 
# cabinet.clear



# # 15. 튜플 : 리스트와 다르게 내용변경이나 추가 불가 / 속도가 리스트보다 빠르다! 
# 
# # 특정한 돈가스 집이 있다고 하자 
# menu = ("돈까스", "치즈까스")
# # 값을 출력하는 방법 
# print(menu[0])
# print(menu[1])

# # 튜플의 더블 할당 
# (x,y) = (4, "fred")
# print(y) # fred가 출력됨 

# (x,y,z) = (4, 99, 45)
# print(y) # 99가 출력됨 

# # 튜플로 dict에 삽입하기 
# d = dict()
# d["csev"] = 2
# d["cwen"] = 4
# for (k,v) in d.items():
#   print(k, v)
# # csev 2 
# # cwen 4 위와 같은 형식으로 출력됨
# # 만약 튜플형태로 출력하고 싶다면
# tups = d.items()
# print(tups)# 변수를 중간에 만들어주고 기재하면 됨

# # 튜플의 비교(comparable)
# (0,1,2) < (5,1,2)
# (0,1,200000) < (0,3,4)
# ("Jones", "sally") < ("Jones", "Sam")
# ("Jones", "sally") > ("Adams", "Sam")


# # 튜플 한줄씩 출력하기
# c = { 'a':10, "b":1, "c":22 }
# d = sorted(c.items())
# for k, v in sorted(c.items()):
#   print(k, v)

# # 튜플 리스트 순차정렬
# c = { 'a':10, "b":1, "c":22 }
# c.items()
# print(sorted(c.items()))


# # 튜플 리스트 역순정렬 및 key&value 치환 
# c = { 'a':10, "b":1, "c":22 }
# tmp = list()
# for k, v in c.items():
#   tmp.append( (v, k))

# tmp = sorted(tmp, reverse=True)
# print(tmp)

# #문장에서 가장 많이 나온 단어 상위 10개 뽑아보기 
# fhand = ["he Iranian nuclear scientist assassinated Friday east of Tehran was shot by a remote-controlled machine gun operating out of another car, the semi-official Fars News Agency said Sunday. With top Iranian officials blaming Israel, Supreme Leader Ayatollah Seyyed Ali Khamenei and others have promised revenge for the killing of Mohsen Fakhrizadeh, who was the country's chief nuclear scientist.There were conflicting accounts from Iranian news agencies about how the attack unfolded. One report published Sunday from Fars News said Fakhrizadeh was traveling with his wife Friday in a bulletproof car, alongside three security personnel vehicles, when he heard what sounded like bullets hitting a vehicle, and he exited the car to determine what had happened. When he exited the vehicle, a remote-controlled machine gun opened fire from a Nissan stopped about 150 meters (164 yards) from Fakhrizadeh's car, Fars News said."]
# counts = dict()
# for line in fhand:
#   words = line.split()
#   for word in words:
#     counts[word] = counts.get(word, 0) + 1

# lst = list()
# for k, v in counts.items():
#   newsup = (k, v)
#   lst.append(newsup)

# lst = sorted(lst, reverse=True)

# for k, v in lst[:10]:
#   print(k, v)

# # lst부터 print(k, v)까지 한줄로 쓸 수 있는데 잘 봐봐 
# print(sorted([(v,k) for k,v in counts.items()]) )



# # 16. set( 수학의 집합 개념 / 중복이 안되고 순서가 없는 것 )
# my_list = {1, 2, 3, 3, 3, 4, 5, 6}
# print(my_set)

# java = {"abc", "cdf", "qwe", "asd"}
# python = set(["abc", "qwe"])

# # 교집합 ( java, python을 모두 할 수 있는 사람 )
# print(java & python)
# print(java.intersection(python))
# # 합집합 ( java를 할 수 있거나  python을 할 수 있는 사람 )
# print(java | python)
# print(java.union(python))
# # 차집합 ( java는 할 수 있지만 python은 할 줄 모르는 사람 )
# print(java - python)
# print(java.difference(python))
# # set 추가 ( python을 할 줄 아는 사람이 늘어날 경우 )
# python.add("kang")
# # set 제거 ( java를 할 줄 알았는데 갑자기 까먹은 경우 )
# java.remove("abc")



# # 17. 자료구조형변경
# # 세트 -> 리스트, 리스트 -> 튜플, 튜플 -> 세트, 리스트 -> 세트, 세트 -> 튜플로 변경 가능 
# menu = {"커피", "우유", "주스"}
# menu = list(menu)
# print(menu)
# print(type(menu))
# menu = tuple(menu)
# print(type(menu))
# print(menu)
# menu = set(menu)
# print(type(menu))
# print(menu)

# Quiz
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# (출력예제)
#  - - 당첨발표 - -
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  - - 축하합니다.  - -

# from random import *
# #내가 푼 답 
# lst = list(range(1, 21))
# shuffle(lst)
# lst = set(lst)
# chicken = sample(lst, 1)
# chicken =set(chicken)
# reminder_lst = lst - chicken
# coffee = sample(reminder_lst, 3)
# print(f"치킨 당첨자 : {chicken}")
# print(f"커피 당첨자 : {coffee}")

# # 해설에서는 4명을 뽑고 그중에 치킨과 커피를 나누어서 했네
# lst = list(range(1, 21))
# shuffle(lst)
# winners = sample(lst, 4)
# print(f"치킨 당첨자 : {chicken}")
# print(f"커피 당첨자 : {coffee}")


# 18. if 
# weather = input("오늘의 날씨는 어때요?:")
# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온이 어때요?"))
# if 30 <= temp:
#     print("너무 더워요")
# elif 10 <= temp < 30:
#     print("날씨가 좋아요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")


# #19. for 
# for waiting_num in [1, 2, 3, 4, 5]:
#     print(f"대기번호 : {waiting_num}")
# for waiting_num in range(1,6):
#     print(f"대기번호 : {waiting_num}")


# #20. while
# customer = "woong"
# index = 5
# while index >= 1:
#     print(f"{customer}님, 커피가 준비되었으며, {index}남았습니다.")
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")



# # 20. coutinue and break 
# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"오늘은 수업여기까지, {student}는 교무실로 따라와 ")
#         break
#     print(f"{student}, 책을 읽어봐")


# # 21. 한줄 for 
# student = ["i am groot", "Thor"]
# student = [i.upper() for i in student]
# print(student)

##########꼭 다시 풀어봐야할 문제###############
#Quiz
# 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# 출력예제
# [O] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# ...
# [] 50번째 손님 (소요시간: 16분)
# 총 탑승 승객 : 2분 
# from random import *
# count = 0
# for index in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print(f"[O]{index}번째 손님 소요시간 : {time}분")
#         count += 1
#     else:
#         print(f"[ ]{index}번째 손님 소요시간 : {time}분")

# print(f"총 탑승 승객 : {count}분")


# 내가 푸는 방식은 지역변수와 전역변수 개념을 잘 몰라서 못풀었던거네
# from random import *
# # work_time = randrange(5, 51)
# work_time =int(random() * 50) + 1
# # real_time = randrange(5, 16)
# real_time = int(random() * 15) + 1

# def taxi_working(real_time, work_time):
#     index = 1
#     count = 0 
#     while index < 51:
#         if real_time in work_time:
#             print(f"[O]{index}번째 손님 소요시간 : {real_time}분")
#             count += 1
#         else:
#             print(f"[ ]{index}번째 손님 소요시간 : {work_time}분")
#     return real_time, work_time
#     print(f"총 탑승 승객 : {count}분")


# 21. 함수 
# 21-1. 함수란 
# def deposit(balance, money):
#     print(f"입금이 완료되었습니다. 잔액은 {balance+money}원 입니다.")
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print(f"출금이 완료되었습니다. 잔액은 {balance-money}입니다.")
#         return balance - money
#     else:
#         print("출금이 되지 않았습니다.")
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission
# balance = 0
# balance = deposit(balance, 1000)
# ########이건 몰랐던 부분 이렇게 쓰면 되는구만##########################################################
# commission, balance = withdraw_night(balance, 500)
# print(f"{commission}   {balance}")


# # 21-2. 함수의 기본값 
# #우리가 프로파일 함수를 만들어보자 
# def profile(name, age, main_lang):
#     print(f"name:{name}, age:{age}, lang:{main_lang}")
# profile("유재석", 20, "파이썬")
# profile("Kan.G", 50, "Java")
# #또한 키워드를 통해 함수를 호출할 경우, 순서가 뒤섞여 있어서도 함수가 정상적으로 출력이 됨
# profile( age=50, main_lang="Java", name="Kan.G",)
# #그런데 같은 고등학교 반에서 같은 수업을 듣는 경우, 매번 동일한 정보를 적을 필요가 없다 
# #이럴때 사용할 수 있는게 함수의 기본값 이다. 
# def profile(name, age=18, main_lang="파이썬"):
#     print(f"name:{name}, age:{age}, lang:{main_lang}")
# profile("ㅎ.ㅎ")
# profile("Kan.G")

# 21-3. 가변인자를 통한 함수 
# 가변인자 사용이유 : 우리가 사용하는 함수의 인자가 변경되는 경우를 대비하여 사용함 

# #예시1 
# def profile(name, age, lang10, lang11, lang12):
#     print(f"name:{name}, age:{age}", end=" ")
#     print(lang10, lang11, lang12)

# profile("sdf", 20, "C", "C#", "C++")
# #이러한 경우 사용할 수 있는 언어가 증가할 경우 함수를 변경해줘야함 
# # end=" "는 2개의 print를 사용해도 줄바꿈이 일어나지 않도록 하는 키워드임 

# #예시2
# def profile(name, age, *lang):
#     print(f"name:{name}, age:{age}", end=" ")
#     for lng in lang:
#         print(lng, end=" ")

# profile("sdf", 20, "python", "Java", "C", "C#", "C++")
# # lang이 증가하여도 함수 변경 없이 그래도 출력되는 것을 볼 수가 있다 

# # 21-4. 전역변수와 지역변수를 사용하는 함수 
# gun = 20
# def checkpoint(soliders):
#     gun = gun - soliders
#     print(f"함수 내에 있는 남은 총 : {gun}")
# checkpoint(soliders)
# # 이렇게 적으면 gun이 정의되어 있지 않다는 오류가 발생됨 
# # 현재 gun은 전역변수로 함수 내에서 쓸 수 가 없어 
# # 저 gun을 쓰기 위해서는 gun을 global로 지정해주거나 인자로 받아와야해 

# #gun을 global로 지정하는 방법 (비권장사항)
# gun = 20 
# def checkpoint(soliders):
#     global gun
#     gun = gun - soliders
#     print(f"함수 내에 있는 남은 총 : {gun}")
# checkpoint(2)

# #gun을 인자로 받는 방법 (권장사항)
# gun = 20 
# def checkpoint(gun, soliders):
#     gun = gun - soliders
#     print(f"함수 내에 있는 남은 총 : {gun}")
#     return gun  # 이렇게 리턴을 해줌으로써 전역변수 건의 값이 변경된다 
    
# gun = checkpoint(gun, 2)
# ##########내가 잘 몰랐던 부분이니 꼭!!!! 반복복습할 것###############

# #Quiz
# import math

# def std_weight(height, gender):
#     if gender == "남자":
#         weight = round((height * height * 22 * 0.0001), 2)
#         print(f"키 {height}cm 남자의 표준 체중은 {weight}kg입니다.")
#     else:
#         weight = round((height * height * 21 * 0.0001), 2)
#         print(f"키 {height} 여자의 표준 체중은 {weight}kg입니다.")

# height = 175
# gender = "남자"
# std_weight(height, gender)


# # 22. 표준입출력
# #sep : pyhton과 java사이에 콤마를 대신할 수 있음 
# print("python", "Java", sep=",")

# #end : end의 기본은 줄바꿈인데 문장의 끝부분을 물음표로 바꾸어주라 
# print("python", "Java", sep=",", end="?")

# import sys
# print("python", "Java", file=sys.stdout)
# print("python", "Java", file=sys.stderr)

# # ljust, rjust 출력되는 문자열 정렬방법
# scores = {"math": 0, "english": 100, "coding": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# #zfill(int) : int만큼 공간을 확보하고 값이 없는 공간은 0(숫자)으로 채워주는 함수 
# # 활용할 수 있는 곳 : 은행 대기순번표 
# for num in range(1, 21):
#     print("대기번호 : " + str(num))

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))
# #input으로 받은 값은 모두 str이니 숫자처리할 때 꼭 type 변경을 진행해야 한다 
# answer = input("아무값이나 입력하세요:")
# print("입력하신 값은 " + answer + "입니다.")



# # 23. 다양한 출력 포맷 
# # 빈 자리를 빈공간으로 두고 오른쪽 정렬을 하되 총 10자리 공간을 확보 
# print("{0: >10}".format(500))
# #양수일땐 +로 표시, 음수일 땐 -로 표시 
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# #왼쪽 정렬하고 빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000000))
# # 3자리 마다 콤마를 찍어주기 및 +-부호도 붙이기 
# print("{0:+,}".format(1000000000000))
# print("{0:+,}".format(-1000000000000))
# #3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릴수 확보하기
# print("{0:^<+30,}".format(1000000000000))
# #소수점 출력
# print("{0:f}".format(5/3))
# #소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))



# 24. 외부에서 파일 불러오기 
#w는 덮어쓰기(없다면 파일 생성하기)
# score_file = open("score.txt", "w", encoding="utf-8")
# print("math:0", file=score_file)
# print("english : 50", file=score_file)
# score_file.close()

#a(append)는 기존에 생성된 파일에 추가하는 것 
# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("science:100")
# score_file.write("\ncoding:100")
# score_file.close()

# #r은 read로 어떤 파일을 읽어오는 것 
# # 한번에 다 읽는 방법 
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# # 한줄 한줄 읽는 방법 
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline(), end="")  
# # 줄별로 읽기 한줄 읽고 커서는 다음 줄로 이동 / end=""가 없다면 한줄씩 띄어서 써짐
# print(score_file.readline())  # 줄별로 읽기 한줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# # 몇줄인지 모를때 총 내용 확인 방법 
# #방법1
# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# #방법2
# score_file = open("score.txt", "r", encoding="utf-8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

# pickle : 프로그램 상에서 사용하고 있는 것을 파일 형태로 다른 사람에게 전달하는 것 
# import pickle
# profile_file = open("profile.pickle", "wb") #wb는 쓰기 
# profile = {"name": "coding", "age": 30, "hobby": ["sdf", "sdfr", "wersdf"]}
# pickle.dump(profile, profile_file) # 프로필에 있는 정보를 file에 저장하는 것 
# profile_file.close()

# profile_file = open("profile.pickle", "rb")  # rb는 읽기 
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# # with 편하게 파일을 읽기 쓰기가 가능하다 
# import pickle
# with open("profile.pickle", "rb") as porfile_file:
#     print(pickle.load(porfile_file))

#with으로 pickle 없이도 파일을 쓰고 읽을 수 있다 
#매번 close를 해줄 필요가 없어서 좋네요! 
# with open("studying.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("나는 파이썬을 다시 정리하고 있습니다. ")

# with open("studying.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())

# Quiz
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건 : 파일명은 1주차.txt, 2주차.txt 와 같이 만듭니다.

# for x in range(1, 6):
#     with open(f"{x}주차.txt", "w", encoding="utf-8") as report_file:
#         report_file.write(f"- {x}주차 주간보고 -")
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")



# #25. class(클래스)
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name} 유닛이 생성되었습니다.")
#         print(f"체력 {self.hp}, 공격력{self.damage}")

# marine1 = Unit("마린", 40, 5)

# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름:{wraith1.name}, 공격력:{wraith1.damage}")
# # 맴버 변수 : 클래스 내에 있는 .으로 시작되는 변수 이고 
# # 클래스 외부에서도 맴버 변수를 이용하여 새로운 유닛을 만들 수 있다. 

# #마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True
# if wraith2.clocking == True:
#     print(f"유닛 이름:{wraith1.name}는 현재 클로킹 상태입니다.")
# #클래스 외부에서 맴버 변수를 확장할 수 있고, 확장을 한 객체(유닛)에만 적용이 되고 
# #기존에 있는 다른 객체에는 적용이 되지 않는다 



# #메소드 
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("f{self.name}:{location} 방향으로 적군을 공격 합니다. [공격력 : {self.damage}]")

#     def damaged(self, damage):
#         print("f{self.name}:{damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print("f{self.name}:{self.hp}입니다.")
#         if self.hp <= 0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("firebat", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)
# 여기에서는 꼭 .format으로 기재해야 출력이 된다 

# #상속 
# #우리는 unit class와 Attack class를 만들었다 
# #그런데 self.name과 self.hp가 중복된다 이에, 상속이라는 개념을 통해서  unit에서 name과 hp를 받아오고자 한다 
# # AttackUnit을 AttackUnit(Unit)로 수정해주고 
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("f{self.name}:{location} 방향으로 적군을 공격 합니다. [공격력 : {self.damage}]")

#     def damaged(self, damage):
#         print("f{self.name}:{damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print("f{self.name}:{self.hp}입니다.")
#         if self.hp <= 0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("firebat", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


# #다중상속 
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("f{self.name}:{location} 방향으로 적군을 공격 합니다. [공격력 : {self.damage}]")

#     def damaged(self, damage):
#         print("f{self.name}:{damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print("f{self.name}:{self.hp}입니다.")
#         if self.hp <= 0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# #날 수 있는 기능을 가진 클래스 
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0}:{1} 방향으로 날아갑니다. [속도{2}]" \
#             .format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스 
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)


# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


#메소드 오버라이딩 
#부모클래스 정의한 메소드 말고 자식 클래스에서 정의한 메소드를 쓰고 싶을 때
#메소드를 새롭게 정의하여 쓸 수 있는데 이를 오버라이딩이라고 한다 

#pass : 함수 내 pass를 기재하면 오류 없이 함수를 종료시키는 역할을 함 
#super : 

# #건물 
# class BuildingUnit(Unit):
#     # def __init__(self, name, hp, location):
#     #     Unit.__init__(self, name, hp, 0)  #건물이니까speed는 0으로 기재
#     #     self.location = location

#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0)  #건물이니까speed는 0으로 기재
#         self.location = location


# #quiz 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

# # (출력 예제)
# # 총 3대의 매물이 있습니다.
# # 강남 아파트 매매 10억 2010년
# # 마포 오피스텔 전세 5억 2007년
# # 송파 빌라 월세 500 / 50 2000년

# # [코드]
# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
    
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("chd {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()


# #예외처리
# try: 
#     print("나누기 전용 계산기입니다")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("첫번째 숫자를 입력하세요: "))
#     #print(f"{num1} / {num2} = {num1/num2}")
#     print("{0}/{1}={2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)


# #예외 발생시키기
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("첫번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print(num1 / num2)  
#     print("{0}/{1}={2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)

# #finally : 에러가 발생되어도 무조건 실행되는 구문
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")


# Quiz 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오
# 조건1 : 1보다 작거나 숫자가 아닌 입력밧이 들어올때는 ValueError로 처리
#        출력 메시지 : "잘못된 값을 이력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#        치킨 소진 시 사용자 정의 에러[soldOutError]를 발생시키고 프로그램 종료
#        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# class soldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while (True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise soldOutError    
#     except ValueError:
#         print("잘못된 값을 이력하였습니다.")
#     except soldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break


# #모듈 : 필요한 것들이 묶음처럼 잘 만들어진 파일 
# import theater_module

# theater_module.price(3)  # 3명이서 영화보러 갔을 때 가격 
# theater_module.price_morning(4)
# theater_module.price_soldier(4)
# # 그런데 이렇게 쓰면 코드가 길어지잖아 그래서 as로 별명을 붙여줄 수가 있어 
# #그런데 그것도 귀찮으니까 이렇게 쓰면 더 짧아져

# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)


# # 패키지 : 모듈을 모아둔 것을 패키지라고 함 
# # 모듈만 패키지만 import가 가능하다 
# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시 
# #glob : 경로 내의 폴더 / 파일 목록 조회 ( 윈도우 dir)
# # OS : 운영체제에서 제공하는 기본 기능 
# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
# else:
#     print(folder, "폴더를 생성합니다.")

# #time : 시간 관련 함수 
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# #timedelta : 두 날짜 사이의 간격 
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은" today + td)

