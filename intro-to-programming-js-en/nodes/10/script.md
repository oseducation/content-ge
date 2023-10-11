In some cases we need to repeat some Karel commands several times, of course  we could copy and paste the commands, but it's way better to use the `for` loop.

Generally copy and pasting the code is not a good idea, you end up with the with same code in different places. And that's the bug factory. But why?
Changing the code is pretty frequent occasion, so at some point you will have to change the code you've copy and pasted. You've changed in one place but now you have to remember all the other places you've pasted the code. If you forget one it becomes buggy, basically program will get messy pretty quickly. So do not copy and paste the code.


Ok, Let's get back to the `for` loop. Let's assume Karel is on the corner of the first street and first avenue - or coordinates (1,1). We want to pick a beeper that is on coordinates(100,1). Pretty straightforward right? We have to write a program with 99 `move();`s and a single `pickBeeper();` at the end. But copying `move();` that many times is quite time-taking and in the process we might miscount add an extra `move();` or miss one. The good news is we can use `for` loop and do it easily.


This is the general use of the `for` loop in Karel
```js
for (let i = 0; i < some_number; i++) {
    Commands that we want to repeat
}
```

This is the header, this is the body
In the header only thing you can change is this number here and you can write the actual number. And it will determine the number of iterations - or how many times you want to repeat something.

In the body you can write any set of instructions and they will be repeated the number of time you specified here.

For now you can ignore the exact meaning of `let i =` the only thing you have to change is the number here.

And of course for the readability we are using tabs to more clearly indicate that these instructions are inside the `for` loop, or in the `for` loop's body.

Ok so if we want to pick a beeper on the 100th street we have to write

```js
for (let i = 0; i < 99; i++) {
    move();
}
pickBeeper();
```

Let's try out this example:
```js
for (let i = 0; i < 4; i++) {
    move();
    turnLeft();
}
```

We can write as many instructions inside `for` loop as we want. Ok so instructions will be repeated 4 times. But this does not mean that `move` will be repeated 4 times and then `turnLeft` will be repeated 4 times. No no no. This means the there will be the 4 iterations of the `for` loop and in each iteration we will do `move` first then `turnLeft`
You can imagine that `for` loop just copies whatever it has inside and pastes it several times.
So this code is the same as this

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

Ok let's run the code. Great! 


