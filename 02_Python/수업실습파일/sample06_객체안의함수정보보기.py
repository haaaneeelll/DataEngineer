

# 객체안의 함수 보기
print(dir(str)) # 문자열 객체(클래스), str
'''
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

print(dir(list)) # 리스트 객체(클래스), list
'''
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
'pop', 'remove', 'reverse', 'sort']
'''
print(dir(tuple)) # 튜플 객체(클래스), tuple , 수정할 함수가 제공안됨.
'''
'count', 'index'
'''
print(dir(set))  # 셋 객체(클래스), set
'''
'add', 'clear', 'copy', 'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 'isdisjoint', 
'issubset', 'issuperset', 'pop', 
'remove', 'symmetric_difference', 'symmetric_difference_update', 
'union', 'update'
'''
print(dir(dict)) # 디트(딕셔너리) 객체(클래스), dict
'''
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
 'pop', 'popitem', 'setdefault', 'update', 'values'
'''

print(dir(int))
'''
'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 
'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'
'''


### 빌트인즈 객체 ==> . 없이  사용가능
print(dir(__builtins__))
'''
['ArithmeticError', 'AssertionError', 'AttributeError', 
'BaseException', 'BlockingIOError', 'BrokenPipeError', 
'BufferError', 'BytesWarning', 'ChildProcessError', 
'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 
'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 
'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 
'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 
'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 
'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 
'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 
'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 
'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 
'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 
'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 
'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 
'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 
'ZeroDivisionError', 
'abs', 'all', 'any', 'ascii', 'bin', 'bool', 
'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 
'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 
'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 
'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 
'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 
'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 
'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 
'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 
'tuple', 'type', 'vars', 'zip']
'''