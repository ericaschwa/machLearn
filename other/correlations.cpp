#include <stdio.h>
#include <stdlib.h>

const unsigned int DIM_HGT = 8;
const unsigned int DIM_WID = 8;
const unsigned int MAX_LINES = 500;

struct point {
	int x;
	int y;
};

struct point *read_data(FILE *fp);

/*
 * main
 * opens a .um program file; passes it to a function to be executed
 */
int main (int argc, char *argv[])
{
        if (argc != 3) { /* command line must contain progname and 1 filename */
                exit(1);
        }



        FILE *fp_source = fopen(argv[1], "rb");
        assert(fp_source != NULL);
        FILE *fp_test = fopen(argv[1], "rb");
        assert(fp_test != NULL);

        /*begins fetch-get-execute loop*/
        struct point *point_arr = read_data(fp_source);

       	fprintf("%d %d\n", point_arr->x, point_arr->y);


        return EXIT_SUCCESS;
}

/*
 * read_element
 * arguments: column of element, row of element, uarray2, pointer to the
 * element, and map (data that contains element to be added)
 * apply function called by Uarray2_map_row_major, stores input into each
 * element in uarray2
 * it is a checked runtime error to have an out of bounds element
 * exits with a checked runtime error if bad format
 */
struct point *read_data(FILE *fp)
{
    long pos = ftell(fp);
    fseek(fp, 0, SEEK_END);
    length = ftell(fp);
    fseek(fp, pos, SEEK_SET);
    length = (length/4);

    struct point *new_point = new struct point;
    new_point->x = length;
    new_point->y = length;

    return new_point;

	// ifstream myReadFile;
	// myReadFile.open("perceptron_test2.txt");

	// for (int i = 0; ((i < MAX_LINES) && (!myReadFile.fail())); i++) {
	// 	myReadFile >> lines[i].true_direction;
	// 	if ((!myReadFile.fail()) && (lines[i].true_direction != -1)) {
	// 		num_lines++;
	// 		getline(myReadFile, input_line);
	// 		for (int r = 0; r < IMG_HGT; r++) {
	// 			getline(myReadFile, input_line);
	// 			for (int c = 0; c < IMG_WID; c++) {
	// 				lines[i].image[r][c] = input_line[c];
	// 			}
	// 		}
	// 	}
	// }
	// myReadFile.close();
}