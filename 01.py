# 풀이 1
nums = [100, 200, 300, 400, 500]
nums.remove(400)
nums.remove(500)
print(nums)

# 풀이 2
nums = [100, 200, 300, 400, 500]
del nums[3:]
print(nums)

# 풀이 3
nums = [100, 200, 300, 400, 500]
nums.pop()
nums.pop()
print(nums)
