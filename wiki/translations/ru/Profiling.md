

## Описание

Profiling the code of FreeCAD helps find bottlenecks in the algorithms used to create or manipulate objects.

To profile [Python](Python.md) code use the standard `cProfile` module to define start and end points to profile in the code. 
```python
import cProfile
pr = cProfile.Profile()
pr.enable()

# --------------------------------------
# Lines of code that you want to profile
# --------------------------------------

pr.disable()
pr.dump_stats("/tmp/profile.cprof")
```

Then install and use `pyprof2calltree` to convert the profile output into cachegrind input. 
```python
pyprof2calltree -i /tmp/profile.cprof -o /tmp/callgrind.out
```

Then visualize this information with `kcachegrind` for Linux or `qcachegrind` for Windows. 
```python
kcachegrind /tmp/callgrind.out
```

## Resources

-   [The Python profilers](https://docs.python.org/3/library/profile.html), `cProfile` and `python`.
-   [pyprof2calltree](https://pypi.org/project/pyprof2calltree/) at PyPI; [pyprof2calltree](https://github.com/pwaller/pyprof2calltree/) repository.
-   [FreeCAD\'s Python profiling tutorial](https://forum.freecadweb.org/viewtopic.php?f=10&t=44785).


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)