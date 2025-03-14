import os

from utils import log_func_call


def logger(path):

    def __logger(old_function):

        def new_function(*args, **kwargs):
            return log_func_call(path, old_function, *args, **kwargs)

        return new_function

    return __logger


def test_3():

    def flat_generator(list_of_lists):
        for row in list_of_lists:
            for el in row:
                yield el

    @logger(path=os.path.join(os.getcwd(), 'logs', 'flat_list.log'))
    def get_flat_list(list_of_lists):
        return list(flat_generator(list_of_lists))

    test_data = [
        [
            [
                ['a', 'b', 'c'],
                ['d', 'e', 'f', 'h', False],
                [1, 2, None]
            ],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ],
        [
            [
                ['a', None, 'b'],
                [],
                ['c', 'd'],
                ['e'],
            ],
            ['a', None, 'b', 'c', 'd', 'e']
        ],
        [
            [
                [],
                [],
                [0, 1, 2],
                [],
                [3],
                []
            ],
            [0, 1, 2, 3]
        ]
    ]

    for item in test_data:
        assert get_flat_list(item[0]) == item[1]


if __name__ == '__main__':
    test_3()