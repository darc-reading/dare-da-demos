# Demonstration of optimal interpolation using Streamlit

import math
import streamlit as st
import numpy as np
from scipy import interpolate
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
    '''Returns three diffrent options for the background function.'''

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
st.subheader('Introduction')
st.markdown('In this interactive demo, we perform data assimilation in order to '
            'estimate the values of a function over the interval [0,10]. '
            'A simple data assimilation scheme, called _optimal interpolation_, '
            'is used. We do not focus on the details of the scheme, but recap '
            'the necessary components for data assimilation that are used: '
            'the _background_, _observations_, _error covariances_, and '
            '_observation operator_.')

st.markdown('The exercises explore two ideas:')
st.markdown('1. the effect of the uncertainty in the observations on the analysis')
st.markdown('2. how the information from observations is spread to the unobserved variables.')

st.subheader("Instructions")
st.markdown('Use the selection boxes and sliders in the left-hand control panel to adjust parameter values. '
            'The plot will automatically update, although you might have to wait a few seconds '
            'after changing a parameter value.')
st.markdown('Choose the shape of the background function from the drop-down list, and set '
            'the location and the values of two observations using the sliders.')
st.markdown('We address the role of uncertainty by choosing different standard deviations '
            'for the observation error using the slider. What happens when the observations '
            'are assumed to be perfect and hence the standard deviation is set to zero? '
            'Increase the standard deviation incrementally until you reach the maximum '
            'value and observe how the analysis changes and compares to the background.')
st.markdown('To experiment with the spread of information to unobserved variables, change '
            'the background error correlation length scale. At which locations is the '
            'analysis different from the background? How does this change when the correlation '
            'length scale is increased or decreased?')


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

with st.sidebar:

    st.header("Controls")

    bg_func = st.selectbox(
        'Background function shape',
        ('Flat', 'Linear', 'Sine wave')
    )
    fb = get_background_function(bg_func, x)

    x1 = st.slider('First observation location', 0, 4, 1)
    o1 = st.slider('First observation value', 0.0, 1.0, 0.4, 0.2)
    x2 = st.slider('Second observation location', 5, 10, 7)
    o2 = st.slider('Second observation value', -1.0, 0.0, -0.6, 0.2)

    sigo = st.slider('Observation error standard deviation', 0.0, 1.0, 0.1, 0.1)

    Lf = st.slider('Background correlation length scale', 0.0, 2.0, 1.0, 0.2)

# These parameters are not adjustable via the Streamlit widgets
sigf = 0.2 # background error standard deviation
Lo   = 0.0 # correlation length scale

# get value of background field at observation locations, Hxb

# Create a function that estimates the background at any point
# by interpolating linearly between the given background points
Hfb = interpolate.interp1d(x, fb, 'linear')

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
# If you want, you can re-enable the calculation of the analysis with only one observation
# by uncommenting the following two lines
#a1 = fb + cf1*W1*d1  # analysis for o1 only
#a2 = fb + cf2*W1*d2  # analysis for o2 only

# Plot the data
fig = plt.figure()
plt.errorbar([x1, x2], [o1, o2], [sigo, sigo], marker='o', linestyle='None', label="Observations")  # observation locations
plt.plot(x, a, 'r--', label="Analysis")        # analysis in red dashed line
#plt.plot(x, a1, 'b:', label="Analysis (first obs only)")  # analysis with o1 only in blue dotted line
#plt.plot(x, a2, 'b-', label="Analysis (second obs only)") # analysis with o2 only in blue dashed line
plt.plot(x, fb, 'k', label="Background")                  # background in black solid line
plt.legend()
plt.xlim(0, 10)
plt.ylim(-1.2, 1.2)

st.write(fig)

st.subheader("Conclusions")
st.markdown('We performed simple data assimilation experiments, changing the observation '
            'uncertainty and the background error correlation length scale. A small '
            'observation uncertainty draws the analysis closer to observations, whereas '
            'large observation uncertainty means that the analysis is more similar to the '
            'background. A small correlation length scale indicates that changes in one '
            'variable affect only the variables that are close to it.')

st.subheader("Acknowledgements")
st.markdown("This code has been created by authors from the "
            "[Data Assimilation Research Centre](https://research.reading.ac.uk/met-darc/) (DARC) "
            "at the [University of Reading](https://www.reading.ac.uk), funded in part "
            "by the [Data Assimilation for the REsilient City](https://research.reading.ac.uk/dare/) "
            "(DARE) project (EPSRC EP/P002331/1) and the NERC [National Centre for Earth Observation](https://www.nceo.ac.uk) "
            "(NCEO).")