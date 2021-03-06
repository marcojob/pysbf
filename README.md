# pysbf

A Python module to read "Septentrio Binary Format" (SBF) files generated by Septentrio receivers.

## Dependencies

### Required:
* A C compiler (GCC preferred).
* Python 3.5+ (Make sure your C compiler can find the Python API `"Python.h"` header file)
* Cython


## Installation

A Python distutils **setup.py** script is included.
Run this script with the Python interpreter you would normally use.  
For example,
>python setup.py build  
>python setup.py install

## Release Notes

* Up to 100x times faster parsing (than pure Python, thanks to Cython). Python module is written in C and complied for C-like speeds.
* All blocks documented in documentation v1.13.0 are now supported.

## Usage

The basic function of this module is to parse every block inside a SBF file into a map.
Therefore, the `dict` built-in Python object is used to represent each block. 

### Functions

#### `load(f_obj, limit=-1, blocknames=set())`:
Returns a iterator/generator of SBF blocks.  
`f_obj` should be a file object.  

By default every type of block is generated, however most of the time only certain types
of blocks are needed. This can be accomplished by providing a set of block names to 
the `blocknames` parameter.  

`limit` limits the number of blocks generated.  


## Examples

Print the block name for the first 100 blocks:

```python
import pysbf
    
with open('./dummy.sbf') as sbf_fobj:
 for blockName, block in pysbf.load(sbf_fobj, limit=100):
  print blockName
```
      
Print the azimuth & elevation for each visible satellite using the first 100 *SatVisibility* blocks:

```python
import pysbf
    
with open('./dummy.sbf') as sbf_fobj:
 for blockName, block in pysbf.load(sbf_fobj, limit=100, blocknames={'SatVisibility'}):
  for satInfo in block['SatInfo']:
   print satInfo['SVID'], satInfo['Azimuth'], satInfo['Elevation']
```

Combine with matplotlib & numpy for plots. A simple plot of CPU load vs time using the first 100 *ReceiverStatus* blocks:

```python
import matplotlib.pyplot as plt
import numpy as np
import pysbf as sbf
    
with open('./dummy.sbf') as sbf_fobj:
 cpuload = ( '{} {}\n'.format(b['TOW'], b['CPULoad']) for bn, b in sbf.load(sbf_fobj, 100, {'ReceiverStatus_v2'}) )
 data = np.loadtxt(cpuload)
 plt.xlabel('Time (ms)')
 plt.ylabel('CPU Load (%)')
 plt.plot(data[:,0], data[:,1])
 plt.show()
```
