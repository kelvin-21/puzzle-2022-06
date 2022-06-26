# Block Party 4
The Jane Street puzzle for June 2022.

## Problem Statement

The original problem statement can be found [here](https://www.janestreet.com/puzzles/current-puzzle/).

><p align="center"><img src="https://www.janestreet.com/puzzles/block-party-4.png" width="640" height="640" /></p>
>
> *Fill each region with the numbers 1 through N, where N is the number of cells in the region. For each number K in the grid, the nearest K via [taxicab distance](https://en.wikipedia.org/wiki/Taxicab_geometry) must be exactly K cells away.*
>
> *Once the grid is completed, the answer to the puzzle is found as follows: compute the product of the values in each row, and then take the sum of these products.*

To give proper notation to the problem:

<p align="center" width="640">
  Given a $M \times M$ grid with some initial values and $n$ regions ($R_1, R_2, ..., R_n$) that partition the grid, fill the grid such that
  (i) for any region $R_i$, it consists of $1, 2, ..., |R_i|$ exactly one each, and 
  (ii) for every cell $c$ in the grid, there exists cell $c' \ne c$ such that value($c$) = value($c'$) = |$c - c'$|, where the distance is measured as the taxicab distance.
</p>

# Solution 1 (brute force)

# Solution 2 (backtracking)

# Solution 2 enhanced (with memorization)
