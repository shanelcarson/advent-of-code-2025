
rotations = open("input.txt", "r").readlines()

def part_1():
    curr_position = 50
    password = 0
    for rotation in rotations:
        normalized_rotation = int(rotation[1:]) % 100
        if rotation.startswith("R"):
            curr_position += normalized_rotation
        else:
            curr_position -= normalized_rotation

        curr_position %= 100
        if curr_position == 0:
            password += 1
    print(f"Part 1 Password is {password}")


def part_2():
    curr_position = 50
    password = 0
    for rotation in rotations:
        # Evaluate how many times the dial would pass zero if the rotations are greater than 100
        intial_zero_passthroughs = int(rotation[1:]) // 100

        password += intial_zero_passthroughs
        starting_position = curr_position

        normalized_rotation = int(rotation[1:]) % 100

        # Simulate going left
        if rotation.startswith("L"):
            normalized_rotation *= -1
        
        
        if starting_position == 0:
            # If we are starting at position zero, we need to just update the current position to the right value and not update the password
            curr_position = curr_position + normalized_rotation if normalized_rotation >= 0 else 100 + normalized_rotation
            continue

        curr_position = curr_position + normalized_rotation

        # If we land on 0 after the rotation, or if we exceed the bounds of the numbers we can assume we have passed the '0' once
        if curr_position == 0 or curr_position < 0 or curr_position > 99:
            password += 1
            curr_position %= 100
        
    print(f"Part 2 Password is {password}")

if __name__ in "__main__":
    part_1()
    part_2()