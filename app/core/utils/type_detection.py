import pandas as pd
from app.Exception import MyException
import sys

class DataTypeAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def infer_semantic_types(self) -> dict:
        """
        Infers semantic data types for each column
        Returns:
            dict: {column_name: semantic_type}
        """
        try:
            column_types = {}

            for column in self.df.columns:
                dtype = self.df[column].dtype

                if pd.api.types.is_numeric_dtype(dtype):
                    column_types[column] = "numeric"

                elif pd.api.types.is_datetime64_any_dtype(dtype):
                    column_types[column] = "datetime"

                elif pd.api.types.is_bool_dtype(dtype):
                    column_types[column] = "boolean"

                else:
                    column_types[column] = "categorical"

            return column_types

        except Exception as e:
            raise MyException(e, sys)
        