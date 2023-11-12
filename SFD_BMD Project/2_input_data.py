
load = [] # 하중 리스트
load_num = int(input("하중의 갯수를 입력하세요 : ")) # 하중 갯수

for i in range(load_num):
    load.append(int(input(print("하중을 입력하세요"))))

print(load)

place = [] # 하중 위치
for i in range(load_num):
    place.append(int(input(print("하중의 위치를 입력하세요(왼쪽 기준)"))))

print(place)

beam_len = input("보의 길이를 입력하세요") # 보의 길이를 입력받음. 두께는 무시할만큼 얇다고 가정

# 가정 : 
# 1. 단순 지지보
# 2. 빔의 두께는 매우 얇다
