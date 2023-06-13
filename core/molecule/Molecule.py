import  numpy  as  np
import  scipy.linalg  as linalg

class Molecule:
  def __init__(self, atoms : list, charge : int, multiplicity : int, symmetry : bool):
    self.natoms  =  len(atoms)
    self.charge  =  charge
    self.multiplicity  =  multiplicity
    self.geometry  =  {}
    for atomindex, atom in enumerate(atoms):
        atomname  =  atom[0]
        atomcoord  =  [float(x) for x in atom[1:]]
        self.geometry[atomname + str(atomindex)] = atomcoord
