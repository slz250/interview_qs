"""
NOTES:
since the question is asking for the res to be sorted
in ascending order, think about preprocessing the input
in sorted order so it's easier to get a sorted res
    -similiarly this concept is reversed for the findPairWithGivenDifferences
    problem b/c the result is required to be in the same order
    as the input was presented in so sorting the input might
    not be the best idea

trying to optimize O(n^4) --> realize that it would take
A LOT of optimization to go down to O(n) or even O(nlogn) and
perhaps O(n^2)

let's first try to get it down to O(n^3), my brain is saying
how the solution btwn O(n^3) and potentially O(n^2) or O(n)
would be drastically different so what's the point
    -let's ignore that thought and just go for the next possible
    improvement

so how can we improve to O(n^3)?
well O(n^4) is looking at each possible combination
so O(n^3) would require reducing possible combinations by
an order of n
well forming combinations of 3 will yield O(n^3) but we're
still missing the 4th element needed to form a quadruplet
what if we formed pairs thus taking O(n^2) then we have
one order of n to spare so the question becomes..
================================
how can we take each pair and form quadruplets in O(n) time
so we have:
1) each pair (x,y) in arr
2) counter_pair can be formed by taking two eles from
the rest of the arr --> get one quadruplet and see if its equal
to desired sum
    -if smaller then we need a bigger counter_pair
    -if bigger then we need a smaller counter_pair
"""