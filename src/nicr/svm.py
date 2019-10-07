 Import numpy for number manipulation
import numpy as np

# Import pandas for data manipulation
import pandas as pd

# Map plotting tools
import matplotlib.pyplot as plt
import matplotlib.cm as cm

"""
Extract information and draw trends from platinum-group elements (PGE)
with nickel and chromium mineralization.
"""

# Read the .txt file as a pandas DataFrame df
df = pd.read_csv("data/nicr/nicrpge.txt", sep="|", encoding = "ISO-8859-1")

# Extract data of interest for the svm.
y = [] # The target values of interest with a specific number assocaited with each target
ynames = [] # Names for each target valuea
count = 0 # Used for keeping track of each target
for i in range(len(gdf["Commod_gp"])): # Use the "Commod_gp" column as targaet names
    if i in ynames:
        y.append(ynames.index(i))
    else:
        count += 1
        y.append(count)
        ynames.append(count)
zipped = zip(gdf["WGS84_Lat"], gdf["WGS84_Lon"])
lat, long = zip(*zipped)
X = [list(a) for a in zip(gdf["WGS84_Lat"], gdf["WGS84_Lon"])] # Features we test
target = ynames
feature = ["WGS84_Lat", "WGS84_Lon"] # Feature names

# Let's get machine learning in this joint. 
clf = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma="auto", kernel="rbf",
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

# Fit.
clf.fit(X,y)

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title="Confusion matrix",
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    fig = plt.figure(figsize=(10, 8)) 
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
