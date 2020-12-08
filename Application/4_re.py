import re
# 정규식은 import re 통해 사용할 수 있음 
# p는 패턴 
# . : 하나의 문자를 의미한다 
# ^ : 문자열의 시작 
# $ : 문자열의 끝 
p = re.compile("ca.e")

# 매칭되었는지 안되었는지 확인하는 방법  
def print_match(m):        
    if m:
        print("m.group():", m.group())
        print("m.string", m.string)
        print("m.start():", m.start())
        print("m.end()", m.end())
        print("m.span():", m.span())
    else:
        print("매칭되지 않음")

# m = p.match("case") 
# # match의 경우 주어진 문자열의 처음부터 일치하는지를 확인하기에 careless라고 하면 일치한다고 나오게 됨 

# m = p.search("case")
# print_match(m)
# # search : 주어진 문자열 중에 일치하는게 있는지 확인 

lst = p.findall("good care")
#findall : 일치하는 모든 것을 리스트 형태로 반환 
print(lst)


# 정규식 정리 
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")
# 3. m = p.search("비교할 문자열")
# 4. lst = p.findall("비교할 문자열") -> 리스트 형태로 !! 


