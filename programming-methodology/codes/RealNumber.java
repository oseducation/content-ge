/*
 * File: RealNumber.java
 * ---------------------
 * 
 * ამოცანის პირობა:
 * 	კონსოლიდან წაიკითხეთ ნამდვილი რიცხვი და დაბეჭდეთ მისი მთელი ნაწილი და მისი
 *	წილადი ნაწილი. მაგალითად, მომხმარებელმა თუ შეიყვანა 3.14 თქვენმა პროგრამამ უნდა
 *	დაბეჭდოს 3 და 0.14.
 * 
 */

import acm.program.*;

public class RealNumber extends ConsoleProgram {
	public void run() {
		// We get a real number and store it in a variable.
		double realNumber = readDouble("Input real number: ");
		
		// By casting, we turn the value of the float type variable into an int.
		int integralPart = (int) realNumber;
		
		// By subtracting the whole number, we are left with only the fractional part.
		double fractionalPart = realNumber - integralPart;

		println("Integral Part: " + integralPart);
		println("Fractional Part: " + fractionalPart);	
	}
}

