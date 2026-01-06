from app.constants.values import CATEGORICAL_THRESHOLDS

def pct_change(prev, curr):
    if prev == 0:
        return 0 if curr == 0 else 100
    return abs((curr - prev) / prev) * 100

def abs_change(prev, curr):
    return abs(curr - prev)

class CategoricalDriftEvaluator:

    def evaluate(self, prev: dict, curr: dict) -> dict:
        score = 0
        reasons = []

        if prev["top_category"] != curr["top_category"]:
            score += 2
            reasons.append("TOP_CATEGORY_CHANGED")

        if pct_change(prev["top_category_percentage"], curr["top_category_percentage"]) > CATEGORICAL_THRESHOLDS["top_freq_pct_change"]:
            score += 1
            reasons.append("TOP_FREQ_SHIFT")

        if pct_change(prev["unique_count"], curr["unique_count"]) > CATEGORICAL_THRESHOLDS["unique_count_pct_change"]:
            score += 1
            reasons.append("UNIQUE_COUNT_SHIFT")

        return self._severity(score, reasons)

    def _severity(self, score, reasons):
        if score == 0:
            return {"severity": "PASS", "score": score, "reasons": []}
        elif score <= 2:
            return {"severity": "WARN", "score": score, "reasons": reasons}
        else:
            return {"severity": "FAIL", "score": score, "reasons": reasons}
