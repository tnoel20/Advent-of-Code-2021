# Day 1 of Advent of Code 2021
#
# Counting the number of times the sonar depth measurement
# increases according to the given input


def count_increasing(measurements):
    ''' Counts the number of times the depth measurements increase. '''
    num_measurements = len(measurements)
    increasing_count = 0
    for i in range(1,num_measurements):
        if measurements[i] > measurements[i-1]:
            increasing_count += 1
    
    return increasing_count

def count_increasing_sliding(measurements):
    ''' 
    Counts number of times depth measurements increase when
    using sums determined by a three element sliding window.
    '''
    # Compute sum list
    num_measurements = len(measurements)

    a = 0
    b = 1
    c = 2
    sum_list = []
    while c < num_measurements:
        sum_list.append(measurements[a]+measurements[b]+measurements[c])
        a += 1
        b += 1
        c += 1

    # send list to "count_increasing"
    return count_increasing(sum_list)


if __name__ == '__main__':
    with open('input', mode='r') as f:
        sonar_measurements = f.readlines()
    sonar_measurements = [int(s) for s in sonar_measurements]
    print(count_increasing_sliding(sonar_measurements))