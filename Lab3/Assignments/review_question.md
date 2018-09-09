# Why should we use functions at all?
- Using functions allows you to keep your logic contained in one central place (the function), so you are also less likely to introduce bugs, and if you need to fix a bug, there is only one place where the logic resides

# How to define/declare a function?
- the `def` keyword;
- is followed by the function’s name, then
- the `arguments` of the function are given between parentheses followed by a colon.
- the function body;
- and `return` object for optionally returning values.

# How to call/use a function?
- Using the function's name, follow by arguments
- ```print("abc"), my_function(my_arguments)```

# What is return, why and how do we use it?
- The `return` statement causes your function to exit and hand back a value to its caller. The point of functions in general is to take in inputs and return something. The `return` statement is used when a function is ready to return a value to its caller.

# Do we have to use return in every function?
- Yes and No.  In Python, all functions return a value, but often we write functions that only ever return None, because their return value is ignored.

# What are function arguments/parameters, why and how we use it?
- A `parameter` is a variable in a method definition. When a method is called, the `arguments` are the data you pass into the method's parameters. `Parameter` is variable in the declaration of `function`. `Argument` is the actual value of this variable that gets passed to function

# How to use function from a different file other than our currently working file?
- Use `import` function
- For example, you want to import function `calculate` from file `calc.py`: ```from calc import calculate```
