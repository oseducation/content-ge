# MoveKarel

## Problem
```
Karel is on the 1x1 corner, facing east. On the 3x1 corner there is a beeper. 
Karel should take the beeper and put it on the 4x1 corner. 
```

## Solution
Let's start with the algorithm:
1. Karel starts at the 1x1 corner, facing east.
2. Karel needs to move to the 3x1 corner to pick up the beeper.
3. After picking up the beeper, Karel should then move to the 4x1 corner.
4. Karel will then place the beeper at this spot.

We will get following code:
```js
move()
move()
pickBeeper()
move()
putBeeper()
```