# 작성자 : 정규혁_2020243007

import numpy as np

# 0 이상 100 미만의 정수 난수 16개로 4x4 배열 생성
random_array = np.random.randint(0, 100, size=(4, 4))
print('생성된 4x4 배열:\n', random_array)

# 짝수인지 판별하는 불리언 배열 생성
# 각 원소를 2로 나눈 나머지가 0인지 확인
even_numbers = random_array[random_array % 2 == 0]
print('배열에서 추출된 짝수:', even_numbers)

# 배열의 대각선 원소만 추출
diagonal_elements = np.diag(random_array)
print('배열의 대각선 원소:', diagonal_elements)

