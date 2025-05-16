package solutions.pack12b_SSP;

import java.util.*;

interface InterfaceSwapAdjacentPairs {

    int[] swapAdjacentPairs(InterfaceSwapAdjacentPairs.State s);

    class State {

        int[] state;

        State(int[] state) {
            this.state = state;
        }
    }
}

interface InterfaceSwapCorrespondingHalves {

    int[] swapCorrespondingHalves(InterfaceSwapCorrespondingHalves.State s);

    class State {

        int[] state;

        State(int[] state) {
            this.state = state;
        }
    }
}

public class Task3 {

    class State {

        int[] state;
        int level;

        State(int[] state, int level) {
            this.state = state;
            this.level = level;
        }
    }

    public int stateSpace(int[] beginState, int[] goalState) {
        if (Arrays.equals(beginState, goalState)) {
            return 0;
        }

        InterfaceSwapAdjacentPairs swapPairs = (InterfaceSwapAdjacentPairs.State s) -> {
            int[] newState = Arrays.copyOf(s.state, s.state.length);
            for (int i = 0; i < newState.length - 1; i += 2) {
                int temp = newState[i];
                newState[i] = newState[i + 1];
                newState[i + 1] = temp;
            }
            return newState;
        };

        InterfaceSwapCorrespondingHalves swapHalves = (InterfaceSwapCorrespondingHalves.State s) -> {
            int[] newState = Arrays.copyOf(s.state, s.state.length);
            int mid = newState.length / 2;
            for (int i = 0; i < mid; i++) {
                int temp = newState[i];
                newState[i] = newState[mid + i];
                newState[mid + i] = temp;
            }
            return newState;
        };

        Queue<State> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.add(new State(beginState, 0));
        visited.add(Arrays.toString(beginState));

        while (!queue.isEmpty()) {
            State current = queue.poll();
            int[] currentState = current.state;
            int level = current.level;

            int[] swappedPairs = swapPairs.swapAdjacentPairs(new InterfaceSwapAdjacentPairs.State(currentState));
            int[] swappedHalves = swapHalves.swapCorrespondingHalves(new InterfaceSwapCorrespondingHalves.State(currentState));

            if (Arrays.equals(swappedPairs, goalState) || Arrays.equals(swappedHalves, goalState)) {
                return level + 1;
            }

            if (!visited.contains(Arrays.toString(swappedPairs))) {
                queue.add(new State(swappedPairs, level + 1));
                visited.add(Arrays.toString(swappedPairs));
            }

            if (!visited.contains(Arrays.toString(swappedHalves))) {
                queue.add(new State(swappedHalves, level + 1));
                visited.add(Arrays.toString(swappedHalves));
            }
        }

        return -1;
    }
}
