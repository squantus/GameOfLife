import model
import argparse
import graphics


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', type=str, default='stdin',
                        help='Path to input file(stdin as default)')

    parser.add_argument('--output_file', type=str, default='stdout',
                        help='Path to output file(stdout as default)')

    parser.add_argument('--mode', type=str, default='every_turn',
                        help='Showing mode(every_turn or just_once)\n' +
                             'every_turn as default')

    parser.add_argument('--graphical_mode', type=str, default='True',
                        help='Graphical mode(\'False\' if only text)\n' +
                             'For normal usage you need pygame')

    parser.add_argument('--height_of_world', type=int, default=1,
                        help='Height of World(1 as default)')

    parser.add_argument('--width_of_world', type=int, default=1,
                        help='Width of World(1 as default)')

    parser.add_argument('--number_of_generations', type=int, default=-1,
                        help='Number of generations(infinite as default)\n' +
                             'Should be infinite only in graphical mode')

    args = parser.parse_args()

    world = model.World((args.width_of_world, args.height_of_world),
                        args.number_of_generations,
                        args.mode, args.input_file, args.output_file)

    if args.graphical_mode == 'True':
        block_size = min(800 // args.width_of_world,
                         600 // args.height_of_world)
        display = graphics.init((args.width_of_world * block_size,
                                 args.height_of_world * block_size))
        graphics.loop(world, display, block_size)

    while args.number_of_generations != -1 and world.update():
        pass


if __name__ == '__main__':
    main()
