from collections import defaultdict


class World:
    def __init__(self, size_of_world=(3, 5),  # load from file in init?
                 number_of_generations=-1, mode='every_turn', file=None):
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

        if file is not None:
            self._load_state(file)

    def _load_state(self, file=None):
        if file is None:
            return

    def _save_state(self, file=None):
        if file is None:
            return

    def _rules(self, cell='.', neighbors=None):
        return

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

                    new_field[i][j] = self._rules(self._field[i][j], neighbors)

            self._field = new_field

            if self._mode == 'every_turn' or \
                    self._current_generation == self._number_of_generations:
                self._save_state()
                return True

        return False
