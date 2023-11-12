from tkinter import *
import matplotlib.pyplot as plt
import tkinter.messagebox as msgbox
import math

root = Tk()
root. title("SFD / BMD")
root. geometry("1250x500")

load = [] # 하중 리스트 (+ : 윗방향 하중, -: 아래방향 하중)
load_num = 0 # 하중 갯수
place = [] # 하중 위치
beam_len = 0
multiplier = 0
def add_load():
    global load
    global load_num
    global place
    global beam_len
    global multiplier

    beam_len = float(len_in.get())
     # 보의 총 길이는 970이다.
    # multiplier = 970/beam_len # beam_len에 맞는 위치에 하중이 가게 하기 위해서 곱하기 해줄 값 생성
    multiplier = 970/beam_len # beam_len에 맞는 위치에 하중이 가게 하기 위해서 곱하기 해줄 값 생성
    load.append(float(load_in.get()))
    place.append(float(place_in.get()))
    load_num += 1

    if(float(load_in.get())>0):
        beam_canvas. create_polygon(float(place_in.get())*multiplier, 120, float(place_in.get())*multiplier+20, 140,\
             float(place_in.get())*multiplier+10, 140, float(place_in.get())*multiplier+10, 220,\
             float(place_in.get())*multiplier-10, 220, float(place_in.get())*multiplier-10, 140,\
                  float(place_in.get())*multiplier-20, 140, fill = 'blue')
    elif(float(load_in.get())<0):
        beam_canvas. create_polygon(float(place_in.get())*multiplier, 100, float(place_in.get())*multiplier+20, 80,\
             float(place_in.get())*multiplier+10, 80, float(place_in.get())*multiplier+10, 0,\
             float(place_in.get())*multiplier-10, 0, float(place_in.get())*multiplier-10, 80,\
                  float(place_in.get())*multiplier-20, 80, fill = 'blue')

