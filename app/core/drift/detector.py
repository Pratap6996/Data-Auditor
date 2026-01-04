class SchemaValidator:
    def __init__(self, prev_profile: dict, curr_profile: dict):
        self.prev = prev_profile
        self.curr = curr_profile

    def validate(self) -> dict:
        prev_cols = set(self.prev.keys())
        curr_cols = set(self.curr.keys())

        missing_columns = list(prev_cols - curr_cols)
        new_columns = list(curr_cols - prev_cols)

        type_changes = {}

        for col in prev_cols & curr_cols:
            prev_type = self.prev[col].get("semantic_type")
            curr_type = self.curr[col].get("semantic_type")

            if prev_type != curr_type:
                type_changes[col] = {
                    "previous": prev_type,
                    "current": curr_type
                }

        return {
            "missing_columns": missing_columns,
            "new_columns": new_columns,
            "semantic_type_changes": type_changes
        }
    
    def detect_numeric_drift(prev_metrics, curr_metrics, threshold=0.05):
        drift = {}

        for col in prev_metrics:
            if col not in curr_metrics:
                continue

            prev_mean = prev_metrics[col]["mean"]
            curr_mean = curr_metrics[col]["mean"]

            if prev_mean == 0:
                continue

            relative_change = abs(curr_mean - prev_mean) / prev_mean

            if relative_change > threshold:
                drift[col] = {
                    "prev_mean": prev_mean,
                    "curr_mean": curr_mean,
                    "change_ratio": round(relative_change, 3)
                }

        return drift

