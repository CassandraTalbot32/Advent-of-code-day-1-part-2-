with open("day1data.txt")as f:
    lines = f.readlines()

nums = [ int(line.strip())for line in lines ]

largest = -1
#iterate +1 so not going through previously examined numbers
for i in range(len(nums)+2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            num1, num2, num3 = nums[i], nums[j], nums[k]
        
            if num1+num2+num3 == 2020:
                balance = num1 * num2 * num3

                if balance > largest:
                    largest = balance

print(largest)
