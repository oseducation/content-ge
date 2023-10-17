# Conditions in Karel

Karel can learn some conditions about the world it lives in. For example, it can test whether or not there's a wall in front of it. Or whether or not there is a beeper where it stands. Here is the list of all conditions Karel can understand:

* **frontIsClear** - tests if there is no wall next to Karel in the direction it is facing.
* **frontIsBlocked** - tests if there is a wall next to Karel in the direction it is facing. Note: If the front is blocked, the command `move()` would end up with Karel colliding with the wall; hence it would be a bug. 
* **rightIsClear** - tests if there is no wall right to Karel
* **rightIsBlocked** - tests if there is a wall right to Karel
* **leftIsClear** - tests if there is no wall left to Karel
* **leftIsBlocked** - tests if there is a wall left to Karel
* **beepersPresent** - test if there is a beeper on the corner Karel stands. Note that Karel can not determine if there is a beeper somewhere else, only on the corner where it stands.


Condition names should be used with uppercase and lowercase characters exactly as written. 

That's all. Next, let's find out exactly how Karel can use these conditions.