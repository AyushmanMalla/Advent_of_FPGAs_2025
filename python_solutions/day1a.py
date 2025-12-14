file_object = open("../puzzle_inputs/day1.txt", "r") # Open the file in read mode ('r')
content = file_object.read()          # Read the entire content


# content = '''L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82'''.splitlines()

current_sum = 50
counter = 0
for line in content.splitlines():
    if line[0] == 'L':
        current_sum -= int(line[1:])
    elif line[0] == 'R':
        current_sum += int(line[1:])

    if abs(current_sum) % 100 == 0:
        counter += 1

print(counter)

file_object.close()       

