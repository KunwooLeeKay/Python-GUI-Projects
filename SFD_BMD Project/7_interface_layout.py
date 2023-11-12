from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root. title("SFD / BMD")
root. geometry("1100x400")

# 보 그림 프레임
beam_frame = Frame(root)
beam_frame.pack(fill = "x", padx = 5, pady = 5)
beam_canvas = Canvas(beam_frame,width = 1030, height = 220) 
beam = beam_canvas. create_polygon(30, 100, 30, 120, 1000, 120, 1000, 100, fill = "black")
 # 보의 총 길이는 970이다.
# multiplier = 970/beam_len # beam_len에 맞는 위치에 하중이 가게 하기 위해서 곱하기 해줄 값 생성
support = beam_canvas. create_polygon(0, 160, 30, 120, 60, 160, fill = 'green')
support = beam_canvas. create_polygon(970, 160, 1000, 120, 1030, 160, fill = 'green')

# for i in range(load_num):
#     if(load[i]>0):
#         beam_canvas. create_polygon(place[i]*multiplier, 120, palce[i]+20, 140,\
#              place[i]*multiplier+10, 140, place[i]*multiplier+10, 220,\
#              place[i]*multiplier-10, 220, place[i]*multiplier-10, 140, place[i]*multiplier-20, 140, fill = 'blue')
#     elif(load[i]<0):
#         beam_canvas. create_polygon(place[i]*multiplier, 100, place[i]*multiplier+20, 80,\
#              place[i]*multiplier+10, 80, place[i]*multiplier+10, 0,\
#              place[i]*multiplier-10, 0, place[i]*multiplier-10, 80, place[i]*multiplier-20, 80, fill = 'blue')

# force_down = beam_canvas. create_polygon(500, 100, 520, 80, 510, 80, 510, 0, 490, 0, 490, 80, 480, 80, fill = 'blue')
# force_up = beam_canvas. create_polygon(700, 120, 700+20, 140, 700+10, 140, 700+10, 220, 700-10, 220, 700-10, 140, 700-20, 140, fill = 'blue')
beam_canvas.pack()


# 재료의 특성 입력
property_frame = LabelFrame(root,text = "재료의 특성")
property_frame.pack(fill = "x",padx = 5, pady = 5, ipady = 5)

label_sf = Label(property_frame, text = "허용 전단응력", width = 10)
label_sf.pack(side = "left",padx = 5, pady = 5)
btn_sf = Button(property_frame, padx = 5, pady = 5, text = "입력", width = 15)
btn_sf.pack(side = "left", padx = 5, pady = 5)

label_tensile = Label(property_frame, text = "허용 인장응력", width = 10)
label_tensile.pack(side = "left",padx = 5, pady = 5)
btn_ts = Button(property_frame, padx = 5, pady = 5, text = "입력", width = 15)
btn_ts.pack(side = "left", padx = 5, pady = 5)

label_comp = Label(property_frame, text = "허용 압축응력", width = 10)
label_comp.pack(side = "left",padx = 5, pady = 5)
btn_cs = Button(property_frame, padx = 5, pady = 5, text = "입력", width = 15)
btn_cs.pack(side = "left", padx = 5, pady = 5)

label_area = Label(property_frame, text = "단면적", width = 10)
label_area.pack(side = "left",padx = 5, pady = 5)
btn_area = Button(property_frame, padx = 5, pady = 5, text = "입력", width = 15)
btn_area.pack(side = "left", padx = 5, pady = 5)

# label_mks = Label(property_frame, text = "단위", width = 10)
# label_mks.pack(side = "left",padx = 5, pady = 5)
# btn_mks = Button(property_frame, padx = 5, pady = 5, text = "입력", width = 10)
# btn_mks.pack(side = "left", padx = 5, pady = 5)


# 하중 추가
frame_load = Frame(root)
frame_load.pack(fill = 'x', padx = 5, pady = 5, ipady = 5)
btn_add_load = Button(frame_load, padx = 5, pady = 5, text = "하중 추가", width = 20, height = 5)
btn_add_load.pack(side = "left", padx = 5, pady = 5)

# 설명란
instruction_label = Label(frame_load, text = "<주의사항>\n\
    1. 본 프로그램의 모든 단위계는 MKS단위계를 이용합니다.\n\
    2. 모든 값을 입력하실 때에는 숫자로만 입력하시길 바랍니다.\n")
instruction_label.pack(side = "left")

frame_progress = LabelFrame(frame_load, text = "진행상황")
frame_progress.pack(fill = "x", padx = 5, pady = 10, ipady = 5)
p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var)
progress_bar.pack(fill = 'x',padx = 5, pady = 5)


root. resizable(False, False) 
root. mainloop()