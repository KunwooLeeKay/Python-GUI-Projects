# 콤보 박스

import tkinter.ttk as ttk # 콤보박스는 tkinter.ttk에 있어서, 호출해서 써야함
from tkinter import *

root = Tk() 
root. title("Kunwoo's GUI")
root. geometry("640x480")

# 콤보 박스
values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values = values) # height: 목록을 몇개 보이게 할건지, values: 값을 반환
combobox. pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정 
# 그런데 이렇게 설정하면 날짜를 고르는 것 외에 그냥 직접 입력할 수도 있고, 그게 반환됨. -> 에러가 날 수 있음

# state = "readonly" 하면 입력이 안되는 콤보박스가 된다.
readonly_combobox = ttk.Combobox(root, height = 10, values = values, state = "readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox. pack()
# readonly_combobox.set("카드 결제일") 여기선 이거 하면 안됨. 날짜만 들어가게 하려고 한거니까. (그대로 입력누르면...)


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text = "선택", command = btncmd)
btn. pack()

root. mainloop()