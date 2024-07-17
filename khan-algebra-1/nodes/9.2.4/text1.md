Sure! Let's go through this step by step.

---

Hey there! Let's look at this together. We have a function, let's call it $$h(n)$$, and it tells us the terms of a sequence. I'll make a quick table to show what's happening.

When $$n = 1$$:

$$h(1) = -31 - 7(1 - 1) = -31 - 0 = -31$$

When $$n = 2$$:

$$h(2) = -31 - 7(2 - 1) = -31 - 7(1) = -31 - 7 = -38$$

When $$n = 3$$:

$$h(3) = -31 - 7(3 - 1) = -31 - 7(2) = -31 - 14 = -45$$

What do we notice? We start at $$-31$$ and keep subtracting $$7$$ each time. Actually, we subtract $$7$$ one less time than the term number we're looking at. For the third term, we subtract twice; for the second term, once.

Now, I want you to pause and see if you can write this sequence using a recursive function. A recursive function defines each term based on the previous one.

Let's call this function $$g(n)$$. It's pretty simple:

- For the first term ($$n = 1$$): $$g(1) = -31$$
- For $$n > 1$$: $$g(n) = g(n-1) - 7$$

This means to get any term, we look at the previous term and subtract $$7$$.

How about we try another example but start with a recursive definition and turn it into an explicit one?

Let's say we have a sequence where the first term is $$9.6$$, and each term is the previous one minus $$0.1$$.

So, if $$n = 1$$, the term is $$9.6$$. If $$n = 2$$, it'll be $$9.5$$ (which is $$9.6 - 0.1$$), and for $$n = 3$$, it'll be $$9.4$$ (which is $$9.5 - 0.1$$).

Let's put this into a table:

- When $$n = 1$$, $$h(1) = 9.6$$
- When $$n = 2$$, $$h(2) = h(1) - 0.1 = 9.6 - 0.1 = 9.5$$
- When $$n = 3$$, $$h(3) = h(2) - 0.1 = 9.5 - 0.1 = 9.4$$

Now, let's define this sequence explicitly. We'll call it $$f(n)$$. 

- Start at $$9.6$$ and subtract $$0.1$$ a certain number of times based on the term number. For the first term, subtract zero times, for the second term, subtract once, and so on.

So, our explicit function will be: 

$$f(n) = 9.6 - 0.1(n - 1)$$

You can check this works:

- For $$n = 1$$: $$f(1) = 9.6 - 0.1(1 - 1) = 9.6$$
- For $$n = 2$$: $$f(2) = 9.6 - 0.1(2 - 1) = 9.5$$
- For $$n = 3$$: $$f(3) = 9.6 - 0.1(3 - 1) = 9.4$$

So, you’re starting at $$9.6$$ and subtracting $$0.1$$ one fewer times than the term number.

Great job following along! Try similar problems to get more practice.