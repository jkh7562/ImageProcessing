# 작성자 : 정규혁_2020243007

import numpy as np

math_scores = np.array([72, 88, 95, 60, 77, 85, 90, 66, 82, 74])

# 평균 계산
mean_score = np.mean(math_scores)
print(f'평균 점수: {mean_score:.2f}')

# 중앙값 계산
median_score = np.median(math_scores)
print(f'중앙값 점수: {median_score}')

# 분산 계산
variance = np.var(math_scores)
print(f'분산(variance): {variance:.2f}')

# 표준편차 계산
std_dev = np.std(math_scores)
print(f'표준편차(std): {std_dev:.2f}')

# Z-점수 표준화
z_scores = (math_scores - mean_score) / std_dev
print(f'Z-점수 표준화된 점수: {z_scores}')

# 표준화된 데이터의 평균 다시 계산
new_mean = np.mean(z_scores)
print(f'표준화된 데이터의 평균: {new_mean:.2f}')

# 표준화된 데이터의 표준편차 다시 계산
new_std = np.std(z_scores)
print(f'표준화된 데이터의 표준편차: {new_std:.2f}')


