# 🧠 Stress Level Analysis App (Streamlit)

## 📌 Overview
The **Stress Level Analysis App** is an interactive Streamlit-based application designed to analyze, visualize, and interpret stress levels among students. It uses a combination of mental health indicators, physical symptoms, academic performance, social factors, and environmental conditions to identify key stress drivers and patterns.

The app offers **data-driven insights** that can help educational institutions, counselors, and policymakers design targeted interventions for student wellbeing.

**🌐 Live App:** [Click here to try it out](https://stress-level-analysis-built-with-app-fjhqunngozzmnmcrpz5pie.streamlit.app/)

---

## 🎯 Objectives
- **Identify** the most significant factors contributing to student stress.
- **Visualize** relationships between mental health, physical health, academics, and environment.
- **Classify** students into three stress levels (Low, Medium, High).
- **Recommend** actionable strategies for stress reduction and prevention.

---

## 📝 Problem Statement
Student stress is a growing global concern that affects mental health, academic success, and overall wellbeing.  
However, stress is **multi-dimensional** and influenced by:
- Mental health conditions (e.g., anxiety, depression)
- Lifestyle factors (e.g., sleep, physical activity)
- Academic pressure and workload
- Social support systems
- Environmental stressors

Without proper tools to analyze these factors together, interventions are often **reactive** rather than **preventive**.

---

## 📊 Methodology Overview
### **Data Processing Pipeline**
1. **Initial Exploration** – EDA with 10 research questions using diverse visualizations.
2. **Data Quality Assessment** – Checking for missing values, distribution patterns, and anomalies.
3. **Outlier Treatment** – Capping extreme values to maintain integrity.
4. **Statistical Analysis** – Correlation and group comparisons.
5. **Advanced Visualization** – Multi-dimensional plots for comprehensive insights.

### **Analytical Approach**
- **21 Variables Analyzed**: Mental health, physical symptoms, academics, social, environmental.
- **10+ Visualization Types**: Pie charts, violin plots, heatmaps, radar charts, box plots, scatter plots.
- **Multi-level Analysis**: Univariate, bivariate, and multivariate.
- **Risk Stratification**: Low, Medium, High stress classification.

---

## 📌 Key Findings
### 1. **Mental Health as Primary Driver**
- Anxiety & depression are top predictors (correlation > 0.7).
- 84% of high-stress students had elevated anxiety levels.
- Comorbidity: Anxiety increases depression likelihood 3.5x.

### 2. **Sleep Quality: The Critical Gateway**
- Strongest inverse relationship with stress.
- Poor sleep quality doubles likelihood of medium/high stress.

### 3. **Physical Health Manifestations**
- Headaches 3.2x higher in high-stress students.
- Breathing problems and blood pressure issues increase with stress level.

### 4. **Academic Performance Complexity**
- High study load + poor performance = highest stress.
- Academic pressure acts as a multiplier.

### 5. **Social Support as a Buffer**
- Strong peer/teacher relationships reduce stress by ~40%.
- High-stress students have fewer meaningful social connections.

### 6. **Environmental Stress Foundation**
- Noise levels, living conditions, and unmet basic needs amplify stress impact.

---

## 📈 Statistical Summary
| Stress Level | Count | Percentage | Avg Anxiety | Avg Depression | Sleep Quality | Social Support |
|--------------|-------|------------|-------------|----------------|---------------|----------------|
| Low          | 445   | 40.5%      | 4.2         | 5.1            | 4.2           | 3.8            |
| Medium       | 434   | 39.5%      | 10.5        | 11.3           | 3.1           | 2.9            |
| High         | 221   | 20.1%      | 17.8        | 18.2           | 2.1           | 2.2            |

---

## 💡 Recommendations
### **Immediate Interventions (0–3 months)**
- Campus-wide mental health screening.
- Sleep hygiene programs.
- Peer mentoring networks.

### **Medium-term (3–12 months)**
- Stress management workshops.
- Noise reduction & better living conditions.
- Academic load balancing.

### **Long-term (12+ months)**
- Predictive analytics for early stress detection.
- Wellness culture transformation.
- Longitudinal research tracking.

---

## 🚀 Features in the Streamlit App
- Upload custom CSV datasets.
- View raw data in an interactive table.
- Pie charts for stress level distribution.
- Scatter plots for mental health indicators.
- Violin plots for physical health patterns.
- Heatmaps for academic performance vs stress.
- Boxplots for numerical variable spread.


