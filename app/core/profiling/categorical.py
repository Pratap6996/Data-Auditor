import pandas as pd
from app.Exception import MyException
import sys

class CategoricalProfiler:
    def profile(self, series: pd.Series, top_k: int = 5) -> dict:
        """
        Profile categorical column and emit FLAT drift-ready signals
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
            metrics["unique_count"] = int(clean_series.nunique())

            # ---------- Cardinality bucket ----------
            if metrics["unique_count"] <= 10:
                metrics["cardinality_type"] = "low"
            elif metrics["unique_count"] <= 100:
                metrics["cardinality_type"] = "mid"
            else:
                metrics["cardinality_type"] = "high"

            # ---------- Empty column ----------
            if clean_series.empty:
                metrics["top_category"] = None
                metrics["top_category_percentage"] = 0.0
                metrics["other_percentage"] = 0.0
                return metrics

            # ---------- Top category ----------
            value_counts = clean_series.value_counts(normalize=True)
            top_category = value_counts.idxmax()
            top_pct = value_counts.iloc[0] * 100

            metrics["top_category"] = str(top_category)
            metrics["top_category_percentage"] = float(round(top_pct, 2))

            # ---------- Other bucket ----------
            metrics["other_percentage"] =float(round(
                (1 - value_counts.iloc[0]) * 100, 2
            ))

            return metrics

        except Exception as e:
            raise MyException(e, sys)
