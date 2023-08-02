/*
 * File: HarmonicMean.java
 * -----------------------
 * Read three integers from the console and print their harmonic mean.
 */

import acm.program.*;

public class HarmonicMean extends ConsoleProgram {
    public void run() {
        int x = readInt("Enter a number: ");
        int y = readInt("Enter a number: ");
        int z = readInt("Enter a number: ");
        double numerator = (double) x * y * z;
        double denominator = (double) y * z + x * z + x * y;
        double result = numerator/denominator;
        println(result);
    }
}
