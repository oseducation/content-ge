import stanford.karel.*;

public class KarelMethods extends SuperKarel {
	public void run(){
		move();
		pickBeeper();
		move();
		turnLeft();
		move();
		turnRight();
		move();
		putBeeper();
		move();
	}
}
