package solutions.pack7;

public class EqualSubsets_661249 {
    public static boolean canPartition_Recur(int [] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        } 
        if (sum % 2 != 0) {
            return false;
        }
        return canPartition_Recur_helper(arr, 0, sum/2);
    } 

    public static boolean canPartition_Recur_helper(int [] arr, int index, int sum) {
        if (sum == 0) {
            return true;
        }
        if (index >= arr.length) {
            return false;
        }
        if (arr[index] <= sum) {
            if (canPartition_Recur_helper(arr, index+1, sum - arr[index])) {
                return true;
            }
        }
        return canPartition_Recur_helper(arr, index+1, sum);
    }

    public static boolean canPartition_Memoiz(int [] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        if (sum % 2 != 0) {
            return false;
        }
        Boolean [][] memo = new Boolean[arr.length][sum/2 + 1];
        return canPartition_Memoiz_helper(arr, 0, sum/2, memo);
    }

    public static boolean canPartition_Memoiz_helper(int [] arr, int index, int sum, Boolean [][] memo) {
        if (sum == 0) {
            return true;
        }
        if (index >= arr.length) {
            return false;
        }
        if (memo[index][sum] != null) {
            return memo[index][sum];
        }
        if (arr[index] <= sum) {
            if (canPartition_Memoiz_helper(arr, index+1, sum - arr[index], memo)) {
                memo[index][sum] = true;
                return true;
            }
        }
        memo[index][sum] = canPartition_Memoiz_helper(arr, index+1, sum, memo);
        return memo[index][sum];
    }

    public static boolean canPartition_DP(int [] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        if (sum % 2 != 0) {
            return false;
        }

        boolean [][] dp = new boolean[arr.length][sum/2 + 1];

        for (int i = 0; i < arr.length; i++) {
            dp[i][0] = true;
        }

        for (int j = 1; j <= sum/2; j++) {
            dp[0][j] = (arr[0] == j);
        }

        for (int i = 1; i < arr.length; i++) {
            for (int j = 1; j <= sum/2; j++) {
                if (dp[i-1][j]) {
                    dp[i][j] = true;
                } else if (arr[i] <= j) {
                    dp[i][j] = dp[i-1][j - arr[i]];
                }
            }
        }
        
        return dp[arr.length-1][sum/2];
    }
}
