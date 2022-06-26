# Block Party 4
The Jane Street puzzle for June 2022. Implemented the solution with backtracking.

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
  (ii) for any cell $c$ in the grid, for any $s \ne c$ with value($s$) = value($c$), min |$s - c$| = value($c$), where the distance is measured as the taxicab distance.
</p>

## Solution 1 (brute force)

### Algorithm

Iterate through every different configuration of the cells to fill the grid, return True if all of the followings hold:
<ol type="i">
  <li>Every region $R_i$ consists of unique values $1, 2, ...,|R_i|$ only.</li>
  <li>For every cell whose value is $K$, the nearest $K$ is exactly $K$ units away.</li>
</ol>

### Time complexity

Denote $R$ as the size of the largest region. Overall there will be $O(R^{M^2})$ iterations.

## Solution 2 (backtracking)

For each cell $c$ in the grid, try each possible value $K$ for that region that has not been used, and perform backtracking based. Continue if all of the followings hold, abandon otherwise.
1. (**Local neighbor check**) Check that the nearest $K$ is at least $K$ units away. Raise failure if the boundary of $K$-ball (centered at $c$) has been filled but does not contain any $K$.
2. (**Global neighbor check**) For each cell $s$ with value $S$ in the grid, if $s$ is exactly $S$ units away from the newly added cell $c$, then perform local neighbor check on $s$.

### Time complexity

Denote $T(X)X$ as the time complexity for solving grid with $X$ cells yet to fill, and $R$ as the size of the largest region.

Step (1) takes $O(R)$ to find the nearest $K$ and another $O(R)$ to check whether the boundary of $K$-ball has been filled, thus taking $O(R)$ overall.

For step (2), note that a boundary of a $K$-ball can only contain a limited number of $K$'s because they also have to be $K$ units away from each other (for exampe, the boundary of $1$-ball at any point can contain at most 4 $1$'s, for $2$-ball it is 8 $2$'s, for $3$-ball it is 4 $3$'s, for $4$-ball it is 8 $4$'s, etc). Thus in average there will be $O(R)$ cells we need to check and each check takes $O(R)$ time. Overall, step (2) takes $O(R^2)$ time.

Combining the property of backtracking and time required for local and global neighbor checks gives
$$T(X) = RT(X-1) + O(R^2)$$

### Remarks
1. Memorization helps optimize the performance. For this problem, it is found useful to store mappings like
    * cell position $\mapsto$ region
    * cell position, value $K$ $\mapsto$ boundary of $K$-ball
2. For this problem in particular, it is found faster to start backtracking with smaller regions.
