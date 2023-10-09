When writing new functions we can only use functions Karel already knows, so we can not create inherently new behavior. So, the question is Why teach Karel new functions at all? Let's dive in

In fact, we can write any code without ever using any new functions but it's not quite wise.

Imagine Karel does not know turnRight and we have to write 3 turnLefts every time we want to turn right. We will be repeating same code a lot. With new functions we reduce code repetition a lot and this is very important for several reasons:

Firstly it saves our time, less code to write.

Secondly it makes code easier to read and understand, when seeing new functions's name we will understand what function does without even looking into the implementation details.

Thirdly probability of the bugs reduces. If we want to change some functions' behavior we do this in the single place. Without functions we have to change same thing in different places and we might create bugs if we forget to change everywhere. 

So, you can view new functions as your little helpers, they make programming with Karel smooth, easy, and fun.