def draw():
    global load
    global load_num
    global place
    global beam_len

    reaction_left = 0
    reaction_right = 0

    # 힘평형 계산
    # 1. 모멘트 평형: 왼쪽 기준

    moment_sum = 0
    for i in range(load_num):
        moment_sum += load[i]*place[i]

    reaction_right = -moment_sum/beam_len
    round(reaction_right, 2)

    print(reaction_right)

    # 2. Y축 방향 힘평형
    y_axis_force_sum = 0
    for i in range(load_num):
        y_axis_force_sum += load[i]
    y_axis_force_sum += reaction_right

    reaction_left = -y_axis_force_sum
    round(reaction_left,2)
    print(reaction_left)

    # SFD 그리기
    x_range = [0] # 하중이 가해지는 곳을 기준으로 범위를 나눔
    x_range.extend(place) # 첫부분에 0추가하고 뒤는 하중이 가해지는 만큼
    x_range.append(beam_len) # 끝에 보의 총 길이가 오도록
    x_range.extend(x_range)
    x_range.sort()

    shear_force = [0] # 원점을 찍기 위해 첫번째 리스트에 0할당
    sf = 0 # 평행한 그래프를 그리기 위해 리스트에 같은 전단력을 두번씩 할당하기 위한 임시 변수

    shear_force.append(reaction_left) 
    shear_force.append(reaction_left)
    for i in range(load_num):
        sf = shear_force[i+2] + load[i]
        shear_force.append(sf)
        shear_force.append(sf)
    shear_force.append(0)

    # Plot SFD
    plt.subplot(2,1,1)
    plt.title("SFD")
    plt.xlabel("Length in meters")
    plt.ylabel("Shear Force in Newton")
    plt.axvline(x=0, color = 'black')  # x축 그리기
    plt.axhline(y=0, color = 'black')   # y축 그리기
    plt.plot(x_range,shear_force)
  
  # 최대 전단응력 구하기
    find_max_sf = []
    for i in range(len(shear_force)):
        find_max_sf.append(abs(shear_force[i]))
    print(find_max_sf)
    max_sf = max(find_max_sf)
    print("최대 전단력 : ",max_sf)

    

    # BMD 그리기
    # x_range 다시 초기화
    x_range = [0] # 하중이 가해지는 곳을 기준으로 범위를 나눔
    x_range.extend(place) # 첫부분에 0추가하고 뒤는 하중이 가해지는 만큼
    x_range.append(beam_len) # 끝에 보의 총 길이가 오도록

    bending_moment = [0]
    shear_force2 = []
    shear_force2.append(reaction_left)
    place2 = [0]
    place2.extend(place)
    place2.append(beam_len)
    for i in range(load_num):
        shear_force2.append(shear_force2[i] + load[i])
    shear_force2.append(0)
    print("SF",shear_force2)
    print("위치",place2)

    for i in range(load_num):
        bending_moment.append(bending_moment[i]+shear_force2[i]*(place2[i+1]-place2[i]))

    bending_moment.append(0)
    print("BM", bending_moment)

    #파손 판단
    # 파손될지 판단
    # 타우all, 시그마all입력받고, 위의 max_sf, max_bm을 활용해서 파손될지 판단.

    area = float(area_in.get())
    shear_stress_allowed = float(sf_in.get())
    tensile_stress_allowed = float(ts_in.get())
    comp_stress_allowed = float(cs_in.get())
    
    max_shear_stress = max_sf/area
  
    # 최대 수직 응력 구하기
    find_max_bm = []
    for i in range(len(bending_moment)):
        find_max_bm.append(abs(bending_moment[i]))

    diameter = math.sqrt(area*4/(math.pi)) # 단면적을 이용해 직경 값 계산
    sec_modulus = ((math.pi)*diameter**3)/32
    max_bm_stress = max(find_max_bm) / sec_modulus
    

    # 파손이 일어난다면 메세지박스로 어떤 이유로 파손이 일어나는지 출력
    if(max_shear_stress>shear_stress_allowed):
        msgbox.showinfo("파손!", "허용 전단응력을 넘어선 값입니다.")

    if (-max_bm_stress<-comp_stress_allowed):
        msgbox.showinfo("파손!", "허용 압축응력을 넘어선 값입니다.")

    if(max_bm_stress>tensile_stress_allowed):
        msgbox.showinfo("파손!", "허용 인장응력을 넘어선 값입니다.")

    #Plot BMD
    plt.subplot(2,1,2)
    plt.title("BMD")
    plt.xlabel("Length in meters")
    plt.ylabel("Bending Moment in Newton * Meter")
    plt.axvline(x=0, color = 'black')  # x축 그리기
    plt.axhline(y=0, color = 'black')   # y축 그리기
    plt.plot(x_range,bending_moment)

    plt.tight_layout()
    plt.show()



# 보 그림 프레임
beam_frame = Frame(root)
beam_frame.pack(fill = "x", padx = 5, pady = 5)
beam_canvas = Canvas(beam_frame,width = 1030, height = 220) 
beam = beam_canvas. create_polygon(30, 100, 30, 120, 1000, 120, 1000, 100, fill = "black")

support = beam_canvas. create_polygon(0, 160, 30, 120, 60, 160, fill = 'green')
support = beam_canvas. create_polygon(970, 160, 1000, 120, 1030, 160, fill = 'green')
beam_canvas.pack()


# 재료의 특성 입력
property_frame = LabelFrame(root,text = "재료의 특성")
property_frame.pack(fill = "x",padx = 5, pady = 5, ipady = 5)

# 허용 전단응력
label_sf = Label(property_frame, text = "허용 전단응력", width = 10)
label_sf.pack(side = "left",padx = 5, pady = 5)

frame_sf = Frame(property_frame)
frame_sf.pack(side = "left")
sf_in = Entry(frame_sf, width = 10)
sf_in.pack(side = "left")
sf_in.insert(0,"1000000")
label_in = Label(frame_sf, text = "[Pa]")
label_in.pack(side = 'left')

# 허용 인장응력
label_tensile = Label(property_frame, text = "허용 인장응력", width = 10)
label_tensile.pack(side = "left",padx = 5, pady = 5)

