
'''
Series 요소
'T', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 
'apply', 'argmax', 'argmin', 'argsort', 'array', 'asfreq', 'asof', 'astype', 'at', 'at_time', 
'attrs', 'autocorr', 'axes', 'backfill', 'between', 'between_time', 'bfill', 'bool', 'clip', 'combine', 
'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 
'cumsum', 'describe', 'diff', 'div', 'divide', 'divmod', 'dot', 'drop', 'drop_duplicates', 'droplevel', 
'dropna', 'dtype', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'ewm', 'expanding', 'explode', 'factorize', 
'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'ge', 'get', 'groupby', 'gt', 
'hasnans', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'interpolate', 
'is_monotonic_decreasing', 'is_monotonic_increasing', 'is_unique', 'isin', 'isna', 'isnull', 'item', 'items', 
'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lt', 'map', 'mask', 'max', 'mean', 
'median', 'memory_usage', 'min', 'mod', 'mode', 'mul', 'multiply', 'name', 'nbytes', 'ndim', 'ne', 'nlargest', 
'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'plot', 'pop', 'pow', 'prod', 'product', 
'quantile', 'radd', 'rank', 'ravel', 'rdiv', 'rdivmod', 'reindex', 'reindex_like', 'rename', 'rename_axis', 
'reorder_levels', 'repeat', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 
'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'searchsorted', 'sem', 'set_axis', 'set_flags', 'shape', 'shift', 
'size', 'skew', 'sort_index', 'sort_values', 'squeeze', 'std', 'str', 'sub', 'subtract', 'sum', 'swapaxes', 
'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_frame', 'to_hdf', 'to_json', 
'to_latex', 'to_list', 'to_markdown', 'to_numpy', 'to_period', 'to_pickle', 'to_sql', 'to_string', 'to_timestamp', 
'to_xarray', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unique', 'unstack', 
'update', 'value_counts', 'values', 'var', 'view', 'where', 'xs'

'''










## 2. Series의 기술통계관련 함수
'''
  1. 최대(소)값         ==>  df['컬럼'].max(), df['컬럼'].min()

     누적최대(소)값,     ==>  df['컬럼'].cummax(), df['컬럼'].cummin()
      최대(소)값label   ==>  df['컬럼'].idxmax(), df['컬럼'].idxmin()
  2. (누적)합계         ==>  df['컬럼'].sum(), df['컬럼'].cumsum()
      평균              ==>  df['컬럼'].mean()
      중앙값            ==>  df['컬럼'].median()
      (누적)곱          ==>  df['컬럼'].prod(), df['컬럼'].cumprod()
  3. 사분위             ==>  df.quantile()
     분산               ==>  df['컬럼'].var()
      표준편차           ==>  df['컬럼'].std()
  4. count(갯수)         ==>  df['컬럼'].count()
  5. 통합 통계           ==>  df['컬럼'].describe()

'''

import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame({"col1" : [4 ,6, 9, 5, 15],
                   "col2" : [16, 8, np.nan, 6, 6],
                   "col3" : [10, 11, 12, 12, 12]},
                    index = list("ABCDE"))
'''
    col1  col2  col3
A     4  16.0    10
B     6   8.0    11
C     9   NaN    12
D     5   6.0    12
E    15   6.0    12
'''
print(df)
# 1. 행을 축으로 최대/최소값 구하기 (컬럼별)
x = df['col1'].max(axis=0) # axis=0  위/아래,
x = df['col1'].min(axis=0) # axis=0  위/아래,

# 3. 행을 축으로 누적최대/누적최소 구하기 (컬럼별)
x = df['col1'].cummax(axis=0)
x = df['col1'].cummin(axis=0)

# 4. 행을 축으로 최대/최소값 라벨(인덱스라벨) 구하기 (컬럼별)
x = df['col1'].idxmax(axis=0)
x = df['col1'].idxmin(axis=0)
print(x)

# 5. 행을 축으로 총합/누적총합 구하기 (컬럼별) -  중요
x = df['col1'].sum(axis=0)
x = df['col1'].cumsum(axis=0)
print(x)


# 6. 행/컬럼을 축으로 평균 구하기
x = df['col1'].mean(axis=0)

# 7. 행/컬럼을 축으로 중앙값 구하기
x = df['col1'].median(axis=0)

# 8. 행/컬럼을 축으로 곱연산 구하기
x = df['col1'].prod(axis=0)

# 9. 행/컬럼을 축으로 분산 구하기
x = df['col1'].var(axis=0)

# 10. 행/컬럼을 축으로 표준편차 구하기
x = df['col1'].std(axis=0)

# 11. 행/컬럼을 축으로 갯수 구하기 ( 기본적으로 null 제외 )
x = df['col1'].count(axis=0)