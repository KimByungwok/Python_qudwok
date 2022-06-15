# 정상적인 경우
try:
    print(10/2)
except:
    print('예외 발생...')

# 비정상적인 경우
try:
    print(10/0)
except:
    print('예외 발생...')

# except의 종류 알아보기
print(10/0)

# except의 종류에 대한 처리
try:
    print(10/0)
except ZeroDivisionError:
    print('분모가 0입니다.')

# 여러개의 예외가 발생하는 경우 처리
try:
    a = [1,2]
    print(a[3])
    print(10/0)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱스 범위를 벗어났습니다.")

# 여러개의 예외에 대한 예외 객체 다루기
try:
    a = [1,2]
    #print(a[3])
    print(10/0)
except ZeroDivisionError as e1:
    print(e1)
except IndexError as e2:
    print(e2)

# 여러개의 예외를 한꺼번에 처리하기
try:
    a = [1,2]
    print(a[3])
    print(10/0)
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 오류 회피
try:
    f = open("없는파일.txt", 'r')
except FileNotFoundError:
    pass

# else 사용하기
try:
  print(10/2)
  #print(10/0)
except:
  print("앗 뭔가 잘못되었습니다.")
else:
  print("다 잘 처리되었습니다.")

# finally 사용하기
try:
  print(10/2)
  print(10/0)
except:
  print("앗 뭔가 잘못되었습니다.")
else:
  print("다 잘 처리되었습니다.")
finally:
  print("잘되든 잘못되든 마무리는 여기서...")

# 예외를 강제로 발생시키기
def checkInt(x):
    if not type(x) is int:
        raise TypeError("정수가 아니네?")
    return True

try:
    #checkInt("hello")
    checkInt(100)
except:
    print('정수가 아닌가봅니다.')
else:
    print('정수네...')

# 사용자 정의 예외를 만들어 처리하기
class NotIntegerException(Exception):
    pass

def checkInt(x):
    if not type(x) is int:
        raise NotIntegerException()
    return True

try:
    checkInt("hello")
    checkInt(100)
except NotIntegerException:
    print('정수가 아닌가봅니다.')
else:
    print('정수네...')

# 사용자 정의 예외를 만들고 커스텀 메시지 출력하도록 하기
class NotIntegerException(Exception):
    def __str__(self):
        return 'Not Integer Number excecption'

def checkInt(x):
    if not type(x) is int:
        raise NotIntegerException()
    return True

try:
    checkInt("hello")
    checkInt(100)
except NotIntegerException as e:
    print(e)
else:
    print('정수네...')

