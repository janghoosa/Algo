import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
class Solution {
    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();        
        int m = maps.length;
        int n = maps[0].length();

        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (Character.isDigit(maps[i].charAt(j)) && !visited[i][j]) {
                    int cellSum = dfs(maps, visited, i, j);
                    answer.add(cellSum);
                }
            }
        }
        
        int[] numbersArray;
        if (answer.isEmpty()) {
            numbersArray = new int[]{-1};
        } else {
            // List를 배열로 변환
            numbersArray = new int[answer.size()];
            for (int i = 0; i < answer.size(); i++) {
                numbersArray[i] = answer.get(i);
            }
            // 배열을 정렬
            Arrays.sort(numbersArray);
        }

        return numbersArray;
    }
    
    public int dfs(String[] maps, boolean[][] visited, int row, int col) {
        int m = maps.length;
        int n = maps[0].length();

        if (row < 0 || row >= m || col < 0 || col >= n || visited[row][col] || !Character.isDigit(maps[row].charAt(col))) {
            return 0;
        }

        visited[row][col] = true;
        int cellValue = Character.getNumericValue(maps[row].charAt(col));
        int cellSum = cellValue;

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int newRow = row + dr[i];
            int newCol = col + dc[i];
            cellSum += dfs(maps, visited, newRow, newCol);
        }
        return cellSum;
    }
}