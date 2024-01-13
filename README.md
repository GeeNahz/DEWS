# DEWS
A Drought Early Warning System (DEWS) for northern Nigeria

> The project is a backend API service for predicting drought.
> It consists of two parts:

1. Sensor Data Collection
2. Drought Prediction using ARIMA model

Sensor readings are taken from a data collection unit and POSTed to this server. They are stored and computations are carried out using these readings to predict drought.

For the prediction, an ARIMA model, a time series model, was trained using historical dataset and used to predict drought.

The dataset is a Standard Precipitation Evapotranspiration Index (SPEI) data and this, along with some threshold are used to determine the occurence of drought.
