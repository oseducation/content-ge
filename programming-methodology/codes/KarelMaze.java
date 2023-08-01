import stanford.karel.*;

public class KarelMaze extends Karel {
 	public void run() {
 		while (noBeepersPresent()) {
 			if (rightIsBlocked()) {
 				if (frontIsClear()) {
 					move();
 				} else {
 					while (frontIsBlocked()) {
 						turnRight();
					}
 				}
 			} else {
 				turnRight();
 				move();
 			}
 		}
 	}
}