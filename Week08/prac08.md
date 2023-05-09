# CP2410 Practical 08
## Sihan Chen, jcu ID: 14187662

## Question 1
Hash function: $(3i+5) \% 11$

| Key | Hash Value |
| --- | ---        |
| 12 | 8 |
| 44 | 5 |
| 13 | 0 |
| 88 | 5 |
| 23 | 8 |
| 94 | 1 |
| 11 | 5 |
| 39 | 1 |
| 20 | 10|
| 16 | 9 |
| 5  | 9 |

and handling collisions with chaining will give us a hash table below: 

<img src="./images/q1.jpg" width="500px" />

<div style="page-break-after: always;"></div>

## Question 2
If the collisions are handled by linear probing, we will have a hash table look like this:

<img src="./images/q2.jpg" width="400px" />

## Question 3
If the collisions are handled by quadratic probing

$A[h(i) + j^2]\ (mod\ N), for\ j = 0, 1, \cdots, N - 1$

we can build a simple python function helps us to check quadratic probing new values

<img src="./images/q3_func.png" width="200px" />

and insert elements up to the point of failure, we will have a hash table look like this:

<img src="./images/q3_1.jpg" width="400px" />

<img src="./images/q3_2.jpg" width="500px" />

<div style="page-break-after: always;"></div>

## Question 4
If the collisions are handled by double hashing

$H(i) = (h(i) + j*h'(i))\ mod\ N, for\ j = 0, 1, \cdots, N - 1$

we can build a simple python function helps us to check quadratic probing new values

<img src="./images/q4_func.png" width="300px" />

the final hash table would look like this:

<img src="./images/q4.jpg" width="500px" />

<div style="page-break-after: always;"></div>

## Question 5

<div style="page-break-after: always;"></div>

## Question 6