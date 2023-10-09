Turns out you can teach Karel new functions, how Fun!
Let's teach Karel how to turn right.
It's important to understand that Karel can not do inherently new things. Everything we teach Karel should be based on it's previous knowledge

Clearly to turn right Karel can turn left three times. Let's write that.

Ok, to create new function we must write
function, then function_name, then open parentheses, close parentheses. 

function_name can be anything you wish, but in this case we are writing turnRight function so let's call it turnRight.

Every Function consists of 2 parts - function header and function body. This is function header. and anything inside the parentheses is the function body. Function body determines the implementation or what function does. and function header determines function name and basically how we can call it.

In our case turn right will be just three turnLefts. And that's it.

We are using indentation to be more visible that inside the turnRight function body we have these commands, So they are for us humans Karel cares nothing about indentation.

Now we can already use this function so instead of these 3 turnLefts we could just write turnRight. What Karel does is executes each command one by one. When Karel gets to the turnRight it thinks Ok I did not knew turnRight before, but wait maybe someone taught me? Ahh yes here, so turn right is turnLeft turnLeft turnLeft, Karel executes them one by one and when all the functions are executed called function or turnRight is finished and we continue from here.

That's it we can teach Karel new functions this way.

In fact turnRight is very commonly used function and our Karel knew it all along. So we do not need this function definition, and this code will run just fine.

