# 작성자 : 정규혁_2020243007

import numpy as np

scores = np.array([[75, 82, 91, 66, 88],  # 학생 A
                   [59, 93, 85, 72, 77],  # 학생 B
                   [88, 90, 92, 85, 91],  # 학생 C
                   [70, 65, 80, 75, 60]]) # 학생 D

# 각 학생별(행 기준) 평균 계산
student_avg = np.mean(scores, axis=1)
print(f'각 학생별 평균 점수: {student_avg}')

# 각 과목별(열 기준) 최고 점수 계산
subject_max = np.max(scores, axis=0)
print(f'각 과목별 최고 점수: {subject_max}')

# 각 과목별(열 기준) 최저 점수 계산
subject_min = np.min(scores, axis=0)
print(f'각 과목별 최저 점수: {subject_min}')

# 전체 점수의 분산 계산
total_variance = np.var(scores)
print(f'전체 점수의 분산(variance): {total_variance:.2f}')

# 전체 점수의 표준편차 계산
total_std = np.std(scores)
print(f'전체 점수의 표준편차(std): {total_std:.2f}')



