# Intro to Limit Laws
The following theorems make it easy to calculate limits and one-sided limits of many kinds of functions when we know some elementary limits.


## Relationship between one-sided and two-sided limits
A function $$f(x)$$ has limit $$L$$ at $$x = a$$ if and only if it has both left and right limits there and these one-sided limits are both equal to $$L$$:

$$\\lim_{x \\to a} f(x) = L  \\impliedby \\lim_{x \\to a-} f(x) = \\lim_{x \\to a+} f(x) = L$$


## Limit Rules
If $$\\lim_{x \\to a} f(x) = L$$, $$\\lim_{x \\to a} g(x) = M$$, and $$k$$ is a constant, then
1. **Limit of a sum**: $$\\lim_{x \\to a} [f(x) + g(x)] = L + M$$
2. **Limit of a difference**: $$\\lim_{x \\to a} [f(x) - g(x)] = L - M$$
3. **Limit of a product**: $$\\lim_{x \\to a} f(x)g(x) = LM$$
4. **Limit of a multiple**: $$\\lim_{x \\to a} kf(x) = kL$$
5. **Limit of a quotient**: $$\\lim_{x \\to a} \\frac f(x) g(x) = \\frac L M$$, if $$M \\ne 0$$. 

If $$m$$ is an integer and $$n$$ is a positive integer, then
6. **Limit of a power**: $$\\lim_{x \\to a} [f(x)] ^ \\frac m n = L ^ \\frac m n$$, provided $$L > 0$$ if $$n$$ is even, and $$L \\ne 0$$ if $$m < 0$$.

If $$f(x) \\le g(x)$$ on an interval containing $$a$$ in its interior, then
7. **Order is preserved**: $$L \\le M$$


## Limits of Polynomials and Rational Functions
1. If $$P(x)$$ is a polynomial and $$a$$ is any real number, then 

    $$\\lim_{x \\to a} P(x) = P(a)$$

2. If $$P(x)$$ and $$Q(x)$$ are polynomials and $$Q(a) \\ne 0$$, then

    $$\\lim_{x \\to a} {\\frac {P(x)} {Q(x)}} = \\frac {P(a)} {Q(a)}$$


Notice that we are not proving the theorems because we need the formal definition of the limit for the proof.