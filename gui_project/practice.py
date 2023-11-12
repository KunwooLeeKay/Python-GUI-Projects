# zip : 리스트를 세로로 섞어주는 라이브러리

kor = ["사과", "바나나", "포도", "모히또"]
eng = ["apple", "banana", "grape", "mojito"]

print(list(zip(kor, eng)))


# unzip은 대상 리스트 앞에 *을 붙이면 된다.
mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print (kor2)
print (eng2)