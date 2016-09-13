nums=[3,2,4]
target=6

r={}
for i in range(len(nums)):
    r[nums[i]] = i

print r

for i in range(len(nums)):
    diff = target - nums[i]
    print diff
    if diff in r:
       print [i, r[diff]]
