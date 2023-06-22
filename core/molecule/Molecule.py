import numpy
import typing  
import scipy.linalg

# class gto:
#   def __init__(self, shell: typing.List[int], exponents: typing.List[float], coefficients: typing.List[float], center: typing.List[float]) -> None:
#     self.shell          =   numpy.array(shell)
#     self.exponents      =   numpy.array(exponents)
#     self.coefficients   =   numpy.array(coefficients)
#     self.normcoeffs     =   numpy.zeros(self.coefficients.size)
#     self.center         =   numpy.array(center)

class Molecule:
  def __init__(self, atoms : typing.List[typing.Tuple[str, typing.Tuple[float, float, float]]], charge : int, multiplicity : int, basis: str) -> None:
    self.n_atoms      = len(atoms)
    self.geometry     = atoms
    self.charge       = charge
    self.muliplicity  = multiplicity
    self.basis_set    = basis
    self.exponents    = []
    self.coefficients = []
    self.shells       = []

  def read_basis(self):
    atom_names        = [row[0] for row in self.geometry]
    for atom in atom_names:
      with open("../basissets/{}-{}".format(atom, self.basis_set)) as basis_object:
        basis_data  = basis_object.readlines()
        for lnumber, line in enumerate(basis_data[1:]):
          if "S" in line and "P" not in line:
              nprims          =   int(line.split()[1])
              pgtodata        =   [x.replace('D', 'E').split() for x in basis_data[lnumber+2:lnumber+2+nprims]]
              exponents       =   [float(x[0]) for x in pgtodata]
              coefficients    =   [float(x[1]) for x in pgtodata]
              shell00         =   [0, 0, 0]

              self.shells.append(shell00)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)
          
          if "P" in line:
              nprims          =   int(line.split()[1])
              pgtodata        =   [x.replace('D', 'E').split() for x in basis_data[lnumber+2:lnumber+2+nprims]]
              coefficient1    =   [float(x[1]) for x in pgtodata]
              coefficient2    =   [float(x[2]) for x in pgtodata]
              exponents       =   [float(x[0]) for x in pgtodata]
              shell00         =   [0, 0, 0]
              shell11         =   [1, 0, 0]
              shell12         =   [0, 1, 0]
              shell13         =   [0, 0, 1]
            
              self.shells.append(shell00)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

              self.shells.append(shell11)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

              self.shells.append(shell12)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

              self.shells.append(shell13)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

          if "D" in line and "+" not in line:
              nprims          =   int(line.split()[1])
              pgtodata        =   [x.replace('D', 'E').split() for x in basis_data[lnumber+2:lnumber+2+nprims]]
              exponents       =   [float(x[0]) for x in pgtodata]
              coefficients    =   [float(x[1]) for x in pgtodata]
              shell20         =   [2, 0, 0]
              shell21         =   [1, 1, 0]
              shell22         =   [1, 0, 1]
              shell23         =   [0, 2, 0]
              shell24         =   [0, 1, 1]
              shell25         =   [0, 0, 2]

              self.shells.append(shell20)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

              self.shells.append(shell21)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

              self.shells.append(shell22)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

              self.shells.append(shell23)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

              self.shells.append(shell24)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)

              self.shells.append(shell25)
              self.exponents.append(exponents)
              self.coefficients.append(coefficients)