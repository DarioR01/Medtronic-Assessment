# Medtronic Take-Home Task

## Solution
This solution employs a mix of bin packing and random walk techniques to select three non-overlapping random samples from the user's input image.

To determine if a valid solution exists, the bin packing problem is used to calculate the initial coordinates for the samples in a 2D space. If a solution is possible, these coordinates are passed to the RandomWalk algorithm, which randomizes the positions of the samples. The samples move for a total of 10,000 steps. Once a solution is confirmed, the final coordinates are used to crop the image into the desired samples.

## How To Use
1. Run the script from the terminal.
2. The script will prompt you to enter the path to an image, accepting both relative and absolute paths.
3. Next, input the width and height of the patches, ensuring these values are integers.
4. If a solution is found, the script will output the three image samples into the image_output folder.