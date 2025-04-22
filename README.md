
# K-Nearest Neighbors (KNN) Classifier on Iris Dataset

This Python script implements a basic K-Nearest Neighbors (KNN) classifier using the famous Iris dataset. The script performs the following steps:

1. **Load the Dataset**: The Iris dataset is loaded using Pandas, and the data is split into training and testing sets.
2. **Data Preprocessing**: The dataset is divided randomly into training and testing sets. Each item is then numbered for easy tracking.
3. **Distance Calculation**: The Euclidean distance is calculated between the testing data and the training data for each test sample.
4. **K-Nearest Neighbors**: The script finds the nearest 10 neighbors for each test sample and performs classification based on the majority vote.
5. **Accuracy Calculation**: The accuracy of the classifier is determined by comparing the predicted labels with the actual labels from the testing set.

## Requirements:
- Python 3.x
- Pandas library
- Math and Statistics libraries (both are standard Python libraries)

## Files:
- `Iris.csv`: Contains the Iris dataset with the following columns: Sepal Length, Sepal Width, Petal Length, Petal Width, and Class (label).
  
## How the Script Works:
1. **Data Loading**: The dataset is read from `Iris.csv` using `pandas.read_csv()`.
2. **Training and Testing Split**: The data is split into a random 100-point training set and the rest as a testing set.
3. **Distance Calculation**: The script calculates the Euclidean distance between each test sample and all training samples.
4. **Find Nearest Neighbors**: The nearest 10 neighbors for each test sample are identified.
5. **Label Prediction**: The class label for each test sample is predicted based on the majority vote from its nearest neighbors.
6. **Accuracy**: The percentage of correctly predicted labels is printed as the final result.

## How to Run:
1. Ensure you have Python installed along with the required libraries.
2. Place the `Iris.csv` file in the same directory as the Python script.
3. Run the script by executing `python knn_classifier.py` in the terminal.
4. The script will output the accuracy of the classifier based on the K-Nearest Neighbors algorithm.
