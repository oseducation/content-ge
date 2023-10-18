# Incorrect `while` Loop in Karel
Sometimes, people use the `while` loop incorrectly. It is essential to understand that Karel performs all the instructions in the `while` loop's body if the checked condition is true. In the process of the body execution, the condition may be false at some point, but it is not checked. The condition is checked only at the beginning of the iteration and never during the iteration.

For example, let's consider the code:

```js
while (frontIsClear()) {
    move();
    move();
}
```


One may assume that the loop will end whenever there is a wall up against Karel, but it's not true.

If Karel is on the (1,1) coordinates and there are four avenues in the world. What will happen is:
1. Karel will check if the front is clear; 
2. it is, so Karel will perform instructions in the while loop body, which is `move()` 
3. and another `move()`. Karel will be on the (3,1) coordinates, and the first iteration of the `while` loop will be finished. 
4. Next, Karel will again check if the front is clear; 
5. and it is clear, so Karel will perform `move()`, Karel will get to (4,1) coordinates, 
6. and another `move()`, but Karel is already in front of the wall, so the second move will fail. 

And that's a bug in our program.