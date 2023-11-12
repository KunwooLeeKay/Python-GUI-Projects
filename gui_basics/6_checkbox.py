# 체크 박스

from tkinter import *

root = Tk() 
root. title("Kunwoo's GUI")
root. geometry("640x480")

chkvar = IntVar() # chkvar변수에 int형으로 값을 저장한다는 뜻이다. (IntVar() 명령아)
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable = chkvar)
    # 체크박스를 쓸 때에는 variable이라고 쓰고 int형 변수를 넣어줘서 체크여부를 변수에 저장해줘야한다.
chkbox.select() # 선택 처리
chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일동안 보지 않기", variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크 됨
    print(chkvar2.get())

btn = Button(root, text = "클릭", command = btncmd)
btn. pack()

root. mainloop()