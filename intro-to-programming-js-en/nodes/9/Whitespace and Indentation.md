# Whitespace and Indentation

Let's see what's the purpose of the use of whitespace, which includes enters, spaces, and tabs.

Whitespace makes no difference in your code execution. For example Karel does exactly the same in these two programs:

```js
move();
pickBeeper();
jump();
move();

function jump() {
    move();
    turnLeft();
    move();
}
```

```js
        move();
    pickBeeper();
jump();move();

function jump() 
{
move();
turnLeft();
        
        
        move();
    }
```

The only difference is readability. You are free to format and indent your programs anyway you like. The key is to make your code easy to read and understand.

Clearly first code is easier to read, so we will be using similar style, but you can pick a style that suits you, then use it consistently throughout the program.

Sometimes there's a "war" between engineers on different uses of whitespace, just google(or ask ChatGPT whichever is more popular when you are reading this) "tabs vs spaces". In the end of a day it'a matter of preference.