# 프레임 : 여러개의 위젯들을 하나의 프레임에 넣어놓는 것

from tkinter import *

root = Tk() 
root. title("Kunwoo's GUI")
root. geometry("640x480")

Label(root, text = "메뉴를 선택해 주세요."). pack(side = "top")
Button(root, text = "주문하기"). pack(side = "bottom")

# 버거 프레임
frame_burger = Frame(root, relief = "solid", bd = 1) # relief : 테두리, bd : 두께(?)
frame_burger.pack(side = "left", fill = "both", expand = True) 
    # side : 어디에 프레임을 배치할지, fill : 위아래로 꽉차게, expand = True : 창의 가운데까지 확장
    # pack할때 변경 가능

Button(frame_burger, text = "햄버거").pack() # root가 아닌 frame_burger를 써서 메인이 아닌 프레임 속에 버튼이 들어가도록 함
Button(frame_burger, text = "치즈버거").pack()
Button(frame_burger, text = "치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text = "음료") # 이런식으로 작성하면 프레임에 이름을 지정할 수 있다.
frame_drink.pack(side = "right", fill = "both", expand = True)

Button(frame_drink, text = "콜라"). pack()
Button(frame_drink, text = "사이다"). pack()

root. mainloop()