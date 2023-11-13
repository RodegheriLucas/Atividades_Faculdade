'''Fazer uma função que recebe três argumentos, e que
retorne o produto desses três argumentos.
'''
def prod(*x):
    return x[0]*x[1]*x[2]

nums = []
for i in range(3):
    num = int(input(': '))
    nums.append(num)
print(prod(nums[0],nums[1],nums[2]))