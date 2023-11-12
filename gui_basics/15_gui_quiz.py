# 메모장 프로그램 만들기

from tkinter import *
import os # 파일이 있는지 없는지 확인한후 실행하기 위해 임포트함

root = Tk()
root.title("제목없음 - Mac 메모장")
root.geometry("640x480")
root.resizable(True, True)

filename = "mynote.txt" # 파일을 열고닫고 하며 조정하기 위해선 파일 이름에 해당하는 변수를 만들어줘야함

def open_file():
    if os.path.isfile(filename): # 파일이 있다면 TRUE 없으면 FALSE 반환 -> 파일이 있을때만 가져오게 함.
        print("파일을 엽니다...")
        with open (filename, "r", encoding = "utf8") as file_open:
            txt. delete("1.0", END) # 이 부분이 없다면 txt 위젯 뒤에 그냥 내용을 계속 이어서 붙이게 됨. 삭제하고 넣기
            txt. insert(END, file_open.read()) # txt.insert를 통해 내용 추가.
def save_file():
    print("파일을 저장합니다...")
    with open(filename, "w", encoding = "utf8") as file_save:
        file_save.write(txt. get("1.0", END)) # write, get을 활용한 파일저장

    

menu = Menu(root) # 이건 한번만 선언해야함. 계속 하면 덮어쓰기 됨.

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "열기", command = open_file)
menu_file.add_command(label = "저장", command = save_file)
menu_file.add_separator()
menu_file.add_command(label = "끝내기", command = root.quit)

menu.add_cascade(label = "파일", menu = menu_file)

# edit
menu_edit = Menu(menu, tearoff = 0)
menu_edit.add_command(label = "편집")
menu_edit.add_command(label = "삽입")

menu.add_cascade(label = "편집", menu = menu_edit)

# about
menu_about = Menu(menu, tearoff = 0)
menu_about.add_command(label = "서서식식")
menu_about.add_command(label = "서식서식")

menu.add_cascade(label = "서식", menu = menu_about)

# view
menu_view = Menu(menu, tearoff = 0)
menu_view.add_command(label = "보보기기")
menu_view.add_command(label = "보기보기")
menu.add_cascade(label = "보기", menu = menu_view)

frame_main = Frame(root, relief = "solid")
frame_main.pack(fill = "both")

bar = Scrollbar(frame_main)
bar. pack(side = "right", fill = "y")

txt = Text(frame_main, width = 640, height = 320, yscrollcommand = bar.set)
txt.pack(side = "left", fill = "both")

bar.config(command = txt.yview)
root.config(menu = menu)
root.mainloop()