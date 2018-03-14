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

    def update(self):  # what about rules? maybe classes or functions?
        return
