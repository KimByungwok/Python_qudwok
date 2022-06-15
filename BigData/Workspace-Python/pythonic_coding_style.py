'''
s = 'a b c'
l = s.split()

# l의 데이터 타입은?
print(type(l))
print(l)

# 문자열을 공백으로 분리해서 개별적인 변수에 값 저장
a, b, c = s.split()
print('a의 값은 {}, b의 값은 {}, c의 값은 {}'.format(a, b, c))
print(type(a))

# split()함수를 사용해서 개별 자료항목으로 unpack 하는 경우
# 자료항목 갯수와 값을 받을 변수의 갯수가 일치해야 함

# 분리될 자료 갯수보다 적은 수의 변수로 받는 경우
#a, b = s.split() # 에러

# 분리될 자료 갯수보다 많은 수의 변수로 받는 경우
# a, b, c, d = s.split() # 에러

# 문제 : url 문자열을 입력받아 어느나라 도메인인지 알아내는 프로그램을 작성하라.
# 예) >>>url을 입력하세요 : http://www.kyungmin.ac.kr
#     >>>한국 도메인 입니다.


url = input('url을 입력하세요 : ')
url_list = url.split('.')
tid = url_list[len(url_list)-1]
if tid == 'kr':
    print('한국 도메인 입니다')
elif tid == 'us':
    print('미국 도메인 입니다')
elif tid == 'cn':
    print('중국 도메인 입니다')
elif tid == 'jp':
    print('일본 도메인 입니다')
else:
    print('모르겠는데?')

result = [ i for i in range(10)]
print(result)


# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]와 같은 리스트가 있을 때
# l2 = [2, 3, 4, 5]이 되도록 l1을 사용해서 처리해 보자!
# 리스트 컴프리헨션 방법 사용
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [i for i in l1[2:6]]
print(l2)


result = [ i for i in range(10) if i%2 == 0]
print(result)

# else 부분의 값을 반드시 써야 함
result = [ i if i%2 == 0 else 10 for i in range(10) ]
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

for i in stuff:
    print(i)
'''
l1 = ['a1', 'a2', 'a3', 'a4']
l2 = ['b1', 'b2', 'b3']
l3 = ['c1', 'c2', 'c3', 'c4']
'''
# l1, l2, l3를 zip() 함수를 사용해 하나의 리스트 항목으로 묶어라
l = [ [a,b,c] for a,b,c in zip(l1, l2, l3)]
print(l)
'''
a,b,c = zip(l3, l2, l1)
print(a, b, c)