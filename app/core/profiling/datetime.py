import pandas as pd
from app.Exception import MyException
import sys

class DatetimeProfiler:
    def profile(self, series: pd.Series) -> dict:
        """
        Profile datetime column: min date, max date, range, missing %
        """
        try:
            metrics = {}
            metrics["count"] = int(series.count())
            metrics["missing_percentage"] = float(series.isna().mean() * 100)

            if series.dropna().empty:
                metrics["min"] = None
                metrics["max"] = None
                metrics["range_days"] = None
            else:
                metrics["min"] = series.min()
                metrics["max"] = series.max()
                metrics["range_days"] = (series.max() - series.min()).days

            return metrics
        except Exception as e:
            raise MyException(e, sys)
