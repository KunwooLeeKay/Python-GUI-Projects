# 그리드
# pack()을 사용하면 위젯을 계속 쌓아가는 느낌으로 넣음. 반면 그리드를 이용하면 좌표를 이용해서 위젯을 원하는 위치에 넣을 수 있음

# ++ : grid에 sticky 속성 추가
# ++ : Button에 padx, pady 추가 (버튼 크기 변경) - 근데 이렇게하면 enter처럼 글이 길면 버튼이 더 커짐 
#        ->그게 싫다면 width, height속성으로 하기. 근데 왠지 모르겠지만 mac에선 정렬이 안되네..?
# ++ ; grid에 padx, pady 추가 (버튼간 간격 변경)

from tkinter import *
root = Tk()
root.title("Kunwoo's GUI")
root.geometry("640x480")

# btn_f16 = Button(root, text = "F16", padx = 10, pady = 10) # padx, pady이용법
btn_f16 = Button(root, text = "F16", width = 5, height = 2)
btn_f17 = Button(root, text = "F17", width = 5, height = 2)
btn_f18 = Button(root, text = "F18", width = 5, height = 2)
btn_f19 = Button(root, text = "F19", width = 5, height = 2)

# sticky 속성 : 위젯을 그리드의 크기만큼 동서남북으로 늘려줌(방향 설정 가능)
btn_f16.grid(row = 0, column = 0, sticky = N+E+W+S, padx = 3, pady = 3) 
btn_f17.grid(row = 0, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_f18.grid(row = 0, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_f19.grid(row = 0, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

# clear 줄
btn_clear = Button(root, text = "clear", width = 5, height = 2)
btn_equal = Button(root, text = "=", width = 5, height = 2)
btn_div = Button(root, text = "/", width = 5, height = 2)
btn_mul = Button(root, text = "*", width = 5, height = 2)

btn_clear.grid(row = 1, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_equal.grid(row = 1, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_div.grid(row = 1, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_mul.grid(row = 1, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

# 7 숫자 줄

btn_7 = Button(root, text = "7", width = 5, height = 2)
btn_8 = Button(root, text = "8", width = 5, height = 2)
btn_9 = Button(root, text = "9", width = 5, height = 2)
btn_sub = Button(root, text = "-", width = 5, height = 2)

btn_7.grid(row = 2, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_8.grid(row = 2, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_9.grid(row = 2, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_sub.grid(row = 2, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

# 4 숫자 줄

btn_4 = Button(root, text = "4", width = 5, height = 2)
btn_5 = Button(root, text = "5", width = 5, height = 2)
btn_6 = Button(root, text = "6", width = 5, height = 2)
btn_add = Button(root, text = "+", width = 5, height = 2)

btn_4.grid(row = 3, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_5.grid(row = 3, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_6.grid(row = 3, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_add.grid(row = 3, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

# 1 숫자 줄

btn_1 = Button(root, text = "1", width = 5, height = 2)
btn_2 = Button(root, text = "2", width = 5, height = 2)
btn_3 = Button(root, text = "3", width = 5, height = 2)
btn_enter = Button(root, text = "enter", width = 5, height = 2)

btn_1.grid(row = 4, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_2.grid(row = 4, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_3.grid(row = 4, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_enter.grid(row = 4, column = 3, rowspan = 2, sticky = N+E+W+S) 
    # rowspan을 하면 row를 합칠 수 있음. 현재 위치로부터 아래쪽으로 먹는 면적

# 1 숫자 줄

btn_0 = Button(root, text = "0", width = 5, height = 2)
btn_point = Button(root, text = ".", width = 5, height = 2)

btn_0.grid(row = 5, column = 0, columnspan = 2, sticky = N+E+W+S)
    # columnspan을 하면 column을 현재 위치로부터 오른쪽으로 먹는 면적 설정 가능.
btn_point.grid(row = 5, column = 2, sticky = N+E+W+S)

root.mainloop()