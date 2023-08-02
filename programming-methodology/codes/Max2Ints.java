import acm.program.*;

public class Max2Ints extends ConsoleProgram {
	public void run() {
		int a = readInt("Enter the first Integer: ");
		int b = readInt("Enter the second Integer: ");
		int bigger;
		if(a > b) {
			bigger = a;
		} else {
			bigger = b;
		}
		println("The bigger integer of the two is " + bigger);
	}
}
