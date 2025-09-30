# 작성자 : 정규혁_2020243007

person = ("Alice", 23, "Seoul")

# 각 변수에 나누어 저장하고 출력
name, age, city = person
print(f"이름: {name}")
print(f"나이: {age}")
print(f"도시: {city}")

# 나이를 5년 뒤 값으로 변경한 새로운 튜플 생성 및 출력
# 튜플은 불변(immutable)이므로 새로운 튜플을 만들어야 합니다.
new_age = age + 5
new_person = (name, new_age, city)
print(f"5년 뒤 정보: {new_person}")


