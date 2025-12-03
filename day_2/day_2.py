from math import ceil
import re


id_ranges = open("input.txt", "r").readline().split(",")

def part_1():
    invalid_id_sum = 0
    for id_range in id_ranges:
        bounds = id_range.split("-")
        print(bounds)
        start, end = bounds[0], bounds[1]
        start_int, end_int = int(start), int(end)
        start_len, end_len = len(start), len(end)


        # Take the first half of start and end numbers to iterate through and evaluate for invalid ID
        l, r = int(start[:ceil(start_len / 2)]), int(end[:ceil(end_len / 2)])
        half_num_len_space = [length // 2 for length in range(start_len, end_len + 1) if length % 2 == 0]

        for len_space in half_num_len_space:
            for half_num in range(pow(10, len_space - 1), pow(10, len_space)):
                paired_num = int(str(half_num) + str(half_num))

                # We stop if paired num exceeds the end interval number
                if paired_num > end_int:
                    break
                if paired_num >= start_int and paired_num <= end_int:
                    invalid_id_sum += paired_num

    print(f"Invalid ID sum: {invalid_id_sum}")


def part_2():
    invalid_id_sum = 0
    for id_range in id_ranges:
        bounds = id_range.split("-")
        start, end = bounds[0], bounds[1]
        start_int, end_int = int(start), int(end)
        for num in range(start_int, end_int + 1):
            match = re.fullmatch(r"(.+?)\1+", str(num))
            if match:
                invalid_id_sum += num
    print(f"Invalid ID sum: {invalid_id_sum}")

if __name__ in "__main__":
    part_1()
    part_2()    
        


