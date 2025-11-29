import joblib
import numpy as np

model = joblib.load("model/rf_crypto_model.pkl")

feature_order = [
    "total_vol", "price", "volume_24h", "change_7d", "marketcap",
    "price_to_mc", "vol_to_mc", "vol_to_price", "log_price", "log_vol",
    "log_marketcap", "abs_change_7d", "diff_change", "name_encodedr", "symbol_encoder"
]

def predict_crypto(data):
    row = np.array([[data[feat] for feat in feature_order]])

    pred = model.predict(row)[0]
    prob = model.predict_proba(row)[0]

    return {
        "prediction": int(pred),
        "probability_down": float(prob[0]),
        "probability_up": float(prob[1])
    }
