import pandas as pd
from app.core.profiling.numeric import NumericProfiler
from app.core.profiling.categorical import CategoricalProfiler
from app.core.profiling.datetime import DatetimeProfiler
from app.Exception import MyException
import sys

class Profiler:
    def __init__(self, df: pd.DataFrame, semantic_types: dict):
        """
        df: pandas DataFrame
        semantic_types: {column_name: semantic_type}
        """
        self.df = df
        self.semantic_types = semantic_types

    def run_all(self) -> dict:
        """
        Run profiling for all columns based on their semantic type
        Returns:
            column_profiles: dict[column_name] = {semantic_type, raw_dtype, metrics}
        """
        try:
            column_profiles = {}

            for col, sem_type in self.semantic_types.items():
                column_profiles[col] = {
                    "semantic_type": sem_type,
                    "raw_dtype": str(self.df[col].dtype),
                    "metrics": {}
                }

                series = self.df[col]

                if sem_type == "numeric":
                    column_profiles[col]["metrics"] = NumericProfiler().profile(series)

                elif sem_type == "categorical":
                    column_profiles[col]["metrics"] = CategoricalProfiler().profile(series)

                elif sem_type == "datetime":
                    column_profiles[col]["metrics"] = DatetimeProfiler().profile(series)

                else:
                    
                    column_profiles[col]["metrics"] = CategoricalProfiler().profile(series)

            return column_profiles

        except Exception as e:
            raise MyException(e, sys)
