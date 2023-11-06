# 04. Conditional statements and loops
## Conditional Statements
Conditional statements in Python allow you to make decisions in your code based on whether certain conditions are true or false. These statements are fundamental for controlling the flow of your program. In Python, you primarily use `if`, `elif`, and `else` to create conditional statements.

Here's an explanation of conditional statements along with examples:

### `if` Statement:

The `if` statement is used to execute a block of code only if a condition is true.

```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```
In this example, the code inside the if block is executed because the condition `age >= 18` is true.
### `if`...`else` Statement:
The `if`...`else` statement allows you to execute one block of code when the condition is true and another block when it's false.
```python
age = 15
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
```
In this case, the `if` block is executed when the condition is true, and the else block is executed when it's false.

### `if`...`elif`...`else` Statement:
You can use elif (short for "else if") to test multiple conditions in sequence.
```python
score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```
Here, the program checks each condition in order and prints the corresponding grade based on the first condition that is true. If none of the conditions are met, it falls back to the `else` block.
### Nested `if` Statements:
You can nest `if` statements within other `if` statements to create more complex conditional logic.
```python
is_student = True
age = 17

if is_student:
    if age >= 18:
        print("You are a student and eligible to vote.")
    else:
        print("You are a student but not eligible to vote.")
else:
    print("You are not a student.")
```
In this example, the program first checks if someone is a student and then, if they are, it further checks their age for voting eligibility.

### Ternary Conditional Expression:
Python also supports a concise way to write conditional statements in a single line using the ternary conditional expression.
```python
age = 20
message = "You are eligible to vote" if age >= 18 else "You are not eligible to vote"
print(message)
```
Here, `message` is assigned based on the condition, and it's printed in a single line.

Conditional statements are essential for making decisions in your Python programs. They allow your code to respond dynamically to different situations and conditions.

## loops
In Python, loops are used to repeatedly execute a block of code. There are two main types of loops in Python: `for` loops and `while` loops. These loops are essential for automating repetitive tasks and processing data efficiently. Here's an explanation of both types of loops with examples:
### `for` Loops:
`for` loops are used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. They allow you to execute a block of code for each item in the sequence.
```python
# Iterating over a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
This `for` loop iterates over the list of fruits and prints each fruit.

> Using the `range` Function

for loops are often used with the `range` function to iterate a specific number of times.

```python
for i in range(1, 6):
    print(i)
```
This loop prints the numbers from 1 to 5.

### `while` Loops:
`while` loops are used to repeatedly execute a block of code as long as a specified condition is true.

```python
# Countdown using a while Loop
count = 5
while count > 0:
    print(count)
    count -= 1
```
This `while` loop counts down from 5 to 1.

## Loop Control Statements:
Python also provides loop control statements to modify the flow of loops:
- `break`: Terminates the loop prematurely.
- `continue`: Skips the current iteration and continues with the next one.

> Using `break` and `continue`

```python
for i in range(1, 11):
    if i == 3:
        break  # Terminate the loop when i is 3
    if i == 7:
        continue  # Skip iteration when i is 7
    print(i)
```
In this example, the loop is terminated when `i` is 3 and skips iteration when `i` is 7.

## Nested Loops:
You can also nest loops, which means placing one loop inside another. This is useful for tasks that involve multiple levels of iteration.

>  Nested `for` Loop

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```
This code demonstrates a nested `for` loop that prints combinations of `i` and `j`.

Loops are powerful constructs in Python that enable you to automate repetitive tasks, process data, and iterate over sequences. They are fundamental to many programming tasks and are a key part of the language.
