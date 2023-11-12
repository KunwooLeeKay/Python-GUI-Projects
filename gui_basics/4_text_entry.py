from tkinter import *

root = Tk() 
root. title("Kunwoo's GUI")
root. geometry("640x480")

# Text : 텍스트를 입력받음
txt = Text(root, width = 30, height = 5)
txt.pack()

txt. insert(END, "글자를 입력하세요") # insert를 사용하면 기본 값을 설정할 수 있다. 앞의 END는 글자가 들어갈 위치이다.

# Entry : 1줄의 텍스트만 입력받을 수 있는 것.
e = Entry(root, width = 30)
e.pack()
e.insert(0, "한줄만 입력해요") # 기본값 설정. 앞의 0은 END와 유사한 기능이다.

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) 
        # 이렇게 쓰면 버튼을 눌렀을 때 txt 안에 있는 내용을 get으로 가져올 수 있는데, 이때 "1.0"은
        # 1행 0열(첫번째 자리), END는 끝까지를 의미하여 처음부터 끝까지 가져오게 된다.
    print(e.get()) # 엔트리에서 가져올 때에는 엔트리 이름. get() 하면 끝난다.

    # 내용 삭제
    txt. delete("1.0", END)
    e. delete(0, END)

btn = Button(root, text = "클릭", command = btncmd)
btn. pack()

root. mainloop()