def data_types():
    a = 1                # int
    b = "Hello"          # str
    c = 3.14             # float
    d = True             # bool
    e = [1, 2, 3]        # list
    f = {"key": "value"} # dict
    g = (1, 2, 3)        # tuple
    h = {1, 2, 3}        # set

    types = [type(a).__name__, type(b).__name__, type(c).__name__, type(d).__name__, type(e).__name__, type(f).__name__, type(g).__name__, type(h).__name__]
    print(f"[{', '.join(types)}]")

if __name__ == '__main__':
  data_types()