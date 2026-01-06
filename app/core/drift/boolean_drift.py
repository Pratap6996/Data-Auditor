from app.constants.values import BOOLEAN_THRESHOLDS

def pct_change(prev, curr):
    if prev == 0:
        return 0 if curr == 0 else 100
    return abs((curr - prev) / prev) * 100

def abs_change(prev, curr):
    return abs(curr - prev)

class BooleanDriftEvaluator:

    def evaluate(self, prev: dict, curr: dict) -> dict:
        score = 0
        reasons = []

        if abs_change(prev["missing_percentage"], curr["missing_percentage"]) > BOOLEAN_THRESHOLDS["missing_pct_change"]:
            score += 1
            reasons.append("MISSING_RATE_SHIFT")

        if abs_change(prev["true_percentage"], curr["true_percentage"]) > BOOLEAN_THRESHOLDS["true_pct_change"]:
            score += 2
            reasons.append("TRUE_RATE_SHIFT")

        # extreme collapse
        if curr["true_percentage"] in (0, 100):
            score += 2
            reasons.append("BOOLEAN_COLLAPSE")

        return self._severity(score, reasons)

    def _severity(self, score, reasons):
        if score == 0:
            return {"severity": "PASS", "score": score, "reasons": []}
        elif score <= 2:
            return {"severity": "WARN", "score": score, "reasons": reasons}
        else:
            return {"severity": "FAIL", "score": score, "reasons": reasons}
