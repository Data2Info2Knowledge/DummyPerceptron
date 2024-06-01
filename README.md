This code implements a **Perceptron Learning Algorithm** on linearly separable data, as part of the answer to [Homework Assignment 1](https://work.caltech.edu/homework/hw1.pdf) of the online course [***'Learning From Data'***](https://work.caltech.edu/telecourse.html) taught by Caltech Professor Yaser Abu-Mostafa.  

For simplicity, the dimension is taken as d = 2.  
All data points lie inside *X* = [−1, 1] × [−1, 1].  
A point cloud (of dimension *numpoints*) is created, and a straight line is constructed by randomly picking two points in *X*. The target function is then defined so as to be 1 for those points that lie above the line, and -1 below it.  

The perceptron implements &nbsp; &nbsp; h(x) = sign (**w**.**x**).  
Given a misclassified point: &nbsp; &nbsp; sign(**w**.**x**_n) &ne; y_n , &nbsp; &nbsp; it corrects the weight vector by assigning &nbsp; &nbsp; &nbsp; **w** &larr; **w** + y_n.**x**_n