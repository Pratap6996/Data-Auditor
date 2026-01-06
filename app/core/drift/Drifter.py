from app.core.drift.drift_dispatcher import DriftDispatcher
class CheckDrift:
    def __init__(self, prev: dict, curr: dict):
        self.prev = prev
        self.curr = curr
        self.dispatcher = DriftDispatcher()

    def find(self):
        drift_report = {}

        common_columns = self.prev.keys() & self.curr.keys()

        for column in common_columns:
            prev_values = self.prev[column]
            curr_values = self.curr[column]

            result = self.dispatcher.dispatch(
                prev_profile=prev_values,
                curr_profile=curr_values
            )

            if result["severity"] != "PASS":
                drift_report[column] = {
                    "severity": result["severity"],
                    "score": result["score"],
                    "reasons": result["reasons"],
                    "semantic_type": prev_values["semantic_type"]
                }

        return drift_report
