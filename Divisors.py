my_num = int(input('Digite um número'))
num_range = range(2, my_num)
storage = []
for x in num_range:
    if my_num%x == 0:
        storage.append(x)

print('Dos numeros entre 2 e',my_num,'os divisores de',my_num,'são:',storage)