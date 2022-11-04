# Demonstrators for DARE data assimiliation course
This repository contains Python code with a set of demonstrations of data assimilation techniques. This code accompanies the DARE data assimilation online course (https://discoverda.org/).

## Interactive demonstrators
Note that demonstrators may take a few minutes to load when first used.
 * [1. Optimal interpolation](https://share.streamlit.io/darc-reading/dare-da-demos/main/1_optimal_interpolation.py) - uses [Streamlit](https://streamlit.io)
 * [2.1. Variational data assimilation (3D vs 4D)](https://mybinder.org/v2/gh/darc-reading/dare-da-demos/HEAD?labpath=2-1_variational_activity-3D_vs_4D_var_single_obs.ipynb) - uses [Binder](https://mybinder.org)
 * [2.2. Variational data assimilation (window length)](https://mybinder.org/v2/gh/darc-reading/dare-da-demos/HEAD?labpath=2-2_variational_activity_4D-var_assimilation_window.ipynb) - uses [Binder](https://mybinder.org)
 * [3.1. Ensemble Kalman Filter (ensemble size)](https://mybinder.org/v2/gh/darc-reading/dare-da-demos/HEAD?labpath=3-1_ensemble_activity_ensemble_size.ipynb) - uses [Binder](https://mybinder.org)
 * [3.2. Ensemble Kalman Filter (observation localisation)](https://mybinder.org/v2/gh/darc-reading/dare-da-demos/HEAD?labpath=3-2_ensemble_activity_observation_localisation.ipynb) - uses [Binder](https://mybinder.org)

## Static demonstrators
If for any reason the above interactive demonstrators don't work, you can view a online, read-only version of the demonstrators using the following links:
 * [2.1. Variational data assimilation (3D vs 4D)](https://nbviewer.org/github/darc-reading/dare-da-demos/blob/HEAD/2-1_variational_activity-3D_vs_4D_var_single_obs.ipynb)
 * [2.2. Variational data assimilation (window length)](https://nbviewer.org/github/darc-reading/dare-da-demos/blob/HEAD/2-2_variational_activity_4D-var_assimilation_window.ipynb)
 * [3.1. Ensemble Kalman Filter (ensemble size)](https://nbviewer.org/github/darc-reading/dare-da-demos/blob/HEAD/3-1_ensemble_activity_ensemble_size.ipynb)
 * [3.2. Ensemble Kalman Filter (observation localisation)](https://nbviewer.org/github/darc-reading/dare-da-demos/blob/HEAD/3-2_ensemble_activity_observation_localisation.ipynb)

## Download and run the code locally
You may also download or clone the code from this repository to run it in your local Python environment. You can install the dependencies with `pip install -r requirements.txt`.

To run the Optimal Interpolation demo using Streamlit, install the dependencies and run `streamlit run 1_optimal_interpolation.py`. This should open the app in your browser.

## Acknowledgements
This code has been created by  authors from the [Data Assimilation Research Centre](https://research.reading.ac.uk/met-darc/) (DARC) at the [University of Reading](https://www.reading.ac.uk), funded in part by the [Data Assimilation for the REsilient City](https://research.reading.ac.uk/dare/) (DARE) project (EPSRC EP/P002331/1) and the NERC [National Centre for Earth Observation](https://www.nceo.ac.uk) (NCEO).
