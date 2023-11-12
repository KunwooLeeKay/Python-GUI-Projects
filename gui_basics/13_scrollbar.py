# 스크롤 바

from tkinter import *
root = Tk()
root.title("Kunwoo's GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame) # 스크롤바를 만들 때, 리스트박스랑 스크롤바를 다 프레임 하나에 집어넣고 하는게 관리하기 편함.
scrollbar.pack(side = "right", fill = "y") # fill = "y"를 해줘야 상하로 꽉찬 스크롤바가 생긴다.


listbox = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand = scrollbar.set) 
    # yscrollcommand = scrollbar.set 을 해줘야 상호작용 가능
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side = "left")

scrollbar.config(command = listbox.yview)
    # 이쪽에서도 스크롤바 이름. config(command = 리스트박스 이름. yview) 해줘야 상호작용이 가능하다.

root.mainloop()