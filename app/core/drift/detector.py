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
    
    
