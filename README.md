## **planck**
<div style='text-align: justify;'>
Planck is a rewrite of the older <a href="https://github.com/HemanthHaridas/plank.py">plank.py</a> project, aiming to take advantage of the modular design and efficient use of python libraries with minimal external bindings written in C++ and (or) Fortran. This code is not aimed at being as optimized or efficient as the commerically avaialble quantum chemistry codes like Gaussian, Orca or NWChem, but is meant to provide a toy model for the regular users to teach quantum chemistry and (or) build their own codes based on this library.
</div>

### **Usage Instructions**

To build a molecule, you must first import the ```Molecule``` class from planck library. For example to construct a Hydrogen molecule, you can do the following:

```python
from planck.core.molecule.Molecule import Molecule

hydrogen_mol = Molecule(atoms = [["H", (0.00, 0.00, 0.00)], ["H", (0.73, 0.00, 0.00)]], charge = 0, multiplicity = 1, basis = "sto-3g")
```
This will generate a molecule object with the specified parameters. The code currently supports ```sto-3g```, 3-21g and 6-31g basis sets.   