import stanford.karel.*;

public class KarelMethods extends Karel {
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

	private void turnRight(){
		turnLeft();
		turnLeft();
		turnLeft();
	}
}
