This day is brute force, but there are a few optimizations one can make
to develop it faster:

#. Use vector<vector<int>> for the board, so as to have deep copy for free.
#. Define constants EMPTY and OCCUPIED equal to 'L' and '#' instead of 0, 1, for instance.
#. Using templates to avoid having to declare types for the routines. 
   (However, that can complicate the error messages if you're not used to.)

In addition, using a small template library for printing two-dimensional arrays
can speed up the debugging. Not in my case, since my error was to forget to copy
the board into board2 in the iterate routine.

In terms of speed programming, using shorter variable names can also help (if
it does not sow confusion).

With this, the modification from part 1 to part 2 is simply in the neighbor counting
and is quite easy to handle with the extra loop for p (remember, brute force).
