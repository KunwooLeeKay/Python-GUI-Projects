from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root. title("건우의 사진 합치기 프로그램")

# 파일 프레임 : 맨 위에 있는 파일 추가 / 선택 삭제가 있는 영역
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

btn_add_file = Button(file_frame, pady = 5, width = 12, text = "파일 추가")
btn_add_file. pack(side = "left")

btn_delete_file = Button(file_frame, pady = 5, width = 12, text = "선택 삭제")
btn_delete_file. pack(side = "right")

# 리스트 프레임 : 파일 목록이 뜨는 리스트
list_frame = Frame(root)
list_frame.pack(fill = "both", padx = 5, pady = 5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill = "y")

list_file = Listbox(list_frame, selectmode = "extended", height = 15, yscrollcommand = scrollbar.set)
list_file.pack(side = "left", fill = "both", expand = True)
scrollbar.config(command = list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text = "저장경로")
path_frame.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = "left", fill = "x", expand = True, padx = 5, pady = 5, ipady = 4)
    #ipadx/y : 안쪽 너비 조정. ipady로 설정하여 Entry가 조금 넓어짐
btn_dest_path = Button(path_frame, text = "찾아보기", width = 10)
btn_dest_path.pack(side = "right", padx = 5, pady = 5)

# 옵션 프레임
option_frame = LabelFrame(root, text = "옵션")
option_frame.pack(padx = 5, pady = 5, ipady = 5)

# 1. 가로넓이 옵션
# 가로넓이 레이블
width_label = Label(option_frame, text = "가로넓이", width = 8)
width_label.pack(side = "left", padx = 5, pady = 5) # 여러가지 레이블을 넣어야할 때, side = "left"로 모두 설정하면 가로로 쌓이게 할 수 있다.(안하면 세로로)

# 가로넓이 콤보박스
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state = "readonly", values = opt_width, width = 10)
cmb_width.current(0)
cmb_width.pack(side = "left", padx = 5, pady = 5)

# 2. 간격 옵션
# 간격 옵션 레이블
label_space = Label(option_frame, text = "간격", width = 8)
label_space.pack(side = "left", padx = 5, pady = 5) # 여러가지 레이블을 넣어야할 때, side = "left"로 모두 설정하면 가로로 쌓이게 할 수 있다.(안하면 세로로)

# 간격 옵션 콤보박스
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(option_frame, state = "readonly", values = opt_width, width = 10)
cmb_space.current(0)
cmb_space.pack(side = "left", padx = 5, pady = 5)

# 3. 파일 포맷 옵션
# 포맷 옵션 레이블
label_format = Label(option_frame, text = "파일 포맷", width = 8)
label_format.pack(side = "left", padx = 5, pady = 5) # 여러가지 레이블을 넣어야할 때, side = "left"로 모두 설정하면 가로로 쌓이게 할 수 있다.(안하면 세로로)

# 포맷 옵션 콤보박스
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state = "readonly", values = opt_width, width = 10)
cmb_format.current(0)
cmb_format.pack(side = "left", padx = 5, pady = 5)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text = "진행상황")
frame_progress.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var)
progress_bar.pack(fill = "x", padx = 5, pady = 5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill = "x", padx = 5, pady = 5)

btn_start = Button(frame_run,padx = 5, pady = 5 ,text = "시작", width = 12)
btn_start.pack(side = "left", padx = 5, pady = 5)

btn_close = Button(frame_run, text = "닫기", padx = 5, pady = 5, width = 12, command = root.quit)
btn_close.pack(side = "right", padx = 5, pady = 5)

root. resizable(False, False) 
root. mainloop()