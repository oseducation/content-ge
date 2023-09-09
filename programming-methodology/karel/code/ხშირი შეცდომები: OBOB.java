import stanford.karel.*;

public class KarelOBOB extends SuperKarel {
	public void run(){
		move();
		move();
		turnLeft();
		move();
		while (frontIsClear()) {
			turnLeft();
		}
	}
}
