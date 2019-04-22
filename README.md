# Mandelpy

A python library for exploring the Mandelbrot Set

## Getting Started

Mandelpy is an easy to use library that gives you the opportunity to navigate the Mandelbrot Set, it needs just few parameters to work giving you gorgeous resoults.

### Prerequisites

Mandelpy has just two dependencies, numpy and Pillow, to install them via pip:

```
pip install numpy
pip install Pillow
```

### Installing

The easiest way to install Mandelpy is with pip, just type in the command

```
pip install mandelpy
```

alternativly the whole source code can be found at the following [GitHub link](https://github.com/MatteoMagri/Mandelpy)


## Usage

Mandelpy implements just one class, the MandelbotSet one, this class defines a pecise position, a zoom value, the size of the picture and the unit pixel of the picture.

### Example

To create the easiest picture of the Mandelbrot Set, just call the image() function:

```
form mandelpy import MandelbrotSet as MS

m = MS()
m.image()
```

this will create an image of the Mandelbrot Set, anywhen you want to create the image call the image() function.

If you want to change the position of the view use the function coordinates()

```
m.coordinate(x,y)
```

to change the size:

```
m.size(x,y)
```

and the zoom:

```
m.zoom(zoom_value)
```
notice that the zoom value is the negative natural logarithm of the radius of the photo, to set the radius instead use ``` m.radius = r_value```

changeing the image name is also very easy:

```
m.set_name(picture_name)
```

to change the iteration number for the Mandelbrot Set calculator (normaly set on 100)

```
m.definition = # of iteration
```

is even possible to change the pattern unit of the Mandelbrot

```
m.typo(path_to_the_image)
```

notice that will be in grey scale.

In some cases the image may take a while to render, to help out is available a printed workflow, just add the True parameter in the image() function

```
m.image(True)
``` 
	
## Authors

* **Matteo Magri** - *Initial work* - [MatteoMagri](https://github.com/MatteoMagri)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/MatteoMagri/Mandelpy/blob/master/LICENCE.txt) file for details
