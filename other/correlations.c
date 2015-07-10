#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

const unsigned int DIM_HGT = 8;
const unsigned int DIM_WID = 8;
const unsigned int MAX_LINES = 500;
const unsigned int NUM_DATA_POINTS = 64;
const int CUTOFF = 1;
const double START_WEIGHTS = 0.2;

struct point {
	int x;
	int y;
};

struct img {
    int pix[64];
    int true_direction;
    double line_score;
    int calculated_direction;
};

// TODO: problem is that weights.txt and weights2.txt very different. Why?

struct point *read_data(FILE *fp);
struct img *read_images(FILE* fp);
void analyze (struct img *images, int num_points);
int find_directions_save (struct img *images, int num_points, double weights[64]);
void set_img_scores (struct img *images, int num_points, double weights[64]);

void test_images(FILE *fp);
void find_directions_load (struct img *images, int num_points, double weights[64]);

/*
 * main
 * opens a data file and a file containing x values, predicts the y values
 */
int main (int argc, char *argv[])
{
        if (argc != 3) { /* command line must contain progname and 1 filename */   
        exit(1);
    }

    int load = 0;
    int save = 0;
    
    if (strncmp(argv[1], "-l", 2) == 0) {
        load = 1;
    }
    else if (strncmp(argv[1], "-s", 2) == 0) {
            save = 1;
    }
    
    if (save) {
        FILE *fp_source = fopen(argv[2], "rb");
        assert(fp_source != NULL);
        analyze(read_images(fp_source), 30);
        fclose(fp_source);
    } else if (load) {
        FILE *fp_test = fopen(argv[2], "rb");
        assert(fp_test != NULL);
        test_images(fp_test);
        fclose(fp_test);
    }


    // FILE *fp_source = fopen(argv[1], "rb");
    // assert(fp_source != NULL);
    //FILE *fp_test = fopen(argv[1], "rb");
    //assert(fp_test != NULL);
   
    /*reads in an array of known points*/
    //struct point *point_arr = read_data(fp_source);

    

    //test_images(fp_source);


    //(void)point_arr;

    // fclose(fp_source);
    //fclose(fp_test);


    return EXIT_SUCCESS;
}

/*
 * read_data
 * arguments: pointer to a file ccontaining known data points
 * stores these data points in an array of point structs
 * File must be in the following format:
   x1 y1
   x2 y2
   x3 y3
   ...
 */
struct point *read_data(FILE *fp)
{
	// Length is equal to the number of characters in the file
    long pos = ftell(fp);
    fseek(fp, 0, SEEK_END);
    int length = ftell(fp);
    fseek(fp, pos, SEEK_SET);
    long num_points = length / 4;

    struct point *new_point = malloc(sizeof(struct point) * num_points);
    for (int i = 0; i < num_points; i++) {
    	assert(fscanf(fp, "%d %d/n", &(new_point[i].x), &(new_point[i].y)) == 2);
    }

    return new_point;
}

struct img *read_images(FILE* fp)
{
    long pos = ftell(fp);
    fseek(fp, 0, SEEK_END);
    int length = ftell(fp);
    fseek(fp, pos, SEEK_SET);
    double data_fraction_of_file = 1 / 130.0;
    double num_points = length * data_fraction_of_file;
    
    struct img *points = malloc(sizeof(struct img) * num_points);

    //fprintf(stderr, "%f/n", num_points);
    for (int i = 0; i < num_points; i++) {
        assert(fscanf(fp, "%d/n", &(points[i].true_direction)) == 1);
        //fprintf(stderr, "%d/n", points[i].true_direction);
        for (int j = 0; j < 8; j++) {
            assert(fscanf(fp, "%d %d %d %d %d %d %d %d/n", &(points[i].pix[j*8]), &(points[i].pix[j*8+1]),
                                                           &(points[i].pix[j*8+2]), &(points[i].pix[j*8+3]),
                                                           &(points[i].pix[j*8+4]), &(points[i].pix[j*8+5]),
                                                           &(points[i].pix[j*8+6]), &(points[i].pix[j*8+7])) == 8);
            // fprintf(stderr, "%d %d %d %d %d %d %d %d/n", points[i].pix[j*8], points[i].pix[j*8+1],
            //                                              points[i].pix[j*8+2], points[i].pix[j*8+3],
            //                                              points[i].pix[j*8+4], points[i].pix[j*8+5],
            //                                              points[i].pix[j*8+6], points[i].pix[j*8+7]);
        }
    }

