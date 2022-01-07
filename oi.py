# Demonstration of optimal interpolation using Streamlit

import math
import streamlit as st
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib as mpl
import matplotlib.pyplot as plt


@st.cache
def soar2(x1, x2, L):
    '''
    function to compute correlation between two points x1, x2
    according to their separation
    
    uses a SOAR correlation function with length scale L
    (L = 0 => uncorrelated)

    rho = [1 + (dx/L)]*exp(-dx/L); dx = |x1-x2|
    '''

    d = abs(x1 - x2)
    if d == 0:
        return 1.0
    elif L > 0.0:
        return (1.0 + d/L) * math.exp(-d/L)
    else:
        return 0.0


@st.cache
def get_background_function(bg_type, x):

    if bg_type == 'Flat':
        return np.zeros(len(x))
    elif bg_type == 'Linear':
        y2 = 0.5
        y1 = -0.5
        x2 = x[-1]
        x1 = x[0]
        m = (y2 - y1) / (x2 - x1)
        return m * (x - x1) + y1
    elif bg_type == 'Sine wave':
        return 0.3 * np.sin(2 * math.pi * x/xn)
    else:
        raise ValueError('Unknown value of bg_type: ' + bg_type)


st.title('Optimal interpolation demonstration')
st.markdown('Here is some explanation of what is going on, including some **bold text** and LaTeX: $\\overleftarrow{AB}$.')

# set x values at which equations are solved
x0 = 0.
xn = 10.
nx = 100 # will have nx+1 points
x = np.linspace(x0, xn, nx + 1)

# initialise analysis vectors
xdim = len(x)
a  = np.zeros(xdim) # analysis for 2 obs case
a1 = np.zeros(xdim) # analysis for o1 only case
a2 = np.zeros(xdim) # analysis for o2 only case

bg_func = st.selectbox(
    'Select background function',
    ('Flat', 'Linear', 'Sine wave')
)
fb = get_background_function(bg_func, x)

st.subheader("Set observation values and locations")
# default observation values and locations
x1 = st.slider('First observation location', 0, 4, 1)
o1 = st.slider('First observation value', 0.0, 1.0, 1.0, 0.2)
x2 = 7.5; o2 = -1.0

# default covariances and correlation lengths
# forecast (background)
sigf = 1.0 # background error standard deviation
Lf   = 2.0 # correlation length scale
# observations
sigo = 1.0 # observation error standard deviation
Lo   = 1.0 # correlation length scale

# get value of background field at observation locations, Hxb

# Create a function that estimates the background at any point
# by interpolating linearly between the given background points
Hfb = interpolate.interp1d(x, fb, 'linear') # This will always be zero since fb=0 everywhere

# Compute y-Hxb at each obs location
d1 = o1 - Hfb(x1)
d2 = o2 - Hfb(x2)

# Compute weighted correlation for each obs
cf12 = soar2(x1, x2, Lf) # background
co12 = soar2(x1, x2, Lo) # observations

C = sigf*sigf*cf12 + sigo*sigo*co12 # var_b*rho(x1,x2) + var_o*rho(x1,x2)

C = C/(sigf*sigf+sigo*sigo)         # [var_b*rho(x1,x2) + var_o*rho(x1,x2)]/[var_b+var_o]

W = (sigf*sigf+sigo*sigo)*(1.-C*C) 

W = sigf*sigf/W 

# weight for a single ob:  var_b/(var_b+var_o)
W1 = sigf*sigf/(sigf*sigf+sigo*sigo)

# OI analysis
cf1 = np.array([soar2(xi, x1, Lf) for xi in x]) # rho(x,x1), (xdim x 1) vector
cf2 = np.array([soar2(xi, x2, Lf) for xi in x]) # rho(x,x2), (xdim x 1) vector
  
z = cf1*(d1-C*d2)+cf2*(d2-C*d1);   
  
a  = fb + W*z        # analysis for 2 obs case
a1 = fb + cf1*W1*d1  # analysis for o1 only
a2 = fb + cf2*W1*d2  # analysis for o2 only

# Plot the data
fig = plt.figure()
plt.plot([x1, x2], [o1, o2], 'kx') # observation locations
plt.plot(x, a, 'r--')              # analysis in red dashed line
plt.plot(x, a1, 'b:')              # analysis with o1 only in blue dotted line
plt.plot(x, a2, 'b-')              # analysis with o2 only in blue dashed line
plt.plot(x, fb, 'k')               # background in black solid line
#plt.show()

st.subheader("Plot")
st.write(fig)
