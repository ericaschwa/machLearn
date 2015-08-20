#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <math.h>
#include <cctype>
#include <ctype.h>
using namespace std;

// perceptron.cpp: digital recognizer of whether or not lines are vertical.     
//        purpose: reads in lines in bitmaps. Prints 1 if the line is     
//                 considered vertical and 0 if horizontal. (Decision is made
//                 based on a constant cutoff value.)
//          input: a sequence of images of lines, each preceded by either a 1
//                 (if the line is vertical) or 0 (if the line is horizontal).
//                 Input ends with a sentinel value of -1.
//      arguments: -l if loading weights to use in calculations, or -s if the
//                 program will determine and save them
//         output: for each image, a list of whether each line is vertical or   
//                 horizontal (1 if vertical, 0 if horizontal). The end of
//                 the list has a -1 sentinel value.
//         format: 1, 0, 0, 0, 1, 1, 0, 1, ... -1                                                 
//        code by: Erica Schwartz.                                                    
//           Date: 7/27/14. 

const int MAX_LINES = 500;
const int IMG_HGT = 8;
const int IMG_WID = 8;
const double CUTOFF = 1.6;
const double START_WEIGHTS = 0.2;

// Line
// Stores a 2D array of char values which represents an image of a line, an
// int value that represents whether the line is vertical (represented by a
// value of 1) or horizontal (represented by a 0), another int value that
// represents whether this program finds the line to be vertical (1) or
// horizontal (0), and an int that represents the line's "line score," which
// will be used to determine whether the line is vertical or horizontal.
struct Line {
     unsigned int image[IMG_HGT][IMG_WID];
     double       line_score;
     int          true_direction;
     int          calculated_direction;
};

int    input_save           (Line lines [MAX_LINES]);
int    input_load           (Line lines [MAX_LINES]);
void   analyze              (Line lines [MAX_LINES], int num_lines,
			                  string save, string load);
bool   find_directions_save (Line lines [MAX_LINES], int num_lines,
				  double weights[IMG_HGT][IMG_WID],
			                               string save);
void   find_directions_load (Line lines [MAX_LINES], int num_lines,
				  double weights[IMG_HGT][IMG_WID]);
void set_line_scores        (Line lines [MAX_LINES], int num_lines,
				  double weights[IMG_HGT][IMG_WID]);
void   print                (Line lines [MAX_LINES], int num_lines);

int main (int argc, char* argv[])
{
    string load = "";
    string save = "";
    
    for (int i = 1; i < argc; ++i) {
		if (std::string(argv[i]) == "-l") {
	            load = "load";
		} else if (std::string(argv[i]) == "-s") {
	            save = "save";
		}
    }
    
    Line lines[MAX_LINES];
    
    if (save != "")			analyze(lines, input_save(lines), save, load);
    else if (load != "")	analyze(lines, input_load(lines), save, load);
    
    return 0;
}

// input_save                                                                    
//   purpose: to read in input about lines, and store it in Line values.                   
// arguments: an array of values of type Line that includes a 2D array of
//            char values which represents an image of a line, an int value
//            that represents whether the line is vertical (represented by a
//            value of 1) or horizontal (represented by a 0), another int
//            value that represents whether this program finds the line to be
//            vertical (1) or horizontal (0), and an int that represents the
//            line's "line score," which will be used to determine whether the
//            line is vertical or horizontal.
//   returns: an int value that represents the number of lines.                     
//   effects: modifies the Line values in the array to reflect the input
//            information.
//     notes: Line values must contain the correct "image" (2D array of char
//            values), and the correct answer as to whether the line is
//            considered vertical or horizontal, according to a constant
//            angle cutoff.                                     
int input_save (Line lines [MAX_LINES])
{
    string input_line;
    int num_lines = 0;

    ifstream myReadFile;
    myReadFile.open("perceptron_test2.txt"); // file with correct answers

    for (int i = 0; ((i < MAX_LINES) && (!myReadFile.fail())); i++) {
		myReadFile >> lines[i].true_direction; // read in true direction
		if ((!myReadFile.fail()) && (lines[i].true_direction != -1)) {
		    num_lines++;
		    getline(myReadFile, input_line);
		    for (int r = 0; r < IMG_HGT; r++) {
				getline(myReadFile, input_line); // get and parse line in image
				for (int c = 0; c < IMG_WID; c++) {
				    lines[i].image[r][c] = input_line[c];
				}
		    }
		}
    }

    myReadFile.close();
    return (num_lines);
}

