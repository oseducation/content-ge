Let's write our first Karel program. Let's assume the initial world looks like this: Karel is standing on the corner of First Street and First Avenue - or let's say at the coordinates (1,1). A beeper is at the coordinates (2,1), and we also have some walls in the world.

What we want to do is write a program so that Karel picks up the beeper and drops it at the coordinates (4,2), then finishes work at coordinates (5,2).

Basically, we want a program that changes this initial world to this.

Let's go ahead and write it here. 
What are the commands we have to tell Karel to accomplish all this? 
Clearly, the first command would be `move`, and Karel will get to the (2,1) corner. 
Then `pickBeeper`, `move` - now Karel is at coordinates (3,1) and it can't move forward. 
We'd like Karel to jump over the wall but Karel knows nothing about jumping. What Karel knows is how to `turnLeft`. After turning left, Karel is facing north. 
So Let's have it `move`. Now Karel is at coordinates (3,2), facing north. 
Ideally, we would have it turn right, but Karel does not have that command. So what we could do instead is instruct Karel to `turnLeft` three times. 

Now Karel is facing east. Let's have it `move`, `putBeeper`, and `move` again, so Karel gets to coordinates (5,2). That's it!

But wait, what we have here is not a program. It's an algorithm, a set of instructions that is understandable for a human, but not for a computer, or for Karel.

To create a program, we must transform these commands into functions. And functions are something computers can understand. It's really easy; we just have to put open parentheses, close parentheses, and a semicolon at the end of each command.

What you have to know is that each symbol here is important, and function names are exactly as written. for example pickBeeper with small p and Capital B

That's it! Now this is a program, and we can run it and see the result!

Karel picks the beeper up, puts it on the correct corner and finishes work, cool!