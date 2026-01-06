from app.core.drift.statistical_drift import NumericDriftEvaluator
from app.core.drift.categorical_drift import CategoricalDriftEvaluator
from app.core.drift.boolean_drift import BooleanDriftEvaluator  
from app.Exception import MyException
import sys
try:
    class DriftDispatcher:

        def dispatch(self, prev_profile, curr_profile):
            semantic_type = prev_profile["semantic_type"]
            raw_dtype=prev_profile["raw_dtype"]

            if semantic_type == "numeric" and raw_dtype=='bool':
                return BooleanDriftEvaluator().evaluate(
                    prev_profile["metrics"],
                    curr_profile["metrics"]
                )


            if semantic_type == "numeric":
                return NumericDriftEvaluator().evaluate(
                    prev_profile["metrics"],
                    curr_profile["metrics"]
                )

           
            if semantic_type == "categorical":
                return CategoricalDriftEvaluator().evaluate(
                    prev_profile["metrics"],
                    curr_profile["metrics"]
                )

            raise ValueError(f"Unsupported semantic type: {semantic_type}")
except Exception as e:
    raise MyException(e,sys)