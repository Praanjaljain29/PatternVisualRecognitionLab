# Lab 2: Regression vs Classification (Drug200 and MNIST)

## Objective
Compare linear-regression and logistic-regression behavior for classification-focused tasks.

## Files
- `lab2.ipynb`: Drug200 dataset experiment with linear vs logistic regression and ROC analysis.
- `lab2_mnist.ipynb`: MNIST binary setup (`0` vs `non-0`) with regression/classification metrics.
- `mnist_lab2.ipynb`: additional MNIST-focused lab variant.
- `drug200.csv`: dataset used in `lab2.ipynb`.

## Workflow Summary
### Part A: Drug200 (`lab2.ipynb`)
- Encode categorical features and target labels.
- Split train/test data.
- Train a linear-regression pipeline (used as approximate classifier).
- Train multinomial logistic regression.
- Compare metrics: accuracy, precision, recall, AUC, ROC curves.

### Part B: MNIST (`lab2_mnist.ipynb` and `mnist_lab2.ipynb`)
- Load MNIST CSV data.
- Convert targets to binary class (`digit 0` vs others).
- Train linear regression and logistic regression.
- Report MSE, R2, correlation, and classification metrics.

## Output
- Regression and classification performance comparison.
- ROC and metric-based interpretation for multi-class and binary settings.

## How to Run
Open each notebook and run all cells in order:
1. `lab2.ipynb`
2. `lab2_mnist.ipynb`
3. `mnist_lab2.ipynb`
