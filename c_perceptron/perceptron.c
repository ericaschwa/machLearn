#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

#define NUM_DATA_POINTS 64
#define CUTOFF 1.6
#define START_WEIGHTS 0.2
#define NUM_ITEMS 32

/*
 * Represents an image for the perceptron to analyze
 */
struct img {
    int pix[NUM_DATA_POINTS];
    int true_direction;
    double line_score;
    int calculated_direction;
};

struct img *read_images(FILE* fp);
void analyze (struct img *images, int num_points);
int find_directions_save (struct img *images, int num_points, double weights[NUM_DATA_POINTS]);
void set_img_scores (struct img *images, int num_points, double weights[NUM_DATA_POINTS]);
void test_images(FILE *fp);
void find_directions_load (struct img *images, int num_points, double weights[NUM_DATA_POINTS]);

/*
 * main
 * reads in lines in bitmaps.
 * Prints 1 if the line is considered vertical and 0 if horizontal. 
 * Decision is made based on a constant cutoff value.)
 * input: a sequence of images of lines, each preceded by either a 1
 *      (if the line is vertical) or 0 (if the line is horizontal).
 *      Input ends with a sentinel value of -1.
 * arguments: -l if loading weights to use in calculations, or -s if the
 *      program will determine and save them
 * output: for each image, a list of whether each line is vertical or   
 *      horizontal (1 if vertical, 0 if horizontal). The end of
 *      the list has a -1 sentinel value.
 * format: 1, 0, 0, 0, 1, 1, 0, 1, ... -1                                                 
 * code by: Erica Schwartz.                                                    
 * Date: 6/27/14. 
 */
int main (int argc, char *argv[])
{
    if (argc != 3) { /* command line must contain progname and 1 filename */   
        exit(1);
    }

    int load = 0;
    int save = 0;
    if (strncmp(argv[1], "-l", 2) == 0) { // load data
        load = 1;
    } else if (strncmp(argv[1], "-s", 2) == 0) { // dave data
        save = 1;
    }
    
    if (save) {
        FILE *fp_source = fopen(argv[2], "rb");
        assert(fp_source != NULL);
        analyze(read_images(fp_source), NUM_ITEMS);
        fclose(fp_source);
    } else if (load) {
        FILE *fp_test = fopen(argv[2], "rb");
        assert(fp_test != NULL);
        test_images(fp_test);
        fclose(fp_test);
    }
    return EXIT_SUCCESS;
}

/*
 * Set line scores based on given weights; these line scores will be used to determine
 * whether or not the line is vertical. If the line score is above a given cutoff,
 * it is considered vertical.
 */
void set_img_scores (struct img *images, int num_points, double weights[NUM_DATA_POINTS])
{
    for (int i = 0; i < num_points; i++) {
        images[i].line_score = 0;
        for (int j = 0; j < NUM_DATA_POINTS; j++) {
            images[i].line_score = images[i].line_score + (weights[j] * (double)images[i].pix[j]);
        }
    }
}

/*****************************     SAVE FUNCS     *****************************/

/*
 * Reads in images from a given file; each image contains a 1 or 0, depending on whether or not it
 * is considered to be vertical, followed by an 8x8 bitmap of pixels.
 * Returns an img data structure containing this information.
 */
struct img *read_images(FILE* fp)
{
    long pos = ftell(fp);
    fseek(fp, 0, SEEK_END);
    int length = ftell(fp);
    fseek(fp, pos, SEEK_SET);
    double data_fraction_of_file = 1 / 130.0; // 130 characters per image
    double num_points = length * data_fraction_of_file; // number of images in the file
    
    struct img *points = malloc(sizeof(struct img) * num_points);

    for (int i = 0; i < num_points; i++) {
        assert(fscanf(fp, "%d\n", &(points[i].true_direction)) == 1); // read in true direction of image
        for (int j = 0; j < 8; j++) { // read in pixels in bitmap
            assert(fscanf(fp, "%d %d %d %d %d %d %d %d\n", &(points[i].pix[(j*8)]), &(points[i].pix[(j*8)+1]),
                                                           &(points[i].pix[(j*8)+2]), &(points[i].pix[(j*8)+3]),
                                                           &(points[i].pix[(j*8)+4]), &(points[i].pix[(j*8)+5]),
                                                           &(points[i].pix[(j*8)+6]), &(points[i].pix[(j*8)+7])) == 8);
        }
    }
    return points;
}

