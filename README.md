## Problem Statement
Histopathological images are fundamental in diagnosing breast cancer, offering detailed insights into tissue morphology and cellular structures. However, accurately classifying breast tumors from histopathological images presents unique challenges due to variations in tissue appearance, staining techniques, and tumor heterogeneity.

This capstone project aims to develop a robust and accurate breast tumor classifier using machine learning techniques applied to histopathological images. The primary objective is to create a model capable of distinguishing between benign and malignant tumors with high precision and recall, leveraging the rich information contained within histopathological images.

## Proposed Solution
1. Preprocessing of Histopathological Images
2. Feature Extraction and Representation
3. Model Training
4. Model Evaluation
5. Model Deployment
6. Productizing the work using Steamlit application

## Data Source
#### Breast Cancer Histopathological Database

[BreaKHis – Breast Cancer Histopathological Database](https://web.inf.ufpr.br/vri/databases/breast-cancer-histopathological-database-breakhis/) by [Spanhol, F., Oliveira, L. S., Petitjean, C. and Heutte, L.](https://ieeexplore.ieee.org/document/7312934) is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)

The Breast Cancer Histopathological Image Classification (BreakHis) is composed of images of breast tumor tissue collected from 82 patients using different magnifying factors (40X, 100X, 200X, and 400X). To date, it contains 2,480 benign and 5,429 malignant samples (700X460 pixels, 3-channel RGB, 8-bit depth in each channel, PNG format).

## Folds.csv
## Source of dataset 'Folds.csv' -  Kaggle

The authors of the dataset 'Folds.csv' have chosen to use a 5-fold cross-validation strategy. In this approach, the dataset is divided into five approximately equal-sized subsets (folds).

The cross-validation strategy is designed such that the images in the training and test sets come from different individuals across each fold. This means that when the model is trained on a particular fold, it learns from data collected from certain individuals, and when it's tested on that fold, it's evaluated on data from different individuals. This helps in evaluating the model's ability to generalize to unseen individuals.
