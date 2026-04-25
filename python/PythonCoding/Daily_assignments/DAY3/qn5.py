
def average(numbers):
    return sum(numbers) / len(numbers)

nums = [int(x) for x in input('Enter numbers (space separated:)').split()]
avg = average(nums)

print('Average:',avg)