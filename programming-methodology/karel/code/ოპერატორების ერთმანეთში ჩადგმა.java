import stanford.karel.*;

public class KarelWhileLoop extends SuperKarel {
	public void run(){
		while (frontIsClear()) {
			if (noBeepersPresent()) {
				putBeeper();
			} else {
				move();
			}
			move();
		}
	}
}
