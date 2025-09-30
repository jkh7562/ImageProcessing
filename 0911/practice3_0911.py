# 작성자 : 정규혁_2020243007

scores = {"Kong": 86, "Kim": 82, "Lee": 91, "Park": 77, "Cha": 79}

# for문을 이용해 "이름: 점수" 형식으로 모든 학생 정보 출력
print("1. 모든 학생 정보:")
for name, score in scores.items():
    print(f"{name}: {score}")
print("-" * 20)

# 점수가 80점 이상인 학생들만 출력
print("2. 80점 이상인 학생:")
for name, score in scores.items():
    if score >= 80:
        print(f"{name}: {score}")

