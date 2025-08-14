import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as w

w.filterwarnings("ignore")

# Streamlit page settings
st.set_page_config(page_title="🧠 Stress Level Analysis", layout="wide")
st.title("🧠 Stress Level Analysis Built with Streamlit")
st.write("This Streamlit app visualizes stress levels and related factors from the dataset.")

# File uploader
uploaded_file = st.file_uploader("Upload your Stress Level CSV file", type=["csv"])

# Load data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using default dataset: StressLevelDataset.csv")
    df = pd.read_csv("StressLevelDataset.csv")

# Show raw data
if st.checkbox("Show data"):
    st.dataframe(df)

# =====================
# 1. Distribution of stress levels
# =====================
st.subheader("📊 Distribution of Stress Levels")
fig, ax = plt.subplots(figsize=(8, 6))
stress_counts = df['stress_level'].value_counts().sort_index()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
ax.pie(stress_counts.values, labels=[f'Level {i}' for i in stress_counts.index],
       autopct='%1.1f%%', colors=colors, startangle=90)
ax.set_title('Distribution of Stress Levels Among Students', fontsize=14, fontweight='bold')
st.pyplot(fig)

# =====================
# 2. Anxiety vs Depression
# =====================
st.subheader("📉 Relationship Between Anxiety and Depression Levels")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='anxiety_level', y='depression',
                hue='stress_level', palette='viridis', alpha=0.7, s=50, ax=ax)
sns.regplot(data=df, x='anxiety_level', y='depression',
            scatter=False, color='red', line_kws={'linewidth': 2}, ax=ax)
ax.set_title('Anxiety vs Depression', fontsize=14, fontweight='bold')
st.pyplot(fig)

# =====================
# 3. Physical factors by stress level
# =====================
st.subheader("🩺 Physical Factors by Stress Level")
physical_factors = ['headache', 'blood_pressure', 'sleep_quality', 'breathing_problem']
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()
for i, factor in enumerate(physical_factors):
    sns.violinplot(data=df, x='stress_level', y=factor, ax=axes[i], palette='Set2')
    axes[i].set_title(f'{factor.replace("_", " ").title()} by Stress Level')
plt.tight_layout()
st.pyplot(fig)

# =====================
# 4. Heatmap of academic performance vs stress level by study load
# =====================
st.subheader("📚 Academic Performance vs Stress Level by Study Load")
pivot_table = df.groupby(['academic_performance', 'study_load'])['stress_level'].mean().unstack()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Mean Stress Level by Academic Performance & Study Load')
st.pyplot(fig)

# =====================
# 5. Boxplots for numerical columns
# =====================
st.subheader("📦 Boxplots of All Numerical Columns")
numerical_cols = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]
cols_per_row = 3
rows_needed = (len(numerical_cols) + cols_per_row - 1) // cols_per_row
fig, axes = plt.subplots(nrows=rows_needed, ncols=cols_per_row, figsize=(15, rows_needed * 4))
axes = axes.flatten()
for i, col in enumerate(numerical_cols):
    sns.boxplot(x=df[col], ax=axes[i])
    axes[i].set_title(f'Boxplot of {col}')
    axes[i].grid(False)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])
plt.tight_layout()
st.pyplot(fig)
