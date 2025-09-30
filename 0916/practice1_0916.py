# 작성자 : 정규혁_2020243007

import numpy as np

# 3x3 2차 배열 생성
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# 배열의 행과 열의 수를 출력
print(f'배열의 크기 : {arr.shape}')
# 배열의 차원을 출력
print(f'배열의 차원 : {arr.ndim}')

# 행을 따라 합을 계산
row_sum = np.sum(arr, axis=1)
print(f'각 행의 합 : {row_sum}')

# 열을 따라 합을 계산
column_sum = np.sum(arr, axis=0)
print(f'각 열의 합 : {column_sum}')

