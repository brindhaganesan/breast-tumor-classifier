## Problem Statement
Histopathological images are fundamental in diagnosing breast cancer, offering detailed insights into tissue morphology and cellular structures. However, accurately classifying breast tumors from histopathological images presents unique challenges due to variations in tissue appearance, staining techniques, and tumor heterogeneity.

This capstone project aims to develop a robust and accurate breast tumor classifier using machine learning techniques applied to histopathological images. The primary objective is to create a model capable of distinguishing between benign and malignant tumors with high precision and recall, leveraging the rich information contained within histopathological images.

<img width="1006" alt="github" src="https://github.com/brindhaganesan/breast-tumor-classifier/assets/50005288/d67febf1-5518-4761-9877-a307a47c22ad">


## Proposed Solution
1. Preprocessing of Histopathological Images
2. Feature Extraction and Representation
3. Model Training
4. Model Evaluation
5. Model Deployment
6. Productizing the work using Steamlit application

## Files in the Repository for Sprint 2

- Folds.csv
- breast-tumor-classifier-eda-v2.ipynb
- Sprint 2 Brindha Ganesan - Breast Tumor Classifier.pdf


## Data Source
#### Breast Cancer Histopathological Database

[BreaKHis – Breast Cancer Histopathological Database](https://web.inf.ufpr.br/vri/databases/breast-cancer-histopathological-database-breakhis/) by [Spanhol, F., Oliveira, L. S., Petitjean, C. and Heutte, L.](https://ieeexplore.ieee.org/document/7312934) is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)

The Breast Cancer Histopathological Image Classification (BreakHis) is composed of images of breast tumor tissue collected from 82 patients using different magnifying factors (40X, 100X, 200X, and 400X). To date, it contains 2,480 benign and 5,429 malignant samples (700X460 pixels, 3-channel RGB, 8-bit depth in each channel, PNG format).

## Folds.csv

The BreaKHis dataset has been randomly divided into a training (70%) and a testing (30%) set. To make sure the classifier generalizes to unseen patients, the patients used to
build the training set are not used for the testing set. The results presented in this work are the average of five trials.

## Exploratory Data Analysis

<img width="441" alt="class-imbalance" src="https://github.com/brindhaganesan/breast-tumor-classifier/assets/50005288/7afb1282-8306-4df5-8239-a5eb9938d980">



<img width="763" alt="benign-malignant" src="https://github.com/brindhaganesan/breast-tumor-classifier/assets/50005288/90cbbdd0-ff14-4c84-9edc-5915c1259bd2">



<img width="1000" alt="cross-validation" src="https://github.com/brindhaganesan/breast-tumor-classifier/assets/50005288/8987fad4-d4bc-478e-a851-b6a8bda46ae4">





Second fold is chosen specifically because it contains the highest proportion of training data. Second fold has a larger number of samples compared to other folds, making it suitable for training the model.
