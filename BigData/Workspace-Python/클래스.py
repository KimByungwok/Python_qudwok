# 기본적인 클래스 선언
class MyClass:
    my_field = 10
    
    def my_method(self):
        print(self.my_field)

# 객체 생성
my_object = MyClass()

# 객체의 필드와 메서드 참조
my_object.my_field = 20
my_object.my_method()

# 생성자
class Student:
    def __init__(self, name, sno):
        self.name = name
        self.sno = sno

# 생성자 사용한 객체 생성
s1 = Student('김경민', '19830001')    
print(s1.name, s1.sno)

# 생성자와 메소드
class Student:
    # 마지막 __init__() 만 적용됨
    def __init__(self, name, sno):
        self.name = name
        self.sno = sno

    def __init__(self, name):
        self.name = name
        self.sno = None
    
    def __init__(self):
        self.name = None
        self.sno = None
    
    def get_name(self): return self.name    
    def get_sno(self): return self.sno
    def set_name(self, name): self.name = name
    def set_sno(self, sno): self.sno = sno

# 매개변수 없는 생성자 호출
s1 = Student() 
print(s1.name)

s1.set_name('홍길동')  
s1.set_sno('20830001')

print(s1.get_name(), s1.get_sno())

# 매개변수 1개 생성자 호출
#s2 = Student('김경민')
#print(s2.name)
#print(s2.sno)

# 필드 삭제
del s1.sno
#print(s1.get_sno())   # 오류 발생

# 필드 추가
s1.set_sno('20830001') 
print(s1.get_sno())    # 필드 존재 확인

# 아무 것도 없는 클래스
class Dummy:
    pass

# 객체에 멤버변수(속성) 추가
o1 = Dummy()
print(type(o1))

o1.x = 10
print(o1.x)

# 새로운 Dummy 객체에는 x가 있을까?
o2 = Dummy()
#print(o2.x)    # 원래 Dummy 클래스에는 없음


# 클래스 상속
class Parent:
   family_name = None

   def __init__(self, family_name):
       self.family_name = family_name

class Child(Parent):
    name = None

    def __init__(self, family_name, name):
        self.family_name = family_name
        self.name = name


me = Child('김', '경민')
print(me.family_name, me.name)

# 클래스 다중 상속
class A:
    a = None

class B:
    b = None

class C(A,B):
    c = None
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def printAll(self):
        print('{},{},{}'.format(self.a,self.b,self.c))

obj = C(10, 20, 30)
obj.printAll()

# 클래스 메소드 오버라이딩
class Parent:
   family_name = None

   def __init__(self, family_name):
       self.family_name = family_name
        
   def print_name(self):
       print(self.family_name)


class Child(Parent):
    name = None

    def __init__(self, family_name, name):
        self.family_name = family_name
        self.name = name

    def print_name(self):
       print(self.family_name, self.name)

    def print_family_name(self):
        super().print_name()
        print(self.name)

me = Child('김', '경민')
me.print_name()
me.print_family_name()        
