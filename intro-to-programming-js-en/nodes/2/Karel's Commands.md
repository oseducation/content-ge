# Karel's Commands

Let's see how we can guide Karel through its world. Just like how we use words to communicate with each other, we use specific commands, to tell Karel what to do.

## The Basic Commands

* **move**: When you want Karel to go forward to the next spot on the grid. Karel goes in the direction it is facing.
* **turnLeft**: Directs Karel to take a sharp 90-degree turn to the left. Karel stays in the same corner.
* **pickBeeper**: Karel picks up a beeper from its current location. Karel can not pick beepers from far away, so the beeper has to be in the same location(corner) as Karel.
* **putBeeper**: Karel puts down a beeper in the corner where it stands. You may assume that Karel has the infinite number of beepers and it always can produce one.

## Understanding Commands
Each command is a direct instruction and Karel will execute them one by one, if it can. For example, Karel will not be able to move through walls or pick up beepers if there are none.


