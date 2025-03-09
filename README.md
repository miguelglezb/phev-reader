# phev-reader
> Module to read .ev text files.


This Python module reads .ev files, which are made by the [Phantom](https://github.com/danieljprice/phantom) code. The data is stored as [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html). 

## Documentation

Full documentation of **phev-reader** can be found [here](https://phev-reader.readthedocs.io/en/latest/).

## Installation: 

```bash
pip install phev-reader
```

## Structure of a .ev file

These files are typically in a table form:

```text
# [ 1         time]     [ 2total energy ]     [ 3  pot energy ]     ...
    0.00000000000E+00    -9.15160740747E-03    -1.79950917829E-02   ...
    ...                 ...                   ...
```


## Examples

**phev-reader** can be used from a jupyter notebook or python script:

```python
import phev

phdf = phev.evreader('energy.ev')
```

By default, this function prints the headers of the file, which are also stored as keys for the dataframe:

```python
['time', 'total energy', 'pot energy', 'kin energy', 'therm energy', 'sink pot', 'sink kin', 'sink orb', 'comp orb', 'env pot', 'env energy', 'bound kin', 'unbound kin', 'bound mass', 'unbound mass', 'p-p pot', 'p-s pot', 'tot ang mom', 'b ang mom', 'ub ang mom', 'orb ang mom', 'gas energy', 'fallback', 'fallback mom']
```

If phev is run from a jupyter notebook:
```python
In [2]: phdf
Out[2]: 
          time  total energy  pot energy  kin energy  therm energy  sink pot  sink kin  sink orb  ...   p-s pot  tot ang mom  b ang mom  ub ang mom  orb ang mom  gas energy  fallback  fallback mom
0          0.0     -0.009152   -0.017995    0.000931      0.007912 -0.000615  0.000768  0.000154  ... -0.011739    15.804520   2.753940    0.000000    13.050580   -0.011576       0.0           0.0
1         50.0     -0.009152   -0.017994    0.000931      0.007912 -0.000615  0.000768  0.000154  ... -0.011738    15.804525   2.752241    0.000000    13.052284   -0.011575       0.0           0.0
2        100.0     -0.009152   -0.017993    0.000931      0.007911 -0.000615  0.000768  0.000154  ... -0.011737    15.804530   2.752194    0.000000    13.052336   -0.011575       0.0           0.0
3        150.0     -0.009152   -0.017993    0.000931      0.007910 -0.000615  0.000768  0.000154  ... -0.011737    15.804537   2.752197    0.000000    13.052340   -0.011575       0.0           0.0
4        200.0     -0.009152   -0.017992    0.000931      0.007910 -0.000615  0.000768  0.000154  ... -0.011737    15.804543   2.752238    0.000000    13.052305   -0.011574       0.0           0.0
...        ...           ...         ...         ...           ...       ...       ...       ...  ...       ...          ...        ...         ...          ...         ...       ...           ...
6996  349800.0     -0.009194   -0.018549    0.007892      0.001463 -0.012831  0.006697 -0.006134  ... -0.005224    15.811252   6.786975    7.449286     1.574991   -0.004029       0.0           0.0
6997  349850.0     -0.009194   -0.018701    0.008045      0.001462 -0.012982  0.006848 -0.006134  ... -0.005225    15.811252   6.780038    7.456772     1.574443   -0.004029       0.0           0.0
6998  349900.0     -0.009194   -0.018760    0.008105      0.001461 -0.013041  0.006907 -0.006134  ... -0.005225    15.811252   6.772186    7.464296     1.574770   -0.004028       0.0           0.0
6999  349950.0     -0.009194   -0.018713    0.008059      0.001460 -0.012997  0.006862 -0.006135  ... -0.005223    15.811252   6.764819    7.470044     1.576390   -0.004026       0.0           0.0
7000  350000.0     -0.009194   -0.018571    0.007918      0.001459 -0.012858  0.006721 -0.006137  ... -0.005220    15.811252   6.753799    7.477806     1.579647   -0.004024       0.0           0.0

[7001 rows x 24 columns]

```
