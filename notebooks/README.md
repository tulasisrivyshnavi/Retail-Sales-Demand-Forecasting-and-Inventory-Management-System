# notebooks/

This folder will contain the Jupyter notebook built in Phase 2.

**File:**  `demand_forecasting.ipynb`

**Contents (Phase 2):**
1. Load and inspect the cleaned dataset
2. Time-based train/test split (80/20 by Date)
3. Fix target leakage — remove post-sale columns
4. Baseline models (mean, category mean)
5. Random Forest and XGBoost with TimeSeriesSplit CV
6. Leakage proof (shuffle target, retrain)
7. Evaluation: MAE, RMSE, R², WAPE — no hand-typed numbers
8. Actual vs predicted plot, residuals, feature importance
9. Optional: ARIMA, Prophet, LSTM on daily aggregated series

**Run with:**
```
..\venv\Scripts\jupyter lab
```
