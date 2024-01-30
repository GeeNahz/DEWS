import pickle
import pandas as pd

from django.conf import settings

from DEWSapp.threshold_constants import thresholds

model_pathname = settings.MODEL_FILE_PATH
historical_data_pathname = (
    settings.BASE_DIR / "DEWSapp" / "dewsdocs" / "Shiroro-Spei.csv"
)


class PredictionData:
    def __init__(self, month, year, spei, drought_index) -> None:
        self.month = month
        self.year = year
        self.spei = spei
        self.drought_index = drought_index


class ModelPrediction:
    @staticmethod
    def determine_forecast_steps(historical_data, current_year):
        latest_year_historical_data = pd.DatetimeIndex(
            historical_data["Date"]
        ).year.max()

        year_diff = int(current_year) - int(latest_year_historical_data)

        steps = year_diff * 12
        return steps

    @staticmethod
    def extract_spei(forecast_spei: pd.DataFrame, month: int, year: int):
        # forecast_spei = forecast_spei.drop(index=0)

        forecast_year = forecast_spei[
            pd.DatetimeIndex(forecast_spei["Date"]).year == year
        ]
        required_forecast = forecast_year[
            pd.DatetimeIndex(forecast_year["Date"]).month == month
        ]

        return required_forecast.iat[0, 1]

    @staticmethod
    def forecast_spei(year):
        """
        Make predictions using the saved ARIMA model
        ### Args:
        ```py
            year: int # the desired year for the prediction
        ```

        ### Response:
        ```py
            forecast_data: DataFrame # a pandas dataframe object for further processing
        ``` 
        """

        # Load the saved ARIMA model
        with open(model_pathname, "rb") as model_file:
            model = pickle.load(model_file)

        # Load saved historical data
        historical_spei = pd.read_csv(historical_data_pathname)

        latest_date = historical_spei["Date"].max()
        forecast_start_date = pd.to_datetime(latest_date) + pd.DateOffset(months=1)

        forecast_steps = ModelPrediction.determine_forecast_steps(
            historical_spei, year
        )  # Adjust as needed

        forecast_index = pd.date_range(
            forecast_start_date, periods=forecast_steps, freq="M"
        )
        print('forecast steps: ', forecast_steps)
        forecast = model.get_forecast(steps=forecast_steps)
        forecast_values = forecast.predicted_mean

        forecast_data = pd.DataFrame(
            {"Date": forecast_index, "Forecasted_SPEI": forecast_values}
        )

        # ModelPrediction.update_historical_data(
        #     forecast_index, forecast_values
        # )  # update historical data

        return forecast_data

    @staticmethod
    def update_historical_data(date, forecast):
        forecast_data = {"Date": date, "0": forecast}
        df = pd.DataFrame(forecast_data)

        # Update historical data
        df.to_csv(
            historical_data_pathname,
            mode="a",
            index=False,
            header=False,
        )

    @staticmethod
    def threshold(spei_value: int | float):
        index = thresholds(value=spei_value)

        data = {
            "spei": round(spei_value, 3),
            "drought_index": index,
        }

        return data

    @staticmethod
    def predict(month, year): # entry point
        spei_value = ModelPrediction.extract_spei(
            forecast_spei=ModelPrediction.forecast_spei(year),
            month=int(month),
            year=int(year),
        )

        data = ModelPrediction.threshold(spei_value=spei_value)
        result = PredictionData(month=month, year=year, **data)

        return result


def main(month, year):
    """
    ### Description
    Takes in the month and year for forecasts and utitlises the
    ModelPrediction class to make forecasts.

    It is the entry point for the making forecasts and
    returns the PredictionData object suitable for further serialisation.

    ### Args:
    ```py
        month: int # the month of the year to forecast for
        year: int # the year to forecast for
    ```

    ### Return:
    ```py
        PredictionData(): PredictionData # suitable for further serialisation using DRF serialiser class
    ```
    """
    return ModelPrediction.predict(month=month, year=year)


# TODO: After including the update dataset function, implement a check
# this check would look for a forecast data that already exists
# in the dataset. It will then extract the details for that particular
# year and month and return it instead of making another prediction
