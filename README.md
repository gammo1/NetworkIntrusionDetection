# Network Intrusion Detection System

A machine-learning-based Network Intrusion Detection System (NIDS) that classifies network flows as **Benign** or **Attack** using the CIC-IDS2017 dataset. The project includes a Streamlit dashboard for uploading CSV files, analyzing network-flow records, viewing predictions, and downloading results.

## Features

- Upload CSV files containing network-flow features.
- Classify flows as benign or potential attacks.
- Display attack predictions and attack probabilities.
- View prediction results in the dashboard.
- Download analyzed results as a CSV file.
- Compare multiple machine-learning models using evaluation metrics.

## Machine Learning Models

Three classification algorithms were evaluated using the same cleaned train/test split.

1. **Logistic Regression** — baseline classification model.
2. **Random Forest** — ensemble model using multiple decision trees.
3. **HistGradientBoosting** — gradient-boosting model selected for the dashboard.

### Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 92.51% | 77.45% | 98.17% | 86.59% |
| Random Forest | 99.70% | 99.35% | 99.44% | 99.40% |
| HistGradientBoosting | 99.73% | 99.34% | 99.54% | 99.44% |

HistGradientBoosting was selected because it achieved the highest accuracy, recall, and F1-score among the three evaluated models, while training in approximately 10 seconds.

For intrusion detection, recall is especially important because a false negative means an attack was not detected. Precision is also important because false alarms can cause unnecessary investigation.

*Note: Training times are specific to the environment in which the experiments were run.*

## Dataset

This project uses the **CIC-IDS2017** dataset, which contains benign network traffic and multiple types of attacks.

Attack categories represented in the source data include:

- DDoS
- DoS
- Brute-force attacks
- Port scanning
- Botnet traffic
- Web attacks
- Infiltration
- Heartbleed

The trained model uses 77 numeric network-flow features. The dashboard expects uploaded CSV files to contain compatible feature columns.

Dataset source: [CIC-IDS2017 — Canadian Institute for Cybersecurity](https://www.unb.ca/cic/datasets/ids-2017.html)


## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- Joblib
- Streamlit
- PyArrow
- CIC-IDS2017 dataset


###  Run the dashboard


streamlit run app.py

Open the local URL displayed in the terminal, upload a compatible CSV file, and review the predictions.


## Future Improvements

- Test against additional datasets and unseen attack types.
- Improve probability calibration and threshold selection.
- Add more detailed visualizations and downloadable evaluation reports.
- Investigate explainability methods to help users understand predictions.

