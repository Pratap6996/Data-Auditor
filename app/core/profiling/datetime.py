import pandas as pd
from app.Exception import MyException
import sys

class DatetimeProfiler:
    def profile(self, series: pd.Series) -> dict:
        """
        Profile datetime column and emit FLAT drift-ready signals
        """
        try:
            metrics = {}

            # ---------- Basic ----------
            total_count = len(series)
            non_null_count = series.count()

            metrics["count"] = int(non_null_count)
            metrics["missing_percentage"] = round(
                (total_count - non_null_count) / total_count * 100, 2
            )

            clean_series = series.dropna()

            # ---------- Empty column ----------
            if clean_series.empty:
                metrics["min_epoch"] = None
                metrics["max_epoch"] = None
                metrics["range_days"] = 0
                return metrics

            # ---------- Datetime signals ----------
            min_ts = clean_series.min()
            max_ts = clean_series.max()

            metrics["min_epoch"] = int(min_ts.timestamp())
            metrics["max_epoch"] = int(max_ts.timestamp())
            metrics["range_days"] = int((max_ts - min_ts).days)

            return metrics

        except Exception as e:
            raise MyException(e, sys)
