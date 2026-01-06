dic={'accident_risk': {'metrics': {'count': 517754,
                               'max': 1.0,
                               'mean': 0.35238,        
                               'median': 0.34,
                               'min': 0.0,
                               'missing_percentage': 0,
                               'std': 0.16642},        
                   'raw_dtype': 'float64',
                   'semantic_type': 'numeric'}
                   }
x={}
for d,c in dic.items():
    # metrics = col_data['metrics']
    # raw_dtype = col_data['raw_dtype']
    # semantic_type = col_data['semantic_type']
    # print(col_data.get('metrics',{}))
    # print(col_name)
    # m=col_name.get('raw_dtype')
    # print(m['mean'])
    # print(col_name )
    x[d]=c
    print(x)
    # print(d.get('semantic_type'))
from app.constants.values import NUMERIC_THRESHOLDS

print(NUMERIC_THRESHOLDS['mean_pct_change'])