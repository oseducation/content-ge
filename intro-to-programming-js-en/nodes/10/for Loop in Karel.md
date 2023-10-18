# `for` Loop in Karel

In some cases we need to repeat some Karel commands several times, We could copy and paste the commands, but it's way better to use the `for` loop.

Generally copy and pasting the code is not a good idea, we end up with the same code in different places. Which makes code changes tricky and error prone.

Let's assume Karel is on the corner of the first street and first avenue - or coordinates (1,1). We want to pick a beeper that is on coordinates(100,1). Pretty straightforward right? We have to write a program with 99 `move();`s and a single `pickBeeper();` at the end. But copying `move();` that many times is quite time-taking and in the process we might miscount add an extra `move();` or miss one. The good news is we can use `for` loop and do it easily.

```js
for (let i = 0; i < some_number; i++) {
    Commands that we want to repeat
}
```

`for` loop consists of 2 parts the header and the body. The header defines number of iterations - or how many times you want to repeat something. And the body defines what you want to repeat - a set of instructions that will be repeated several times. Let's do not dwell on the exact meaning of the `for (let i = 0; i < some_number; i++)` the only thing interesting here is the `some_number` where you can write the actual number - how many times you want to repeat the instructions. And inside the `for` loop or in the body you can write the actual set of instructions.

So the program to solve our stated problem goes as follows:

```js
for (let i = 0; i < 99; i++) {
    move();
}
pickBeeper();
```
If you notices we used tab inside the `for` loop to make clearer for the code reader that `move();` part of the `for` loop's body.

## Several instructions in `for`
Of course we can put several instructions inside the `for` loop. In this case `for` loop executes these set of instructions one by one on each iterations. And the number of iterations is determined in the header of the loop. You can imagine that `for` loop just copies whatever it has inside and pastes it several times. So the code:

```js
for (let i = 0; i < 4; i++) {
    move();
    turnLeft();
}
```

is exactly the same as the code:

```js
move();
turnLeft();
move();
turnLeft();
move();
turnLeft();
move();
turnLeft();
```


