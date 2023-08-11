# opencv-TrafficLight
The aim of this mini project was to develop a program in opencv, which reads several images of traffic lights provided, and based on the analysis of the histogram of these images, detects whether the respective lights are on, namely green, red and yellow .

Software used:
OpenCv version 4.4.0, and the Python language in its 3.8 version, and the IDE used pycharm and Jupyter Notebook.

Operation:

The following libraries were imported: opencv which is specific for "computer vision", numpy, for the treatment and manipulation of matrices, and the matplotlib library for analysis and better visualization of histograms.

A for repetition structure was used to open each image, select the mask that highlights the corresponding traffic light and cut the image (lines 31 to 34), leaving only the traffic light for analysis. It then splits the three color channels (line 37).

The respective histograms were created for each channel (line 39 to 41). Histograms with 32 BINs were used because they were found to contain enough information for a correct color analysis. For this, the values ​​of each histogram (line 45 to 47) are added and analyzed.

In a first analysis only part of the spectrum was used, mainly between 20 and 32, as the lights on will have more values ​​in the higher spectra, but it was found to have the same result as an analysis in all 32 BINs.


Next, the analysis is carried out using decision structures, this algorithm detects whether the color is lit or not (lines 53 to 61). Taking into account that it is already known in advance that the green color does not trigger at the same time as the yellow color, and the green color values ​​can interfere with the yellow color, the analysis of the green color only triggers if the yellow color does not occur.
The colors activate according to the following values ​​in table I.

![TableI](images/tableI.png)