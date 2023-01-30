def divide_positive_and_negatives_and_sum_numbers(nums):
    result_negatives = 0
    result_positives = 0
    for num in nums:
        if num < 0:
            result_negatives += num
        elif num > 0:
            result_positives += num

    return result_negatives, result_positives


numbers = [int(x) for x in input().split()]

sum_negative,sum_positive = divide_positive_and_negatives_and_sum_numbers(numbers)

print(f'{sum_negative}\n{sum_positive}')
if abs(sum_negative) > abs(sum_positive):
    print('The negatives are stronger than the positives')
elif abs(sum_positive) > abs(sum_negative):
    print('The positives are stronger than the negatives')