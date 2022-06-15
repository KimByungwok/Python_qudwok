def my_function(name):
  print(name)

f = my_function
f("김경민")
f("홍길동")
f("유관순")

def no_return():
    pass

print(no_return())


globals()

def swap(x, y):
  return y, x

a, b = swap(10, 20)
print('{},{} ==> {},{}'.format(10, 20, a, b))

x = swap(10, 20)
print(x)
print(type(x))

def intersect(l_list, r_list):
  result = []
  for x in l_list:
    if x in r_list and x not in result:
      result.append(x)

  return result

r = intersect("hotdog","dot")
print(r)


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

s = ['J','A','M']
change(s)
print(s)

# mutable 자료형에 대한 파라메터 변경 방지
def change(x):
  x = x[:]
  x[0] = 'H'

s = ['J','A','M']
change(s)
print(s)

g = 1

def scoping(a):
  global g
  g += a

print(g)
scoping(5)
print(g)

#dir(__builtins__)

# 함수 인자 : 기본값
def my_function( major= "융합소프트웨어"):
  print("제 전공은 " + major + "입니다.")

my_function("정보통신")
my_function("사회복지")
my_function()
my_function("간호학")

# 함수 인자 : 인자 갯수 미확정
def lunch_menu(*foods):
  print(type(foods))
  print('매개변수의 갯수: {}'.format(len(foods)))
  for food in foods:
    print(food)

lunch_menu('햄버거', '샌드위치', '핫도그')


# 함수 인자 : 키워드 인자
def my_function(student3, student2, student1):
  print("3번째 학생 " + student3)

my_function(student1 = "홍길동", student2 = "이순신", student3 = "김경민")

# 함수 인자 : 매개변수 갯수 모를 때
def lunch_menu(**foods):
  print(type(foods))
  keys = foods.keys()
  for key in keys:
    print("{}은 {}".format(key, foods[key]))


lunch_menu(한식 = "육개장", 중식 = "짬뽕", 일식 = "돈까스")

# lambda function
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))