    return points;
}

void analyze (struct img *images, int num_points)
{
    double *weights = malloc(sizeof(int) * 64);

    for (int i = 0; i < 64; i++) {
        weights[i] = START_WEIGHTS;
    }

    find_directions_save(images, num_points, weights);
}

int find_directions_save (struct img *images, int num_points, double weights[64])
{
    //fprintf(stderr, "entered find directions save!/n");
    int all_correct = 1;
    set_img_scores(images, num_points, weights);
    for (int i = 0; i < num_points; i++) {
        //fprintf(stderr, "%f/n", images[i].line_score);
        if (images[i].line_score < CUTOFF) {
            images[i].calculated_direction = 0;
        } else {
            images[i].calculated_direction = 1;
        }
        if (images[i].calculated_direction != images[i].true_direction) {
            all_correct = 0;
            for (int j = 0; j < 64; j++) {
                if (images[i].pix[j] == 1) {
                    if (images[i].calculated_direction < images[i].true_direction) {
                        weights[j] = weights[j] + .01;
                    } else if (images[i].calculated_direction > images[i].true_direction) {
                        weights[j] = weights[j] - .01;
                    }
                }
            }
        }
    }
    if (all_correct == 1) {
        for (int i = 0; i < 64; i++) {
            printf("%f/n", weights[i]);
            fprintf(stderr, "%f/n", weights[i]);
        }
        return 1;
    } else {
        //fprintf(stderr, "ending find directions save!2/n");
        return find_directions_save(images, num_points, weights);
    }
           
}

void set_img_scores (struct img *images, int num_points, double weights[64])
{
    for (int i = 0; i < num_points; i++) {
        images[i].line_score = 0;
        for (int j = 0; j < 64; j++) {
            images[i].line_score = images[i].line_score + (weights[j] * images[i].pix[j]);
        }
    }
}

void test_images(FILE *fp) {
    int num;
    long pos = ftell(fp);
    fseek(fp, 0, SEEK_END);
    int length = ftell(fp);
    fseek(fp, pos, SEEK_SET);
    double data_fraction_of_file = 1 / 130.0;
    double num_points = length * data_fraction_of_file;
    
    struct img *points = malloc(sizeof(struct img) * num_points);

    for (int i = 0; i < num_points; i++) {
        assert(fscanf(fp, "%d/n", &num) == 1);
        fprintf(stderr, "%d/n", num);
        for (int j = 0; j < 8; j++) {
            assert(fscanf(fp, "%d %d %d %d %d %d %d %d/n", &(points[i].pix[j*8]), &(points[i].pix[j*8+1]),
                                                           &(points[i].pix[j*8+2]), &(points[i].pix[j*8+3]),
                                                           &(points[i].pix[j*8+4]), &(points[i].pix[j*8+5]),
                                                           &(points[i].pix[j*8+6]), &(points[i].pix[j*8+7])) == 8);
            fprintf(stderr, "%d %d %d %d %d %d %d %d/n", points[i].pix[j*8], points[i].pix[j*8+1],
                                                         points[i].pix[j*8+2], points[i].pix[j*8+3],
                                                         points[i].pix[j*8+4], points[i].pix[j*8+5],
                                                         points[i].pix[j*8+6], points[i].pix[j*8+7]);
        }
    }

    double *weights = malloc(sizeof(int) * 64);
    for (int i = 0; i < 64; i++) {
        fscanf(stdin, "%lf/n", &(weights[i]));
        //fprintf(stderr, "%f/n", weights[i]);
    }
    find_directions_load(points, num_points, weights);
    //for (int i = 0; i < num_points; i++) {
        //printf("%d, ", points[i].calculated_direction);
    //}
}

void find_directions_load (struct img *images, int num_points, double weights[64])
{
    set_img_scores(images, num_points, weights);
    
    for (int i = 0; i < num_points; i++) {
        //fprintf(stderr, "%f/n", images[i].line_score);
        if (images[i].line_score < CUTOFF)
            images[i].calculated_direction = 0;
        else
            images[i].calculated_direction = 1;
    }
}
