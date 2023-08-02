/*
* File: NumberOfDivisors.java
* ---------------------------

* ამოცანის პირობა:
* მომხმარებელს შეყავს მთელი რიცხვი n, პროგრამამ უნდა დაბეჭდოს n ის გამყოფების რაოდენობა
*/
import acm.program.*;

public class NumberOfDivisors extends ConsoleProgram {
	public void run() {
		int num = readInt("Enter a number: ");
			
		// In case entered number is not natural
		while (num <= 0) {
			num = readInt("Please enter positive number: ");
		}		
		
		int cnt = 0;
		for (int i = 1; i <= num; i++) {
			if (num % i == 0) {
				cnt += 1;
			}
		}
	
		println("The number: " + num + " has " + cnt + " divisors");
	}
}