// input_load                                                                     
//   purpose: to read in input about lines, and store it in Line values.                   
// arguments: an array of values of type Line that includes a 2D array of
//            char values which represents an image of a line, an int value
//            that represents whether the line is vertical (represented by a
//            value of 1) or horizontal (represented by a 0), another int
//            value that represents whether this program finds the line to be
//            vertical (1) or horizontal (0), and an int that represents the
//            line's "line score," which will be used to determine whether the
//            line is vertical or horizontal.
//   returns: an int value that represents the number of lines.                     
//   effects: modifies the Line values in the array to reflect the input
//            information.
//     notes: Line values must contain the correct "image" (2D array of char
//            values). However, unlike in input_save, it does not need to
//            contain the correct answer as to whether the line is
//            considered vertical or horizontal.                                    
int input_load (Line lines [MAX_LINES])
{
    string input_line;
    int num_lines = 0;

    ifstream myReadFile;
    myReadFile.open("perceptron_test3.txt"); // file without correct answers

    for (int i = 0; ((i < MAX_LINES) && (!myReadFile.fail())); i++) {
	myReadFile >> input_line;
	if ((!myReadFile.fail()) && (input_line != "-1")) {
	    num_lines++;
	    getline(myReadFile, input_line);
	    for (int r = 0; r < IMG_HGT; r++) {
		getline(myReadFile, input_line); // get and parse line in image
		for (int c = 0; c < IMG_WID; c++)
		    lines[i].image[r][c] = input_line[c];
	    }
	}
    }    
    myReadFile.close();
    return (num_lines);
}

// analyze                                                                      
//   purpose: to read lines in an image, and determine whether those lines 
//            are vertical or horizontal.                     
// arguments: an array of values of type Line that includes a 2D array of
//            char values which represents an image of a line, an int value
//            that represents whether the line is vertical (represented by a
//            value of 1) or horizontal (represented by a 0), another int
//            value that represents whether this program finds the line to be
//            vertical (1) or horizontal (0), and an int that represents the
//            line's "line score," which will be used to determine whether the
//            line is vertical or horizontal.
//            Also takes an int value that represents the number of lines, and
//            two strings representing which files (if any) the function
//            will load or save.                                                                      
//    prints: whether the lines are vertical or horizontal.     
//   effects: modifies the angle and calculated direction of each line to
//            reflect calculations.
//     notes: Line values must contain the correct "image" (2D array of char
//            values), and either the the correct answer as to whether the line
//            is considered vertical or horizontal, according to a constant
//            angle cutoff, or come with the name of a data file to load that
//            contains this information.                                     
void analyze (Line lines [MAX_LINES], int num_lines, string save, string load)
{
    double weights[IMG_HGT][IMG_WID];
    
    if (save != "") { // set weights to start weights
		for (int r = 0; r < IMG_HGT; r++) {
		    for (int c = 0; c < IMG_WID; c++)
			weights[r][c] = START_WEIGHTS;
		}
		find_directions_save(lines, num_lines, weights, save);
    }
    else if (load != "") { // set weights to weights input
		for (int r = 0; r < IMG_HGT; r++) {
		    for (int c = 0; c < IMG_WID; c++) {
			cin >> weights[r][c];
		    }
		}
		find_directions_load(lines, num_lines, weights);
		print(lines, num_lines);
    }
}

// find_directions_save
// purpose:   Determines the correct direction for
//            all Lines in an array of values of type Line.
// arguments: an array of values of type Line that includes a 2D array of
//            char values which represents an image of a line, an int value
//            that represents whether the line is vertical (represented by a
//            value of 1) or horizontal (represented by a 0), and another int
//            value that represents whether this program finds the line to be
//            vertical (1) or horizontal (0), and an int that represents the
//            line's "score," which will be used to determine whether the line
//            is vertical or horizontal.
//            Also takes an int value that represents the number of lines,
//            a 2D array of double values that represents the weights given
//            to characters at each point in the 2D image that represents the
//            lines, when determining whether the lines are vertical or
//            horizontal.
//            Also takes a string representing which file the function
//            will save.
// returns:   a boolean value representing whether true directions and
//            calculated directions match for all lines. (This function will
//            not completely return and exit until this is true.)
// effects:   modifies the lines' calculated directions.
bool find_directions_save (Line lines [MAX_LINES], int num_lines,
                           double weights[IMG_HGT][IMG_WID], string save)
{
    bool all_correct = true;
    set_line_scores(lines, num_lines, weights);
    for (int i = 0; i < num_lines; i++) {
		if (lines[i].line_score < CUTOFF) // find calculated direction
		    lines[i].calculated_direction = 0;
		else
		    lines[i].calculated_direction = 1;
		if (lines[i].calculated_direction != lines[i].true_direction) { 
			// incorrect answer
		    all_correct = false;
		    for (int r = 0; r < IMG_HGT; r++) {
				for (int c = 0; c < IMG_WID; c++) {
				    if (lines[i].image[r][c] == '1') {
				    // adjust weights that caused incorrect result
						if (lines[i].calculated_direction <
						    lines[i].true_direction)
						    weights[r][c] = weights[r][c] + .01;
						else if (lines[i].calculated_direction >
						         lines[i].true_direction)
						    weights[r][c] = weights[r][c] - .01;
					}
				}
		    }
		}
    }
    // keep going and adjusting weights until it gets them all correct
    if (all_correct) { 
		for (int r = 0; r < IMG_HGT; r++) {
		    for (int c = 0; c < IMG_WID; c++) {
	                cout << weights[r][c] << endl; // print the weights
		    }
		}
		return true;
    } else return find_directions_save(lines, num_lines, weights, save);   
}

