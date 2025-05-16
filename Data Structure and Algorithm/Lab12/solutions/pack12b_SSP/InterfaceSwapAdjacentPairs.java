package solutions.pack12b_SSP;

public interface InterfaceSwapAdjacentPairs {

    public class State {

        int[] state;

        public State(int[] state) {
            this.state = state;
        }
    }

    int[] swapAdjacentPairs(State s);
}
