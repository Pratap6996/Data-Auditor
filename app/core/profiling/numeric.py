import pandas as pd
from app.Exception import MyException
import sys

class NumericProfiler:
    def profile(self, series: pd.Series) -> dict:
        """
        Profile numeric column: mean, median, std, min, max, missing %
        """
        try:
            metrics = {}
            metrics["count"] = int(series.count())
            metrics["missing_percentage"] = int(series.isna().mean() * 100)
            metrics["mean"] =round(float( series.mean()),5)
            metrics["median"] = float(series.median())
            metrics["std"] = round(float(series.std()),5)
            metrics["min"] = float(series.min())
            metrics["max"] = float(series.max())
            if(str(series.dtype)=='bool'):
                count_1 = int((series == 1).sum())           
                count_0 = int((series == 0).sum())  
                metrics["count_1"] = count_1
                metrics["count_0"] = count_0
            return metrics
        except Exception as e:
            raise MyException(e, sys)
