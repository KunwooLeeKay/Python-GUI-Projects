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

# BMD 그리기
# x_range 다시 초기화
x_range = [0] # 하중이 가해지는 곳을 기준으로 범위를 나눔
x_range.extend(place) # 첫부분에 0추가하고 뒤는 하중이 가해지는 만큼
x_range.append(beam_len) # 끝에 보의 총 길이가 오도록
print(x_range)

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

# find_max_bm = []
# for i in range(len(bending_moment)):
#     find_max_bm.append(abs(shear_force[i]))

# max_bm = max(find_max_bm)

# print("최대 굽힘 모멘트 : ", max_bm)

plt.subplot(2,1,2)
plt.title("BMD")
plt.xlabel("Length in meters")
plt.ylabel("Bending Moment in Newton * Meter")
plt.axvline(x=0, color = 'black')  # x축 그리기
plt.axhline(y=0, color = 'black')   # y축 그리기
plt.plot(x_range,bending_moment)

plt.tight_layout()
plt.show()