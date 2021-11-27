import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Robot:

    def __init__(self, number, health, vision):
        self.number = number
        self.health = health
        self.vision = vision

    @staticmethod
    def move_left():
        return 'MOVE LEFT'

    @staticmethod
    def move_right():
        return 'MOVE RIGHT'

    @staticmethod
    def move_up():
        return 'MOVE UP'
    
    @staticmethod
    def move_down():
        return 'MOVE DOWN'

    @staticmethod
    def attack_left():
        return 'ATTACK LEFT'

    @staticmethod
    def attack_right():
        return 'ATTACK RIGHT'

    @staticmethod
    def attack_up():
        return 'ATTACK UP'
    
    @staticmethod
    def attack_down():
        return 'ATTACK DOWN'

    @staticmethod
    def selfdestruct():
        return 'SELFDESTRUCTION'
    
    @staticmethod
    def guard():
        return 'GUARD'

    @classmethod
    def from_input(cls, number, health, vision):
        return cls(number, health, vision)

    def __repr__(self):
        return f'Robot({self.number}, h:{self.health})'
    
    def __str__(self):
        return f'Robot n.{self.number} h:{self.health}'



def robots_from_input():
    robots = []
    number_of_robots = int(input())
    # load maps
    for nr in range(number_of_robots):
        vision = []
        health = None
        for row_num in range(5):
            row = list(map(int, input().split()))
            vision.append(row)
            if row_num == 2:
                health = row[2]
        robots.append(Robot.from_input(nr, health, vision))
    return robots

# game loop
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
while True:
    robots = robots_from_input()
    for robot in robots:
        print(robot, file=sys.stderr, flush=True)
        print(robot.selfdestruct())
