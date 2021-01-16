nums = list()
for i in range(0, 5):
    n = int(input('Digite um numero: '))
    if i == 0 or n > nums[-1]:
        nums.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(nums):
            if n <= nums[pos]:
                nums.insert(pos, n)
                print(f'Adicionado a posição {pos} da lista... ')
                break
            pos += 1

print('-=' * 30)
print(f'os valores digitados na lista em ordem foram: {nums}')

