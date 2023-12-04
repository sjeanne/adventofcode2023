lotto_file = open('1.txt', 'r')

cards_points = [0] *220
current_card = 0

while True:
    card_line = lotto_file.readline().strip()
    if not card_line:
        break

    cards_points[current_card] += 1
    winning_nums, elf_nums = card_line.split(':')[1].strip().split('|')
    winning_nums = winning_nums.split()
    elf_nums = elf_nums.split()
    matching_num = len([num for num in elf_nums if num in winning_nums])
    for i in range(matching_num):
        print(matching_num, i)
        if current_card+1+i < 220:
            cards_points[current_card+1+i] += cards_points[current_card]
    
    current_card += 1

print(sum(cards_points))
