#  Global Variables

# Rovers count
rover_count = 2
# orientation list
orient = ['N', 'E', 'S', 'W']
# movement of rovers, 1 grid point
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
# commands sent to rovers
instructions = {'L': 'left', 'R': 'right', 'M': 'move'}


class Rover:

    def __init__(self, x, y, x_max, y_max, direction, series_of_instructions):

        self.x = x
        self.y = y
        self.x_max = x_max
        self.y_max = y_max
        self.direction = direction
        self.series_of_instructions = set(series_of_instructions)

    def right(self):
        # Turn right
        self.direction = orient[(orient.index(self.direction.upper()) + 1) % len(orient)]

    def left(self):
        # Turn left
        self.direction = orient[(orient.index(self.direction.upper()) - 1) % len(orient)]

    def move(self):

        # Moving forward 1 grid point method

        x_mov = self.x + move[self.direction.upper()][0]
        y_mov = self.y + move[self.direction.upper()][1]

        if (x_mov, y_mov) not in self.series_of_instructions:
            if self.x_max >= x_mov >= 0:
                self.x = x_mov
            if self.y_max >= y_mov >= 0:
                self.y = y_mov
            else:
                print('Out of the grid limits. Please Try Again!!')
                exit()
        else:
            print('Rovers cannot be the same place. Please Try Again!!')
            exit()


if __name__ == '__main__':

    # get grid size from input
    x_max, y_max = map(int, input('grid:').split())

    series_of_instructions = set([])
    check_coordinates = []
    results = []

    # count_a for rover_count for loop
    count_a = 1
    # count_b for instructions for loop
    count_b = 1

    for _ in range(rover_count):

        x, y, direction = input('Enter the coordinates for rover %d:' % count_a).upper().split()
        count_a += 1

        if [x, y, direction] not in check_coordinates:
            check_coordinates.append([x, y, direction])
            rover = Rover(int(x), int(y), x_max, y_max, direction, series_of_instructions)
            # iterate over instructions string
            for i in input('instructions for rover %d:' % count_b).upper():
                if i not in 'MRL':
                    print('Invalid instructions "%s": use M or R or L. Please Try Again' % i)
                    exit()
                else:

                    getattr(rover, instructions[i])()
            count_b += 1

            series_of_instructions.add((rover.x, rover.y))
            results.append((rover.x, rover.y, rover.direction))
        else:
            print('2 rovers share the same point. Please Try Again')
            exit()

    # print results
    for x, y, z in results:
        print(x, y, z)
