# 함수 기본 구조
def my_function(name):
    print(name)

f = my_function
f("김경민")
f("홍길동")
f("유관순")

# 아무 일도 하지 않는 함수
# return 문이 없는 경우 값의 반환 : None
def no_return():
    pass

print(no_return())

# 내장 함수 및 사용자 정의 함수 확인
globals()

# 여러 값의 반환
def swap(x, y):
    return y, x


# 개별 값 반환
a, b = swap(10, 20)
print('{},{} ==> {},{}'.format(10, 20, a, b))
print(type(a))
print(type(b))

# 투플을 반환
x = swap(10, 20)
print(x)
print(x[0], x[1])
print(type(x))

# 리스트를 반환
def intersect(l_list, r_list):
    result = []
    for x in l_list:
        if x in r_list and x not in result:
            result.append(x)

    return result


r = intersect("hotdog", "dot")
print(r)
print(type(r))

# 함수 매개변수 전달
# immutable
a = 10
b = 20


def my_sum1(x, y):
    return x + y


print(my_sum1(a, b))


def my_sum2(x, y):
    x = 1
    return x + y


a = 10
b = 20
print('함수호출 전 a의 값은 {}'.format(a))
print(my_sum2(a, b))
print('함수호출 후 a의 값은 {}'.format(a))


# mutable
def change(x):
    x[0] = 'H'


s = ['J', 'A', 'M']
change(s)
print(s)

# mutable 자료형에 대한 파라메터 변경 방지
def change(x):
    x = x[:]
    x[0] = 'H'


s = ['J', 'A', 'M']
change(s)
print(s)

# local 영역에서 global 영역 변수 사용
g = 1


def scoping(a):
    global g
    g += a


print(g)
scoping(5)
print(g)

# dir(__builtins__)

# 함수 인자 : 기본값
def my_function(major="융합소프트웨어"):
    print("제 전공은 " + major + "입니다.")


my_function("정보통신")
my_function("사회복지")
my_function()
my_function("간호학")

# 함수 인자 : 키워드 인자
def my_function(student3, student2, student1):
    print("3번째 학생 " + student3)


my_function(student1="홍길동", student2="이순신", student3="김경민")


# 함수 인자 : 인자 갯수 미확정
def lunch_menu(*foods):
    print(type(foods))
    print('매개변수의 갯수: {}'.format(len(foods)))
    for food in foods:
        print(food)

lunch_menu('햄버거', '샌드위치', '핫도그')

# 함수 인자 : 매개변수 갯수 모를 때
def lunch_menu(**foods):
    print(type(foods))
    keys = foods.keys()
    for key in keys:
        print("{}은 {}".format(key, foods[key]))


lunch_menu(한식="육개장", 중식="짬뽕", 일식="돈까스")

# lambda function
def x(a): return a + 10

print(x(5))

def x(a, b): return a * b

print(x(5, 6))

def x(a, b, c): return a + b + c

print(x(5, 6, 2))
