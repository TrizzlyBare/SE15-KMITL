package Labs;

import java.util.ArrayList;
import java.util.List;
import solutions.pack7.EqualSubsets_661249;
import solutions.pack7.GridPaths_661249;
import solutions.pack7.Subsets_661249;

public class Lab7_Recursion_DP_Main {
    public static void main(String[] args) {
        testEqualSubsets();
        System.out.println("----");
        testSubSets();
        testGridPaths();
    }
    static void testEqualSubsets() {
        int [] a = {1,5,11,5};
        int [] b = {1,5,3};
        System.out.println(EqualSubsets_661249.canPartition_Recur(a));
        System.out.println(EqualSubsets_661249.canPartition_Recur(b));
        System.out.println(EqualSubsets_661249.canPartition_Memoiz(a));
        System.out.println(EqualSubsets_661249.canPartition_Memoiz(b));
        System.out.println(EqualSubsets_661249.canPartition_DP(a));
        System.out.println(EqualSubsets_661249.canPartition_DP(b));     
    }
    static void testSubSets() { 
        System.out.println("--- Subsets ---");
        List<Integer> set = new ArrayList<>();
        set.add(1); 
        set.add(2); 
        set.add(3);
        System.out.println("using recursive method");
        Subsets_661249.printAllSubsets_Recurse(set);
        System.out.println("using dynamic programming method");
        Subsets_661249.printAllSubsets_DP(set);
    }
    static void testGridPaths() {
        int [][] grid = { {0,0,0},
                          {0,1,0},  
                          {0,0,0},
                          };
        System.out.println("--- grid paths ---");
        System.out.println("number of paths: " + GridPaths_661249.numberOfPaths(grid));
    }
}