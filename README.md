# Drawing using Bezier Curves

Buat jalanin, harus extract the interpolation points dulu. Bisa modify berapa interpolating pointsnya (resolusinya) by modifying the `N` value in `find_interpolation_points.py`.

extract interpolation points,

```
python find_interpolation_points.py
```

lalu buka octave,

```
P = importdata('bezier_segments.txt')
bezierdrawpoints(P)
```
