You can teach Karel new functions. How fun!
Let's teach Karel how to turn right, so when KArel gets to this point it can use this turn right function to continue it's work.
It's important to understand that Karel can not do inherently new things. Everything you teach Karel should be based on it's previous knowledge.

Clearly, to turn right, Karel can turn left three times. So let's write that.

Okay, to create a new function you must write
function, then function_name, then open parentheses, close parentheses. Open curly braces, close curly braces. 
And inside here you can write any instructions Karel can understand.

Every function consists of 2 parts - function header and function body. This is the function header. And anything inside the parentheses is the function body. Function body determines the implementation or what function does. And function header defines the function name and basically how you can call it.

function_name can be anything you wish, but in this case, I'm are writing turnRight function so let's call it turnRight.

In our case, turnRight will be just three turnLefts. And that's it.

I'm using indentation to make it more visible that these commands are inside the turnRight function body. 
So, these tabs are for humans, and Karel cares nothing about indentation.

You can already use this function, so instead of these 3 turnLefts, you could write turnRight. What Karel does is execute each command one by one. When Karel gets to the turnRight function, it thinks, Okay, I did not know turnRight before, but wait, maybe someone taught me? Ahh, yes, here, so turn right is defined here, and Karel executes what's inside of it. turnLeft turnLeft turnLeft, are executed one by one, and when all the instructions are done, the turnRight function is finished, and code execution continues from here.

That's it. You can teach Karel new functions this way.

Notice that you can define new functions before you use them in the code or even after. Karel will find the definition anyway.

Okay, in fact, turnRight is a very commonly used function, and our Karel knew it all along. So, you do not need this function definition, and this code will run just fine.
