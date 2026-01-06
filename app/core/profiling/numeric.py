import pandas as pd
from app.Exception import MyException
import sys

class NumericProfiler:
    def profile(self, series: pd.Series) -> dict:
        """
        Profile numeric column and emit FLAT drift-ready signals
        """
        try:
            metrics = {}

            # ---------- Basic ----------
            total_count = len(series)
            non_null_count = series.count()
            metrics["count"] = int(non_null_count)
            metrics["missing_percentage"] = float(round(
                (total_count - non_null_count) / total_count * 100, 2
            ))

            clean_series = series.dropna()

            # ---------- Boolean (numeric encoded) ----------
            if str(series.dtype) == "bool":
                true_pct = round((clean_series == 1).mean() * 100, 2)
                false_pct = round((clean_series == 0).mean() * 100, 2)

                metrics["true_percentage"] = float(true_pct)
                metrics["false_percentage"] = float(false_pct)

                return metrics

            # ---------- Core statistics ----------
            metrics["mean"] = round(float(clean_series.mean()), 5)
            metrics["median"] = round(float(clean_series.median()), 5)
            metrics["std"] = round(float(clean_series.std()), 5)
            metrics["min"] = round(float(clean_series.min()), 5)
            metrics["max"] = round(float(clean_series.max()), 5)

            # ---------- Quantiles (FLATTENED) ----------
            metrics["p05"] = round(float(clean_series.quantile(0.05)), 5)
            metrics["p25"] = round(float(clean_series.quantile(0.25)), 5)
            metrics["p50"] = round(float(clean_series.quantile(0.50)), 5)
            metrics["p75"] = round(float(clean_series.quantile(0.75)), 5)
            metrics["p95"] = round(float(clean_series.quantile(0.95)), 5)

            # ---------- IQR & range ----------
            iqr = metrics["p75"] - metrics["p25"]
            metrics["iqr"] = round(float(iqr), 5)
            metrics["range"] = round(metrics["max"] - metrics["min"], 5)

            # ---------- Zero / negative ----------
            metrics["zero_percentage"] = float(round((clean_series == 0).mean() * 100, 2))
            metrics["negative_percentage"] = float(round((clean_series < 0).mean() * 100, 2))

            # ---------- Outliers (IQR rule) ----------
            lower = metrics["p25"] - 1.5 * iqr
            upper = metrics["p75"] + 1.5 * iqr
            outliers = ((clean_series < lower) | (clean_series > upper)).mean()
            metrics["outlier_percentage"] = float(round(outliers * 100, 2))

            return metrics

        except Exception as e:
            raise MyException(e, sys)
