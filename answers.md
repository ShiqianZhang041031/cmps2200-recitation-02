# CMPS 2200 Recitation 02

## Answers

**Name:** Shiqian Zhang

Place all written answers from `recitation-02.md` here for easier grading.


## 4) Work Recurrences

Here we have

$$
W(n)=2W(n/2)+f(n)
$$

with $W(1)=1$.

### (a) $f(n)=1$

The recurrence is

$$
W(n)=2W(n/2)+1.
$$

At level $i$ of the recursion tree, there are $2^i$ nodes, and each
node does constant work. Therefore, the cost of level $i$ is

$$
2^i.
$$

There are $\log_2 n$ levels, so the total work is

$$
1+2+4+\cdots+n.
$$

This is a geometric series, so

$$
W(n)=\Theta(n).
$$

For powers of two, some actual values are:

| $n$ | $W(n)$ |
|---|---:|
| 2 | 3 |
| 4 | 7 |
| 8 | 15 |
| 16 | 31 |

These values grow approximately linearly with $n$, which agrees with
the asymptotic bound $\Theta(n)$.


### (b) $f(n)=n$

Now the recurrence is

$$
W(n)=2W(n/2)+n.
$$

At level $i$, there are $2^i$ nodes. Each node has input size

$$
\frac{n}{2^i}.
$$

Therefore, the total cost at level $i$ is

$$
2^i\left(\frac{n}{2^i}\right)=n.
$$

There are $\log_2 n$ levels, so

$$
W(n)=\Theta(n\log n).
$$

Some actual values are:

| $n$ | $W(n)$ |
|---|---:|
| 2 | 4 |
| 4 | 12 |
| 8 | 32 |
| 16 | 80 |

The growth is faster than linear and matches the expected
$\Theta(n\log n)$ behavior.


### (c) $f(n)=n^2$

The recurrence is

$$
W(n)=2W(n/2)+n^2.
$$

At level $i$, the total cost is

$$
2^i\left(\frac{n}{2^i}\right)^2
=
\frac{n^2}{2^i}.
$$

Therefore,

$$
W(n)
=
n^2+\frac{n^2}{2}+\frac{n^2}{4}+\cdots.
$$

This is a decreasing geometric series, so

$$
W(n)=\Theta(n^2).
$$

Some actual values are:

| $n$ | $W(n)$ |
|---|---:|
| 2 | 6 |
| 4 | 28 |
| 8 | 120 |
| 16 | 496 |

These values grow quadratically, which agrees with the bound
$\Theta(n^2)$.


## 5) Master Method

Consider the general recurrence

$$
T(n)=aT(n/b)+n^c.
$$

At level $i$ of the recursion tree, there are $a^i$ subproblems.

The size of each subproblem is

$$
\frac{n}{b^i}.
$$

The work done by one node at level $i$ is

$$
\left(\frac{n}{b^i}\right)^c.
$$

Therefore, the total work at level $i$ is

$$
a^i\left(\frac{n}{b^i}\right)^c.
$$

Rearranging gives

$$
n^c\left(\frac{a}{b^c}\right)^i.
$$

The height of the tree is

$$
\log_b n.
$$

Therefore, the total cost is determined by the ratio

$$
\frac{a}{b^c}.
$$


### Case 1: $\log_b a < c$

The condition

$$
\log_b a<c
$$

is equivalent to

$$
a<b^c.
$$

Therefore,

$$
\frac{a}{b^c}<1.
$$

The cost at each level decreases geometrically:

$$
n^c,
\quad
n^c\frac{a}{b^c},
\quad
n^c\left(\frac{a}{b^c}\right)^2,
\quad \ldots
$$

The root level dominates the sum. Therefore,

$$
T(n)=\Theta(n^c).
$$


### Case 2: $\log_b a=c$

In this case,

$$
a=b^c,
$$

so

$$
\frac{a}{b^c}=1.
$$

Therefore, every level of the recursion tree has cost

$$
n^c.
$$

The tree has $\log_b n$ levels, so

$$
T(n)
=
n^c\log_b n.
$$

Thus,

$$
T(n)=\Theta(n^c\log n).
$$


### Case 3: $\log_b a>c$

Now

$$
a>b^c,
$$

so

$$
\frac{a}{b^c}>1.
$$

The cost increases as we move down the recursion tree, so the leaves
dominate the total cost.

The number of leaves is

$$
a^{\log_b n}.
$$

Using

$$
a^{\log_b n}=n^{\log_b a},
$$

the total cost is

$$
T(n)=\Theta\left(n^{\log_b a}\right).
$$


Therefore, the three cases of the Master Method are

$$
T(n)=
\begin{cases}
\Theta(n^c), & \log_b a<c,\\
\Theta(n^c\log n), & \log_b a=c,\\
\Theta(n^{\log_b a}), & \log_b a>c.
\end{cases}
$$


## 7) Span Recurrences

For span, the recursive subproblems can run in parallel. Therefore,
instead of including all $a$ recursive calls, we only follow one path
through the recursion tree.

With $a=2$ and $b=2$, the span recurrence is

$$
S(n)=S(n/2)+f(n).
$$


### (a) $f(n)=1$

We have

$$
S(n)=S(n/2)+1.
$$

There are $\log_2 n$ levels in the recursion tree, and each level has
constant span. Therefore,

$$
S(n)=\Theta(\log n).
$$


### (b) $f(n)=n$

We have

$$
S(n)=S(n/2)+n.
$$

Expanding the recurrence gives

$$
S(n)
=
n+\frac{n}{2}+\frac{n}{4}+\cdots.
$$

This is a geometric series, so

$$
S(n)=\Theta(n).
$$


### (c) $f(n)=n^2$

We have

$$
S(n)=S(n/2)+n^2.
$$

Expanding gives

$$
S(n)
=
n^2+\frac{n^2}{4}+\frac{n^2}{16}+\cdots.
$$

Again this is a geometric series, so

$$
S(n)=\Theta(n^2).
$$

Thus the span bounds are

$$
\boxed{
\begin{aligned}
f(n)=1 &: \Theta(\log n),\\
f(n)=n &: \Theta(n),\\
f(n)=n^2 &: \Theta(n^2).
\end{aligned}
}
$$

These match what we would expect, since span follows only one
recursive branch instead of adding the work from all branches.