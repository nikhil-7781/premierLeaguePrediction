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

Match: Liverpool (1993.0) vs Bournemouth  (1808.0), Result: H
Match: Aston Villa (1873.0) vs Newcastle Utd (1869.0), Result: D
Match: Brighton (1827.0) vs Fulham (1782.0), Result: H
Match: Sunderland (1547.0) vs West Ham (1750.0), Result: A
Match: Tottenham  (1774.0) vs Burnley (1730.0), Result: H
Match: Wolves (1736.0) vs Man City (1960.0), Result: A
Match: Nottm Forest (1803.0) vs Brentford (1811.0), Result: D
Match: Chelsea (1903.0) vs Crystal Palace (1835.0), Result: H
Match: Man Utd (1799.0) vs Arsenal  (1993.0), Result: A
Match: Leeds (1722.0) vs Everton (1794.0), Result: D
Match: West Ham (1754.7) vs Chelsea (1911.1), Result: A
Match: Man City (1964.3) vs Tottenham  (1782.7), Result: H
Match: Bournemouth  (1802.9) vs Wolves (1731.7), Result: H
Match: Brentford (1810.8) vs Aston Villa (1872.9), Result: A
Match: Burnley (1721.3) vs Sunderland (1542.3), Result: H
Match: Arsenal  (1997.9) vs Leeds (1724.0), Result: H
Match: Crystal Palace (1826.9) vs Nottm Forest (1803.2), Result: D
Match: Everton (1792.0) vs Brighton (1835.7), Result: D
Match: Fulham (1773.3) vs Man Utd (1794.1), Result: H
Match: Newcastle Utd (1869.1) vs Liverpool (1998.1), Result: A
Match: Chelsea (1916.8) vs Fulham (1783.9), Result: H
Match: Man Utd (1783.5) vs Burnley (1726.5), Result: H
Match: Sunderland (1537.0) vs Brentford (1802.5), Result: A
Match: Tottenham  (1777.5) vs Bournemouth  (1810.9), Result: H
Match: Wolves (1723.7) vs Everton (1793.2), Result: H
Match: Leeds (1720.6) vs Newcastle Utd (1862.7), Result: D
Match: Brighton (1834.5) vs Man City (1969.5), Result: A
Match: Nottm Forest (1803.9) vs West Ham (1749.0), Result: H
Match: Liverpool (2004.6) vs Arsenal  (2001.4), Result: D
Match: Aston Villa (1881.1) vs Crystal Palace (1826.3), Result: H
Match: Arsenal  (2001.5) vs Nottm Forest (1812.3), Result: H
Match: Bournemouth  (1799.9) vs Brighton (1828.2), Result: H
Match: Crystal Palace (1817.8) vs Sunderland (1533.4), Result: H
Match: Everton (1781.2) vs Aston Villa (1889.5), Result: D
Match: Fulham (1777.5) vs Leeds (1724.5), Result: H
Match: Newcastle Utd (1858.8) vs Wolves (1735.7), Result: H
Match: West Ham (1740.5) vs Tottenham  (1788.5), Result: D
Match: Brentford (1806.1) vs Chelsea (1923.2), Result: D
Match: Burnley (1718.1) vs Liverpool (2004.5), Result: A
Match: Man City (1975.8) vs Man Utd (1791.8), Result: D
Match: Liverpool (2007.7) vs Everton (1784.3), Result: H
Match: Bournemouth  (1810.7) vs Newcastle Utd (1865.4), Result: D
Match: Brighton (1817.4) vs Tottenham  (1787.1), Result: H
Match: Burnley (1714.9) vs Nottm Forest (1807.3), Result: H
Match: West Ham (1741.9) vs Crystal Palace (1821.1), Result: D
Match: Wolves (1729.1) vs Leeds (1716.0), Result: D
Match: Man Utd (1796.7) vs Chelsea (1920.0), Result: H
Match: Fulham (1786.0) vs Brentford (1809.4), Result: H
Match: Sunderland (1530.2) vs Aston Villa (1886.5), Result: A
Match: Arsenal  (2006.5) vs Man City (1971.0), Result: D
Match: Brentford (1798.7) vs Man Utd (1810.1), Result: D
Match: Aston Villa (1888.8) vs Fulham (1796.7), Result: H
Match: Chelsea (1906.5) vs Brighton (1826.5), Result: H
Match: Crystal Palace (1818.8) vs Liverpool (2012.0), Result: A
Match: Leeds (1716.4) vs Bournemouth  (1812.3), Result: H
Match: Man City (1972.0) vs Burnley (1727.5), Result: H
Match: Nottm Forest (1794.7) vs Sunderland (1527.9), Result: H
Match: Tottenham  (1778.0) vs Wolves (1728.7), Result: H
Match: Newcastle Utd (1863.8) vs Arsenal  (2005.5), Result: H
Match: Everton (1779.9) vs West Ham (1744.1), Result: D
Match: Arsenal  (1991.6) vs West Ham (1745.2), Result: H
Match: Aston Villa (1896.2) vs Burnley (1723.6), Result: H
Match: Bournemouth  (1799.6) vs Fulham (1789.3), Result: H
Match: Brentford (1799.0) vs Man City (1975.9), Result: A
Match: Chelsea (1914.3) vs Liverpool (2017.0), Result: D
Match: Everton (1778.9) vs Crystal Palace (1813.9), Result: H
Match: Leeds (1729.1) vs Tottenham  (1786.6), Result: A
Match: Man Utd (1809.8) vs Sunderland (1524.4), Result: H
Match: Newcastle Utd (1877.7) vs Nottm Forest (1798.2), Result: H
Match: Wolves (1720.1) vs Brighton (1818.7), Result: D
Match: Brighton (1816.0) vs Newcastle Utd (1885.4), Result: H
Match: Burnley (1718.2) vs Leeds (1720.7), Result: H
Match: Crystal Palace (1802.9) vs Bournemouth  (1809.3), Result: D
Match: Fulham (1779.6) vs Arsenal  (1995.5), Result: A
Match: Liverpool (2014.1) vs Man Utd (1813.0), Result: H
Match: Man City (1981.2) vs Everton (1789.9), Result: H
Match: Nottm Forest (1790.5) vs Chelsea (1917.2), Result: D
Match: Sunderland (1521.1) vs Wolves (1722.9), Result: D
Match: Tottenham  (1794.9) vs Aston Villa (1901.6), Result: A
Match: West Ham (1741.3) vs Brentford (1793.7), Result: D
Match: Arsenal  (2000.0) vs Crystal Palace (1803.1), Result: H
Match: Aston Villa (1908.6) vs Man City (1986.2), Result: D
Match: Bournemouth  (1809.1) vs Nottm Forest (1794.0), Result: H
Match: Brentford (1792.2) vs Liverpool (2018.9), Result: A
Match: Chelsea (1913.7) vs Sunderland (1526.3), Result: H
Match: Everton (1784.9) vs Tottenham  (1787.9), Result: H
Match: Leeds (1710.6) vs West Ham (1742.8), Result: H
Match: Man Utd (1808.2) vs Brighton (1828.0), Result: H
Match: Newcastle Utd (1873.5) vs Fulham (1775.1), Result: H
Match: Wolves (1717.6) vs Burnley (1728.3), Result: H
Match: Brighton (1817.4) vs Leeds (1721.6), Result: H
Match: Burnley (1717.9) vs Arsenal  (2004.9), Result: A
Match: Crystal Palace (1798.2) vs Brentford (1787.9), Result: D
Match: Fulham (1767.9) vs Wolves (1728.0), Result: D
Match: Liverpool (2023.2) vs Aston Villa (1910.8), Result: H
Match: Man City (1984.0) vs Bournemouth  (1818.7), Result: H
Match: Nottm Forest (1784.4) vs Man Utd (1818.8), Result: H
Match: Sunderland (1524.4) vs Everton (1795.0), Result: A
Match: Tottenham  (1777.8) vs Chelsea (1915.6), Result: A
Match: West Ham (1731.8) vs Newcastle Utd (1880.7), Result: A
Match: Aston Villa (1904.0) vs Bournemouth  (1813.1), Result: H
Match: Brentford (1788.2) vs Newcastle Utd (1886.7), Result: A
Match: Chelsea (1921.8) vs Wolves (1729.1), Result: D
Match: Crystal Palace (1797.9) vs Brighton (1824.7), Result: H
Match: Everton (1798.5) vs Fulham (1766.7), Result: D
Match: Man City (1989.6) vs Liverpool (2030.0), Result: D
Match: Nottm Forest (1795.4) vs Leeds (1714.3), Result: H
Match: Sunderland (1520.9) vs Arsenal  (2008.1), Result: H
Match: Tottenham  (1771.6) vs Man Utd (1807.8), Result: H
Match: West Ham (1725.9) vs Burnley (1714.7), Result: H
Match: Arsenal  (1989.2) vs Tottenham  (1782.6), Result: H
Match: Bournemouth  (1805.6) vs West Ham (1735.6), Result: D
Match: Brighton (1813.9) vs Brentford (1781.0), Result: D
Match: Burnley (1705.1) vs Chelsea (1916.8), Result: A
Match: Fulham (1767.6) vs Sunderland (1539.8), Result: H
Match: Leeds (1706.5) vs Aston Villa (1911.4), Result: A
Match: Liverpool (2028.9) vs Nottm Forest (1803.1), Result: H
Match: Man Utd (1796.8) vs Everton (1797.6), Result: H
Match: Newcastle Utd (1893.9) vs Man City (1990.8), Result: D
Match: Wolves (1734.1) vs Crystal Palace (1808.7), Result: A
Match: Aston Villa (1916.1) vs Wolves (1726.2), Result: D
Match: Brentford (1781.9) vs Burnley (1700.5), Result: H
Match: Chelsea (1921.4) vs Arsenal  (1993.9), Result: A
Match: Crystal Palace (1816.6) vs Man Utd (1806.8), Result: H
Match: Everton (1787.5) vs Newcastle Utd (1896.6), Result: H
Match: Man City (1988.0) vs Leeds (1701.8), Result: H
Match: Nottm Forest (1798.8) vs Brighton (1813.0), Result: D
Match: Sunderland (1535.5) vs Bournemouth  (1803.7), Result: A
Match: Tottenham  (1778.0) vs Fulham (1771.9), Result: H
Match: West Ham (1737.6) vs Liverpool (2033.2), Result: A
Match: Arsenal  (2001.8) vs Brentford (1789.6), Result: H
Match: Bournemouth  (1807.2) vs Everton (1800.6), Result: H
Match: Brighton (1812.6) vs Aston Villa (1911.1), Result: H
Match: Burnley (1692.8) vs Crystal Palace (1826.3), Result: H
Match: Fulham (1762.0) vs Man City (1991.3), Result: A
Match: Leeds (1698.6) vs Chelsea (1913.4), Result: A
Match: Liverpool (2036.3) vs Sunderland (1532.0), Result: H
Match: Man Utd (1797.1) vs West Ham (1734.5), Result: D
Match: Newcastle Utd (1883.6) vs Tottenham  (1787.8), Result: H
Match: Wolves (1731.2) vs Nottm Forest (1799.2), Result: D
Match: Aston Villa (1898.4) vs Arsenal  (2006.4), Result: A
Match: Bournemouth  (1817.0) vs Chelsea (1917.9), Result: A
Match: Brighton (1825.3) vs West Ham (1736.3), Result: H
Match: Everton (1790.8) vs Nottm Forest (1797.3), Result: H
Match: Fulham (1757.8) vs Crystal Palace (1812.6), Result: D
Match: Leeds (1694.1) vs Liverpool (2037.3), Result: A
Match: Man City (1995.5) vs Sunderland (1531.0), Result: H
Match: Newcastle Utd (1890.9) vs Burnley (1706.5), Result: H
Match: Tottenham  (1780.5) vs Brentford (1785.1), Result: H
Match: Wolves (1733.2) vs Man Utd (1795.3), Result: A
Match: Arsenal  (2013.4) vs Wolves (1724.9), Result: H
Match: Brentford (1774.9) vs Leeds (1691.7), Result: H
Match: Burnley (1701.3) vs Fulham (1759.4), Result: H
Match: Chelsea (1925.1) vs Everton (1801.0), Result: H
Match: Crystal Palace (1811.0) vs Man City (1996.8), Result: A
Match: Liverpool (2039.7) vs Brighton (1832.8), Result: H
Match: Man Utd (1803.5) vs Bournemouth  (1809.8), Result: H
Match: Nottm Forest (1787.1) vs Tottenham  (1790.6), Result: D
Match: Sunderland (1529.7) vs Newcastle Utd (1896.0), Result: A
Match: West Ham (1728.8) vs Aston Villa (1891.4), Result: A
Match: Aston Villa (1897.0) vs Man Utd (1813.7), Result: H
Match: Bournemouth  (1799.6) vs Burnley (1713.0), Result: H
Match: Brighton (1828.2) vs Sunderland (1527.5), Result: H
Match: Everton (1794.4) vs Arsenal  (2016.6), Result: A
Match: Fulham (1747.7) vs Nottm Forest (1787.2), Result: H
Match: Leeds (1684.0) vs Crystal Palace (1805.9), Result: H
Match: Man City (2001.9) vs West Ham (1723.1), Result: H
Match: Newcastle Utd (1898.2) vs Chelsea (1931.7), Result: H
Match: Tottenham  (1790.5) vs Liverpool (2044.4), Result: A
Match: Wolves (1721.7) vs Brentford (1782.6), Result: H
Match: Arsenal  (2020.9) vs Brighton (1831.2), Result: H
Match: Brentford (1770.9) vs Bournemouth  (1807.2), Result: H
Match: Burnley (1705.4) vs Everton (1790.0), Result: A
Match: Chelsea (1920.7) vs Aston Villa (1904.7), Result: D
Match: Crystal Palace (1792.6) vs Tottenham  (1786.8), Result: D
Match: Liverpool (2048.2) vs Wolves (1733.5), Result: H
Match: Man Utd (1806.1) vs Newcastle Utd (1909.2), Result: A
Match: Nottm Forest (1776.1) vs Man City (2005.2), Result: A
Match: Sunderland (1524.5) vs Leeds (1697.4), Result: A
Match: West Ham (1719.8) vs Fulham (1758.9), Result: D
Match: Arsenal  (2025.9) vs Aston Villa (1905.1), Result: H
Match: Brentford (1781.9) vs Tottenham  (1786.9), Result: D
Match: Burnley (1697.8) vs Newcastle Utd (1916.3), Result: A
Match: Chelsea (1920.2) vs Bournemouth  (1796.1), Result: H
Match: Crystal Palace (1792.4) vs Fulham (1757.7), Result: H
Match: Liverpool (2051.0) vs Leeds (1702.8), Result: H
Match: Man Utd (1798.9) vs Wolves (1730.7), Result: H
Match: Nottm Forest (1771.9) vs Everton (1797.6), Result: H
Match: Sunderland (1519.1) vs Man City (2009.4), Result: H
Match: West Ham (1720.9) vs Brighton (1826.2), Result: D
Match: Aston Villa (1898.5) vs Nottm Forest (1782.6), Result: H
Match: Bournemouth  (1789.6) vs Arsenal  (2032.6), Result: A
Match: Brighton (1823.2) vs Burnley (1693.4), Result: H
Match: Everton (1786.9) vs Brentford (1782.0), Result: H
Match: Fulham (1748.7) vs Liverpool (2053.3), Result: A
Match: Leeds (1700.4) vs Man Utd (1807.0), Result: A
Match: Man City (1990.6) vs Chelsea (1926.8), Result: H
Match: Newcastle Utd (1920.7) vs Crystal Palace (1801.4), Result: D
Match: Tottenham  (1786.8) vs Sunderland (1538.0), Result: H
Match: Wolves (1722.6) vs West Ham (1723.8), Result: H
Match: Arsenal  (2036.6) vs Liverpool (2056.3), Result: D
Match: Bournemouth  (1785.6) vs Tottenham  (1790.6), Result: D
Match: Brentford (1772.2) vs Sunderland (1534.1), Result: H
Match: Burnley (1686.9) vs Man Utd (1814.0), Result: A
Match: Crystal Palace (1804.7) vs Aston Villa (1905.3), Result: H
Match: Everton (1796.8) vs Wolves (1732.6), Result: D
Match: Fulham (1745.8) vs Chelsea (1918.6), Result: A
Match: Man City (1998.8) vs Brighton (1829.6), Result: H
Match: Newcastle Utd (1917.4) vs Leeds (1693.4), Result: D
Match: West Ham (1713.8) vs Nottm Forest (1775.8), Result: A
Match: Aston Villa (1892.4) vs Everton (1794.9), Result: H
Match: Brighton (1824.2) vs Bournemouth  (1785.8), Result: H
Match: Chelsea (1924.0) vs Brentford (1776.2), Result: D
Match: Leeds (1699.1) vs Fulham (1740.4), Result: D
Match: Liverpool (2055.7) vs Burnley (1680.5), Result: H
Match: Man Utd (1820.5) vs Man City (2004.2), Result: D
Match: Nottm Forest (1784.1) vs Arsenal  (2037.1), Result: A
Match: Sunderland (1530.1) vs Crystal Palace (1817.5), Result: A
Match: Tottenham  (1790.5) vs West Ham (1705.6), Result: D
Match: Wolves (1734.5) vs Newcastle Utd (1911.7), Result: A
Match: Arsenal  (2040.9) vs Man Utd (1825.4), Result: H
Match: Bournemouth  (1776.9) vs Liverpool (2057.8), Result: A
Match: Brentford (1780.3) vs Nottm Forest (1780.3), Result: D
Match: Burnley (1678.4) vs Tottenham  (1788.1), Result: A
Match: Crystal Palace (1820.7) vs Chelsea (1920.0), Result: D
Match: Everton (1787.7) vs Leeds (1700.3), Result: H
Match: Fulham (1739.2) vs Brighton (1833.1), Result: H
Match: Man City (1999.4) vs Wolves (1729.2), Result: H
Match: Newcastle Utd (1917.0) vs Aston Villa (1899.7), Result: D
Match: West Ham (1708.0) vs Sunderland (1526.9), Result: H
Match: Aston Villa (1900.2) vs Brentford (1780.3), Result: H
Match: Brighton (1820.4) vs Everton (1795.2), Result: D
Match: Chelsea (1917.2) vs West Ham (1713.2), Result: H
Match: Leeds (1692.7) vs Arsenal  (2045.4), Result: A
Match: Liverpool (2061.1) vs Newcastle Utd (1916.5), Result: H
Match: Man Utd (1820.9) vs Fulham (1751.8), Result: H
Match: Nottm Forest (1780.3) vs Crystal Palace (1823.5), Result: H
Match: Sunderland (1521.7) vs Burnley (1671.4), Result: D
Match: Tottenham  (1795.0) vs Man City (2002.9), Result: A
Match: Wolves (1725.7) vs Bournemouth  (1773.5), Result: D
Match: Arsenal  (2047.7) vs Sunderland (1525.7), Result: H
Match: Bournemouth  (1772.2) vs Aston Villa (1906.9), Result: A
Match: Brighton (1819.7) vs Crystal Palace (1812.3), Result: H
Match: Burnley (1667.4) vs West Ham (1708.5), Result: H
Match: Fulham (1743.8) vs Everton (1795.9), Result: H
Match: Leeds (1690.4) vs Nottm Forest (1791.5), Result: D
Match: Liverpool (2067.2) vs Man City (2007.5), Result: D
Match: Man Utd (1828.9) vs Tottenham  (1790.4), Result: H
Match: Newcastle Utd (1910.5) vs Brentford (1773.6), Result: H
Match: Wolves (1727.0) vs Chelsea (1921.9), Result: D
Match: Aston Villa (1913.2) vs Brighton (1829.5), Result: H
Match: Brentford (1767.3) vs Arsenal  (2048.7), Result: A
Match: Chelsea (1916.9) vs Leeds (1693.2), Result: H
Match: Crystal Palace (1802.5) vs Burnley (1678.6), Result: H
Match: Everton (1784.4) vs Bournemouth  (1765.9), Result: H
Match: Man City (2009.2) vs Fulham (1755.3), Result: H
Match: Nottm Forest (1788.7) vs Wolves (1732.1), Result: H
Match: Sunderland (1524.8) vs Liverpool (2065.5), Result: H
Match: Tottenham  (1781.5) vs Newcastle Utd (1916.7), Result: D
Match: West Ham (1697.3) vs Man Utd (1837.8), Result: H
Match: Aston Villa (1920.8) vs Leeds (1688.9), Result: H
Match: Brentford (1764.0) vs Brighton (1821.8), Result: H
Match: Chelsea (1921.2) vs Burnley (1672.0), Result: H
Match: Crystal Palace (1809.1) vs Wolves (1723.7), Result: H
Match: Everton (1793.9) vs Man Utd (1824.0), Result: H
Match: Man City (2013.0) vs Newcastle Utd (1913.0), Result: H
Match: Nottm Forest (1797.1) vs Liverpool (2046.3), Result: A
Match: Sunderland (1543.9) vs Fulham (1751.5), Result: A
Match: Tottenham  (1785.2) vs Arsenal  (2052.0), Result: A
Match: West Ham (1711.1) vs Bournemouth  (1756.4), Result: H
Match: Arsenal  (2055.5) vs Chelsea (1925.0), Result: H
Match: Bournemouth  (1745.1) vs Sunderland (1539.3), Result: H
Match: Brighton (1810.2) vs Nottm Forest (1793.2), Result: D
Match: Burnley (1668.1) vs Brentford (1775.7), Result: H
Match: Fulham (1756.2) vs Tottenham  (1781.7), Result: H
Match: Leeds (1684.7) vs Man City (2020.2), Result: A
Match: Liverpool (2050.2) vs West Ham (1722.4), Result: H
Match: Man Utd (1813.1) vs Crystal Palace (1816.7), Result: D
Match: Newcastle Utd (1905.8) vs Everton (1804.8), Result: H
Match: Wolves (1716.2) vs Aston Villa (1925.0), Result: H
Match: Aston Villa (1909.6) vs Chelsea (1918.6), Result: D
Match: Bournemouth  (1749.8) vs Brentford (1762.7), Result: H
Match: Brighton (1809.7) vs Arsenal  (2061.9), Result: A
Match: Everton (1797.6) vs Burnley (1681.1), Result: H
Match: Fulham (1766.9) vs West Ham (1719.8), Result: D
Match: Leeds (1682.2) vs Sunderland (1534.6), Result: H
Match: Man City (2022.7) vs Nottm Forest (1793.7), Result: H
Match: Newcastle Utd (1913.0) vs Man Utd (1813.2), Result: H
Match: Tottenham  (1770.9) vs Crystal Palace (1816.6), Result: H
Match: Wolves (1731.5) vs Liverpool (2052.8), Result: A
Match: Arsenal  (2065.7) vs Everton (1804.4), Result: H
Match: Brentford (1752.3) vs Wolves (1728.8), Result: H
Match: Burnley (1674.4) vs Bournemouth  (1760.2), Result: H
Match: Chelsea (1918.4) vs Newcastle Utd (1920.2), Result: D
Match: Crystal Palace (1805.3) vs Leeds (1688.2), Result: H
Match: Liverpool (2055.5) vs Tottenham  (1782.2), Result: H
Match: Man Utd (1806.0) vs Aston Villa (1909.9), Result: H
Match: Nottm Forest (1789.5) vs Fulham (1765.6), Result: H
Match: Sunderland (1528.6) vs Brighton (1805.9), Result: A
Match: West Ham (1721.1) vs Man City (2026.9), Result: A
Match: Aston Villa (1897.0) vs West Ham (1718.2), Result: H
Match: Bournemouth  (1747.7) vs Man Utd (1818.9), Result: H
Match: Brighton (1809.3) vs Liverpool (2059.0), Result: A
Match: Everton (1800.7) vs Chelsea (1918.4), Result: A
Match: Fulham (1756.2) vs Burnley (1686.8), Result: H
Match: Leeds (1681.4) vs Brentford (1761.6), Result: D
Match: Man City (2029.9) vs Crystal Palace (1812.0), Result: H
Match: Newcastle Utd (1920.1) vs Sunderland (1525.2), Result: H
Match: Tottenham  (1778.8) vs Nottm Forest (1798.8), Result: D
Match: Wolves (1719.5) vs Arsenal  (2069.3), Result: A
Match: Arsenal  (2071.7) vs Bournemouth  (1759.8), Result: H
Match: Brentford (1759.4) vs Everton (1794.0), Result: H
Match: Burnley (1678.8) vs Brighton (1805.4), Result: H
Match: Chelsea (1925.2) vs Man City (2034.3), Result: A
Match: Crystal Palace (1807.6) vs Newcastle Utd (1922.0), Result: D
Match: Liverpool (2062.8) vs Fulham (1764.3), Result: H
Match: Man Utd (1806.9) vs Leeds (1683.7), Result: H
Match: Nottm Forest (1798.2) vs Aston Villa (1902.2), Result: D
Match: Sunderland (1523.4) vs Tottenham  (1779.4), Result: A
Match: West Ham (1712.9) vs Wolves (1717.1), Result: H
Match: Aston Villa (1899.3) vs Sunderland (1519.6), Result: H
Match: Brentford (1770.3) vs Fulham (1761.2), Result: D
Match: Chelsea (1918.2) vs Man Utd (1813.5), Result: H
Match: Crystal Palace (1810.7) vs West Ham (1723.1), Result: H
Match: Everton (1783.0) vs Liverpool (2065.8), Result: A
Match: Leeds (1677.1) vs Wolves (1707.0), Result: H
Match: Man City (2041.3) vs Arsenal  (2074.5), Result: D
Match: Newcastle Utd (1918.8) vs Bournemouth  (1756.9), Result: D
Match: Nottm Forest (1801.1) vs Burnley (1692.2), Result: H
Match: Tottenham  (1783.1) vs Brighton (1792.0), Result: D
Match: Arsenal  (2073.6) vs Newcastle Utd (1914.5), Result: H
Match: Bournemouth  (1761.3) vs Leeds (1688.0), Result: H
Match: Brighton (1791.7) vs Chelsea (1925.3), Result: D
Match: Burnley (1685.3) vs Man City (2042.2), Result: A
Match: Fulham (1761.5) vs Aston Villa (1901.3), Result: A
Match: Liverpool (2069.1) vs Crystal Palace (1818.3), Result: H
Match: Man Utd (1806.4) vs Brentford (1770.1), Result: H
Match: Sunderland (1517.6) vs Nottm Forest (1808.1), Result: H
Match: West Ham (1715.5) vs Everton (1779.7), Result: H
Match: Wolves (1696.2) vs Tottenham  (1783.4), Result: H
Match: Arsenal  (2079.3) vs Fulham (1755.3), Result: H
Match: Aston Villa (1907.5) vs Tottenham  (1770.9), Result: H
Match: Bournemouth  (1769.2) vs Crystal Palace (1814.5), Result: D
Match: Brentford (1761.1) vs West Ham (1727.4), Result: H
Match: Chelsea (1921.6) vs Nottm Forest (1791.3), Result: H
Match: Everton (1767.9) vs Man City (2044.5), Result: A
Match: Leeds (1680.1) vs Burnley (1683.0), Result: H
Match: Man Utd (1815.4) vs Liverpool (2072.9), Result: A
Match: Newcastle Utd (1908.8) vs Brighton (1795.4), Result: D
Match: Wolves (1708.6) vs Sunderland (1534.5), Result: H
Match: Brighton (1798.5) vs Wolves (1714.0), Result: H
Match: Burnley (1672.9) vs Aston Villa (1913.8), Result: A
Match: Crystal Palace (1813.2) vs Everton (1764.5), Result: H
Match: Fulham (1752.6) vs Bournemouth  (1770.5), Result: H
Match: Liverpool (2076.6) vs Chelsea (1928.0), Result: H
Match: Man City (2047.9) vs Brentford (1770.2), Result: H
Match: Nottm Forest (1784.8) vs Newcastle Utd (1905.6), Result: A
Match: Sunderland (1529.1) vs Man Utd (1811.7), Result: A
Match: Tottenham  (1764.6) vs Leeds (1690.1), Result: H
Match: West Ham (1718.3) vs Arsenal  (2082.0), Result: H
Match: Arsenal  (2064.2) vs Burnley (1668.9), Result: H
Match: Aston Villa (1917.8) vs Liverpool (2082.6), Result: A
Match: Bournemouth  (1760.0) vs Man City (2051.2), Result: A
Match: Brentford (1766.8) vs Crystal Palace (1821.8), Result: H
Match: Chelsea (1922.1) vs Tottenham  (1772.5), Result: H
Match: Everton (1755.9) vs Sunderland (1525.8), Result: H
Match: Leeds (1682.3) vs Brighton (1806.1), Result: A
Match: Man Utd (1815.0) vs Nottm Forest (1778.2), Result: H
Match: Newcastle Utd (1912.3) vs West Ham (1736.1), Result: H
Match: Wolves (1706.4) vs Fulham (1763.1), Result: D
Match: Brighton (1812.7) vs Man Utd (1823.9), Result: H
Match: Burnley (1667.1) vs Wolves (1708.0), Result: H
Match: Crystal Palace (1810.2) vs Arsenal  (2066.0), Result: A
Match: Fulham (1761.5) vs Newcastle Utd (1917.6), Result: D
Match: Liverpool (2088.2) vs Brentford (1778.4), Result: H
Match: Man City (2054.4) vs Aston Villa (1912.2), Result: H
Match: Nottm Forest (1769.2) vs Bournemouth  (1756.8), Result: H
Match: Sunderland (1521.6) vs Chelsea (1928.0), Result: A
Match: Tottenham  (1766.6) vs Everton (1760.1), Result: H
Match: West Ham (1730.8) vs Leeds (1675.7), Result: H

