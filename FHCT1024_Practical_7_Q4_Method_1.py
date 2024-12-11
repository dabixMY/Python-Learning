import random
#               0  1  2  3  4  5  6  7  8  9
# count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count_list = [0]*10
# num_list = []

for count in range(1000):
    number = random.randint(0, 9)
    count_list[number] += 1

    # num_list.append(number)

    print(number)
    # num_list.append(random.randint(0,4))

print("Num | Count")

for num in range(10):
    print(f"{num:3d} : {count_list[num]:3d}")
