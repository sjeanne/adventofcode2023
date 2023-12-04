lotto_file = open('1.txt', 'r')

cards_points = []

while True:
    card_line = lotto_file.readline().strip()
    if not card_line:
        break

    winning_nums, elf_nums = card_line.split(':')[1].strip().split('|')
    winning_nums = winning_nums.split()
    elf_nums = elf_nums.split()
    matching_num = len([num for num in elf_nums if num in winning_nums])
    cards_points.append(0 if matching_num == 0 else 2 ** (matching_num-1))
print(sum(cards_points)) #28538
