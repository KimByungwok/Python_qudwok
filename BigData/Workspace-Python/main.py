import mypkg.operation as op   # calcpkg 패키지의 operation 모듈을 가져옴
import mypkg.geometry     # calcpkg 패키지의 geometry 모듈을 가져옴
 
print(op.add(10, 20))    # operation 모듈의 add 함수 사용
print(op.mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(mypkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(mypkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용