def material(blocks):

    span = len(blocks)
    highest = blocks[0]
    result = 0
    last_ending_point = 0

    for i in range(span):
        block_value = blocks[i]
        if block_value >= highest:
            second_highest = highest
            highest = block_value
            ending_point = i
            for j in range(last_ending_point + 1, ending_point):
                result += second_highest - blocks[j]
            last_ending_point = ending_point
        elif i == (span-1):
            while ending_point < (span-1):
                second_highest = -1
                for j in range(last_ending_point+1,span):
                    if blocks[j] > second_highest:
                        second_highest = blocks[j]
                        emergency_help = j
                        ending_point = j
                for j in range(last_ending_point+1,ending_point):
                    result += second_highest - blocks[j]
                last_ending_point = emergency_help

    return result

print(material([6, 2, 1, 1, 8, 0, 5, 5, 0, 1, 8, 9, 6, 9, 4, 8, 0, 0]))
print(material([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]))
