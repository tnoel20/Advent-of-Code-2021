# Advent of Code
# 
# Day 7
# 
# Aligns crab submarines horizontally
#
# Written by Thomas Noel

import statistics

def read_input(filename):
    with open(filename, 'r') as f:
        raw_input = f.read().split(',')
    
    data = [int(pos) for pos in raw_input]
    return data


def compute_optimal_position(data):
    return int(statistics.median(data))


def compute_optimal_position_p2(data):
    return int(statistics.mean(data))


def compute_fuel_cost(final_pos, data):
    sum = 0
    for pos in data:
        sum += abs(final_pos - pos)

    return sum


def transform_data(data):
    tx_data = []
    for pos in data:
        tx_data.append((pos)*(pos+1)/2)
    return tx_data


def compute_fuel_cost_new(final_pos, data):
    sum = 0
    for pos in data:
        cost = abs(final_pos - pos)
        sum += cost * (cost + 1) / 2

    return sum

if __name__ == '__main__':
    data = read_input('input.txt')

    # Part 1
    #final_pos = compute_optimal_position(data)
    #fuel_cost = compute_fuel_cost(final_pos, data)
    #print(fuel_cost)

    #data = [16,1,2,0,4,2,7,1,2,14]
    #tx_data = transform_data(data)
    #print(tx_data)
    final_pos = compute_optimal_position_p2(data)
    print(final_pos)
    fuel_cost = compute_fuel_cost_new(final_pos, data)
    print(fuel_cost)