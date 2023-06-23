# print(dir(df))
'''
'T','abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'apply', 'applymap',
'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time',
'bfill', 'bool', 'boxplot', 'clip', 'col1', 'col2', 'col3', 'columns', 'combine', 'combine_first',
'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod',
'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna',
'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna',
'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby',
'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert',
'interpolate', 'isetitem', 'isin', 'isna', 'isnull', 'items', 'iterrows', 'itertuples', 'join', 'keys',
'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lt', 'mask', 'max', 'mean', 'median', 'melt',
'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull',
'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod',
'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis',
'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round',
'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape',
'shift', 'size', 'skew', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract',
'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather',
'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdown', 'to_numpy', 'to_orc', 'to_parquet',
'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray',
'to_xml', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unstack', 'update',
'value_counts', 'values', 'var', 'where', 'xs'
'''
## 3. DataFrame의 기본 함수
'''
   1. 값 변경                                  ==>  df.replace()
   2. 컬럼명 및 인덱스명 변경                     ==> df.rename(columns|index)
   3. 모든(특정) 컬럼(행)값의 참/거짓 여부          ==>  df.any() , df.all()
   4. 중복조회 및 제거                           ==>  df.duplicated(),  df.drop_duplicates()

   5. 임의의 함수 적용 ==> df.apply(함수, axis=0|1)
      임의의 함수를 한번에 DataFrame의 행과 열에 적용.

   7. 값이 있으면 True, 아니면 False ==> df.isin(집합형)
      ==> SQL의 in 연산자 동일
      
    8. unique한 값(종류)의 갯수 ==> df.nunique(dropna=True) 
                            dropna=False 면 nan 포함해서 갯수 반환
        
       df.nunique  ==> 갯수 반환
       series.unique ==> 값 반환                 
'''

import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame({ "a" : [0 ,10, 100],
                    "b" : [2, 20, 200],
                    "c" : [3, 20, 300]},
                    index = list('ABC'))
'''
     a    b    c
A    0    2    3
B   10   20   20
C  100  200  300
'''
print(df)
# 1. df.replace(dict, new값) ==> dict에 지정된 값을 new값으로 치환
new_df = df.replace({'a':100,'b':2,'c':[30,300]}, 999)
print(new_df)

# 2. df.replace(dict) ==> {old:new, old:new}
new_df = df.replace({20:2000, 3:3000})
print(new_df)

# 3. 컬럼명 및 인덱스명 변경
new_df = df.rename(columns={'a':'col1','b':'col2'})
new_df = df.rename(index={'A':'row1','B':'row2'})
print(new_df)


# 4.  모든(특정) 컬럼(행)값의 참/거짓 여부
x = df.all(axis=0) #  모든 컬럼값이 참이냐?
x = df.all(axis=1) #  모든 행값이 참이냐?

x = df.any(axis=0) #   하나라도 컬럼값이 참이냐?
x = df.any(axis=1) #  하나라도 행값이 참이냐?
print(x)


df = pd.DataFrame({"k1":['one']*3 + ['two']*4,
                  "k2":[1,1,2,3,3,4,4] })
print(df)
'''
   k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
'''
# 5. 중복 여부 확인
x = df.duplicated() # df에 중복된 행이냐?
print(x)
#6. 중복된 행 제거후 반환
new_df = df.drop_duplicates(ignore_index=True)
print(new_df)
'''
   k1  k2
0  one   1
1  one   2
2  two   3
3  two   4
'''

df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,60,100,100,80]})
print(df)
'''
  국어   수학
0  50  100
1  60  60
2  70  100
3  80  100
4  90  80
'''

# 7. df에 임의의 함수 적용 ==> callback 처리
x=df.apply(np.sum, axis=0)
x=df.apply(sum, axis=1)
x=df.apply(np.mean, axis=1)
print(x)

# 8. df.isin(집합형) - 중요, SQL의 in연산자와 비슷
new_df = df.isin([60,80]) #  df에서 60 또는 80이 있냐?
new_df = df.isin({"수학":[60,80]}) #  수학에서만 60 또는 80이 있냐?
print(new_df)


df = pd.DataFrame({ "col1" : [1 ,2, 2, None, 1],
                    "col2" : [2, 3, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 2, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
 col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   2.0   3.0   3.0   NaN
3   2.0   2.0   2.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''
# 9. unique한 값의 갯수 반환 - 기본적으로 null 제외
x = df.nunique(axis=0)
x = df.nunique(axis=1)

x = df.nunique(axis=0, dropna=False) # null 값 포함
x = df.nunique(axis=1, dropna=False) # null 값 포함
print(x)