frame_ts = Frame(property_frame)
frame_ts.pack(side = "left")
ts_in = Entry(frame_ts, width = 10)
ts_in.pack(side = "left")
ts_in.insert(0,"1000000000")
label_in = Label(frame_ts, text = "[Pa]")
label_in.pack(side = 'left')

# 허용 압축응력
label_comp = Label(property_frame, text = "허용 압축응력", width = 10)
label_comp.pack(side = "left",padx = 5, pady = 5)

frame_cs = Frame(property_frame)
frame_cs.pack(side = "left")
cs_in = Entry(frame_cs, width = 10)
cs_in.pack(side = "left")
cs_in.insert(0,"1000000000")
label_in = Label(frame_cs, text = "[Pa]")
label_in.pack(side = 'left')

# 단면적
label_area = Label(property_frame, text = "단면적", width = 10)
label_area.pack(side = "left",padx = 5, pady = 5)

frame_area = Frame(property_frame)
frame_area.pack(side = "left")
area_in = Entry(frame_area, width = 10)
area_in.pack(side = "left")
area_in.insert(0,"0.001")
label_in = Label(frame_area, text = "[m^2]")
label_in.pack(side = 'left')


# 보의 길이
label_area = Label(property_frame, text = "보의 길이", width = 10)
label_area.pack(side = "left",padx = 5, pady = 5)

frame_len = Frame(property_frame)
frame_len.pack(side = "left")
len_in = Entry(frame_len, width = 8)
len_in.pack(side = "left")
len_in.insert(0,"10")
label_in = Label(frame_len, text = "[m]")
label_in.pack(side = 'left')


# 하중 추가
frame_load = Frame(root, relief = "solid", bd = 1)
frame_load.pack(fill = 'x', padx = 5, pady = 5, ipady = 5)
btn_add_load = Button(frame_load, padx = 5, pady = 5, text = "하중 추가", width = 20, height = 5, command = add_load)
btn_add_load.pack(side = "left", padx = 5, pady = 5)

# 하중 리스트

# scrollbar = Scrollbar(frame_load)
# scrollbar.pack(side = "right", fill = "y")

# list_load = Listbox(frame_load, selectmode = "extended", height = 5,width = 70, yscrollcommand = scrollbar.set)
# list_load.pack(side = "left", fill = "both")
# scrollbar.config(command = list_load.yview)

# 하중 입력
label_area = Label(frame_load, text = "하중 입력", width = 10)
label_area.pack(side = "left",padx = 5, pady = 5)

input_load = Frame(frame_load, relief = "solid", bd = 1)
input_load.pack(side = "left", padx = 5, pady = 5, ipady = 2)

place_in = Entry(input_load, width = 8)
place_in.pack(side = "left", padx = 5, pady = 5, ipady = 2)
place_in.insert(0,"0")
label_in = Label(input_load, text = "[m from left]")
label_in.pack(side = 'left', padx = 5, pady = 5, ipady = 2)

load_in = Entry(input_load, width = 8)
load_in.pack(side = "left",padx = 5, pady = 5, ipady = 2)
load_in.insert(0,"0")
label_in = Label(input_load, text = "[Newton]")
label_in.pack(side = 'left',padx = 5, pady = 5, ipady = 2)

# 설명란
instruction_label = Label(frame_load, text = "<주의사항>\n\
    1. 본 프로그램의 모든 단위계는 MKS단위계를 이용합니다.\n\
    2. 모든 값을 입력하실 때에는 숫자로만 입력하시길 바랍니다.\n")
instruction_label.pack(side = "right")


frame_start = Frame(root)
frame_start.pack(fill = "x", pady = 0, padx = 5, ipady = 5)
btn_draw = Button(frame_start, padx = 5, pady = 5, text = "그리기", width = 20, height = 20, fg = 'red', command = draw)
btn_draw.pack(side = "right", padx = 5, pady = 5)


root. resizable(True, True) 
root. mainloop()