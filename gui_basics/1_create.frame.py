# from tkinter import *
# root = Tk() 
# root.mainloop() # 창이 닫히지 않도록 설정 
# # 이게 기본적인 양식임. 이렇게 설정하면 창이 뜨는 GUI를 만들 수 있음

from tkinter import *

root = Tk() # root는 메인 창이라는 뜻
root. title("Kunwoo's GUI") # 창 이름 설정
root. geometry("640x480") # 창 크기 설정. 곱하기는 영문 x를 사용한다.
#root. geometry("640x480+100+300") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # 너비, 높이크기 변경 가능 여부 -> 이렇게 하면 크기변경 불가

# 위젯 : 체크박스, 텍스트박스 등등

root. mainloop()