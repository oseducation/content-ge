/*
 * File: SumN.java
 * ---------------------------------
 * კონსოლიდან წაიკითხეთ n, შემდეგ წაიკითხეთ n ცალი მთელი რიცხვი და დაბეჭდეთ ჯამი.
 */

import acm.program.*;

public class SumN extends ConsoleProgram {
	public void run() {
		//Getting number of input values
		int n = readInt("Enter n: ");
		int result = 0;
		
		//Getting numbers from user and increase value of result every iteration
		for(int i = 0; i < n; i++) {
			int tmp = readInt("Enter a number for sum: ");
			result += tmp;
		}
		
		println("Sum of received " + n + " numbers is " + result);
	}
}

