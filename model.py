from collections import defaultdict


class World:
    def __init__(self, size_of_world=(3, 5),  # load from file in init?
                 number_of_generations=-1, mode='every_turn',
                 loading_file=None, saving_file=None):
        if type(size_of_world) != tuple:
            return  # some kind of exception here

        if type(number_of_generations) != int:
            return  # and here

        if mode != 'every_turn' and mode != 'just_result':
            return  # and here, too

        self._width, self._height = size_of_world
        self._number_of_generations = number_of_generations
        self._current_generation = 0
        self._mode = mode
        self._field = [['.' for j in range(self._width)] for i in
                       range(self._height)]

        if loading_file is not None:
            if type(loading_file) != str:
                return

            file = open(loading_file)

            new_field = []

            for line in file:
                if len(line) != self._width:
                    file.close()
                    return

                new_field.append(list(line))

            file.close()

            if len(new_field) != self._height:
                return

            self._field = new_field

        if saving_file is None:
            self._saving_file = 'state.out'
        else:
            if type(saving_file) != str:
                return

            self._saving_file = saving_file

    def _save_state(self):
        file = open(self._saving_file, 'w')

        for line in self._field:
            file.write(''.join(line) + '\n')

        file.close()

    @staticmethod
    def _rules(cell, neighbors):
        if cell == '#':
            return '#'
        elif cell == '.':
            if neighbors['F'] == 3:
                return 'F'
            elif neighbors['C'] == 3:
                return 'C'
        elif cell == 'F':
            if neighbors['F'] >= 4 or neighbors['F'] < 2:
                return '.'
            else:
                return 'F'
        elif cell == 'C':
            if neighbors['C'] >= 4 or neighbors['C'] < 2:
                return '.'
            else:
                return 'C'

    def update(self):
        if self._current_generation < self._number_of_generations or \
                self._number_of_generations == -1:
            self._current_generation += 1

            new_field = [['.' for j in range(self._width)] for i in
                         range(self._height)]

            for i in range(self._height):
                for j in range(self._width):
                    neighbors = defaultdict(int)

                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if di == dj == 0:
                                continue
                            if i + di < 0 or i + di >= self._height:
                                neighbors['.'] += 1
                            elif j + dj < 0 or j + dj >= self._width:
                                neighbors['.'] += 1
                            else:
                                neighbors[self._field[i + di][j + dj]] += 1

                    new_field[i][j] = self._rules(self._field[i][j], neighbors)

            self._field = new_field

            if self._mode == 'every_turn' or \
                    self._current_generation == self._number_of_generations:
                self._save_state()
                return True

        return False
