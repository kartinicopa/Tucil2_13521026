# Tugas Kecil II IF 2211 Strategi Algoritma
> Finding the Closest Pair of Points in R^n dimension using the Divide and Conquer Algorithm

## Author 
Kartini Copa - 13521026

## Table of Contents
* [Description](#description)
* [Feature](#feature)
* [Installation](#installation)
* [Setup](#setup)

## Description
Finding the closest pair of points in Rn dimension is a classic problem in computational geometry. One approach to solving this problem is using the divide and conquer algorithm. This algorithm has a time complexity of O(n log (n)), which is faster than the brute force algorithm that has a time complexity of O(n^2).
The divide and conquer algorithm works by dividing the set of points into two halves recursively until the subsets only contain one or two points. After the base case is reached, the algorithm starts to merge the subsets while finding the closest pair of points between them. To find the closest pair of points, the algorithm uses Euclidean distance formula. Finally, the algorithm returns the pair of points with the smallest distance found between the subsets. As a comparison, the brute force algorithm finds the closest pair of points by calculating the distance between each pair of points and returning the pair with the smallest distance. This algorithm has a time complexity of O(n^2), which is slower than the divide and conquer algorithm. The divide and conquer algorithm for finding the closest pair of points in Rn dimension is a faster solution compared to the brute force algorithm. However, it requires more memory due to the recursive nature of the algorithm. The brute force algorithm, although slower, is more memory efficient and can be used for smaller datasets.

<p align="center">
<img width="513" alt="image" src="https://user-images.githubusercontent.com/102657926/221998685-233561ad-0134-42d5-bb16-f2470736a791.png">
</p>
<p align="center">
<img width="289" alt="image" src="https://user-images.githubusercontent.com/102657926/221995218-bc1792ab-2047-452a-ae73-e830a10fcf43.png">
</p>
<p align="center">
<img width="289" alt="image" src="https://user-images.githubusercontent.com/102657926/222000758-10641861-8b3a-4e93-876a-651789d3b6db.png"></p>


## Feature
- Find closest pair points
- Find closest distance
- Plotting points


## Installation
- python version 3.10
- library platform
- library math
- library matplotlib
- library time
- library random


## Setup
1. Clone this repository to your local directory
2. Change directory to the src folder
3. Run main.py
