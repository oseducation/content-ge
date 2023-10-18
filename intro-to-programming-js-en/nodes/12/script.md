`for`` loop is a powerful tool when you know the exact number of iterations in advance. When you want to repeat some set of instructions several times. And you know exactly how many times you want to repeat instructions.

But life isn't always so predictable. What do you do when you're unsure about how many times instructions need to be repeated?

Consider this scenario: Karel starts at the intersection of the first street and the first avenue. And on the corner of the first street and last avenue lies a beeper. And you don't know how far away it is. 

A for loop would be great if you knew the distance, dictating precisely how many move() commands are required. But in this case, you're in the dark."

This is where you will need a while loop

Here's a general structure of the while loop:

while(some_condition()) {
	command1();
	command2();
	...
}

This is the header of the while loop and this is the body of the while loop. How this works is Karel will check the condition; if it's true, it will execute all the instructions in the loop body one by one. This is called an iteration. After the first iteration, Karel will recheck the condition, and if it's true, it will perform all the instructions one by one again, this is the second iteration, and so on. 
When Karel checks the condition, and it is false, the loop will end. And we do not know in advance how many iterations it took to end the loop.

For the above example what we could do is write

while (frontIsClear())

and frontIsClear is the condition that checks if there is no wall in front of Karel.

move();

What this code will do is move Karel until there's a will in front of it. That's exactly what we wanted.
And after the loop finishes, we could write pickBeeper to pick the beeper at the last avenue.



