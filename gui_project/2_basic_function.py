from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog # filedialog는 __all__에 정의된 부분이 아니기때문에 *로 import했어도 따로 또 해줘야함.
import tkinter.messagebox as messagebox

root = Tk()
root. title("건우의 사진 합치기 프로그램")

#파일 추가
def add_file():
    # filedialog.askopenfilenames : 사용자가 원하는 여러개의 파일을 선택해서 열 수 있게 해주는 부분.
    # filetypes : 사용자가 원하는 파일형식만 보도록 선택하게 해주는 부분
    # initialdir : 기본으로 뜰 폴더를 지정 (files = 뒤에 다 한줄임.)
    files = filedialog.askopenfilenames(title = "이미지 파일을 선택하세요"\
        , filetypes = (("PNG 파일", "*.png"), ("모든 파일", "*.*"))\
            , initialdir = "C:/")
    for file in files:
        list_file.insert(END, file) # 뒤에서 선택한 파일 리스트를 보여주는 리스트에 insert를 이용해 추가함.

# 선택 삭제
def delete_file():
    #print(list_file.curselection()) # 이걸 보면 .curselection을 쓰면 이걸 인덱스로 처리함.
    # 근데 앞에서부터 지우면 앞에껄 지우는 순간 인덱스가 바뀌어서 이상한게 삭제되는 버그 발생이 가능하다. 
    # 그러므로 뒤에서부터 지우도록 해야한다. reversed 이용.
    # reverse와 reversed의 차이 : reversed를 하면 원래 리스트는 바뀌지 않고 새로 뒤집은 값을 반환해준다.
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == 'None':
        return
    #print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 시작
def start():
    # 각 옵션들 값을 확인
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        messagebox.showwarning("경고", "이미지 파일을 추가하세요!")
        return
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0 :
        messagebox.showwarning("경고", "저장 경로를 선택하세요!")


# 파일 프레임 : 맨 위에 있는 파일 추가 / 선택 삭제가 있는 영역
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

btn_add_file = Button(file_frame, pady = 5, width = 12, text = "파일 추가", command = add_file)
btn_add_file. pack(side = "left")

btn_delete_file = Button(file_frame, pady = 5, width = 12, text = "선택 삭제", command = delete_file)
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
btn_dest_path = Button(path_frame, text = "찾아보기", width = 10, command = browse_dest_path)
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

btn_start = Button(frame_run,padx = 5, pady = 5 ,text = "시작", width = 12, command = start)
btn_start.pack(side = "left", padx = 5, pady = 5)

btn_close = Button(frame_run, text = "닫기", padx = 5, pady = 5, width = 12, command = root.quit)
btn_close.pack(side = "right", padx = 5, pady = 5)

root. resizable(False, False) 
root. mainloop()