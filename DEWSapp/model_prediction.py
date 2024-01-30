import pickle
import pandas as pd

from django.conf import settings

from DEWSapp.threshold_constants import thresholds

model_pathname = settings.MODEL_FILE_PATH
historical_data_pathname = (
    settings.BASE_DIR / "DEWSapp" / "dewsdocs" / "Shiroro-Spei.csv"
)


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
    def forecast_spei(year):
        """
        Make predictions using the saved ARIMA model
        args:
        1. year: int - the desired year for the prediction
        2. month: str - the desired month for the prediction
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
        forecast = model.get_forecast(steps=forecast_steps)
        forecast_values = forecast.predicted_mean

        forecast_data = pd.DataFrame(
            {"Date": forecast_index, "Forecasted_SPEI": forecast_values}
        )

        return forecast_data

    @staticmethod
    def threshold(spei_value: int | float):
        index = thresholds(value=spei_value)

        data = {
            "spei": round(spei_value, 3),
            "drought_index": index,
        }

        return data

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
    def predict(month, year):
        spei_value = ModelPrediction.extract_spei(
            forecast_spei=ModelPrediction.forecast_spei(year),
            month=int(month),
            year=int(year),
        )

        data = ModelPrediction.threshold(spei_value=spei_value)

        result = {
            "Month": month,
            "Year": year,
            **data,
        }

        print(result)
        return result
