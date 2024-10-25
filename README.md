# Vanguard Web UI A/B Testing

### Presentation Link: https://www.canva.com/design/DAGUfNYNZqo/3dIDhVBJ5UBvxxBmsMPHew/edit?utm_content=DAGUfNYNZqo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Project Overview
This project focuses on A/B testing a new user interface (UI) design for Vanguard Group, with the goal of enhancing user experience (UX) and increasing the investment confirmation rate. The test involves comparing the new design's effectiveness against the current UI by measuring key metrics related to user engagement and efficiency.

## Objectives
- **Improve UX**: The new design is intended to streamline the user journey, making investment processes more intuitive and efficient for users.
- **Key Performance Metrics**:
  - **Confirmation Rate**: Track if the new design leads to a higher rate of investment confirmations.
  - **Time Spent per Step**: Measure if users complete each step more quickly.
  - **Error Rate**: Determine if the new design reduces user errors during the process.

## Methodology
- **Random Sampling**: A random sample of clients was divided into test and control groups.
- **Data Collection**: Client interactions with the UI were monitored and timestamped across all steps of the investment process.
- **Analysis**:
  - **Statistical Tests**: Two-sample T-tests and ANOVA were applied to determine the statistical significance of differences in time spent and confirmation rates between groups.
  - **Data Cleaning**: Removed ambiguous entries and merged datasets by A/B group for accurate analysis.

## Key Findings
- **Confirmation Rate**: Extremely low p-values for confirmation rates indicate a statistically significant improvement in the test group, surpassing the 5% improvement threshold.
- **Time Efficiency**: The test group generally spent less time at each step, with significant differences found across steps via T-tests and ANOVA.
- **Error Rate**: Higher true error rates were observed in the test group, especially at the initial step, suggesting areas for design improvement.

## Conclusion & Learnings
The new UI design demonstrated positive impacts on user engagement and completion rates, though certain design elements may require refinement due to higher error rates in specific steps. Key takeaways include experience with statistical testing (Z-tests, T-tests, ANOVA) and visualization tools like Tableau.
