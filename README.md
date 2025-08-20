# ⚽ Football Match Prediction with Elo, H2H, and CatBoost  

## 📌 Overview  
This project predicts outcomes of football matches (**Home Win / Draw / Away Win**) using a **machine learning pipeline** built around:  

- **Elo Ratings** – base measure of team strength.  
- **Home & Away Win Percentages** – converted into Elo adjustments.  
- **Head-to-Head (H2H) Index** – captures historical matchup tendencies.  
- **CatBoost Classifier** – primary predictive model, with ensemble comparisons.  
- **Evaluation Metrics** – accuracy, log loss, calibration, and averaged points tables.  

The final outputs are:  
- **Predicted match results** (probabilities + labels).  
- **Simulated league table** (points aggregated across fixtures).  


---


## ⚙️ Data & Features  

### Input Data  
- **Elo Ratings** for each team.  
- **Home win %** at home grounds.  
- **Away win %** at away grounds.  
- **Fixture list** (Home vs Away teams, season schedule).  
- **Match results** (for supervised training).  

### Feature Engineering  
- **Adjusted Elo Difference**  
  - Base formula:  
    ```
    adj_home_elo = home_elo + (home_win_pct * scaling_factor)
    adj_away_elo = away_elo + (away_win_pct * scaling_factor)
    elo_diff = adj_home_elo - adj_away_elo
    ```
  - Scaling factor (~130 Elo points) derived from historical **Home Field Advantage** ranges.  
- **Head-to-Head (H2H) Index**  
  - Encodes historical matchup tendency.  
- **Final Features**  
  - `elo_diff`, `h2h_index`  

---

## 🧠 Modeling  

### Algorithms Tried  
- **CatBoostClassifier** (primary model)  
  - Handles categorical features natively  
  - Class imbalance addressed via:  
    - **Inverse class weights**
    - 
- **RandomForestClassifier** (baseline ensemble)  
- **Ensemble Averaging** of multiple CatBoost variants  

### Training Setup  
- **Train/Test Split** (hold-out ~20%)  
- **Cross-validation** (KFold / StratifiedKFold for imbalance)  
- **Class Weights**: computed inversely to class frequency  
- **Evaluation Metrics**:  
  - Accuracy  
  - Log Loss  
  - Calibration curves  

---

## 📊 Outputs  

1. **Match Predictions**  
   - Probability of Home/Draw/Away  
   - Predicted class  

2. **League Table Simulation**  
   - Assigns points (3/1/0) per predicted result  
   - Builds season standings  
   - Supports **averaging across models** for robustness  

3. **Model Evaluation**  
   - Accuracy (~0.44 baseline)  
   - Log loss (~1.02 vs baseline ~1.10)  

---
## Results

# Premier League 2025/26 Final Table

| Pos | Team           | Points | Elo    |
|-----|---------------|--------|--------|
| 1   | Arsenal        | 94     | 2060.7 |
| 2   | Man City       | 91     | 2030.1 |
| 3   | Liverpool      | 88     | 2012.9 |
| 4   | Newcastle Utd  | 75     | 1916.5 |
| 5   | Aston Villa    | 69     | 1913.5 |
| 6   | Chelsea        | 60     | 1871.8 |
| 7   | Man Utd        | 55     | 1814.3 |
| 8   | Tottenham      | 52     | 1773.6 |
| 9   | Everton        | 52     | 1786.6 |
| 10  | Brighton       | 51     | 1806.1 |
| 11  | West Ham       | 49     | 1776.6 |
| 12  | Nottm Forest   | 49     | 1791.9 |
| 13  | Fulham         | 47     | 1771.5 |
| 14  | Crystal Palace | 46     | 1795.1 |
| 15  | Bournemouth    | 44     | 1761.5 |
| 16  | Brentford      | 41     | 1771.4 |
| 17  | Burnley        | 41     | 1730.2 |
| 18  | Wolves         | 35     | 1704.6 |
| 19  | Leeds          | 27     | 1663.6 |
| 20  | Sunderland     | 19     | 1556.6 |

---
## Limitations

- ELO rating does not indicate the strengthening by transfer policy
- Lack of previous ELO data led to generation of syntehtic data for training
 
