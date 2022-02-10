# cairocffi-stubs

This package contains type stubs to provide more precise static types and type inference for cairocffi.

## Installation

```
pip install cairocffi-stubs
```

## Usage

```python
from io import BytesIO
import cairocffi as cairo
import matplotlib.pyplot as plt

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 300, 200)
context = cairo.Context(surface)
context.show_text('Hello World! ')
img = BytesIO(surface.write_to_png())  # overloaded
plt.imshow(plt.imread(img))
plt.show()
```

Static type checker can correctly recognize the return type of `surface.write_to_png()` as `bytes` when passing no arguments. No type errors will be raised.

## Style Guidelines

Follow the same style guidelines as [typeshed](https://github.com/python/typeshed/blob/master/CONTRIBUTING.md).
