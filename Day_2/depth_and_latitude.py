# Advent of Code 2021 Day 2
#
# Thomas Noel
#
# Computing submarine position given a course.

def process_input(filename):
    ''' Processes text input for Day 2 '''
    with open(filename, 'r') as f:
        course = f.read().strip().split('\n')
    
    course = [string_to_tuple(step) for step in course]
    return course


def string_to_tuple(raw_string):
    ''' Splits a string and constructs a tuple of its elements '''
    DISTANCE  = 1

    raw_elements = raw_string.split()
    raw_elements[DISTANCE] = int(raw_elements[DISTANCE])
    return tuple(raw_elements)


def get_position(course):
    ''' Computes the submarine's final position after completing course. '''
    DIRECTION = 0
    DISTANCE  = 1
    
    horizontal = 0
    depth = 0

    for step in course:
        if step[DIRECTION] == 'up':
            depth -= step[DISTANCE]
        elif step[DIRECTION] == 'down':
            depth += step[DISTANCE]
        else:
            horizontal += step[DISTANCE]

    return (horizontal, depth)


def get_position_with_aim(course):
    ''' 
    Computes the submarine's final position after completing course. 
    Takes aim into account.
    '''
    DIRECTION = 0
    DISTANCE  = 1
    
    horizontal = 0
    depth = 0
    aim = 0

    for step in course:
        if step[DIRECTION] == 'up':
            aim -= step[DISTANCE]
        elif step[DIRECTION] == 'down':
            aim += step[DISTANCE]
        else:
            horizontal += step[DISTANCE]
            depth += aim * step[DISTANCE]

    return (horizontal, depth)


if __name__ == '__main__':
    course = process_input('input.txt')
    position = get_position_with_aim(course)
    print(position[0]*position[1])