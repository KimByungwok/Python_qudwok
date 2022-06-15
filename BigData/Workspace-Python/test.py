import my_lib as m
print(m.hello_string)

del m

print(m.hello_string)

# 지웠던 패키지를 다시 메모리에 적재
import importlib
import my_lib as m
importlib.reload(m)
print(m.hello_string)


