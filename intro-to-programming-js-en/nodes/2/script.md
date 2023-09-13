Just like how we use words to communicate with each other, you can use specific commands to tell Karel what to do. There are only 4:

move - what it does is moves Karel one step ahead in the direction it is facing.
turnLeft -  what this command does is turns KArel left 90 degrees. Karel stays on the same corner. 
If you command Karel to pickBeeper - it will pick a single beeper form the corner it is standing. Unfortunately Karel can not pick a beeper if it is far away. So beeper has to be on the same corner.
With putBeeper Karel will put a single beeper on the corner it stands.

Each command is a direct instruction and Karel will execute them one by one, if it can. For example, Karel will not be able to move through walls, or pick up beepers if there are none. 