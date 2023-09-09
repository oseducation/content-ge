/* 
 * File: DoubleBeepers.java 
 * ------------------------ 
 * Karel doubles the number of beepers on the corner directly 
 * in front of him in the world. He then returns to his 
 * original position/orientation. 
 */
import stanford.karel.*;

public class DoubleBeepers extends SuperKarel{
	public void run(){
		move();
		doubleBeepersInPile();
		moveBack();
	}
	
	/* 
	 * Move Karel back one avenue, but have the same 
	 * final orientation. 
	 */
	private void moveBack(){
		turnAround();
		move();
		turnAround();
	}
	
	/* 
	 * For every beeper on the current corner, Karel places 
	 * two beepers on the corner immediately ahead of him. 
	 */
	private void doubleBeepersInPile(){
		while (beepersPresent()){
			pickBeeper();
			putTwoBeepersNextDoor();
		}
		movePileBack();
	}
	
	/* 
	 * Place two beepers on corner one avenue ahead of Karel 
	 * and move back to starting position/orientation 
	 */
	private void putTwoBeepersNextDoor(){
		move();
		putBeeper();
		putBeeper();
		moveBack();
	}
	/* 
	 * Move all the beepers on the corner in front of Karel 
	 * the the corner Karel is currently on. 
	 */
	private void movePileBack(){
		move();
		while(beepersPresent()){
			moveOneBeeperBack();
		}
		moveBack();
	}
	
	/* 
	 * Move one beeper from the current corner back one avenue 
	 * and return to the original position/orientation. 
	 */
	private void moveOneBeeperBack(){
		pickBeeper();
		moveBack();
		putBeeper();
		move();
	}
}
