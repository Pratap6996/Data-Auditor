import pandas as pd
from app.Exception import MyException
import sys

class CategoricalProfiler:
    def profile(self, series: pd.Series) -> dict:
        """
        Profile categorical column: unique count, top value, top frequency, missing %
        """
        try:
            metrics = {}
            metrics["count"] = int(series.count())
            metrics["missing_percentage"] = float(series.isna().mean() * 100)
            metrics["unique_count"] = int(series.nunique(dropna=True))

            if series.dropna().empty:
                metrics["top"] = None
                metrics["top_frequency"] = None
            else:
                top_value = series.mode().iloc[0]
                metrics["top"] = top_value
                metrics["top_frequency"] = (series == top_value).sum()
            
            return metrics
        except Exception as e:
            raise MyException(e, sys)
