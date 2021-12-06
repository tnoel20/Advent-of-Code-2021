# Advent of Code Day 5
#
# Thomas Noel
# 
# Finding number of geothermal vent hotspots on seafloor
# (for the elves)

import numpy as np

def load_data(filename):
    with open(filename, 'r') as f:
        raw_input = f.readlines()
    
    raw_data = [datum.strip().split(' -> ') for datum in raw_input]
    data_list = [[np.array(points.split(','), dtype='int') for points in datum]
                     for datum in raw_data]
    data = np.array(data_list)

    return data


def generate_empty_grid(data):
    ''' Generates an empty grid based on the given data '''
    max_x = np.max(data[:,:,0]) + 1
    max_y = np.max(data[:,:,1]) + 1

    return np.zeros((max_y, max_x))


def filter_data(data, diag=False):
    ''' Retain only horizontal and vertical vent patterns '''
    filtered_data = []

    for datum in data:
        if datum[0,0] == datum[1,0] or datum[0,1] == datum[1,1]:
            filtered_data.append(datum)

        if diag:
            if abs(datum[0,0] - datum[1,0]) == abs(datum[0,1] - datum[1,1]):
                filtered_data.append(datum)

    return np.array(filtered_data)


def generate_geothermal_grid(data, diag=False):
    ''' Generate a map of geothermal activity '''
    grid = generate_empty_grid(data)
    filtered_data = filter_data(data, diag=diag)

    for datum in filtered_data:
        x0 = datum[0,0]
        y0 = datum[0,1]

        x1 = datum[1,0]
        y1 = datum[1,1]

        x_step = 1
        y_step = 1

        if x0 > x1:
            x_step = -1

        if y0 > y1:
            y_step = -1

        if not diag:
            grid[y0:(y1+y_step):y_step,x0:(x1+x_step):x_step] += 1
        else:
            if x0 == x1 or y0 == y1:
                grid[y0:(y1+y_step):y_step,x0:(x1+x_step):x_step] += 1
            else:
                difference = abs(x1-x0)
                x = x0
                y = y0
                for i in range(difference+1):
                    grid[y,x] += 1
                    x += x_step
                    y += y_step

    return grid


def count_hotspots(grid):
    return np.count_nonzero(grid>=2)


if __name__ == '__main__':
    data = load_data('input.txt')

    # Part 1
    ##grid = generate_geothermal_grid(data)
    ##hotspot_count = count_hotspots(grid)
    ##print(hotspot_count)

    # Part 2
    grid = generate_geothermal_grid(data, diag=True)
    hotspot_count = count_hotspots(grid)
    print(hotspot_count)