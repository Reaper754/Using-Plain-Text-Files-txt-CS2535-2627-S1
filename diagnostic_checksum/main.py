with open("checksum_input.txt", "r") as file:
    nums = file.readlines()

total = 0

with open ("checksum_results.txt", "w") as file:
    for num in nums:
        num.strip()
        split_nums = num.split()
        temp_high = split_nums[0]
        temp_low = split_nums[1]
        for i, number in enumerate(split_nums):
            if int(temp_low) > int(temp_high):
                temp_num = temp_low
                temp_low = temp_high
                temp_high = temp_num
            test_num = split_nums[i]
            if int(test_num) > int(temp_high):
                temp_high = test_num
            elif int(test_num) < int(temp_low):
                temp_low = test_num
        add = int(temp_high) - int(temp_low)
        total += add
        file.write(str(add) + "\n")
    file.write("checksum total: " + str(total))