This program exhibits machine learning by reading in lines in bitmaps, and
based on correct examples, prints 1 if the line is vertical and 0 if
horizontal.

To make:
sh compile

To read in correct input and create file of pixel weights (which pixels make
the line more likely to be vertical if shaded in, which otherwise) based on
that input:
./perceptron -s test1.txt > weightsC.txt

To apply this learned knowledge to a test file:
./perceptron -l test2.txt < weightsC.txt

This will result in the printing of a list of 0's and 1's representing whether
the lines, in order, are vertical or horizontal, respectively.

When tested with these files, the perceptron has an 100% accuracy.