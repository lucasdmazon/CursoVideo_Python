from time import sleep
print('OS fogos de artificio começam em:')
sleep(1.75)
i = 10
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('{}FELIZ ANO NOVO'.format('\033[1;35m'))
