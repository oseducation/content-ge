/*
 * File: Average.java
 * ---------------------------------
 * Average
 * კონსოლიდან წაიკითხეთ ორი რიცხვი, დაბეჭდეთ მათი საშუალო არითმეტიკული.
 */
import acm.program.*;

public class Average3 extends ConsoleProgram {
	public void run() {
		// Reading input values
		int firstNumber = readInt("Enter first number: ");
		int secondNumber = readInt("Enter second number: ");
		int thirdNumber = readInt("Enter third number: ");
		int sum = firstNumber + secondNumber + thirdNumber; // Sum of numbers
		double average = (double) sum / 3; // Without cast it would be an integer division
		println(average);
	}

}

