# MohrsCircle-python-

This is a program that calculates the Mohr's Circle plot given the normal stresses in the x and y direction and the shear stress. The output is a graph that displays Mohr's circle, which is a graphical representation of the relationships between the normal stresses and shear stress.

## Dependencies
This program requires two packages, numpy and matplotlib. These packages can be installed by running pip install numpy matplotlib.

## How to Run the Program
The program can be run by executing the following command in a terminal or command prompt:

python3 MohrsCirclePlaneStress.py

The program will prompt the user to input the values for the normal stress in the x-direction, the normal stress in the y-direction, and the shear stress. After the inputs have been entered, the program will generate a plot of the Mohr's circle representation.

## Code Explanation
The code consists of two functions: principal_stresses and MohrsCirclePlaneStress.

The principal_stresses function calculates the principal stresses, the average normal stress, the maximum shear stress, and the angles of the principal stresses.

The MohrsCirclePlaneStress function uses the principal_stresses function to calculate the important values, and then plots the Mohr's circle representation using the matplotlib library. The graph displays the normal stress and shear stress values as well as the principal stresses and the maximum shear stress.