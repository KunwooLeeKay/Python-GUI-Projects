# 라디오 박스 : 보기중 하나를 고르는 버튼

from tkinter import *

root = Tk() 
root. title("Kunwoo's GUI")
root. geometry("640x480")

Label(root, text = "메뉴를 선택하세요"). pack() # 레이블의 값을 바꿀 일이 없다면 이렇게 써도 됨

# 라디오
burger_var = IntVar() # 변수를 하나에 할당해서 하나를 고르면 나머지가 해제되도록 설정하는 식
btn_burger1 = Radiobutton(root, text = "햄버거", value = 1, variable = burger_var)
btn_burger1. select() # 기본으로 햄버거 선택
btn_burger2 = Radiobutton(root, text = "치즈버거", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "치킨버거", value = 3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text = "음료를 선택하세요"). pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "콜라", value = "콜라", variable = drink_var)
btn_drink1. select()
btn_drink2 = Radiobutton(root, text = "사이다", value = "사이다", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var. get()) # 햄버거 중 선택된 라디오 항목의 값(value)를 반환
    print(drink_var.get())

btn = Button(root, text = "주문", command = btncmd)
btn. pack()

root. mainloop()