# 메뉴 바

from tkinter import *

root = Tk() 
root.title("Kunwoo's GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root) # menu라는 변수에 root 에 넣을 메뉴를 Menu(root)를 통해 정의

# File 메뉴
menu_file = Menu(menu, tearoff = 0) # menu_file 변수를 만들어 menu라는 변수에 들어갈 내용을 정의
menu_file.add_command(label = "New File", command = create_new_file) # menu_file 속에 있을 커멘드들을 정의
menu_file.add_command(label = "New Window")
menu_file.add_separator() # 나눠주는 선 삽입
menu_file.add_command(label = "Open File...")
menu_file.add_separator()
menu_file.add_command(labe = "Save All", state = "disable") # state를 통해 비활성화
menu_file.add_separator()
menu_file.add_command(label = "Exit", command = root.quit) # command = root.quit 하면 종료버튼임

menu.add_cascade(label = "File", menu = menu_file)
    # .add_cascade를 하면 File이라는 레이블의 메뉴가 생기고, menu_file에 정의한 내용이 들어간다.

# Edit 메뉴
menu_edit = Menu(menu, tearoff = 0)
menu_edit.add_command(label = "Edit")
menu.add_cascade(label = "Edit", menu = menu_edit) 
# 빈 메뉴를 만들땐 add_cascade 후 그냥 label만 적어주면 된다.근데 맥에서는 command가 없으면 안생기네...

# 라디오 버튼이 들어간 메뉴 추가 (라디오 버튼을 통해 택 1 을 하게 해주는 버튼)
menu_lang = Menu(menu, tearoff = 0)
menu_lang.add_radiobutton(label = "Python") # add_radiobutton으로 라디오 버튼 추가
menu_lang.add_radiobutton(label = "Java")
menu_lang.add_radiobutton(label = "C++")
menu.add_cascade(label = "Language", menu = menu_lang)

# 체크박스 추가
menu_view = Menu(menu, tearoff = 0)
menu_view.add_checkbutton(label = "Show Minimap") # add_checkbutton으로 체크버튼 추가
menu_view.add_checkbutton(label = "Show Interface")
menu.add_cascade(label = "View", menu = menu_view)
# 근데 맥에선 특정 버튼 : Edit, View와 같은 이름의 버튼이 생성되면 기본으로 제공되는 기능이 있는듯. 안만든 메뉴가 생김. 

root.config(menu = menu)

root. mainloop()