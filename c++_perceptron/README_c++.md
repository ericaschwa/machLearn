This program exhibits machine learning by reading in lines in bitmaps, and
based on correct examples, prints 1 if the line is vertical and 0 if
horizontal.

To make:
g++ perceptron_new.cpp

To read in correct input (from a file called perceptron_test2.cpp) and create
file of pixel weights (which pixels make the line more likely to be vertical
if shaded in, which otherwise) based on that input:
./a.out -s > weightsC++.txt

To apply this learned knowledge to a test file (called perceptron_test3.cpp):
./a.out -l < weightsC++.txt
This will result in the printing of a list of 0's and 1's representing whether
the lines, in order, are vertical or horizontal, respectively.

When tested with these files, the perceptron has an 100% accuracy.