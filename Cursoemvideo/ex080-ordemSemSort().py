nums = list()
for c in range(0,5):
    n = int(input('Informe o valor: '))
    if c == 0 or n > nums[-1]:
        nums.append(n)
    else:
        pos = 0
        while pos < len(nums):
            if n <= nums[pos]:
                nums.insert(pos,n)
                break
            pos += 1
print('~='*30)   
print(f'Os valores em ordem {nums}')