--- Final Points Table ---
1. Liverpool: 101 points (Elo 2091.1)
2. Arsenal : 97 points (Elo 2069.8)
3. Man City: 95 points (Elo 2060.5)
4. Chelsea: 71 points (Elo 1929.8)
5. Aston Villa: 71 points (Elo 1906.1)
6. Newcastle Utd: 70 points (Elo 1913.4)
7. Man Utd: 56 points (Elo 1813.6)
8. Brighton: 52 points (Elo 1823.0)
9. Tottenham : 48 points (Elo 1776.4)
10. Crystal Palace: 47 points (Elo 1806.5)
11. Nottm Forest: 44 points (Elo 1778.9)
12. Everton: 43 points (Elo 1750.3)
13. Fulham: 42 points (Elo 1765.7)
14. Brentford: 41 points (Elo 1775.5)
15. Bournemouth : 40 points (Elo 1747.2)
16. West Ham: 37 points (Elo 1739.2)
17. Wolves: 32 points (Elo 1696.8)
18. Burnley: 31 points (Elo 1678.2)
19. Leeds: 28 points (Elo 1667.2)
20. Sunderland: 14 points (Elo 1519.8)

Home Wins: 216, Away Wins: 84, Draws: 80

---
## Limitations

- ELO rating does not indicate the strengthening by transfer policy
- Lack of previous ELO data led to generation of syntehtic data for training
 
