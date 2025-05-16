package solutions;

import java.util.Stack;

public class TheLake {

    public int findTotalMaxDepth(int[][] map) {
        if (map == null || map.length == 0 || map[0].length == 0) {
            return 0;
        }

        int rows = map.length;
        int cols = map[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int maxDepth = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (map[r][c] > 0 && !visited[r][c]) {
                    int currentDepth = exploreLake(map, visited, r, c);
                    maxDepth = Math.max(maxDepth, currentDepth);
                }
            }
        }

        return maxDepth;
    }

    private int exploreLake(int[][] map, boolean[][] visited, int startRow, int startCol) {
        int totalDepth = 0;
        int rows = map.length;
        int cols = map[0].length;
        Stack<int[]> stack = new Stack<>();

        stack.push(new int[]{startRow, startCol});
        visited[startRow][startCol] = true;

        int[] rowDir = {-1, 1, 0, 0};
        int[] colDir = {0, 0, -1, 1};

        while (!stack.isEmpty()) {
            int[] current = stack.pop();
            int r = current[0];
            int c = current[1];

            totalDepth += map[r][c];

            for (int d = 0; d < 4; d++) {
                int newRow = r + rowDir[d];
                int newCol = c + colDir[d];

                if (isValid(newRow, newCol, rows, cols) && !visited[newRow][newCol] && map[newRow][newCol] > 0) {
                    stack.push(new int[]{newRow, newCol});
                    visited[newRow][newCol] = true;
                }
            }
        }

        return totalDepth;
    }

    private boolean isValid(int row, int col, int rows, int cols) {
        return row >= 0 && row < rows && col >= 0 && col < cols;
    }
}
