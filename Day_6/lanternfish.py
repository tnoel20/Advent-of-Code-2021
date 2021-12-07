# Advent of Code
#
# Day 6
# Simulating lanternfish population growth

import numpy as np
import math

class LanternFish:
    ''' A Lantern Fish '''
    def __init__(self, days_until_birth=8):
        self.days = days_until_birth

    def age_one_day(self):
        new_lantern_fish = False

        if self.days == 0:
            self.days = 6
            new_lantern_fish = True
        else:
            self.days -= 1

        return new_lantern_fish


class LanternFishSimulation:
    ''' A Simulation of Lantern Fish Population Dynamics '''
    def __init__(self, days, fish_timers):
        self.days_left = days
        self.lantern_fish = [LanternFish(days) for days in fish_timers]

    def step_one_day(self):
        simulation_in_progress = True
        new_fish = False

        num_lantern_fish = len(self.lantern_fish)

        for i in range(num_lantern_fish):
            new_fish = self.lantern_fish[i].age_one_day()
            if new_fish:
                self.lantern_fish.append(LanternFish())

        self.days_left -= 1

        if self.days_left == 0:
            simulation_in_progress = False

        return simulation_in_progress

    def get_num_fish(self):
        return len(self.lantern_fish)
    

def load_data(filename):
    with open(filename, 'r') as f:
        raw_data = f.read().strip().split(',')

    data = [int(datum) for datum in raw_data]
    return data


def lantern_fish_sim_barebones(total_days, fish_data):
    fish_array = np.array(fish_data)
    fish_bins = 9
    fishtogram, _ = np.histogram(fish_array, bins=fish_bins, range=(0,8))

    for day in range(total_days):
        new_fishtogram = np.zeros_like(fishtogram)
        for i in range(fish_bins-1, -1, -1):
            if i != 0:
                new_fishtogram[i-1] = fishtogram[i]
            else:
                new_fishtogram[-1] = fishtogram[0]
                new_fishtogram[6] += fishtogram[0]

        fishtogram = new_fishtogram

    return np.sum(fishtogram)


def main():
    data = load_data('input.txt')

    # Part 1
    # num_days = 80
    # fish_sim = LanternFishSimulation(num_days, data)
    
    # for i in range(num_days):
    #     print(i)
    #     fish_sim.step_one_day()
    
    # print(fish_sim.get_num_fish())

    # Part 2
    num_days = 256
    num_fish = lantern_fish_sim_barebones(num_days, data)
    print(num_fish)
    

if __name__ == '__main__':
    main()