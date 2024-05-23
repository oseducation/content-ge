## What is a formula?

We are used to describing arithmetic sequences like this: 3,5,7
 
But there are other ways. In this lesson, we'll be learning two new ways to represent arithmetic sequences: recursive formulas and explicit formulas. Formulas give us instructions on how to find any term of a sequence.

To remain general, formulas use `n` to represent any term number and `a(n)` to represent the n-th term of the sequence. For example, here are the first few terms of the arithmetic sequence 3, 5, 7, ...


`n` (term number) - 1, 2, 3

`a(n)` (n-th term) - 3, 5, 7

We mentioned above that formulas give us instructions on how to find any term of a sequence. Now we can rephrase this as follows: formulas tell us how to find `a(n)` for any possible `n`.


### Recursive formulas of arithmetic sequences
Recursive formulas give us two pieces of information:
1. The first term of a sequence
2. The pattern rule to get any term in a sequence from the term that comes before it
   
Here is the recursive formula of our sequence 3, 5, 7, ... along with the interpretation for each part.
* `a(1) = 3` - the first term is three
* `a(n) = a(n-1) + 2` - add two to the previous term
  
In order to find the fifth term, for example, we need to extend the sequence term by term:
1. `a(1) = 3`
2. `a(2) = a(1) + 2 = 3 + 2 = 5`
3. `a(3) = a(2) + 2 = 5 + 2 = 7`
4. `a(4) = a(3) + 2 = 7 + 2 = 9`
5. `a(5) = a(4) + 2 = 9 + 2 = 11`

Cool! This formula gives us the same sequence as described by 3, 5, 7, ...

### Explicit formulas of arithmetic sequences
Here is an explicit formula of 3, 5, 7, ...

`a(n) = 3 + 2(n-1)`

This formula allows us to simply plug in the number of the term we are interested in to get the value of that term.

In order to find the fifth term, for example, we need to plug `n=5` into the explicit formula.

`a(5) = 3 + 2(5-1) = 3 + 2*4 = 3 + 8 = 11`

Lo and behold, we get the same result as before!

### Sequences are functions
Notice that the formulas we used in this lesson work like functions: We input a term number `n`, and the formula outputs the value of that term `a(n)`.
Sequences are in fact defined as functions. However, `n` cannot be any real number value. There's no such thing as the negative fifth term or the 0.4th term of a sequence.
This means that the domain of sequences—which is the set of all possible inputs of the function—is the positive integers.




