# medical_data_visualizer

Instructions for Medical Data Visualizer
Data Preparation
Read data from medical_examination.csv into df.

Calculate BMI: weight / (height / 100)^2.

Create overweight column:
    - 1 if BMI > 25
    - 0 otherwise

Normalize cholesterol and gluc:
    - Set to 0 if value is 1
    - Set to 1 if value > 1

    Categorical Plot (draw_cat_plot())
Use pd.melt on cholesterol, gluc, smoke, alco, active, overweight → create df_cat.
Group by cardio, variable, value. Count occurrences. Rename count column to total.
Use sns.catplot() to create bar plot, separated by cardio.
Store the figure as fig and return it.

Heatmap (draw_heat_map())
Clean data:
    - ap_lo <= ap_hi
    - height between 2.5% and 97.5% quantiles
    - weight between 2.5% and 97.5% quantiles

Calculate correlation matrix: corr = df.corr().
Create mask for upper triangle: np.triu().
Create heatmap: sns.heatmap()
Store the figure as fig and return it.
