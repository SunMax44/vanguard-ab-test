import streamlit as st
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt

# Add title and description
st.title('A/B Test Analysis for New Website Design')
st.write('This dashboard shows the real-time results of the A/B test for a new website design, analyzing whether the new design meets a 5% improvement threshold in completion rate.')

# Input fields for A/B test data
st.sidebar.header("Input your test results")

n_new = st.sidebar.number_input('Sample Size (New Design)', value=29919)
n_old = st.sidebar.number_input('Sample Size (Old Design)', value=26277)
p_new = st.sidebar.number_input('Completion Rate (New Design)', value=0.6107)
p_old = st.sidebar.number_input('Completion Rate (Old Design)', value=0.5755)

# Calculate successes based on input
count_new = p_new * n_new
count_old = p_old * n_old

# Perform the z-test
count = [count_new, count_old]
nobs = [n_new, n_old]

stat, p_value = proportions_ztest(count, nobs, value=0.05, alternative='larger')

# Display the results
st.subheader('Z-Test Results')
st.write(f'Z-Score: {stat}')
st.write(f'P-Value: {p_value}')

# Interpretation
if p_value < 0.05:
    st.success('The new design shows a statistically significant improvement of at least 5% in completion rate.')
else:
    st.warning('The new design does not show a statistically significant improvement of at least 5% in completion rate.')

# Visualization: Plotting the completion rates
st.subheader('Completion Rate Comparison')
fig, ax = plt.subplots()
ax.bar(['New Design', 'Old Design'], [p_new, p_old], color=['green', 'blue'])
ax.set_ylabel('Completion Rate')
ax.set_title('Completion Rates for New and Old Designs')

st.pyplot(fig)

# Option to upload and visualize additional data (Optional)
uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV)", type=['csv'])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write('Uploaded dataset preview:')
    st.write(df.head())
