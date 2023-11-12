import numpy as np
import matplotlib.pyplot as plt

load = [] # 하중 리스트 (+ : 윗방향 하중, -: 아래방향 하중)
load_num = int(input("하중의 갯수를 입력하세요 : ")) # 하중 갯수

for i in range(load_num):
    load.append(round(float(input("하중을 입력하세요")),3))
print(load)
place = [] # 하중 위치

for i in range(load_num):
    place.append(round(float(input("하중의 위치를 입력하세요(왼쪽 기준)")),3))

print(place)

beam_len = round(float(input("보의 길이를 입력하세요")),3) # 보의 길이를 입력받음. 두께는 무시할만큼 얇다고 가정
print(beam_len)

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

shear_force = [0] # 원점을 찍기 위해 첫번째 리스트에 0할당
sf = 0 # 평행한 그래프를 그리기 위해 리스트에 같은 전단력을 두번씩 할당하기 위한 임시 변수

shear_force.append(reaction_left) 
shear_force.append(reaction_left)
for i in range(load_num):
    sf = 0
    sf = shear_force[i+2] + load[i]
    shear_force.append(sf)
    shear_force.append(sf)
shear_force.append(0)

x_range.extend(x_range)
x_range.sort()

find_max_sf = []
for i in range(len(shear_force)):
    find_max_sf.append(abs(shear_force[i]))
print(find_max_sf)
max_sf = max(find_max_sf)
print("최대 전단력 : ",max_sf)

print("x범위 : ",x_range,"전단력",shear_force)

plt.title("SFD")
plt.xlabel("Length in meters")
plt.ylabel("Shear Force in Newton")
plt.axvline(x=0, color = 'black')  # x축 그리기
plt.axhline(y=0, color = 'black')   # y축 그리기
plt.plot(x_range,shear_force)
plt.show()
