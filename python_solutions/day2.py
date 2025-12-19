# '''
# ranges = [x1, x2, x3, ...]
# answer = 0
# for range in ranges:
#     for number in range(range_start, range_end):
#         #logic to check if the number is following the required pattern or not
#         if yes, add it to answer
#         else, continue
# '''
sample = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124']
content = open("../puzzle_inputs/day2.txt", 'r').read().split(',')

# def pattern_checker(num) -> bool:
#     num = str(num)
#     length = len(num)
#     pattern_occurences = 2
#     if length % pattern_occurences == 0:
#         chunk_size = length//pattern_occurences
#         chunks = []
#         for i in range(pattern_occurences):
#             chunk = num[chunk_size*i:chunk_size*(i+1)]
#             chunks.append(chunk)
#         if (len(set(chunks)) == 1):  return True 
#     return False

# def pattern_checker_partTwo(num) -> bool:
#     '''
#     Max pattern length for an invalid number will always be <= length(str(nums)//2)
#     '''
#     num = str(num)
#     length = len(num)
#     for pattern_occurences in range(2, length+1):
#         if (length % pattern_occurences) == 0:
#             chunk_size = length//pattern_occurences
#             chunks = []
#             for i in range(pattern_occurences):
#                 chunk = num[chunk_size*i:chunk_size*(i+1)]
#                 chunks.append(chunk)
#             if (len(set(chunks)) == 1): return True 
#     return False



# answer_partOne = 0
# answer_partTwo = 0
# for id_range in content:
#     start_id = int(id_range.split('-')[0])
#     end_id = int(id_range.split('-')[1])
#     for number in range(start_id, end_id+1):
#         if pattern_checker(number):
#             answer_partOne += number
#         if pattern_checker_partTwo(number):
#             answer_partTwo += number
# print(f"Part One: {answer_partOne}, Part 2: {answer_partTwo}")


def patternCheckerOptimised(num: int, fixed_parts: int = None) -> bool:
    s = str(num)
    n = len(s)
    
    divisors = [fixed_parts] if fixed_parts else range(2, n + 1)
    
    for d in divisors:
        if d > 1 and n % d == 0:
            chunk_size = n // d
            pattern = s[:chunk_size]
            if pattern * d == s:
                return True
    return False

answer_partOne = 0
answer_partTwo = 0
for id_range in content:
    start_id = int(id_range.split('-')[0])
    end_id = int(id_range.split('-')[1])
    for number in range(start_id, end_id+1):
        if (patternCheckerOptimised(number)):
            answer_partTwo += number
            if (patternCheckerOptimised(number, fixed_parts=2)):
                answer_partOne += number

print(f"Part One: {answer_partOne}, Part 2: {answer_partTwo}")