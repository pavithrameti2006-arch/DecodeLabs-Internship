# ============================================================
# PROJECT 2: IRIS FLOWER CLASSIFICATION USING MACHINE LEARNING
# ============================================================

# Import required libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# ============================================================
# STEP 1: LOAD THE DATASET
# ============================================================

print("=" * 60)
print("IRIS FLOWER CLASSIFICATION USING MACHINE LEARNING")
print("=" * 60)

# Load the built-in Iris dataset
iris = load_iris()

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Add the target species
df["Species"] = iris.target

# Display the dataset
print("\n1. DATASET LOADED SUCCESSFULLY!")

print("\nFirst five records:")
print(df.head())

print("\nDataset shape:")
print(f"Number of records: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")


# ============================================================
# STEP 2: UNDERSTAND THE DATASET
# ============================================================

print("\n" + "=" * 60)
print("2. DATASET INFORMATION")
print("=" * 60)

print("\nFeature names:")
for feature in iris.feature_names:
    print("-", feature)

print("\nTarget classes:")
for index, species in enumerate(iris.target_names):
    print(f"{index}: {species}")

print("\nMissing values:")
print(df.isnull().sum())

print("\nSpecies distribution:")
print(df["Species"].value_counts().sort_index())


# ============================================================
# STEP 3: SELECT FEATURES AND TARGET
# ============================================================

# Features: flower measurements
X = df[iris.feature_names]

# Target: flower species
y = iris.target

print("\n" + "=" * 60)
print("3. FEATURES AND TARGET SELECTED")
print("=" * 60)

print("\nInput features:")
print(list(X.columns))

print("\nTarget variable:")
print("Species")


# ============================================================
# STEP 4: SPLIT DATA INTO TRAINING AND TESTING SETS
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 60)
print("4. DATA SPLITTING COMPLETED")
print("=" * 60)

print(f"\nTotal records: {len(X)}")
print(f"Training records: {len(X_train)}")
print(f"Testing records: {len(X_test)}")


# ============================================================
# STEP 5: CREATE AND TRAIN THE CLASSIFICATION MODEL
# ============================================================

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("\n" + "=" * 60)
print("5. MODEL TRAINING COMPLETED SUCCESSFULLY!")
print("=" * 60)


# ============================================================
# STEP 6: MAKE PREDICTIONS
# ============================================================

y_pred = model.predict(X_test)

print("\n" + "=" * 60)
print("6. MODEL PREDICTIONS")
print("=" * 60)

# Display the first ten actual and predicted values
results = pd.DataFrame({
    "Actual Species": iris.target_names[y_test[:10]],
    "Predicted Species": iris.target_names[y_pred[:10]]
})

print("\nActual vs Predicted:")
print(results.to_string(index=False))


# ============================================================
# STEP 7: EVALUATE MODEL ACCURACY
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("7. MODEL EVALUATION")
print("=" * 60)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        labels=[0, 1, 2],
        target_names=iris.target_names,
        zero_division=0
    )
)


# ============================================================
# STEP 8: DISPLAY THE CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=[0, 1, 2]
)

print("\nConfusion Matrix:")
print(cm)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

display.plot()

plt.title("Iris Flower Classification - Confusion Matrix")
plt.tight_layout()
plt.show()


# ============================================================
# STEP 9: PREDICT A NEW FLOWER
# ============================================================

print("\n" + "=" * 60)
print("8. PREDICT A NEW FLOWER")
print("=" * 60)

# Example flower measurements in centimetres:
# [sepal length, sepal width, petal length, petal width]

new_flower = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=iris.feature_names
)

# Predict the flower species
prediction = model.predict(new_flower)

predicted_species = iris.target_names[prediction[0]]

# Display the measurements and prediction
print("\nNew flower measurements:")
print(new_flower.to_string(index=False))

print(f"\nPredicted flower species: {predicted_species}")

# Display prediction probabilities
probabilities = model.predict_proba(new_flower)[0]

print("\nModel prediction probabilities:")

for species, probability in zip(iris.target_names, probabilities):
    print(f"{species}: {probability * 100:.2f}%")


# ============================================================
# PROJECT COMPLETED
# ============================================================

print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 60)
