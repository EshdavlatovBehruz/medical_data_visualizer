import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1-Task
df = pd.read_csv("medical_examination.csv")

# 2-Task
bmi = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = (bmi > 25).astype(int)

# 3-Task
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4-Task
def draw_cat_plot():
    # 5-Task
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    # 6-Task
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7-Task
    plot = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar")
    # 8-Task
    fig = plot.fig
    # 9-Task
    return fig


# 10-Task
def draw_heat_map():
    # 11-Task
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12-Task
    corr = df_heat.corr()

    # 13-Task
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14-Task
    fig, ax = plt.subplots(figsize=(10, 12))
    # 15-Task
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, square=True, linewidths=0.5, cbar_kws={"shrink": .5})
    # 16-Task
    return fig

plt.show()