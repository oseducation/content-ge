# New Functions

We know Karel's functions `move`, `turnLeft`, `pickBeeper` and `putBeeper`. Turns out you can teach Karel new functions, how Fun!

## Turn Right 
You might wonder, "Why doesn't Karel just turn right like it turns left?" Great question! Karel started with a few basic moves, and turning right wasn't one of them. But hey, that's where we come in!

## Crafting the turnRight Function:
* **Think it Through**: Turning right is the same as turning left three times! 
* **Name it**: We can name our new function whatever we want, but for consistency let's call it "turnRight".
* **Teach the Steps**: To turn right, Karel will:
```js
turnLeft()
turnLeft()
turnLeft()
```

Every function consists of 2 parts the header and the body. The header describes the function calls it a name, the body describes what function does - the implementation of a function. The correct syntax of writing a function is following :
```js
function theFunctionName() {
    code...
}
```

## Same Code With New Function
```js
function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}

move();
pickBeeper();
turnLeft();
move();
turnRight();
move();
move();
putBeeper();
move();
```
