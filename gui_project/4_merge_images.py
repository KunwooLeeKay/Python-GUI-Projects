from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog # filedialog는 __all__에 정의된 부분이 아니기때문에 *로 import했어도 따로 또 해줘야함.
import tkinter.messagebox as messagebox
from PIL import Image
import os

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
    if folder_selected == '': 
        # 빈 문자열일때 return함. 만약 if folder_selected is None을 하면 그냥 취소 누를때 폴더 선택했던게 없어지게됨
        return
    #print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합
def merge_image():
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    try: # 이 예외처리 구문을 해주면 프로그램에서 고려하지 못했던 에러들에 대해서 적어도 에러가 떴다고 알리는 부분을 만들어줄 수 있다.
            # 가능한 에러라면 존재하지 않는 드라이브를 직접 입력하여 선택했을 때 등이 있다. 이부분을 안쓰면 마치 정상적으로 작동한것처럼 보인다.
        # 가로넓이
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1 # -1일때는 원본 기준으로 통합
        else:
            img_width = int(img_width) # 콤보박스 내의 정보는 문자형이였음

        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower() # 포맷값을 가져와서 소문자로 변경

        # 모든 파일 목록 가져와서 images 리스트에 저장
        images = [Image.open(x) for x in list_file.get(0, END)]
        image_sizes = [] # [(width1, height1), (width2, height2), ...] 이런식으로 가는 리스트 정의

        if img_width > -1: # 사용자가 선택한 폭 값 사용
            # 원본 폭 : 원본 높이 = 변경 폭 : 변경 높이
            # x : y = x' : y' -> x'y = xy'
            # y' = x'y /x 가 된다.
            # x = size[0], y = size[1]
            # x' = img_width -> y' = img_width * size[1] / size[0]
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]

        else: # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]



        # 위처럼 가져온 images는 size라는 프레퍼런스를 가지고있는데, size[0] = width, size[1] = height이다.
        # 이걸 알아야하는 이유가, 이미지를 붙일 때, 넓이는 가장 큰 사진을 따라서 붙여야하고, 나중에 사진 저장할때 총 높이값을 알아야하기 때문
        # widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images] # 한줄 포문으로 width, height 리스트에 사진의 크기정보 저장.
        # 이걸 zip을 이용하면,
        #widths, heights = zip(*(x.size for x in images)) # 라고 적을 수 있다. 이제 위에서 적용한 폭 값을 적용하려면
        widths, heights = zip(*(image_sizes)) # 로 바꾸면 사용자가 선택한 값을 적용할 수 있다.

        # print("width : ",width,"height : ",height)
        max_width, total_height = max(widths), sum(heights) # max() : 최대값 반환, sum() : 합 반환
        # print(max_width, total_height)


        # 스케치북 준비
        if img_space > 0:
            total_height += (img_space * (len(images)-1))
            # 사용자가 선택한 img_space 값이 0보다 크다면, img_space * (이미지의 개수 - 1)만큼 total_height를 늘린다.

        result_img = Image.new("RGB", (max_width, total_height), (255,255,255)) # 배경 흰색
        y_offset = 0 # y방향으로 다음 사진을 붙일 때에는 밑으로 내려와야하니까, 그것을 해줄 변수 선언

        # for img in images:
        #     result_img.paste(img, (0, y_offset)) # 붙일 스케치북. paste(이미지, (x,y)) 를 해주면 된다
        #     y_offset += img.size[1] # img.size[1]은 방금 붙여넣은 그림의 높이값이다. 계속 더해가며 위치를 맞춘다.

        for idx, img in enumerate(images): # enumerate을 쓰면 리스트 내에서 약간 사전처럼 (인덱스, 내용)이 출력된다.
            
            # width가 원본유지가 아닐 때에는 이미지 크기 조정
            if img_width > -1: # 원본유지일 때에는 -1로 설정했기 때문에 -1보다 크면 원본유지가 아니라는 뜻이다.
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset)) # 붙일 스케치북. paste(이미지, (x,y)) 를 해주면 된다
            y_offset += img.size[1] + img_space 
            # img.size[1]은 방금 붙여넣은 그림의 높이값이다. 계속 더해가며 위치를 맞춘다. 
            # height값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100 # 이렇게 하면 작업중인 사진 순서 / 전체 사진 개수 * 100 -> 퍼센트이다.
            p_var.set(progress)
            progress_bar.update()


        # 포맷 옵션 처리
        file_name = "kunwoo_photo." + img_format # 앞서 lower해놓은 포맷 내용을 kunwoo_photo이름 뒤에 붙임

        dest_path = os.path.join(txt_dest_path.get(), file_name) 
        # os.path.join을 이용해 사용자가 선택한 경로에 file_name을 추가하여 dest_path경로에 저장한다.

        result_img.save(dest_path) # .save(경로) 를 입력하면 그 경로에 저장된다.
        messagebox.showinfo("알림", "작업이 완료되었습니다.")

    except Exception as err: 
        messagebox.showerror("에러", err)


# 시작
def start():
    # 각 옵션들 값을 확인
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        messagebox.showwarning("경고", "이미지 파일을 추가하세요!")
        return
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0 :
        messagebox.showwarning("경고", "저장 경로를 선택하세요!")

    # 이미지 통합 작업
    merge_image()


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
cmb_space = ttk.Combobox(option_frame, state = "readonly", values = opt_space, width = 10)
cmb_space.current(0)
cmb_space.pack(side = "left", padx = 5, pady = 5)

# 3. 파일 포맷 옵션
# 포맷 옵션 레이블
label_format = Label(option_frame, text = "파일 포맷", width = 8)
label_format.pack(side = "left", padx = 5, pady = 5) # 여러가지 레이블을 넣어야할 때, side = "left"로 모두 설정하면 가로로 쌓이게 할 수 있다.(안하면 세로로)

# 포맷 옵션 콤보박스
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state = "readonly", values = opt_format, width = 10)
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