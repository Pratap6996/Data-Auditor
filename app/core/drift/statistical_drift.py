from app.constants.values import NUMERIC_THRESHOLDS
from app.Exception import MyException
import sys
try:
    def pct_change(prev, curr):
        if prev == 0:
            return 0 if curr == 0 else 100
        return abs((curr - prev) / prev) * 100

    def abs_change(prev, curr):
        return abs(curr - prev)

    class NumericDriftEvaluator:

        def evaluate(self, prev: dict, curr: dict) -> dict:
            score = 0
            reasons = []

            if pct_change(prev["mean"], curr["mean"]) > NUMERIC_THRESHOLDS["mean_pct_change"]:
                score += 1
                reasons.append("MEAN_SHIFT")

            if pct_change(prev["std"], curr["std"]) > NUMERIC_THRESHOLDS["std_pct_change"]:
                score += 1
                reasons.append("STD_SHIFT")

            if pct_change(prev["median"], curr["median"]) > NUMERIC_THRESHOLDS["median_pct_change"]:
                score += 1
                reasons.append("MEDIAN_SHIFT")

            if pct_change(prev["iqr"], curr["iqr"]) > NUMERIC_THRESHOLDS["iqr_pct_change"]:
                score += 1
                reasons.append("IQR_SHIFT")

            if abs_change(prev["outlier_percentage"], curr["outlier_percentage"]) > NUMERIC_THRESHOLDS["outlier_pct_change"]:
                score += 1
                reasons.append("OUTLIER_RATE_SHIFT")

            if abs_change(prev["missing_percentage"], curr["missing_percentage"]) > NUMERIC_THRESHOLDS["missing_pct_change"]:
                score += 1
                reasons.append("MISSING_RATE_SHIFT")

            if abs_change(prev["zero_percentage"], curr["zero_percentage"]) > NUMERIC_THRESHOLDS["zero_pct_change"]:
                score += 1
                reasons.append("ZERO_RATE_SHIFT")

            if abs_change(prev["negative_percentage"], curr["negative_percentage"]) > NUMERIC_THRESHOLDS["negative_pct_change"]:
                score += 1
                reasons.append("NEGATIVE_RATE_SHIFT")

            return self._severity(score, reasons)

        def _severity(self, score, reasons):
            if score == 0:
                return {"severity": "PASS", "score": score, "reasons": []}
            elif score <= 2:
                return {"severity": "WARN", "score": score, "reasons": reasons}
            else:
                return {"severity": "FAIL", "score": score, "reasons": reasons}
except Exception as e:
    raise MyException(e,sys)