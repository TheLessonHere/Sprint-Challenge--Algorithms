#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). A single while loop performing one operational check.


b) O(n^2). It's a while loop nested in a for loop, meaning it will loop for each
individual loop in the range given.


c) O(n). It's performing a linear recursive function.

## Exercise II

You would want to do a quick sort type of function to check different floors of the
building. To start, you would begin on floor n//2 (ie f = n//2). If the egg breaks,
we would then take all the floors beneath f and cut that in half. So for example if
f is 10, the next floo we would check is 10//2 or 5. If the egg doesn't break on f=5
we would then go to the middle of floors 6-9 etc. until we find the lowest floor at
which the egg doesn't break.

As far as runtime complexity, the algorithm could be implemented recursively and
would utilize a simple quicksort method which has a runtime complexity of at O(n log(n)).