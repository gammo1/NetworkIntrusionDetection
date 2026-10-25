
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Network Intrusion Detection System")
st.write("Upload network-flow data to detect potentially malicious traffic.")

MODEL_PATH = Path(__file__).parent / "models/hist_gradient_boosting_ids.joblib"



saved = joblib.load(MODEL_PATH)
model = saved["model"]
feature_names = saved["feature_names"]
training_medians = pd.Series(saved["training_medians"])

uploaded_file = st.file_uploader(
    "Upload a CSV file containing network-flow features",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    missing = [col for col in feature_names if col not in df.columns]

    if missing:
        st.error(f"Missing required features: {missing[:10]}")
    else:
        X_input = df[feature_names].apply(
            pd.to_numeric, errors="coerce"
        )
        X_input = X_input.replace([float("inf"), -float("inf")], float("nan"))

        # Use training-data medians as a fallback for missing values.
        # For best consistency, we will save these medians in the next step.
        X_input = X_input.fillna(training_medians)

        predictions = model.predict(X_input)
        probabilities = model.predict_proba(X_input)[:, 1]

        results = df.copy()
        results["Prediction"] = [
            "Attack" if p == 1 else "Benign" for p in predictions
        ]
        results["Attack Probability"] = probabilities.round(4)

        c1, c2 = st.columns(2)
        c1.metric("Flows analyzed", len(results))
        c2.metric("Flows flagged as attacks", int((predictions == 1).sum()))

        st.subheader("Prediction Results")
        st.dataframe(results.head(100), use_container_width=True)

        st.download_button(
            "Download all results",
            data=results.to_csv(index=False).encode("utf-8"),
            file_name="intrusion_predictions.csv",
            mime="text/csv"
        )
