# `while` Loop in Karel

You can use the `for` loop when you want to repeat some set of instructions several times. And you know exactly how many times you want to repeat instructions. But what happens when you want to repeat some commands but do not now how many times? 

## Problem Statement
Let's imagine that Karel is on the corner of the first street and the first avenue. And we have the beeper on the corner of the first street and last avenue. We do not know the world's size and want to write a program to pick the beeper up. Clearly `for` loop would do the job if you knew the size of the world; you would know how many times you have to `move()` to pick the beeper on the last corner.

## Enter `while` loop
The `while` loop repeats a set of instructions, while some conditions are true for Karel. `while` loop consists of a header and a body. You can write a specific condition in a header and a set of instructions in the body. Generally, `while` loop looks like this:

```js
while(some_condition()) {
	command1();
	command2();
	....
}
```

The meaning of this code is to repeat commands written in the while loop body until the condition in the header is true. Karel will check the condition; if it's true, it will execute all the instructions in the loop body one by one. Then Karel will recheck the condition, and if it's true, it will perform all the instructions one by one again, and so on. When Karel checks the condition, and it is false, the loop will end.

For example, the following code:
```js
while (frontIsClear()) {
	move();
}
```

will move Karel until it faces the wall. The loop will end when Karel is facing the wall.