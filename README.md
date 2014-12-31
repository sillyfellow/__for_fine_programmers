pffp: Problems for fine programmers
===================================

In the summers of 2009 and 2010, I offered a course (Python for fine Programmers) at the department of Computer Science, at Technical University Munich.

 2009: http://www14.informatik.tu-muenchen.de/lehre/2009SS/python/

 2010: http://www14.informatik.tu-muenchen.de/lehre/2010SS/pffp/

Over the past few years, I have lost/misplaced the solutions/programs to many of the problems I had given as weekly exercises. I try to quickly go through the list, and write down the solutions here.

1. Write three different functions, each of which gives the fibonacci number
   correspondin to the input number. (iterative, recursive & memoized
   recursive)
   Bonus: Write a 4th and better function (matrix multiplication)

   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/fib.py

2. Write a program to find out the square root of a given number. (Without the
   help of python math library). (think of binary search)
   Bonus: Extend this to nth root.

   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/nth_root.py

3. Write a program, without using the int function of python, to convert a
   string (representing an integer) to the integer.
   Also, do the reverse: Integer to String
   Bonus: Extend this to floating points

   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/atoitoa.py

4. Tower of Hanoi: Write a program to solve the problem of tower of Hanoi. The
   disks could be represented by numbers, and each pole/needle could be a list.
   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/tower_of_hanoi.py

5. Write a program to generate all the permutations of all the characters in a given string,
   or a list of characters
   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/permutation.py

6. Write a program for the following.  There is a List A[n] of n integers. You
   have to create another List Output such that Output[i] will be equal to the
   product of all the elements of A except A[i].  Using a division operator is
   not permitted.
   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/array_product.py

7. Write a set of classes in Python for chess coins. Arrange them so that a
   base class consists of all the basic details (eg. Color of coin and the
   Color of square where it is). And the subclasses could inherit from it - all
   the basic properties and then the subclasses implement the special methods
   for them. (Queen, Bishop, Knight, Rook, King and Pawn)

8. Write a class for Rational numbers. Implement any 3 of the methods which
   would permit one to use the mathematical operators (+, ∗, /, . . . or
   similar ones)

9. Flattening a list.  Write a program, which accepts a list (with sublists,
   and subsublists) as an input and outputs a single list which has the
   members of the sublists/subsublists as elements.  And input of [1, [2, 3],
   [[4, [5], 6], 7], 8] would give an output of [1, 2, 3, 4, 5, 6, 7, 8].
   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/flatten.py

10. Write a class for a node of a binary tree. (Not necessarily a binary search
    tree). Implement the basic methods.

    10.x Write a python program which implements a Binary Search Tree. Implement the methods
    for insertion, deletion, searching and traversal.

    The binary tree class from previous lecture could be used as the base class.

    a. Python - https://github.com/sillyfellow/mishmash/blob/master/Python/simple_tree/tree.py

11. Write a python program to evaluate a mathematical expression (which uses +,
    -, * and /). (Hint: Infix to Postfix and use List as a stack) Bonus:
    Implement the ability to have parenthesis.
   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/evaluate_expression.py

12. Implement any three of the set operations for any collective (list, sets) using lambda
    forms/functions
   a. Python - https://github.com/sillyfellow/pffp/blob/master/python/set_operations_lambda.py
