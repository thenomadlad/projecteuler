primesum = 0
nums = list(range(2, 2000001))
while len(nums) > 0:
    num = nums[0]
    nums = [val for val in nums if val % num != 0]
    primesum += num
    if num > math.sqrt(2000000):
        primesum += sum(nums)
        break
print(primesum)
