package solutions.pack12b_SSP;

public interface InterfaceSwapCorrespondingHalves {

    public class State {

        int[] state;

        public State(int[] state) {
            this.state = state;
        }
    }

    int[] swapCorrespondingHalves(State s);
}
