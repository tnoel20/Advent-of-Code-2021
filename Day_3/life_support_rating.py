# Advent of Code
# Day 3
#
# Computing Life Support Rating

def load_input(filename):
    ''' Load and preprocess data '''

    with open(filename, 'r') as f:
        raw_input = f.readlines()

    raw_data = [datum.strip() for datum in raw_input]
    data = [list(datum) for datum in raw_data]
    tuple_data = [(i, datum) for i, datum in enumerate(data)]
    data = dict(tuple_data)

    return data


def compute_O2_gen_rating(input_data):
    ''' Compute oxygen generator rating '''
    data = input_data.copy()
    num_columns = len(list(data.values())[0])

    for column in range(num_columns):
        ones_count  = 0
        zeros_count = 0
        most_common = None

        if len(data.keys()) == 1:
            return int(''.join(data[list(data.keys())[0]]),2)

        for key in data.keys():
            if data[key][column] == '1':
                ones_count += 1
            else:
                zeros_count += 1

        if ones_count >= zeros_count:
            most_common = '1'
        else:
            most_common = '0'

        keys = list(data.keys())

        for key in keys:
            if data[key][column] != most_common:
                data.pop(key)

    return int(''.join(data[list(data.keys())[0]]),2)


def compute_CO2_scrubber_rating(input_data):
    ''' Compute CO2 Scrubber rating '''
    data = input_data.copy()
    num_columns = len(list(data.values())[0])

    for column in range(num_columns):
        ones_count  = 0
        zeros_count = 0
        most_common = None

        if len(data.keys()) == 1:
            return int(''.join(data[list(data.keys())[0]]),2)

        for key in data.keys():
            if data[key][column] == '1':
                ones_count += 1
            else:
                zeros_count += 1

        if ones_count >= zeros_count:
            most_common = '1'
        else:
            most_common = '0'

        keys = list(data.keys())

        for key in keys:
            if data[key][column] == most_common:
                data.pop(key)

    return int(''.join(data[list(data.keys())[0]]),2)


if __name__ == '__main__':
    data  = load_input('input.txt')
    O2_gen_rating = compute_O2_gen_rating(data)
    CO2_scrubber_rating = compute_CO2_scrubber_rating(data)
    life_support_rating = O2_gen_rating * CO2_scrubber_rating
    print(life_support_rating)