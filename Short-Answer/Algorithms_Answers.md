#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(n), The loop runs n number of times.

b)
    O(n log (n), The outer loop runs n number of times and the inner loop runs (i+1) number of times. 

c)
    O(n), Once the function is called it will recursively for n number of times until reaching zero and exiting with a return of 0.

## Exercise II

1. Divide the maximum number of floor by two, this should be the middle floor. Go to this floor and drop an egg. If it breaks then take the middle floor and divide it by two, this become the new middle of our binary search. Repeat this process until the egg lands without breaking. Once found, check n+1, the next floor to confirm that you are on the edge of f (the eggs limit). Some people will say this is impractical to do in real life, but if a scientist will go to any bounds for an experiment, why shouldn't a software developer!


2. At best this solution is O(log n), and at worst I have a syntax error and it will take an hour.




