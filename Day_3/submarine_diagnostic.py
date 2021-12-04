# Advent of Code 2021 
# Day 3
#
# Computing gamma and epsilon rates from 
# submarine diagnostic data

def load_input(filename):
    ''' Load and preprocess data '''

    with open(filename, 'r') as f:
        raw_input = f.readlines()

    raw_data = [datum.strip() for datum in raw_input]
    data = [list(datum) for datum in raw_data]

    return data


def compute_rates(data):
    ''' Compute gamma rate '''
    num_rows = len(data)
    num_columns = len(data[0])

    gamma = []
    for column in range(num_columns):
        ones_count  = 0
        zeros_count = 0
        for row in range(num_rows):
            if data[row][column] == '1':
                ones_count += 1
            else:
                zeros_count += 1

        if ones_count >= zeros_count:
            gamma.append('1')
        else:
            gamma.append('0')

    epsilon = ['0' if i == '1' else '1' for i in gamma]
    
    return int(''.join(gamma), 2), int(''.join(epsilon), 2)       


if __name__ == '__main__':
    data  = load_input('input.txt')
    gamma, epsilon = compute_rates(data)
    print(gamma * epsilon)