# LAB 7
Here is how you can run a Python script that I created, which uses a plugin called numpy.
Numpy is a package that is used primarily for array computing 

First, let's download numpy with the command.

```bash
pip install numpy
```

Now, lets import the numpy module with the code 
```bash
import numpy as np
```
In order to initialize an array you can do the following
```bash
a = np.array([1, 2, 3], dtype='int32')
print(a)
```

You can also initialize more complex arrays such as a 2d array of floats.
```bash
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)
```
The following code demostrates some information that numpy can return about these arrays.
```bash
# Get Dimension - Returns the demension type of array 
print(a.ndim)
# 1

# Get Shape - Returns the amount of rows and columns in the array.
print(b.shape)
# 2,3

# Get Type - Reurns the data type of the array.
print(a.dtype)
# dtype('int32)

# Get Size - Returns the amount of bytes used.
print(a.itemsize)
# 4

# Get total size - Returns the amount of bits used.
print(a.nbytes)
# 12 
```

This is the very basics of numpy but the main reason to use numpy is that is faster while performing mathematical operations compared to base python. It an essential package and has been used in many scientific achievements, and example of this would be the photo of the black hole that was taken recently.