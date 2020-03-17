#제곱
x=2;
y=3;
print(x**y);


#여러 라인을 문자열로
str="""
hello
sample
"""


#조건문
if not 1>2:
    print("Hello")



#함수
def 함수명(str1, num):
	print("%s : Function" % str1) #문자열은 %s, 숫자형은 %d
	print("%d : Function" % num)
#호출
함수명("인자1", 10)



#반복문
for i in range(3):	# range(a) -> a번 반복(0부터 시작은 같음)
	print("반복문")



#리스트
a=list()
b=[]
print(b[x]) # b리스트의 x번째 데이터 출력

len(b) # b리스트의 길이
sorted(b) # b리스트를 정렬
sum(b) # b리스트들의 데이터를 합함
b.index("데이터") # b리스트에서 "데이터" 원소의 자리를 찾음, 없으면 에러
"데이터" in b # b리스트에서 "데이터" 원소가 있는지 확인, true/false

for n in b: # b리스트의 데이터를 차례로 출력
	print(n) 



#튜플
a=tuple()
b=()
#리스트함수사용가능
#리스트와 비슷 but 튜플은 선언한 데이터를 따로 바꿀 수 없음(immutable)



#딕셔너리: key와 value로 이루어져 있음
a=dic()
b={
	key: value
	#JS의 객체/리스트와 비슷
}
#리스트함수사용가능



#간단한 알고리즘 예제
#리스트 안의 원소들의 개수를 세어라
fruit=["사과","사과","딸기","복숭아","복숭아","복숭아","키위"]
d={}
for i in fruit: #fruit리스트의 원소를 i에 대입
	if i in d: #d딕셔너리에 i가 있으면
		d[f]=d[f]+1 #개수1증가
	else: #d딕셔너리에 i가 없으면
		d[f]=1 #d딕셔너리에 넣고 개수는 1로 



#클래스
class 클래스명:
	__init__(self, 변수명): #인스턴스 호출을 도와줌
		~ ~ ~
	def 함수명:
		~ ~ ~

p = 클래스명(변수) #인스턴스, 
p.함수명() #p클래스 안의 함수를 호출



#상속
class 클래스명(부모클래스명):
	~ ~ ~



#패키지
#폴더로 만듦(폴더이름=패키지이름) -> 폴더 안에 파일명.py 파일들 생성

#__init__.py : 폴더가 패키지라는 것을 알려주는 파일 -> 모든 모듈들을 import함
	#from .파일명 import 해당파일의클래스명 or *(모든코드)
	# . 의미 -> "이 폴더에 있는"

#외부에서 패키지 사용 -> from 패키지명(폴더명) import 파일명
