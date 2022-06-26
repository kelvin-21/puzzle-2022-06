import numpy as np
from typing import List, Tuple, Set


class Solution:
    def __init__(self):
        self.board = None
        self.regions = None
        self.pos_to_region = None  # (i, j) -> region
        self.neighbor_watch_list = list()
        self.k_ball_boundaries = dict()  # (i, j, num) -> list of (i, j)

    def solve(self, board, regions) -> int:
        self.init(board, regions)
        if self.backtrack():
            return self.compute_result()
        return -1

    def backtrack(self, region_index=0, region_pos_index=0) -> bool:
        if self.board_is_all_filled():
            return True

        region = self.regions[region_index]
        pos = region[region_pos_index]
        row, col = pos

        if self.board[row, col] != 0:
            return self.backtrack(*self.next(region_index, region_pos_index))

        max_num = len(region)
        for num in range(max_num, 0, -1):
            self.board[row, col] = num
            if self.validate(row, col, num):
                if self.backtrack(*self.next(region_index, region_pos_index)):
                    return True

            self.board[row, col] = 0

        return False

    def init(self, board, regions):
        self.board = np.array(board)
        self.regions = sorted(regions, key=len)
        self.init_mapping()

    def init_mapping(self):
        self.pos_to_region = dict()  # (i, j) -> region
        for region in self.regions:
            for pos in region:
                self.pos_to_region[pos] = region

    def validate(self, row, col, num) -> bool:
        return self.region_valid(row, col, num) and \
               self.nearest_neighbor_valid(row, col, num) and \
               self.impacted_area_valid(row, col)

    def region_valid(self, row, col, num) -> bool:
        region = self.pos_to_region[(row, col)]
        max_num = len(region)
        if num > max_num:
            return False
        nonzero_values = [self.board[pos] for pos in region if self.board[pos] != 0]
        return len(nonzero_values) == len(set(nonzero_values))

    def nearest_neighbor_valid(self, row, col, num) -> bool:
        nearest_k_dist = self.find_nearest_k_dist(row, col, num)
        if self.is_k_ball_boundary_filled(row, col, num):
            return nearest_k_dist == num
        else:
            return nearest_k_dist >= num

    def impacted_area_valid(self, row, col) -> bool:
        impacted = self.get_impacted_positions(row, col)
        for i, j in impacted:
            k = self.board[i, j]
            if not self.nearest_neighbor_valid(i, j, k):
                return False
        return True

    def get_impacted_positions(self, row, col) -> List[Tuple[int, int]]:
        positions = list()
        for (i, j), num in np.ndenumerate(self.board):
            if num != 0 and self.compute_taxicab_dist(row, col, i, j) == num:
                positions.append((i, j))
        return positions

    def find_nearest_k_dist(self, row, col, num) -> float:
        regions_to_check = [region for region in self.regions if len(region) >= num]
        positions = list()
        for region in regions_to_check:
            for pos in region:
                if self.board[pos] == num:
                    positions.append(pos)
        distances = [self.compute_taxicab_dist(row, col, *pos) for pos in positions]
        distances = set(distances) - {0}
        return min(distances) if distances else float('inf')

    def is_k_ball_boundary_filled(self, row, col, num):
        positions = self.get_k_ball_boundary_positions(row, col, num)
        for pos in positions:
            if self.board[pos] == 0:
                return False
        return True

    def get_k_ball_boundary_positions(self, row, col, num) -> Set[Tuple[int, int]]:
        if (row, col, num) in self.k_ball_boundaries:
            return self.k_ball_boundaries[(row, col, num)]

        positions = set()
        for d in range(0, num + 1):
            reminder = num - d
            positions.add((row - d, col - reminder))
            positions.add((row - d, col + reminder))
            positions.add((row + d, col - reminder))
            positions.add((row + d, col + reminder))

        positions = set(filter(lambda x:
                               0 <= x[0] < self.board.shape[0] and
                               0 <= x[1] < self.board.shape[0],
                               positions))

        self.k_ball_boundaries[(row, col, num)] = positions
        return positions

    @staticmethod
    def compute_taxicab_dist(i1, j1, i2, j2) -> int:
        return abs(i2 - i1) + abs(j2 - j1)

    def board_is_all_filled(self) -> bool:
        return np.all(self.board)

    def next(self, region_index, region_pos_index) -> Tuple[int, int]:
        region = self.regions[region_index]
        if region_pos_index == len(region) - 1:
            return region_index + 1, 0
        return region_index, region_pos_index + 1

    def compute_result(self) -> int:
        return sum(list(map(np.prod, self.board)))
