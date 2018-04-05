import sys
from collections import defaultdict


class Cell:
    @staticmethod
    def name():
        return '~'

    def is_empty(self):
        return False

    def is_alive(self):
        return False

    def update(self, neighbors):
        return self


class EmptyCell(Cell):
    @staticmethod
    def name():
        return '.'

    def is_empty(self):
        return True

    def update(self, neighbors):
        alive_count = defaultdict(int)
        alive_cells = dict()

        for cell in neighbors:
            if cell.is_alive():
                alive_count[cell.name()] += 1
                alive_cells[cell.name()] = cell

        for key in alive_count.keys():
            if alive_count[key] >= 3:
                return alive_cells[key]

        return self


class Rock(Cell):
    @staticmethod
    def name():
        return '#'


class Animal(Cell):
    def is_alive(self):
        return True

    def update(self, neighbors):
        count = 0

        for cell in neighbors:
            if cell.name() == self.name():
                count += 1

        if count >= 4 or count < 2:
            return EmptyCell()
        else:
            return self


class Fish(Animal):
    @staticmethod
    def name():
        return 'F'


class Shrimp(Animal):
    @staticmethod
    def name():
        return 'S'


class World:
    def __init__(self, size_of_world, number_of_generations, mode,
                 input_file, output_file):

        self._width, self._height = size_of_world
        self._number_of_generations = number_of_generations
        self._current_generation = 0
        self._mode = mode
        self._output_file = output_file
        self._field = [[EmptyCell() for j in range(self._width)] for i in
                       range(self._height)]

        if input_file == 'stdin':
            file = sys.stdin
        else:
            file = open(input_file)

        new_field = []

        for line in file:
            new_field.append(list(line))

            if len(new_field) == len(self._field):
                break

        file.close()

        self._field_log = new_field

        for i in range(self._height):
            for j in range(self._width):
                if self._field_log[i][j] == '.':
                    self._field[i][j] = EmptyCell()
                elif self._field_log[i][j] == '#':
                    self._field[i][j] = Rock()
                elif self._field_log[i][j] == 'F':
                    self._field[i][j] = Fish()
                elif self._field_log[i][j] == 'S':
                    self._field[i][i] = Shrimp()

    def get_field_log(self):
        return self._field_log

    def _save_state(self):
        if self._output_file == 'stdout':
            file = sys.stdout
        else:
            file = open(self._output_file, 'w')

        for line in self._field_log:
            file.write(''.join(line) + '\n')

        if self._output_file != 'stdout':
            file.close()

    def update(self):
        if self._current_generation < self._number_of_generations or \
                self._number_of_generations == -1:
            self._current_generation += 1

            new_field = [[EmptyCell() for j in range(self._width)] for i in
                         range(self._height)]
            new_field_log = [['.' for j in range(self._width)] for i in
                             range(self._height)]

            for i in range(self._height):
                for j in range(self._width):
                    neighbors = []

                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if di == dj == 0:
                                continue
                            if i + di < 0 or i + di >= self._height:
                                neighbors.append(EmptyCell())
                            elif j + dj < 0 or j + dj >= self._width:
                                neighbors.append(EmptyCell())
                            else:
                                neighbors.append(self._field[i + di][j + dj])

                    new_field[i][j] = self._field[i][j].update(neighbors)
                    new_field_log[i][j] = new_field[i][j].name()

            self._field = new_field
            self._field_log = new_field_log

            if self._mode == 'every_turn' or \
                    self._current_generation == self._number_of_generations:
                self._save_state()

            return True

        return False
