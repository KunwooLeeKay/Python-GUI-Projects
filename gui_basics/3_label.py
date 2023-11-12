# 레이블 : 글자, 이미지를 보여주기만 하는 것. 동작 불가

from tkinter import *

root = Tk()
root. title("Kunwoo's GUI")
root. geometry("640x480")

label1 = Label(root, text = "안녕하세요")
label1.pack()

photo = PhotoImage(file = "gui_basic/img1.png")
label2 = Label(root, image = photo)
label2. pack()

# 버튼을 눌렀을 때 레이블 내용을 변경하기
def change():
    label1. config(text = "또 만나요~") #config를 이용하면 해당 레이블의 내용을 바꾸도록 할 수 있다.

    global photo2 # global선언 : 지역변수면 change 함수가 끝났을 때 photo2의 값을 버리기 때문에 이미지가 사라진다.
    photo2 = PhotoImage(file = "gui_basic/img2.png")
    label2. config(image = photo2)

btn = Button(root, text = "클릭", command = change)
btn.pack()

root. mainloop()