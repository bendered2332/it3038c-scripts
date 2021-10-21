# LAB 7
Here is how you can run a Python script that I created, which uses a plugin called numpy.
Numpy is a package that is used primarily for array computing 

First, let's download numpy with the command.

```bash
pip install numpy
```

Now, find an image you want to use. It can be anything, really. In fact, if we're smart, we can do it all from the command line. 

Download an image from the internet and save it to your hard drive. 

Now, in Python, run the following code:

```python
from PIL import Image,ImageFilter
myImage = Image.open('/full/path/to/image.jpg')
myImage.load
```

The syntax above will load the image. Now we can run several commands against it to get format and size, and even show the image.

```python
myImage.format
myImage.size
myImage.show()
```

Finally, we can use the ImageFilter module to apply a filter to it and show it, like so...

```python
blur = myImage.filter(ImageFilter(BLUR)).show()
quit()
```

I hope that was fun. Don't forget to deactivate your virtualenv when you're done.

```bash
deactivate
```