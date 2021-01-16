nums = list()
for i in range(0, 5):
    nums.append(int(input(f'Digite o valor da posição {i}: ')))
maior = max(nums)
menor = (min(nums))
print('-=-'*15)
print(f'Você digitou os valores {nums}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(nums):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(nums):
    if v == menor:
        print(f'{i}... ', end='')
print()