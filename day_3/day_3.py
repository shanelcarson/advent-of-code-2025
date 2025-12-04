banks = open("input.txt", "r").readlines()

def part_1():
    total_output_joltage = 0
    for bank in banks:
        batteries = list(bank)
        l, r = 0, 1
        largest_known_number = 0

        while r < len(batteries):
            curr_number = int(batteries[l] + batteries[r])
            if curr_number > largest_known_number:
                largest_known_number = curr_number
            
            if batteries[l] < batteries[r]:
                l = r
            r += 1
        total_output_joltage += largest_known_number

    print(f"Part 1 total output joltage: {total_output_joltage}")




def part_2():
    pass

if __name__ in "__main__":
    part_1()
    part_2()    
        


