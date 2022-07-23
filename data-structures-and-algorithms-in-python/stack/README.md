# Module Overview 

In this module, we are going to consider the stack data structure 
and its implementation in Python.

## Stack Operations 

### Push 
The operation to insert elements in a stack is called push. When we push 
the book on a stack, we put the book on the previous top element which means
that the new book becomes the top element. This is what we mean when we use 
the push operation, we push elements onto a stack. We insert elements onto a 
stack and the last element to be pushed is the new top of the stack.

### Pop 
There is another operation that we can perform on the stack, popping.
Popping is when we take the top book of the stack and put it down. This 
implies that when we remove an element from the stack, the stack follows the 
First-In, Last Out property. This means that the top element, the last to be 
inserted, is removed when we perform the pop operation.

Push and Pop are two fundamental routines that we’ll need for this
data structure.

### Peek 
Another thing that we can do is view the top element of the stack 
so we can ask the data structure: “What’s the top element?” and it can give 
that to us using the peek operation. Note that the peek operation does not 
remove the top element, it merely returns it.

We can also check whether or not the stack is empty, and a few other things
too, that will come along the way as we implement it.