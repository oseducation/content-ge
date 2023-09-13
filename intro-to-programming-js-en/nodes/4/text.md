# First Karel Program
Let's write your first Karel program, you know all the commands already. Imagine that Karel lives in the world below

![World before](./../images/4_first_program_1.png)

You job is to write program, where Karel will take the beeper on the (2,1) corner, will put it on the (4,2) corner and finish working on (5,2). After program execution world should look like this:

![World after](./../images/4_first_program_2.png)

It's easy enough with the following commands:

```js
move
pickBeeper
turnLeft
move
turnLeft
turnLeft
turnLeft
move
move
putBeeper
move
```

But, this is not a program yet. This is the instruction to solve the problem, but it's for humans to understand not for Karel. This is not a program this is an algorithm. Let's turn it to program. To do this we must turn all the commands into the **functions**. Basically **functions** are commands that could be executed. To do that we will just need to add `();` symbols at the end of all the commands. That's it!

So we get:

```ja
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

Yay! It's your first program! Go ahead run it in our [Karel environment](karel_environment_link)

