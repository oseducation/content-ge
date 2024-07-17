Hey there! Let's dive into understanding functions, specifically exponential functions. I'll walk you through an example step by step.

Consider the function $$h(n) = \frac{1}{4} \cdot 2^n$$. Here, you might notice something interesting: the variable \(n\), which is the input of our function, appears in the exponent. This type of function is called an exponential function.

We can make another exponential function such as $$f(t) = 5 \cdot 3^t$$. Once again, the variable \(t\) is in the exponent.

Now, let's talk about some key terms in exponential functions. One of them is the "initial value." The initial value is simply the value of the function when the input is zero. For our function $$h(n)$$, we find the initial value by calculating $$h(0)$$:

$$
h(0) = \frac{1}{4} \cdot 2^0
$$

Since $$2^0$$ is 1, we get:

$$
h(0) = \frac{1}{4}
$$

So, the initial value for $$h(n)$$ is \(\frac{1}{4}\).

Let's do the same for $$f(t)$$:

$$
f(0) = 5 \cdot 3^0
$$

Since $$3^0$$ is also 1, we get:

$$
f(0) = 5
$$

So, the initial value for $$f(t)$$ is 5. Notice how the initial value is the number outside the exponent in both cases.

Next, let's introduce the term "common ratio." This is the number that the function's value is multiplied by as the input increases by 1. To see this, let's look at $$h(n)$$ again:

1. $$h(0) = \frac{1}{4}$$
2. $$h(1) = \frac{1}{4} \cdot 2$$
3. $$h(2) = \frac{1}{4} \cdot 2^2 = \frac{1}{4} \cdot 4 = \frac{1}{4} \cdot 2 \cdot 2$$
   
Notice how $$h(2) = 2 \cdot h(1)$$ and $$h(1) = 2 \cdot h(0)$$. So, the ratio between consecutive values is 2, which we call the common ratio. Mathematically, we can see:

$$
\frac{h(n+1)}{h(n)} = \frac{\frac{1}{4} \cdot 2^{n+1}}{\frac{1}{4} \cdot 2^n} = 2
$$

For $$f(t)$$, the common ratio is 3. You can verify this by calculating the ratios of consecutive values like we did with $$h(n)$$.

To create our own exponential function, suppose we know the initial value is 5 and the common ratio is 6. The function could look like:

$$
g(x) = 5 \cdot 6^x
$$

Here, 5 is the initial value and 6 is the common ratio.

I hope this helps you understand the parts of an exponential function and why we use these terms. If you have any questions, feel free to ask!