# 🧠 AI-Powered Real-Time Trading System for BankNifty (M.Tech Project)

## 📌 Overview

This project implements a **fully automated, real-time trading system** for **BankNifty options**, using **machine learning (XGBoost)** and **live broker API execution (ICICI Breeze)**. Designed as an institutional-grade system, it integrates predictive modeling, risk controls, journaling, and Telegram notifications — enabling disciplined, scalable intraday trading in the Indian derivatives market.

> 🧘‍♂️ *Built with discipline, logic, and surrender to Mahavatar Babaji’s divine plan.*

---

## 🧩 Key Components

| Module | Description |
|--------|-------------|
| 🧠 ML Model | XGBoost classifier trained on 10+ years of BankNifty futures data |
| 🏗 Feature Set | 37 custom features (VWAP, Renko, OI Delta, candle structure, volatility spikes) |
| ⚙️ Execution API | Trade execution via ICICI Breeze API (long/short with SL/TP) |
| 📈 Data Feed | 1-minute live OHLCV + OI from TrueData API |
| 🧾 Risk System | Fixed SL/TP (3R), daily loss limit, cooldown, duplicate direction block |
| 🧠 Confidence Filter | Prediction filtered at `confidence ≥ 0.6` |
| 📊 Journaling | Logs each trade with direction, entry/exit, P&L, confidence, reason |
| 📩 Telegram | Sends real-time entry & exit alerts via Telegram Bot |

---

## 🛠 Technologies Used

- **Language**: Python 3.11+  
- **ML Framework**: XGBoost  
- **Libraries**: Pandas, NumPy, Matplotlib, Scikit-learn  
- **APIs**:  
  - Market Data: TrueData API  
  - Order Execution: ICICI Breeze Connect API  
  - Alerts: Telegram Bot API  

---

## 🔬 Feature Engineering Highlights

- **Price Action**: wick size, body size, candle type  
- **Trend Analysis**: Renko trend, EMA slope, MACD histograms  
- **Volume/OI Dynamics**: volume spikes, OI divergence, CVD  
- **VWAP Metrics**: vwap distance, support/resistance zones  
- **Time Filters**: alpha hours, no-trade zone flags

> ✨ Features aligned using `feature_order.pkl` to ensure schema consistency.

---

## 🧪 Model Training

- **Model**: XGBoost Classifier (`binary:logistic`)  
- **Labeling**: Binary (1 = TP hit before SL; 0 = otherwise) using **3R risk-reward logic**  
- **Target = +0.75%**, **SL = -0.25%**  
- **ROC-AUC (test set)**: `0.7285`  
- **Offline Win Rate**: ~88.5% (on 114 backtested trades)  
- **Live Accuracy**: `60.54%` (paper/live trades)

---

## 📡 Live Trading Pipeline

```plaintext
[Live OHLCV via TrueData] → [Feature Generator] → [Model Prediction]
→ [Confidence Filter ≥ 0.6?] → [Risk Rules]
→ [Order Execution via Breeze API] → [Trade Monitoring]
→ [Exit Logic: TP / SL / Manual] → [Journal + Telegram Alert]



📊 Sample Trade Journal Entry
Time	Dir	Entry	Exit	Conf	Result	Reason	P&L
09:15 AM	LONG	42,350	42,668	0.72	Target	TP Hit	₹318
11:20 AM	SHORT	92.40	90.12	0.68	Target	TP Hit	₹684
13:05 PM	LONG	110.0	108.3	0.71	Stoploss	SL Hit	–₹510

🧭 Future Roadmap
🔄 Trailing SL / Partial Exits

🧠 SHAP-based explainability for predictions

🪙 Multi-Asset Expansion (BTCUSDT, Nifty, Gold)

🎮 Reinforcement Learning (RL agent for signal refinement)

🕸️ Websocket streaming (for low-latency setups)



👤 Author:
Aneesh V R
📍 Thiruvananthapuram, Kerala, India
🎓 M.Tech – Translational Engineering, Govt. Engineering College Barton Hill
🔗 LinkedIn | 🌐 GitHub

