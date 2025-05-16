package solutions.pack7;

import java.util.ArrayList;
import java.util.List;

public class Subsets_661249 {
    public static void printAllSubsets_Recurse(List<Integer> set) {
        List<Integer> currentSubset = new ArrayList<>();
        printAllSubsets_Recurse_helper(set, 0, currentSubset);
    }

    public static void printAllSubsets_Recurse_helper(List<Integer> set, int index, List<Integer> currentSubset) {
        if (index == set.size()) {
            System.out.println(currentSubset);
            return;
        }
        currentSubset.add(set.get(index));
        printAllSubsets_Recurse_helper(set, index+1, currentSubset);
        currentSubset.remove(currentSubset.size()-1);
        printAllSubsets_Recurse_helper(set, index+1, currentSubset);
    }

    public static void printAllSubsets_DP(List<Integer> set) {
        List<List<Integer>> allSubsets = new ArrayList<>();
        allSubsets.add(new ArrayList<>());
        for (int i = 0; i < set.size(); i++) {
            int n = allSubsets.size();
            for (int j = 0; j < n; j++) {
                List<Integer> subset = new ArrayList<>(allSubsets.get(j));
                subset.add(set.get(i));
                allSubsets.add(subset);
            }
        }
        for (List<Integer> subset : allSubsets) {
            System.out.println(subset);
        }
    }
}
