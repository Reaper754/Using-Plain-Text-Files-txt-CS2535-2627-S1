with open("checksum_sample", "r") as file:
    nums = file.readlines()

processed_num = []

for num in nums:
    num = num.split()
    processed_num.append(num)

print(processed_num)

for i, number in enumerate(processed_num):
    print(f"index: {i}, number: {number}")
