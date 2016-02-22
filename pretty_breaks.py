import math

def rpretty(dmin, dmax, n=5):
  """
  R's pretty algorithm implemented in Python
  Code based on R implementation from 'labeling' R package 
  
  Compute a sequence of about 'n+1' equally spaced 'round' values
  which cover the range of the values in 'values'.  The values are chosen
  so that they are 1, 2 or 5 times a power of 10.

  Parameters:
    dmin        : minimum of the data range
    dmax        : maximum of the data range
    n           : number of class intervals
  """

  min_n = int(n / 3) # Nonnegative integer giving the minimal number of intervals
  shrink_sml = 0.75  # Positive numeric by a which a default scale is shrunk 
                     # in the case when range(x) is very small (usually 0).
  high_u_bias = 1.5  # Non-negative numeric, typically > 1. The interval unit 
                     # is determined as {1,2,5,10} times b, a power of 10.
                     # Larger high.u.bias values favor larger units
  u5_bias = 0.5 + 1.5 * high_u_bias
                     # Non-negative numeric multiplier favoring 
                     # factor 5 over 2.
  h = high_u_bias
  h5 = u5_bias
  ndiv = n

  dx = dmax - dmin
  if dx == 0 and dmax == 0:
    cell = 1.0
    i_small = True
    U = 1
  else:
    cell = max(abs(dmin), abs(dmax))
    if h5 >= 1.5 * h + 0.5:
      U = 1 + (1.0/(1 + h))
    else:
      U = 1 + (1.5 / (1 + h5))
    i_small = dx < (cell * U * max(1.0, ndiv) * 1e-07 * 3.0)

  if i_small:
    if cell > 10:
      cell = 9 + cell / 10
      cell = cell * shrink_sml
    if min_n > 1:
      cell = cell / min_n
  else:
    cell = dx
    if ndiv > 1:
      cell = cell / ndiv
  if cell < 20 * 1e-07:
    cell = 20 * 1e-07
  
  base = 10.0**math.floor(math.log10(cell))
  unit = base
  if (2 * base) - cell < h * (cell - unit):
    unit = 2.0 * base
    if (5 * base) - cell < h5 * (cell - unit):
      unit = 5.0 * base
      if (10 * base) - cell < h * (cell - unit):
        unit = 10.0 * base
  # Maybe used to correct for the epsilon here??
  ns = math.floor(dmin / unit + 1e-07)
  nu = math.ceil(dmax / unit - 1e-07)

  # Extend the range out beyond the data. Does this ever happen??
  while ns * unit > dmin + (1e-07 * unit):
    ns = ns-1
  while nu * unit < dmax - (1e-07 * unit):
    nu = nu+1
  # If we don't have quite enough labels, extend the range out to make more (these labels are beyond the data :( )
  k = math.floor(0.5 + nu-ns)
  if k < min_n:
    k = min_n - k
    if ns >= 0:
      nu = nu + k / 2
      ns = ns - k / 2 + k % 2
    else:
      ns = ns - k / 2
      nu = nu + k / 2 + k % 2
    ndiv = min_n
  else:
    ndiv = k
  graphmin = ns * unit
  graphmax = nu * unit
  count = int(math.ceil(graphmax - graphmin)/unit)
  res = [graphmin + k*unit for k in range(count+1)]
  if res[0] < dmin:
    res[0] = dmin
  if res[-1] > dmax:
    res[-1] = dmax
  return res
  
def jenks(values, classes=5):
  """
  Jenks Optimal (Natural Breaks) algorithm implemented in Python.
  The original Python code comes from here:
  http://danieljlewis.org/2010/06/07/jenks-natural-breaks-algorithm-in-python/
  and is based on a JAVA and Fortran code available here:
  https://stat.ethz.ch/pipermail/r-sig-geo/2006-March/000811.html
  
  Returns class breaks such that classes are internally homogeneous while 
  assuring heterogeneity among classes.
  
  """

  values.sort()
  mat1 = []
  for i in range(0,len(values)+1):
    temp = []
    for j in range(0,classes+1):
        temp.append(0)
    mat1.append(temp)
  mat2 = []
  for i in range(0,len(values)+1):
    temp = []
    for j in range(0,classes+1):
        temp.append(0)
    mat2.append(temp)
  for i in range(1,classes+1):
    mat1[1][i] = 1
    mat2[1][i] = 0
    for j in range(2,len(values)+1):
        mat2[j][i] = float('inf')
  v = 0.0
  for l in range(2,len(values)+1):
    s1 = 0.0
    s2 = 0.0
    w = 0.0
    for m in range(1,l+1):
      i3 = l - m + 1
      val = float(values[i3-1])
      s2 += val * val
      s1 += val
      w += 1
      v = s2 - (s1 * s1) / w
      i4 = i3 - 1
      if i4 != 0:
        for j in range(2,classes+1):
          if mat2[l][j] >= (v + mat2[i4][j - 1]):
            mat1[l][j] = i3
            mat2[l][j] = v + mat2[i4][j - 1]
    mat1[l][1] = 1
    mat2[l][1] = v
  k = len(values)
  kclass = []
  for i in range(0,classes+1):
    kclass.append(0)
  kclass[classes] = float(values[len(values) - 1])
  kclass[0] = float(values[0])
  countNum = classes
  while countNum >= 2:
    id = int((mat1[k][countNum]) - 2)
    kclass[countNum - 1] = values[id]
    k = int((mat1[k][countNum] - 1))
    countNum -= 1
  return kclass
  