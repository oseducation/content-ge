import stanford.karel.*;

public class KarelOBOB extends SuperKarel {
	public void run(){
		while (frontIsClear()) {
			putBeeper();
			move();
		}
	}
}
