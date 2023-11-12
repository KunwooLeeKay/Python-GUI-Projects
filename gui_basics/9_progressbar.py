# 프로그래스 바
import tkinter.ttk as ttk # 프로그래스바도 ttk에서 할 수 있음
from tkinter import *
import time

root = Tk() 
root. title("Kunwoo's GUI")
root. geometry("640x480")

progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")
    # maximum : 프로그래스바의 최대 값(%) 지정. 지금 100퍼센트.
    # mode = "indeterminate" : 프로그래스가 언제 끝날지 모를 때 사용(왔다갔다하는 프로그래스 바)
    # mode = "determinate" : 쭈욱 차는 바
progressbar.start(10) # 10ms마다 움직임 - 프로그래스바 속도 설정
progressbar.pack()

def btncmd():
    progressbar. stop() # 작동 중지

btn = Button(root, text = "중지", command = btncmd)
btn. pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
    # length : 프로그래스바의 길이 지정
    # variable : 프로그래스 진행상황 저장 변수
progressbar2. pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100까지. -> 1초짜리 프로그래스 바
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # 프로그래스바의 값 설정
        progressbar2. update() # 포문을 돌때마다 GUI를 업데이트해주는 구문. 이걸 안하면 for문이 다 끝나고 업뎃한다.
        print(p_var2.get()) 

btn2 = Button(root, text = "시작", command = btncmd2)
btn2. pack()


root. mainloop()