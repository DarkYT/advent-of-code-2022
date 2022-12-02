points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win = {
    "A": {
        "X":3,
        "Y":6,
        "Z":0
    },
    "B": {
        "X":0,
        "Y":3,
        "Z":6,
    },
    "C": {
        "X":6,
        "Y":0,
        "Z":3
    }
}

closer = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

win2 = {
    "A": {
        "X":3,
        "Y":1,
        "Z":2
    },
    "B": {
        "X":1,
        "Y":2,
        "Z":3,
    },
    "C": {
        "X":2,
        "Y":3,
        "Z":1
    }
}

def get_result(round):
    return points[round[1]] + win[round[0]][round[1]]

def get_result_2(round):
    return closer[round[1]] + win2[round[0]][round[1]]

with open('day_2/input.txt', 'r') as file:
    strategy = []
    for line in file:
        strategy.append(line.rstrip().split(' '))
    """
    First question
    """

    strategy_result = [get_result(round) for round in strategy]
    print(sum(strategy_result))

    """
    Second question
    """
    strategy_result_2 = [get_result_2(round) for round in strategy]
    print(sum(strategy_result_2))
