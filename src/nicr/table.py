# Import numpy for number manipulation
import numpy as np

# Import pandas for data manipulation
import pandas as pd

# Map plotting tools
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LogNorm, to_hex
from matplotlib.cm import plasma, inferno, magma, viridis, ScalarMappable

# Bokeh plotting
from bokeh.models import (ColumnDataSource, LinearColorMapper, LogColorMapper, 
	ColorBar, BasicTicker)
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge

"""
Extract information and draw trends from platinum-group elements (PGE)
with nickel and chromium mineralization.
"""

# Read the .txt file as a pandas DataFrame df
df = pd.read_csv("data/nicr/nicrpge.txt", sep="|", encoding = "ISO-8859-1")

elements = [
 "Ac",
 "Ag",
 "Al",
 "Am",
 "Ar",
 "As",
 "At",
 "Au",
 "B",
 "Ba",
 "Be",
 "Bh",
 "Bi",
 "Bk",
 "Br",
 "C",
 "Ca",
 "Cd",
 "Ce",
 "Cf",
 "Cl",
 "Cm",
 "Cn",
 "Co",
 "Cr",
 "Cs",
 "Cu",
 "Db",
 "Ds",
 "Dy",
 "Er",
 "Es",
 "Eu",
 "F", 
 "Fe",
 "Fl",
 "Fm",
 "Fr",
 "Ga",
 "Gd",
 "Ge",
 "H", 
 "He",
 "Hf",
 "Hg",
 "Hs",
 "I", 
 "In",
 "Ir",
 "K",
 "Kr",
 "La",
 "Li",
 "Lr",
 "Lu",
 "Lv",
 "Mc",
 "Md",
 "Mg",
 "Mn",
 "Mo",
 "Mt",
 "N",
 "Na",
 "Nb",
 "Nd",
 "Ne",
 "Nh",
 "Ni",
 "No",
 "Np",
 "O",
 "Og",
 "Os",
 "P", 
 "Pa",
 "Pb",
 "Pd",
 "Pm",
 "Po",
 "Pr",
 "Pt",
 "Pu",
 "Ra",
 "Rb",
 "Re",
 "Rf",
 "Rg",
 "Rh",
 "Rn",
 "Ru",
 "S", 
 "Sb",
 "Sc",
 "Se",
 "Sg",
 "Si",
 "Sm",
 "Sn",
 "Sr",
 "Ta",
 "Tb",
 "Tc",
 "Te",
 "Th",
 "Ti",
 "Tl",
 "Tm",
 "Ts",
 "U", 
 "V", 
 "W", 
 "X",
 "Y", 
 "Yb",
 "Zn",
 "Zr"]
