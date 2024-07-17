Hey there! Let’s break down this problem together.

Mohamed is keeping track of the number of leaves on a tree in his backyard every year. The first year, the tree had 500 leaves. Each year after that, the number of leaves grows by 40%. Let's look at what that means and how we can figure out the pattern.

Let’s call $$n$$ the number of years since Mohamed started counting the leaves. Let $$f(n)$$ represent the number of leaves in the $$n$$-th year. So, $$f(n)$$ forms a sequence. What kind of sequence is it?

Each year, the number of leaves grows by 40%, or in other words, it’s multiplied by 1.4. When we consistently multiply by the same number, this makes it a geometric sequence. Let’s make a table to understand this better:

| $$n$$ | $$f(n)$$ |
|------|---------|
| 1    | 500     |
| 2    | 500 * 1.4 = 700 |
| 3    | 700 * 1.4 = 980 |

Notice how each year, the number of leaves isn’t added by a fixed number, like 200 for the first year and 280 for the second. Instead, it’s multiplied by 1.4 each time. That tells us it’s not an arithmetic sequence (where we add or subtract the same amount each time), but a geometric sequence. 

Now, to write the sequence formally:
- For the first year (base case), $$f(1) = 500$$. Here, $$A = 500$$.
- For the subsequent years, each year's number is the previous year's number times 1.4. So, $$B = 1.4$$.

So, our geometric recursive sequence looks like this:
$$f(n) = 500$$ when $$n = 1$$,
and $$f(n) = f(n-1) \cdot 1.4$$ for $$n \gt 1$$.

Now, let’s look at another example involving Seo-Yun’s party:
Seo-Yun starts with 50 party favors and gives away 3 favors to each guest as they arrive. Let $$n$$ be the number of guests that have arrived, and $$g(n)$$ denote the number of party favors she has before the $$n$$-th guest arrives. 

Let's create a table:

| $$n$$ | $$g(n)$$ |
|------|---------|
| 1    | 50      |
| 2    | 50 - 3 = 47 |
| 3    | 47 - 3 = 44 |

Seo-Yun starts with 50 favors. After the first guest, she has 47 (50 - 3). After the second guest, she has 44 (47 - 3), and so on. It’s clear that each time a guest arrives, the number of favors decreases by 3, so this is an arithmetic sequence, where the difference between successive terms is always -3.

To write a general formula:
- Start with 50 favors.
- For each guest, subtract 3 favors times the number of guests before them.

So, $$g(n)$$ is:
$$g(n) = 50 - 3 \cdot (n - 1)$$.

The table helps ensure our pattern is correct:
- Before the first guest: 50 (since $$50 - 3 \cdot 0 = 50$$).
- Before the second guest: 47 (since $$50 - 3 \cdot 1 = 47$$).
- Before the third guest: 44 (since $$50 - 3 \cdot 2 = 44$$).

I hope this makes sense! Let’s keep practicing similar problems to get even better at them!