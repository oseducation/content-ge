Sure, let's break this down and talk through it together. It's a bit lengthy, so let's dig into each part slowly and clearly.

---

We've got a function $$g(n)$$, and we need to find $$g(1)$$, $$g(2)$$, $$g(3)$$, and $$g(4)$$. Take a moment to try it yourself first. Alright, ready to go through it together?

For $$g(1)$$:
- If $$n = 1$$, we directly use the given rule: $$g(1) = 4$$.

For $$g(2)$$:
- If $$n = 2$$, since it’s a whole number greater than 1, we use $$g(n) = g(n-1) + 3.2$$.
- So, $$g(2) = g(1) + 3.2 = 4 + 3.2 = 7.2$$.

For $$g(3)$$:
- If $$n = 3$$, again we apply: $$g(n) = g(n-1) + 3.2$$.
- So, $$g(3) = g(2) + 3.2 = 7.2 + 3.2 = 10.4$$.

For $$g(4)$$:
- We use the same rule: $$g(n) = g(n-1) + 3.2$$.
- So, $$g(4) = g(3) + 3.2 = 10.4 + 3.2 = 13.6$$.

So, the values are:
- $$g(1) = 4$$
- $$g(2) = 7.2$$
- $$g(3) = 10.4$$
- $$g(4) = 13.6$$

This forms a sequence where we start with 4 and add 3.2 each time. It's called a recursive function because each value depends on the one before it.

---

Now, let's look at another function, $$h(n)$$, and find $$h(1)$$, $$h(2)$$, $$h(3)$$, and $$h(4)$$.

For $$h(1)$$:
- If $$n = 1$$, the rule is: $$h(1) = 14$$.

For $$h(2)$$:
- When $$n = 2$$, use: $$h(n) = \frac{28}{h(n-1)}$$.
- So, $$h(2) = \frac{28}{h(1)} = \frac{28}{14} = 2$$.

For $$h(3)$$:
- Again the rule for $$n > 1$$ applies: $$h(n) = \frac{28}{h(n-1)}$$.
- So, $$h(3) = \frac{28}{h(2)} = \frac{28}{2} = 14$$.

For $$h(4)$$:
- Apply the same rule: $$h(n) = \frac{28}{h(n-1)}$$.
- So, $$h(4) = \frac{28}{h(3)} = \frac{28}{14} = 2$$.

Thus, the values are:
- $$h(1) = 14$$
- $$h(2) = 2$$
- $$h(3) = 14$$
- $$h(4) = 2$$

This sequence alternates between 14 and 2, showing an interesting pattern.

---

Finally, let's consider the function $$f(n)$$ and find $$f(4)$$.

For $$f(4)$$, we have:
- The rule for $$n > 2$$ is: $$f(n) = f(n-2) + f(n-1)$$.
- So, $$f(4) = f(2) + f(3)$$.

We need $$f(2)$$ and $$f(3)$$:
- For $$f(2)$$: given directly as $$-4$$.
- For $$f(3)$$: use the same rule: $$f(n) = f(n-2) + f(n-1)$$.
- So, $$f(3) = f(1) + f(2) = -6 + (-4) = -10$$.

Now back to $$f(4)$$:
- $$f(4) = f(2) + f(3) = -4 + (-10) = -14$$.

So, the values are:
- $$f(1) = -6$$
- $$f(2) = -4$$
- $$f(3) = -10$$
- $$f(4) = -14$$

This sequence is also recursive because each term depends on the previous ones.

---

Great job working through these! Recursive functions are a powerful way to create sequences and understand patterns. Keep practicing, and you'll get even better at seeing these connections!