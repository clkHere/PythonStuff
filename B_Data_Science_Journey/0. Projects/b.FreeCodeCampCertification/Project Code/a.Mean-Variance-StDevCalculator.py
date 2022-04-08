import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError('List must contain nine numbers.')
  matx = np.array(list).reshape(3,3)  
  d = {
    'mean': [ np.mean(matx, axis=0).tolist(), np.mean(matx, axis=1).tolist(), np.mean(matx).tolist()],
    'variance': [ np.var(matx, axis=0).tolist(), np.var(matx, axis=1).tolist(), np.var(matx).tolist() ],
    'standard deviation': [ np.std(matx, axis=0).tolist(), np.std(matx, axis=1).tolist(), np.std(matx).tolist() ], 
    'max': [ np.amax(matx, axis=0).tolist(), np.amax(matx, axis=1).tolist(), np.amax(matx).tolist() ],
    'min': [ np.amin(matx, axis=0).tolist(), np.amin(matx, axis=1).tolist(), np.amin(matx).tolist() ],
    'sum': [ np.sum(matx, axis=0).tolist(), np.sum(matx, axis=1).tolist(), np.sum(matx).tolist() ],
      }
  return d
