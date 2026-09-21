# CMPS 2200 Recitation 02

## Answers

**Name:** Shiqian Zhang

Place all written answers from `recitation-02.md` here for easier grading.

## 4) Work Recurrences

We consider the recurrence

```math
W(n) = 2W(n/2) + f(n)
```

with base case

```math
W(1) = 1.
```

### (a) \(f(n) = 1\)

The recurrence is

```math
W(n) = 2W(n/2) + 1.
```

At level \(i\) of the recursion tree, there are

```math
2^i
```

nodes.

Each node does constant work, so the total work at level \(i\) is

```math
2^i.
```

The recursion tree has

```math
\log_2 n
```

levels.

Therefore, the total work is

```math
1 + 2 + 4 + \cdots + n.
```

This is a geometric series, so

```math
W(n) = \Theta(n).
```

For powers of two, some actual values are:

| \(n\) | \(W(n)\) |
|---|---:|
| 2 | 3 |
| 4 | 7 |
| 8 | 15 |
| 16 | 31 |

These values grow approximately linearly with \(n\), which agrees with the asymptotic bound

```math
\Theta(n).
```

### (b) \(f(n) = n\)

Now the recurrence is

```math
W(n) = 2W(n/2) + n.
```

At level \(i\), there are

```math
2^i
```

nodes.

Each node has input size

```math
\frac{n}{2^i}.
```

Therefore, the total cost of level \(i\) is

```math
2^i \left(\frac{n}{2^i}\right) = n.
```

Every level has total cost \(n\), and there are

```math
\log_2 n
```

levels.

Therefore,

```math
W(n) = \Theta(n \log n).
```

Some actual values are:

| \(n\) | \(W(n)\) |
|---|---:|
| 2 | 4 |
| 4 | 12 |
| 8 | 32 |
| 16 | 80 |

These values grow faster than linearly and are consistent with

```math
\Theta(n \log n).
```

### (c) \(f(n) = n^2\)

The recurrence is

```math
W(n) = 2W(n/2) + n^2.
```

At level \(i\), there are

```math
2^i
```

nodes.

Each node has input size

```math
\frac{n}{2^i}.
```

Thus, the total work at level \(i\) is

```math
2^i \left(\frac{n}{2^i}\right)^2.
```

Simplifying,

```math
2^i \cdot \frac{n^2}{2^{2i}}
=
\frac{n^2}{2^i}.
```

Therefore,

```math
W(n)
=
n^2
+
\frac{n^2}{2}
+
\frac{n^2}{4}
+
\cdots.
```

This is a decreasing geometric series, so

```math
W(n) = \Theta(n^2).
```

Some actual values are:

| \(n\) | \(W(n)\) |
|---|---:|
| 2 | 6 |
| 4 | 28 |
| 8 | 120 |
| 16 | 496 |

These values grow quadratically, which agrees with

```math
\Theta(n^2).
```

## 5) Master Method

Consider the general recurrence

```math
T(n) = aT(n/b) + n^c.
```

At level \(i\) of the recursion tree, there are

```math
a^i
```

subproblems.

The size of each subproblem is

```math
\frac{n}{b^i}.
```

The work done by each node at level \(i\) is

```math
\left(\frac{n}{b^i}\right)^c.
```

Therefore, the total work at level \(i\) is

```math
a^i \left(\frac{n}{b^i}\right)^c.
```

This simplifies to

```math
a^i \frac{n^c}{b^{ic}}
=
n^c \left(\frac{a}{b^c}\right)^i.
```

The height of the recursion tree is

```math
\log_b n.
```

Therefore, the behavior of the recurrence depends on the ratio

```math
\frac{a}{b^c}.
```

### Case 1: \(\log_b a < c\)

The condition

```math
\log_b a < c
```

is equivalent to

```math
a < b^c.
```

Therefore,

```math
\frac{a}{b^c} < 1.
```

The cost decreases geometrically as we move down the recursion tree.

The costs of the first few levels are

```math
n^c,
```

```math
n^c \left(\frac{a}{b^c}\right),
```

```math
n^c \left(\frac{a}{b^c}\right)^2,
```

and so on.

Since the ratio is less than 1, the root dominates the sum.

Therefore,

```math
T(n) = \Theta(n^c).
```

### Case 2: \(\log_b a = c\)

In this case,

```math
a = b^c.
```

Therefore,

```math
\frac{a}{b^c} = 1.
```

So every level of the recursion tree has total cost

```math
n^c.
```

The tree has

```math
\log_b n
```

levels.

Therefore,

```math
T(n) = n^c \log_b n.
```

Since the base of the logarithm only changes the result by a constant factor,

```math
T(n) = \Theta(n^c \log n).
```

### Case 3: \(\log_b a > c\)

Now,

```math
\log_b a > c,
```

which is equivalent to

```math
a > b^c.
```

Therefore,

```math
\frac{a}{b^c} > 1.
```

The cost increases geometrically as we move down the recursion tree, so the leaves dominate the total cost.

The number of leaves is

```math
a^{\log_b n}.
```

Using the identity

```math
a^{\log_b n}
=
n^{\log_b a},
```

the leaf cost is

```math
\Theta\left(n^{\log_b a}\right).
```

Therefore,

```math
T(n)
=
\Theta\left(n^{\log_b a}\right).
```

Thus, the three cases of the Master Method are

```math
T(n) = \Theta(n^c)
\quad \text{if } \log_b a < c,
```

```math
T(n) = \Theta(n^c \log n)
\quad \text{if } \log_b a = c,
```

and

```math
T(n)
=
\Theta\left(n^{\log_b a}\right)
\quad \text{if } \log_b a > c.
```

## 7) Span Recurrences

For span, the recursive subproblems can run in parallel.

Therefore, instead of adding the work of all recursive branches, we only follow one recursive path.

For the recurrences in Problem 4, where \(a = 2\) and \(b = 2\), the span recurrence is

```math
S(n) = S(n/2) + f(n).
```

### (a) \(f(n) = 1\)

We have

```math
S(n) = S(n/2) + 1.
```

There are

```math
\log_2 n
```

levels in the recursion tree.

Each level contributes constant span.

Therefore,

```math
S(n) = \Theta(\log n).
```

### (b) \(f(n) = n\)

We have

```math
S(n) = S(n/2) + n.
```

Expanding the recurrence gives

```math
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
```

This is a geometric series.

Therefore,

```math
S(n) = \Theta(n).
```

### (c) \(f(n) = n^2\)

We have

```math
S(n) = S(n/2) + n^2.
```

Expanding the recurrence gives

```math
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
```

This is also a geometric series.

Therefore,

```math
S(n) = \Theta(n^2).
```

So the final span bounds are:

- If \(f(n) = 1\), then

```math
S(n) = \Theta(\log n).
```

- If \(f(n) = n\), then

```math
S(n) = \Theta(n).
```

- If \(f(n) = n^2\), then

```math
S(n) = \Theta(n^2).
```

These results make sense because span follows only one recursive branch, while work includes all recursive branches.