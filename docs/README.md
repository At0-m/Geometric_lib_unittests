# Geometric Lib

A tiny library for computing **areas** and **perimeters** of basic 2D shapes.


## Functions

### In `triangle.py`
- `area(a, h)` — area **by base and height**  
  Formula: `S = a * h / 2`  

- `perimeter(a, b, c)` — perimeter by three sides
  Formula: `P = a + b + c`
  ```py
  from triangle import area, perimeter
  area(3, 4)            # -> 6.0
  perimeter(3, 4, 5)    # -> 12

### In `square.py`
- `area(a)` — square area 
  Formula: `S = a * a`  
-  `perimeter(a)` — square perimeter
  Formula: `P = 4 * a`
  ```py
  from square import area, perimeter
  area(5)       # -> 25
  perimeter(5)  # -> 20

### In `rectangle.py`
- `area(a, b)` — rectangle area
  Formula: `S = a * b`  
  
- `perimeter(a, b)` — rectangle perimeter
  Formula: `P = 2 * (a + b)`
  ```py
  from rectangle import area, perimeter
  area(3, 5)       # -> 15
  perimeter(3, 5)  # -> 16

### In `circle.py`
- `area(r)` — circle area
  Formula: `S = π * r * r`
- `perimeter(r)` — circle circumference
  Formula: `P = 2 * π * r`
  ```py
  from circle import area, perimeter
  round(area(3), 2)      # -> 28.27
  round(perimeter(3), 2) # -> 18.85

## Usage

```python
from triangle import area as tri_area, perimeter as tri_perimeter
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as sq_area, perimeter as sq_perimeter
from circle import area as cir_area, perimeter as cir_perimeter

print(tri_area(3, 4))             # 6.0
print(tri_perimeter(3, 4, 5))     # 12

print(rect_area(3, 5))            # 15
print(rect_perimeter(3, 5))       # 16

print(sq_area(5))                 # 25
print(sq_perimeter(5))            # 20

print(round(cir_area(3), 2))      # 28.27
print(round(cir_perimeter(3), 2)) # 18.85
```

