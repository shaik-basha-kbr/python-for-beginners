# 02. Variables and data types

Python is a powerful and dynamic programming language that offers a variety of data types and variables. Let's dive deeper into this concept and explore the different types of variables and data types in Python
## Variables
- A variable is a storage location that holds a value.
- In Python, variables are created automatically when a value is assigned to them.
- Variables can hold various types of data, including numbers, strings, and lists.
### Integer Variables:
Integer variables are used to store whole numbers. For example, you can create an integer variable called "age" and assign it a value of 25.

```age = 25```
### Float Variables:

Float variables are used to store decimal numbers. For example, you can create a float variable called `price` and assign it a value of 9.99.

```price = 9.99```
### String Variables:
String variables are used to store text. For example, you can create a string variable called `name` and assign it a value of `John`.

```name = "John"```
### Boolean Variables:
Boolean variables are used to store True or False values. For example, you can create a boolean variable called `is_raining` and assign it a value of `True`.

```is_raining = True```

Variables in Python can also be modified and updated at any time during the program execution.
## Data Types
Python is a dynamically typed language, which means that the type of a variable is determined at runtime - as opposed to statically typed languages, where the type of a variable must be declared at compile time.
- Python offers a variety of data types, including numeric, string, boolean, and more.
- Numeric data types include integers, floating-point numbers, and complex numbers.
- String data types consist of a sequence of characters enclosed in quotes, either single or double.
- Boolean data types are used to represent the truth values of True or False.

Some of the built-in data types in Python include:

1. Integers (int) - whole numbers, positive or negative, such as 5 or -2.
2. Floats (float) - decimal numbers, such as 3.14 or -0.5.
3. Strings (str) - sequences of characters, enclosed in single or double quotes, such as "Hello, world!" or 'Python'.
4. Booleans (bool) - logical values that can be either True or False.
5. Lists (list) - ordered collections of items, enclosed in square brackets and separated by commas, such as [1, 2, 3] or ['apple', 'banana', 'orange'].
6. Tuples (tuple) - similar to lists, but immutable (cannot be changed), enclosed in parentheses, such as (1, 2, 3) or ('apple', 'banana', 'orange').
7. Dictionaries (dict) - unordered collections of key-value pairs, enclosed in curly braces and separated by colons, such as {'name': 'John', 'age': 30}.

These are just some examples of data types in Python - there are many more, including sets, bytes, and complex numbers. Understanding data types is important in Python programming, as it affects how variables are stored in memory and how they can be manipulated in code.
## Type Conversion
Type conversion, also known as type casting, is the process of changing a variable from one data type to another.
- Python also allows for type conversion, which is the process of converting one data type to another.
- This can be done using built-in functions, such as int(), float(), str(), and bool().
- Type conversion is important when working with different data types and ensures that operations are performed correctly.

For example, let's say we have a variable `x` that is a string containing the value `5`. If we want to perform mathematical operations on `x`, we need to convert it to an integer type. We can do this using the `int()` function like so:

```
x = "5"
y = int(x)
```
Now the variable `y` contains the integer value `5`, which we can use in mathematical operations.

Similarly, if we have a variable `z` that is a floating point number (`z = 3.14`), we can convert it to an integer using the `int()` function. This will truncate the decimal portion of the number and return an integer value:

```
z = 3.14
w = int(z)
```
Now the variable `w` contains the integer value `3`.

In summary, type conversion is a useful technique in Python for changing the data type of a variable to better suit the needs of your program.

In conclusion, understanding variables and data types is essential to writing effective Python code. By leveraging the various data types and type conversion options, programmers can create robust and versatile programs that can handle a variety of tasks and data.
