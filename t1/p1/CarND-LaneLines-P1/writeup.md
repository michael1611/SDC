# **Finding Lane Lines on the Road** 

## Writeup

The goals / steps of this project are the following:

**1. Make a pipeline that finds lane lines on the road**

![alt text][lane_detection]
<center>A snapshot showing the detected lanes</center>

**2. Reflect on my work in a written report**


[//]: # (Image References)

![lane_detection]: ./test_images_output/lanes.JPG "Original images with lane detected images"
[pipeline]: ./test_images_output/pipeline.JPG "my_pipeline"
[color_filtered]: ./test_images_output/color_filtered.JPG "color_filtered"
[grayscaled]: ./test_images_output/grayscaled.JPG "grayscaled"
[gaussian]: ./test_images_output/gaussian.JPG "gaussian"
[canny_edge]: ./test_images_output/canny_edge.JPG "canny_edge"
[region_of_interest]: ./test_images_output/region_of_interest.JPG "region_of_interest"
[final]: ./test_images_output/final.JPG "final"
[shortcoming]: ./test_images_output/shortcoming.JPG "shortcoming"
[extrapolated_shortcoming]: ./test_images_output/extrapolated_shortcoming.JPG "extrapolated_shortcoming"
---

### My Pipeline

My pipeline consisted of 7 steps as stated below:

- First I filter the image to remove light colors.
- Second, I converted the image to grayscale.
- Third, I applied gaussian filter to reduce noise.
- Fourth, I applied canny edge detector.
- Fifth, I extracted a region of interest from the image.
- Sixth, I extracted lines from the image using hough transform.
- Seventh, I removed outliers from the detected lines by applying the following approcahes:
 -  Removed the lines which are more horizontal then vertical. I did this because for the most part the lanes are supposed to be vertical.
 -  Categorized the lines into two clusters (one for each lane) using kmeans and removed the lines that are near the bottom of the image and either:
     - Have -ve slope and are on the left side of the image or
     - Have +ve slope and are on the right side of the image.
 - Calculated the equation of two lanes using the average of remaining lines in the two clusters respectively.
- Last but not the least, extrapolated the two lanes to show them in the region of interest.

  	

In order to draw a single line on the left and right lanes, I did not modified the draw_lines() function. I instead performed the following steps:
- Removed outliers from the canny-edges using the procedure stated above.
- Divided the lines into two clusters based on slopes (Note that the slopes of the two lane differ in sign).
- Calculated the average line and used polyfit to calculate the equation of the two lanes in the form:
<center>x = ay + b, and not as y = ax + b </center>
I did that because it is easier to first estimate the range of the lanes in vertical direction and then calculating the horizontal position as a function of the vertical position.


### 1. Below I show output image after each step of the pipeline
![space for color filtered image][color_filtered]
![space for grayscaled image][grayscaled]
![space for gaussian filter applied image][gaussian]
![space for canny edge image][canny_edge]
![space for region of interest image][region_of_interest]
![space for final image][final]



### 2. Potential shortcomings with my current pipeline

Sometimes the detected lines for the lanes are too small (observed for challenge.mp4) and it is possible that the extrapolated lanes may not overlay over the actual lanes properly.
![space for shortcoming image][shortcoming]
Although the extrapolated lane image is correct for the detected lines of the above image:
![space for extrapolated_shortcoming image][extrapolated_shortcoming]


### 3. Suggest possible improvements to your pipeline

 I think for detecting the position of the lanes at time 't', taking into account the position of lanes at time 't-1' will definitely help!
