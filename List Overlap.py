first_list = range(1, 11)
second_list = range(5, 16)
storage = []
for i in first_list:
    for j in second_list:
        if i == j and i not in storage:
            storage.append(i)

print(storage)