import numpy as np

def calculate(list):
  try:
    n = 3
    splited = []
    len_l = len(list)
    for i in range(n):
      start = int(i*len_l/n)
      end = int((i+1)*len_l/n)
      splited.append(list[start:end])
  
    arr = np.asarray(splited, dtype = object)
    mean_cols = []
    mean_lines = []
    
    var_cols = []
    var_lines = []
  
    std_cols = []
    std_lines = []
  
    max_cols = []
    max_lines = []
  
    min_cols = []
    min_lines = []
  
    sum_cols = []
    sum_lines = []
    
    for i in range(len(arr)):
      mean_cols.append(sum(arr[:, i])/len(arr[:, i]))
      mean_lines.append(sum(arr[i])/len(arr[i]))
      
      var_cols.append(np.var(arr[:, i]))
      var_lines.append(np.var(arr[i]))
  
      std_cols.append(np.std(arr[:, i]))
      std_lines.append(np.std(arr[i]))
  
      max_cols.append(np.max(arr[:, i]))
      max_lines.append(np.max(arr[i]))
  
      min_cols.append(np.min(arr[:, i]))
      min_lines.append(np.min(arr[i]))
  
      sum_cols.append(np.sum(arr[:, i]))
      sum_lines.append(np.sum(arr[i]))
  
    calculations = {
      'mean': [mean_cols, mean_lines, np.mean(list)],
      'variance': [var_cols, var_lines, np.var(list)],
      'standard deviation': [std_cols, std_lines, np.std(list)],
      'max': [max_cols, max_lines, np.max(list)],
      'min': [min_cols, min_lines, np.min(list)],
      'sum': [sum_cols, sum_lines, np.sum(list)]
    }
  
    return calculations
  except:
    raise ValueError( "List must contain nine numbers.")
    #return "List must contain nine numbers."