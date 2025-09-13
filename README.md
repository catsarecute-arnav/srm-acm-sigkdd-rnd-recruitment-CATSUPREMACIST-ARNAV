# srm-acm-sigkdd-rnd-recruitment-CATSUPREMACIST-ARNAV
This file contains a python program that finds whether a given number entered by the user is a Armstrong number. 

An armstrong number or a narcissistic number is a number whose individual digits when raised to the power of the number of digits in the number give the number itself. 

As an example, 153=1^3+5^3+3^3. We cube the individual digits as 153 is a 3 digit number. 

All single digit numbers are armstrong numbers as they will be raised to the power of one giving the digit itself.

# Algorithm Behind The Code
1. Define function named armstrong
2. Try-error for error handling.
3. Define variable as num for user to enter an integer value.
4. Take the integer as a str in another variable then find length of this variable.
5. Initialize a variable named armstrong_sum with a value of 0.
6. Write a for loop to verify whether number entered is an armstrong number.
7. Write an if-else condiional statement inside the for loop for if being it is and else being it isn't. and put appropriate print statements to let user know the outcome.
8. Indented to the try statement write the except statement for ValueError for when the user enters a non-integer and print appropriate statement.
9. Call the function using __main__==__name__.

# How To Run The Code
To run this code succesfully, you have the following options:
1. Use an online python compiler
2. Use VS code or another alternative such as Notepad++, Vim, Atom, etc.

1. Online Python Compiler
Simply search on google for an online python compiler such as prpgramiz.com, w3schools.com, codechef.com, etc. Open the website and copy-paste the code given into it and click on the run button.

2. VS Code
1. Open VS Code
2. Search for a python extension such as the one from Microsoft which comes with intellisense and can detect the syntax of the language being coded in.
3. Intsall and Enable the extension. 
4. Create a folder in your desktop or another location in your computer with a name of your choice.
5. Go to VS Code and select the open new folder option under file.
6. Click on the new file icon and name it. Just make sure to end the name with a .py at the end.
7. Once done, you can now copy-paste the code given in this repository.
8. Press Ctrl+S for WIndows or Command+S for mac users to save the file. Again check for the .py at the end.
9. Now click the arrow button in the upper right corner of the VS Code app to run the program.
