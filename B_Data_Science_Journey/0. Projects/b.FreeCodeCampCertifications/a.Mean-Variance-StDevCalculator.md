<h1 align="center"> Mean-Variance-Standard Deviation Calculator </h1>
In this project I'll create a function named <code>calculate()</code> that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a <b>3x3</b> matrix.


  <ins>Specs</ins>:
  - The input of the function should be a list containing 9 digits. 
    - If a list containing <ins>less than</ins> 9 digits is passed into the function, it should raise a `ValueError` exception with the message:<br> `List must contain nine numbers.`
    - The values in the returned dictionary should be lists and not numpy arrays. 
  - The function should convert the list into a 3x3 numpy array, then return a dictionary containing the: <b> mean | variance | standard deviation | max | min | sum</b> along both axes and for the flattened matrix. 

<HR NOSHADE="noshade"></HR>

<ins>My Pseudocode</ins>

```
import numpy as np
import sys

DEFINE calculate(LIST):
    IF len(LIST) is less than 9 : 
      raise ValueError ('List must contain nine numbers')        
    DECLARE matrix variable and assign it: np.array(LIST).reshape(3,3) to create a numpy 3x3 matrix    
    
    *CREATE a dictionary that sets --
     calculation_id(cID) as keys : numpy calculations(nCalc) as values --
     which are converted back to a python list*
                
    DECLARE dict = {
        'mean': [ 
                  [nCalc.mean(matrix, axis=0).tolist()], 
                  [nCalc.mean(matrix, axis=1).tolist()], 
                  nCalc.mean(matrix)
                ]
        'variance': [ 
                      [nCalc.var().tolist()], 
                      [nCalc.var().tolist()], 
                      nCalc.var().tolist()
                    ]
        'standard deviation': [ 
                                [nCalc.std().tolist()], 
                                [nCalc.std().tolist()], 
                                nCalc.std().tolist()
                              ]
        'max': [ [...], [...], ... ]
        'min': [ [...], [...], ... ]
        'sum': [ [...], [...], ... ]
    }
    
    return dict
```
   
<h3>My Solution</h3>

```python
import numpy as np

def calculate(list):
  #Make sure we can actually work with the parameter...
  #Exception Handling
  if len(list)<9:
    raise ValueError('List must contain nine numbers.')
    
  #Conversion to Numpy array & 3x3 Matrix
  matx = np.array(list).reshape(3,3)
  
  #Creation of -- {identification keys : numpyCalculation.tolist()}
  d = {
    'mean': [ np.mean(matx, axis=0).tolist(), np.mean(matx, axis=1).tolist(), np.mean(matx).tolist()],
    'variance': [ np.var(matx, axis=0).tolist(), np.var(matx, axis=1).tolist(), np.var(matx).tolist() ],
    'standard deviation': [ np.std(matx, axis=0).tolist(), np.std(matx, axis=1).tolist(), np.std(matx).tolist() ], 
    'max': [ np.amax(matx, axis=0).tolist(), np.amax(matx, axis=1).tolist(), np.amax(matx).tolist() ],
    'min': [ np.amin(matx, axis=0).tolist(), np.amin(matx, axis=1).tolist(), np.amin(matx).tolist() ],
    'sum': [ np.sum(matx, axis=0).tolist(), np.sum(matx, axis=1).tolist(), np.sum(matx).tolist() ],
      }
  return d
```
        
    
             
            
