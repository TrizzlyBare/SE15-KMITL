package solutions.pack7;

public class GridPaths_661249 {
    public static int numberOfPaths(int [][] grid) {
        return numberOfPaths_helper(grid, 0, 0);
    }

    public static int numberOfPaths_helper(int [][] grid, int row, int col) {
        if (row == grid.length-1 && col == grid[0].length-1) {
            return 1;
        }
        if (row >= grid.length || col >= grid[0].length || grid[row][col] == 1) {
            return 0;
        }
        return numberOfPaths_helper(grid, row+1, col) + numberOfPaths_helper(grid, row, col+1);
    }
}
