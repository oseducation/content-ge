import stanford.karel.*;

public class FirstKarel extends Karel {
	public void run(){
		move();
		pickBeeper();
		move();
		turnLeft();
		move();
		turnLeft();
		turnLeft();
		turnLeft();
		move();
		putBeeper();
		move();
	}
}
