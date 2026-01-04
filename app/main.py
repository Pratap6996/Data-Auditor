from app.core.ingestion.loader import DataIngestion
from app.constants.values import DATA_FILE_PATH
from app.core.utils.type_detection import DataTypeAnalyzer
from app.core.profiling.profiler import Profiler
# print(dir(app.constants.values))
# x=DataIngestion(DATA_FILE_PATH)
# x=x.load_data()
# y=DataTypeAnalyzer(x)
# column=y.infer_semantic_types()

# column_profile=Profiler(

# Step 1: Load data
ingestor = DataIngestion(DATA_FILE_PATH)
df = ingestor.load_data()

# Step 2: Detect semantic types
types = DataTypeAnalyzer(df).infer_semantic_types()

# Step 3: Profile all columns
column_profiles = Profiler(df, types).run_all()

# Step 4: Inspect
import pprint
pprint.pprint(column_profiles)

