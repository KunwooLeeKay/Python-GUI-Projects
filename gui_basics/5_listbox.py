# 리스트 박스

from tkinter import *

root = Tk() 
root. title("Kunwoo's GUI")
root. geometry("640x480")

listbox = Listbox(root, selectmode = "extended", height = 0) 
    # selectmode - extended : 다중선택 가능 (single: 하나만)
    # height : 0이면 리스트에 있는 모든 것 출력, 특정 숫자면 특정 숫자만큼만 보여줌(스크롤 내리면 더 볼 수 있음)
listbox. insert(0, "사과")
listbox. insert(1, "딸기")
listbox. insert(2, "바나나")
listbox. insert(END, "수박") # 그냥 END로 적으면 맨 마지막으로 리스트를 작성해줌
listbox. insert(END, "포도")
listbox. pack()

def btncmd():
    # 리스트에서 삭제
    # listbox. delete(END) # 버튼을 누를떄마다 맨 뒤 항목을 삭제
    # listbox. delete(0) # 버튼을 누를떄마다 맨 앞 항목을 삭제
    
    # 갯수 확인 : size
    print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 : get
    print("1번째부터 3번째까지의 항목 :", listbox. get(0, 2))

    # 선택된 항목 확인 : curselection - 선택된 인덱스값 반환
    print("선택된 항목 :,", listbox.curselection())

btn = Button(root, text = "클릭", command = btncmd)
btn. pack()

root. mainloop()