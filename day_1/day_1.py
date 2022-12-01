from itertools import groupby

def process_dupes(dupes_file):
    groups = [
        [int(line.rstrip()) for line in lines]
            for blank, lines in groupby(dupes_file, lambda line: line == '\n')
                if not blank
    ]
    return groups

with open('day_1/input.txt','r') as file:
    separated_data = process_dupes(file)
    total_per_elf = [sum(e) for e in separated_data]

    first = max(total_per_elf)
    total_per_elf.remove(first)
    second = max(total_per_elf)
    total_per_elf.remove(second)
    third = max(total_per_elf)
    print(first + second+ third)

