# CMPS 2200 Recitation 02

## Answers

**Name:** Shiqian Zhang

Place all written answers from `recitation-02.md` here for easier grading.

## 4) Work Recurrences

We consider the recurrence

$$
W(n) = 2W(n/2) + f(n)
$$

with base case

$$
W(1) = 1.
$$

### (a) \(f(n) = 1\)

The recurrence is

$$
W(n) = 2W(n/2) + 1.
$$

At level \(i\) of the recursion tree, there are

$$
2^i
$$

nodes.

Each node does constant work, so the total work at level \(i\) is

$$
2^i.
$$

The recursion tree has

$$
\log_2 n
$$

levels.

Therefore, the total work is

$$
1 + 2 + 4 + \cdots + n.
$$

This is a geometric series, so

$$
W(n) = \Theta(n).
$$

For powers of two, some actual values are:

| \(n\) | \(W(n)\) |
|---|---:|
| 2 | 3 |
| 4 | 7 |
| 8 | 15 |
| 16 | 31 |

These values grow approximately linearly with \(n\), which agrees with the asymptotic bound

$$
\Theta(n).
$$

### (b) \(f(n) = n\)

Now the recurrence is

$$
W(n) = 2W(n/2) + n.
$$

At level \(i\), there are

$$
2^i
$$

nodes.

Each node has input size

$$
\frac{n}{2^i}.
$$

Therefore, the total cost of level \(i\) is

$$
2^i \left(\frac{n}{2^i}\right) = n.
$$

Every level has total cost \(n\), and there are

$$
\log_2 n
$$

levels.

Therefore,

$$
W(n) = \Theta(n \log n).
$$

Some actual values are:

| \(n\) | \(W(n)\) |
|---|---:|
| 2 | 4 |
| 4 | 12 |
| 8 | 32 |
| 16 | 80 |

These values grow faster than linearly and are consistent with

$$
\Theta(n \log n).
$$

### (c) \(f(n) = n^2\)

The recurrence is

$$
W(n) = 2W(n/2) + n^2.
$$

At level \(i\), there are

$$
2^i
$$

nodes.

Each node has input size

$$
\frac{n}{2^i}.
$$

Thus, the total work at level \(i\) is

$$
2^i \left(\frac{n}{2^i}\right)^2.
$$

Simplifying,

$$
2^i \cdot \frac{n^2}{2^{2i}}
=
\frac{n^2}{2^i}.
$$

Therefore,

$$
W(n)
=
n^2
+
\frac{n^2}{2}
+
\frac{n^2}{4}
+
\cdots.
$$

This is a decreasing geometric series, so

$$
W(n) = \Theta(n^2).
$$

Some actual values are:

| \(n\) | \(W(n)\) |
|---|---:|
| 2 | 6 |
| 4 | 28 |
| 8 | 120 |
| 16 | 496 |

These values grow quadratically, which agrees with

$$
\Theta(n^2).
$$

## 5) Master Method

Consider the general recurrence

$$
T(n) = aT(n/b) + n^c.
$$

At level \(i\) of the recursion tree, there are

$$
a^i
$$

subproblems.

The size of each subproblem is

$$
\frac{n}{b^i}.
$$

The work done by each node at level \(i\) is

$$
\left(\frac{n}{b^i}\right)^c.
$$

Therefore, the total work at level \(i\) is

$$
a^i
\left(\frac{n}{b^i}\right)^c.
$$

This simplifies to

$$
a^i
\frac{n^c}{b^{ic}}
=
n^c
\left(\frac{a}{b^c}\right)^i.
$$

The height of the recursion tree is

$$
\log_b n.
$$

Therefore, the behavior of the recurrence depends on the ratio

$$
\frac{a}{b^c}.
$$

### Case 1: \(\log_b a < c\)

The condition

$$
\log_b a < c
$$

is equivalent to

$$
a < b^c.
$$

Therefore,

$$
\frac{a}{b^c} < 1.
$$

The cost decreases geometrically as we move down the recursion tree.

The costs of the first few levels are

$$
n^c,
$$

$$
n^c \left(\frac{a}{b^c}\right),
$$

$$
n^c \left(\frac{a}{b^c}\right)^2,
$$

and so on.

Since the ratio is less than 1, the root dominates the sum.

Therefore,

$$
T(n) = \Theta(n^c).
$$

### Case 2: \(\log_b a = c\)

In this case,

$$
a = b^c.
$$

Therefore,

$$
\frac{a}{b^c} = 1.
$$

So every level of the recursion tree has total cost

$$
n^c.
$$

The tree has

$$
\log_b n
$$

levels.

Therefore,

$$
T(n) = n^c \log_b n.
$$

Since the base of the logarithm only changes the result by a constant factor,

$$
T(n) = \Theta(n^c \log n).
$$

### Case 3: \(\log_b a > c\)

Now,

$$
\log_b a > c,
$$

which is equivalent to

$$
a > b^c.
$$

Therefore,

$$
\frac{a}{b^c} > 1.
$$

The cost increases geometrically as we move down the recursion tree, so the leaves dominate the total cost.

The number of leaves is

$$
a^{\log_b n}.
$$

Using the identity

$$
a^{\log_b n}
=
n^{\log_b a},
$$

the leaf cost is

$$
\Theta\left(n^{\log_b a}\right).
$$

Therefore,

$$
T(n)
=
\Theta\left(n^{\log_b a}\right).
$$

Thus, the three cases of the Master Method are

$$
T(n)
=
\Theta(n^c)
\quad
\text{if }
\log_b a < c,
$$

$$
T(n)
=
\Theta(n^c \log n)
\quad
\text{if }
\log_b a = c,
$$

and

$$
T(n)
=
\Theta\left(n^{\log_b a}\right)
\quad
\text{if }
\log_b a > c.
$$

## 7) Span Recurrences

For span, the recursive subproblems can run in parallel.

Therefore, instead of adding the work of all recursive branches, we only follow one recursive path.

For the recurrences in Problem 4, where \(a = 2\) and \(b = 2\), the span recurrence is

$$
S(n) = S(n/2) + f(n).
$$

### (a) \(f(n) = 1\)

We have

$$
S(n) = S(n/2) + 1.
$$

There are

$$
\log_2 n
$$

levels in the recursion tree.

Each level contributes constant span.

Therefore,

$$
S(n) = \Theta(\log n).
$$

### (b) \(f(n) = n\)

We have

$$
S(n) = S(n/2) + n.
$$

Expanding the recurrence gives

$$
S(n)
=
n
+
\frac{n}{2}
+
\frac{n}{4}
+
\frac{n}{8}
+
\cdots.
$$

This is a geometric series.

Therefore,

$$
S(n) = \Theta(n).
$$

### (c) \(f(n) = n^2\)

We have

$$
S(n) = S(n/2) + n^2.
$$

Expanding the recurrence gives

$$
S(n)
=
n^2
+
\frac{n^2}{4}
+
\frac{n^2}{16}
+
\frac{n^2}{64}
+
\cdots.
$$

This is also a geometric series.

Therefore,

$$
S(n) = \Theta(n^2).
$$

So the final span bounds are:

- If \(f(n) = 1\), then

$$
S(n) = \Theta(\log n).
$$

- If \(f(n) = n\), then

$$
S(n) = \Theta(n).
$$

- If \(f(n) = n^2\), then

$$
S(n) = \Theta(n^2).
$$

These results make sense because span follows only one recursive branch, while work includes all recursive branches.