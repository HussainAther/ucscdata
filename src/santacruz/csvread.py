import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")


plot = sns.lmplot("latitude", "longitude", data=magdf, fit_reg=False, hue="diurnal")
plot.savefig("output/santacruz/quadrangle.png")
