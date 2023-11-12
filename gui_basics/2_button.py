# 위젯 : 체크박스, 텍스트박스 등등
from tkinter import *

root = Tk()
root. title("Kunwoo's GUI")
root. geometry("640x480")

btn1 = Button(root, text = "버튼1") # 버튼 변수 이름 = Button(어디에 띄울것인지, text = "버튼 이름")
btn1.pack() # 변수이름. pack() 을 해줘야 실제 창에서 나타난다.

btn2 = Button(root, padx = 5, pady = 10, text = "버튼2") # padx, pady : 버튼이 들어가는 여백 크기 조절
btn2. pack()

btn3 = Button(root, padx = 10, pady = 5, text = "버튼3")
btn3. pack()

btn4 = Button(root, width = 10, height = 3, text = "버튼4") # width, height : 버튼 자체의 크기 조절
btn4. pack()
# padx,y 와 width/height의 차이 : pad는 이름이 길어지면 버튼 크기도 길어지지만 width/height는 글자가 잘려도 크기는 변하지 않는다

btn5 = Button(root, fg = "red", bg = "yellow", text = "버튼5") # fg : 글자 색, bg : 버튼 색. 인데, Mac에선 bg안댐
btn5. pack()

# 이미지를 사용해서 버튼 만들기
photo = PhotoImage(file = "gui_basic/img1.png") # PhotoImage : 파일에 해당하는 것을 불러와 이미지로 저장해줌
btn6 = Button(root, image = photo) # image : 버튼에 들어갈 이미지 설정
btn6. pack()

# 버튼 동작 만들기
def btncmd():
    print("버튼이 클릭되었어요!")

btn7 = Button(root, text = "동작하는 버튼", command = btncmd) # command 속성을 통해 버튼의 기능을 설정할 수 있다.
btn7. pack()

root. mainloop()