// find_directions_load
// purpose:   Determines the correct direction for
//            all Lines in an array of values of type Line.
// arguments: an array of values of type Line that includes a 2D array of
//            char values which represents an image of a line, an int value
//            that represents whether the line is vertical (represented by a
//            value of 1) or horizontal (represented by a 0), and another int
//            value that represents whether this program finds the line to be
//            vertical (1) or horizontal (0), and an int that represents the
//            line's "score," which will be used to determine whether the line
//            is vertical or horizontal.
//            Also takes an int value that represents the number of lines, and
//            a 2D array of double values that represents the weights given
//            to characters at each point in the 2D image that represents the
//            lines, when determining whether the lines are vertical or
//            horizontal.
// returns:   void function.
// effects:   modifies the lines' calculated directions.
void find_directions_load (Line lines [MAX_LINES], int num_lines,
					      double weights[IMG_HGT][IMG_WID])
{
    set_line_scores(lines, num_lines, weights);
    
    for (int i = 0; i < num_lines; i++) {
    // calculate direction based on line score
		if (lines[i].line_score < CUTOFF)
		    lines[i].calculated_direction = 0;
		else
		    lines[i].calculated_direction = 1;
	}  
}

// set_line_scores
// purpose:   sets line_scores for all Lines in an array of values of type
//            Line.
// arguments: an array of values of type Line that includes a 2D array of
//            char values which represents an image of a line, an int value
//            that represents whether the line is vertical (represented by a
//            value of 1) or horizontal (represented by a 0), and another int
//            value that represents whether this program finds the line to be
//            vertical (1) or horizontal (0), and an int that represents the
//            line's "score," which will be used to determine whether the line
//            is vertical or horizontal.
//            Also takes an int value that represents the number of lines, and
//            a 2D array of double values that represents the
//            weights given to characters at each point in the 2D images that
//            represent the lines, when determining whether the lines are
//            vertical or horizontal.
// returns:   void function.
// effects:   modifies the Line's line_scores.
void set_line_scores (Line lines [MAX_LINES], int num_lines,
					  double weights[IMG_HGT][IMG_WID])
{
    for (int i = 0; i < num_lines; i++) { // calculate line score for each line
		lines[i].line_score = 0;
		for (int r = 0; r < IMG_HGT; r++) {
		    for (int c = 0; c < IMG_WID; c++) {
			    lines[i].line_score = lines[i].line_score +
			    (weights[r][c] * lines[i].image[r][c]);
		    }
		}
    }
}

// print                                                                     
//   purpose: to print out whether the lines input are vertical or horizontal.         
// arguments: an array of values of type Line that includes a 2D array of
//            char values which represents an image of a line, an int value
//            that represents whether the line is vertical (represented by a
//            value of 1) or horizontal (represented by a 0), and another int
//            value that represents whether this program finds the line to be
//            vertical (1) or horizontal (0), and an int that represents the
//            line's "line score," which will be used to determine whether the
//            line is vertical or horizontal.
//            Also takes an int value that represents the number of lines.                     
//   returns: void function.                                                    
//    prints: whether the lines are vertical or horizontal.     
//   effects: does not modify anything.
//     notes: Line values must contain the correct answer as to whether the line
//            is considered vertical or horizontal, according to a constant
//            angle cutoff.  
void print (Line lines [MAX_LINES], int num_lines)
{
    for (int i = 0; i < num_lines; i++) {
		cout << lines[i].calculated_direction << ", ";
    }
    cout << "-1" << endl;
}