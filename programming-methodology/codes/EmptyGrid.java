import acm.graphics.*;
import acm.program.GraphicsProgram;

/*
 * File: EmptyGrid.java
 * ---------------------
 * 
 *  ამოცანის პირობა:
 * 	ხაზებით ბადის დახატვა 10x10 ზე
 * 
 */

public class EmptyGrid extends GraphicsProgram {
	private static final int CELLS = 10; // Number of cells

	public void run() {
		/* Calculate a gap between each row and column */ 
		int rowGap = getHeight() / CELLS; 
		int columnGap = getWidth() / CELLS;

        /* Draw Rows */
		for(int row = 0; row <= CELLS; row++) {
			/* Coordinates */ 
			double x0 = 0;
			double x1 = getWidth();
			double y = row * rowGap;

			GLine line = new GLine(x0, y, x1, y); 
			add(line); 
		}

        /* Draw Columns */
		for(int col = 0; col <= CELLS; col++) {	
			/* Coordinates */
			double y0 = 0;
			double y1 = getHeight();
			double x = col * columnGap;

			GLine line = new GLine(x, y0, x, y1);
			add(line);
		}
	}
}
