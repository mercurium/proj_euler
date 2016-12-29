#NOTE TODO need to solve it



"""
P(n) has n elements
Q(n) has 2^n -1 elements
R(n) has 2^(2^n-1) -1 elements

P(2) = {1,2}
Q(2) = {{1}, {2}, {1,2}}

C(1,1) = 1

C(2,1) = 6 = 2 + 4
C(2,2) = 1

C(3,1) = 3 + 3 x 4 +
C(3,2) =
C(3,3) = 1

C(3,2) = 127 - ( 3 x C(2,1) x C(1,1) + C(1,1)^2) - 1 = 127 - 18 - 1 -1 = 107

P(3) = {1,2,3}
Q(3) = {{{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
|R(3)| = 127 elements


Problem Statement:
  let P(n) be the set of the first n positive integers {1,2,...,n}
  Let Q(n) be the set of all the non-empty subsets of P(n)
  Let R(n) be the set of all the non-empty subsets of Q(n)

  An element X \in R(n) is a non-empty subset of Q(n), so it is itself a set
  From X, we can construct a graph as follows:
    - Each element y \in X corresponds to a vertex and is labeled with Y_i
    - Two vertices Y_1 and Y_2 are connected if Y_1 \intersect Y_2 \neq \nil

  For example, X = {{1}, {1,2,3}, {3}, {5,6}, {6,7}} results in the following graph:
    (graph with edges between:
      {1} and {1,2,3}
      {3} and {1,2,3}
      {5,6} and {6,7}
      )
  This graph has two \bold{connected components}

  Let C(n,k) be the number of elements of R(n) that have exactly k connected components in their graph.
  You are given:
    C(2,1) = 6
    C(3,1) = 111
    C(4,2) = 486
    C(100,10) mod (10^9+7) = 728209718

  Find C(10^4, 10) mod (10^9+7)



"""