/*
 * analyze image data, produce weights for each pixel that will be used to determine whether the image
 * contains a vertical or horizontal line
 */
void analyze (struct img *images, int num_points)
{
    double *weights = malloc(sizeof(double) * NUM_DATA_POINTS);

    for (int i = 0; i < NUM_DATA_POINTS; i++) { // initialize weights to start values
        weights[i] = START_WEIGHTS;
    }

    find_directions_save(images, num_points, weights); // edit weights based on machine learning
    free(images);
    free(weights);
}

/*
 * Given an image with a known verticality, continually changes the weights until it can produce
 * a formula resulting in a correct answer every time
 */
int find_directions_save (struct img *images, int num_points, double weights[NUM_DATA_POINTS])
{
    int all_correct = 1; // all correct is "true", until an incorrect answer occurs
    set_img_scores(images, num_points, weights);
    for (int i = 0; i < num_points; i++) {
        if (images[i].line_score < CUTOFF) { // find calculated direction
            images[i].calculated_direction = 0;
        } else {
            images[i].calculated_direction = 1;
        }
        if (images[i].calculated_direction != images[i].true_direction) { // incorrect answer
            all_correct = 0;
            for (int j = 0; j < NUM_DATA_POINTS; j++) {
                if (images[i].pix[j] == 1) { // adjust weights that caused incorrect result
                    if (images[i].calculated_direction < images[i].true_direction) { 
                        weights[j] = weights[j] + .01;
                    } else if (images[i].calculated_direction > images[i].true_direction) {
                        weights[j] = weights[j] - .01;
                    }
                }
            }
        }
    }
    if (all_correct == 1) { // keep going and adjusting weights until it gets them all correct
        for (int i = 0; i < NUM_DATA_POINTS; i++) {
            printf("%f\n", weights[i]); // then print the weights
        }
        return 1;
    } else {
        return find_directions_save(images, num_points, weights);
    }
           
}


/*****************************     LOAD FUNCS     *****************************/

/*
 * Reads in images from a given file; and weights from standard input
 * each image contains an 8x8 bitmap of pixels; each of these 64
 * pixels corresponds to a weight that determines how much that pixel
 * contributes to the verticality of the image.
 * analyzes the image data, and determines whether each image
 * contains a vertical or horizontal line
 */
void test_images(FILE *fp) {
    int num;
    long pos = ftell(fp);
    fseek(fp, 0, SEEK_END);
    int length = ftell(fp);
    fseek(fp, pos, SEEK_SET);
    double data_fraction_of_file = 1 / 130.0; // 130 characters per image
    double num_points = length * data_fraction_of_file; // number of images in the file
    
    struct img *points = malloc(sizeof(struct img) * num_points);

    for (int i = 0; i < num_points; i++) {
        assert(fscanf(fp, "%d\n", &(num)) == 1);
        for (int j = 0; j < 8; j++) { // read in pixels in bitmap
            assert(fscanf(fp, "%d %d %d %d %d %d %d %d\n", &(points[i].pix[(j*8)]), &(points[i].pix[(j*8)+1]),
                                                           &(points[i].pix[(j*8)+2]), &(points[i].pix[(j*8)+3]),
                                                           &(points[i].pix[(j*8)+4]), &(points[i].pix[(j*8)+5]),
                                                           &(points[i].pix[(j*8)+6]), &(points[i].pix[(j*8)+7])) == 8);
        }
    }

    double *weights = malloc(sizeof(double) * NUM_DATA_POINTS);
    for (int i = 0; i < NUM_DATA_POINTS; i++) { // read in weights
        fscanf(stdin, "%lf\n", &(weights[i]));
    }
    find_directions_load(points, num_points, weights); // find and print directions
    for (int i = 0; i < num_points; i++) {
        printf("%d, ", points[i].calculated_direction);
    }
    printf("-1\n");

    free(points);
    free(weights);
}

/*
 * Based on given weights, set the calculated directions of a given set of images based
 * on their line scores
 */
void find_directions_load (struct img *images, int num_points, double weights[NUM_DATA_POINTS])
{
    set_img_scores(images, num_points, weights);
    
    for (int i = 0; i < num_points; i++) {
        if (images[i].line_score < CUTOFF) {
            images[i].calculated_direction = 0;
        }
        else {
            images[i].calculated_direction = 1;
        }
    }
}
