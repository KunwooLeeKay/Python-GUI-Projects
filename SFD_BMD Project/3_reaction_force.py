
load = [] # 하중 리스트 (+ : 윗방향 하중, -: 아래방향 하중)
load_num = int(input("하중의 갯수를 입력하세요 : ")) # 하중 갯수

for i in range(load_num):
    load.append(int(input("하중을 입력하세요")))

print(load)

place = [] # 하중 위치

for i in range(load_num):
    place.append(int(input("하중의 위치를 입력하세요(왼쪽 기준)")))

print(place)

beam_len = int(input("보의 길이를 입력하세요")) # 보의 길이를 입력받음. 두께는 무시할만큼 얇다고 가정

reaction_left = 0
reaction_right = 0

# 힘평형 계산
# 1. 모멘트 평형: 왼쪽 기준

moment_sum = 0
for i in range(load_num):
    moment_sum += load[i]*place[i]

reaction_right = moment_sum/beam_len

print(reaction_right)

# 2. Y축 방향 힘평형
y_axis_force_sum = 0
for i in range(load_num):
    y_axis_force_sum += load[i]
y_axis_force_sum += reaction_right

reaction_left = -y_axis_force_sum
print(reaction_left)