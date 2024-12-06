import random

num_list = []

for count in range(1000):
    number = random.randint(0, 9)
    num_list.append(number)

    print(number)

print("Num | Count")

for num in range(10):
    print(f"{num:3d} : {num_list.count(num):3d}")
