import unittest
import numpy as np
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assert_regions_partitioned_board(self):
        regions_total_size = sum(list(map(len, self.solution.regions)))
        board_total_size = self.solution.board.shape[0] ** 2
        self.assertEqual(regions_total_size, board_total_size)

        for (row, col), _ in np.ndenumerate(self.solution.board):
            region = self.solution.pos_to_region[(row, col)]
            self.assertIsNotNone(region)

    def assert_board_is_all_filled(self):
        return self.solution.board_is_all_filled()

    def assert_regions_are_valid(self):
        for region in self.solution.regions:
            values = set([self.solution.board[pos] for pos in region])
            self.assertEqual(values, set(range(1, len(region) + 1)))

    def assert_nearest_neighbor_are_valid(self):
        for (row, col), num in np.ndenumerate(self.solution.board):
            nearest_k = self.solution.find_nearest_k_dist(row, col, num)
            self.assertEqual(nearest_k, num)

    def test_case_1(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2],
            [0, 0, 4, 0, 0],
            [3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        regions = (
            ((0, 0), (0, 1), (1, 1), (1, 2), (2, 2)),
            ((0, 2), (0, 3), (0, 4), (1, 4), (2, 4)),
            ((1, 0), (2, 0), (3, 0), (4, 0), (4, 1)),
            ((1, 3),),
            ((2, 1),),
            ((2, 3), (3, 3), (3, 4), (4, 4)),
            ((3, 1), (3, 2), (4, 2)),
            ((4, 3),)
        )

        result = self.solution.solve(board, regions)
        print('\n', self.solution.board)

        self.assert_regions_partitioned_board()
        self.assert_board_is_all_filled()
        self.assert_regions_are_valid()
        self.assert_nearest_neighbor_are_valid()
        assert result == 430

    def test_case_2(self):
        board = [
            [0, 3, 0, 0, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [6, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 3, 0, 6],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 6, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 2, 0]
        ]

        regions = (
            ((0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (5, 0), (6, 0)),
            ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (1, 4)),
            ((0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 5), (1, 8), (1, 9)),
            ((1, 6), (1, 7), (2, 7)),
            ((2, 2), (2, 3), (3, 3)),
            ((2, 4), (2, 5)),
            ((2, 6), (3, 5), (3, 6), (3, 7), (4, 7), (4, 8)),
            ((2, 8), (2, 9), (3, 8), (3, 9), (4, 9), (5, 8), (5, 9)),
            ((3, 2), (4, 1), (4, 2), (5, 2)),
            ((3, 4), (4, 3), (4, 4)),
            ((4, 5), (5, 5)),
            ((4, 6),),
            ((5, 1),),
            ((5, 3), (6, 3), (6, 4), (6, 5), (7, 4)),
            ((5, 4),),
            ((5, 6), (5, 7), (6, 6)),
            ((6, 1), (7, 0), (7, 1), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2), (9, 3)),
            ((6, 2), (7, 2)),
            ((6, 7), (6, 8), (6, 9)),
            ((7, 3), (8, 3), (8, 4), (9, 4), (9, 5)),
            ((7, 5),),
            ((7, 6), (7, 9), (8, 5), (8, 6), (8, 9), (9, 6), (9, 7), (9, 8), (9, 9)),
            ((7, 7), (7, 8), (8, 7), (8, 8))
        )

        result = self.solution.solve(board, regions)

        self.assert_regions_partitioned_board()
        self.assert_board_is_all_filled()
        self.assert_regions_are_valid()
        self.assert_nearest_neighbor_are_valid()
        print('\n', self.solution.board)
        print(f'Result is {result}')


if __name__ == '__main__':
    unittest.main()
