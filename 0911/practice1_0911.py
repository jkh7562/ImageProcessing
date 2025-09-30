# 작성자 : 정규혁_2020243007

scores = [85, 92, 78, 64, 99, 73, 88, 92, 85]

# 평균 점수 계산
# scores의 길이만큼 scores의 총합을 나눔.
average_score = sum(scores) / len(scores)
print(f"1. 평균 점수: {average_score:.2f}")

# 평균보다 높은 점수 리스트 생성
# average_score보다 높은 점수를 scores에서 찾아 high_scores에 저장
high_scores = [score for score in scores if score > average_score]
print(f"2. 평균보다 높은 점수 리스트: {high_scores}")

# 중복 제거 및 내림차순 정렬
# scores를 집합을 이용해서 중복을 없애고 내림차순으로 정렬
unique_sorted_scores = sorted(list(set(scores)), reverse=True)
print(f"3. 중복 제거 및 내림차순 정렬된 리스트: {unique_sorted_scores}")

