# 筛质数,留合数
nums = [45, 78, 87, 13, 67, 89, 17, 243, 56, 67, 311, 431, 111, 171]
for n in nums.copy():
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        nums.remove(n)  # 循环正常结束时执行的语句,break跳出则不会执行
print(len(nums))
print(nums)
