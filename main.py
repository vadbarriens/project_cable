from random import randint
cable_list = [
        52, 52, 52, 31, 31, 31, 31, 31, 31, 31, 31, 44, 44, 44, 44, 44, 44, 44,
        44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44,
        44, 44, 44, 14, 14, 14, 14, 28, 28, 28, 28, 28, 15, 15, 15, 15, 60, 60,
        60, 60, 30, 30, 30, 30, 16, 16, 16, 16, 32, 32, 32, 33, 33, 33
]
target = 250
new_list = []
while True:
    random_index = randint(0, len(cable_list))
    deleted_item = cable_list.pop(random_index - 1)
    new_list.append(deleted_item)
    if sum(new_list) > target:
        cable_list.extend(new_list)
        new_list.clear()
    elif sum(new_list) == target:
        print(new_list)
        break