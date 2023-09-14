# Bug in a First Karel Program

Let's revisit our First Karel Program. 

![World before](./../images/4_first_program_1.png)

Here's the code that does the job.

```js
move();
pickBeeper();
turnLeft();
move();
turnLeft();
turnLeft();
turnLeft();
move();
move();
putBeeper();
move();
```

Let's run code and make sure it's correct. But what happens if we run it again? A bug!
What happened? We ran the same program, but the world was changed Karel was not on the (1,1) corner anymore and it ran into a wall. 

So you should be aware and run the program for the correct world!