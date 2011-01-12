"""
Vector class for Lgm

@author: Brian Larsen
@organization: LANL
@contact: balarsen@lanl.gov

@version: V1: 20-Dec-2010 (BAL)
"""


import ctypes
import itertools
import copy

import Lgm
from Lgm_Types import LgmDouble
from _Lgm import lib

class Lgm_Vector(ctypes.Structure):
    """
    Lgm_Vector class to wrap up the LanlGeoMag routines and add methods

    @todo: partilly finished as an example

    @ivar x: x-component of the vector
    @type x: double
    @ivar y: y-component of the vector
    @type y: double
    @ivar z: z-component of the vector
    @type z: double

    @todo: __eq__ forks vector==list but no others

    @author: Brian Larsen
    @organization: LANL
    @contact: balarsen@lanl.gov

    @version: V1: 22-Dec-2010 (BAL)
    """
    @classmethod
    def assign_fields(cls):
        cls._fields_ = [ ( "x", LgmDouble ),
            ("y", LgmDouble),
            ("z", LgmDouble) ]

    def __eq__(self, other):
        """
        if the components of a Vector are equal the vectors are equal
        """
        if isinstance(other, Lgm_Vector):
            if other.x != self.x:
                return False
            elif other.y != self.y:
                return False
            elif other.z != self.z:
                return False
            else:
                return True
        elif isinstance(other, list):
            try:
                other = Lgm_Vector(other[0], other[1], other[2])
            except:
                raise(TypeError('Bad type: %s in __eq__ comparison' % (type(other)) ))
            else:
                return self == other
        else:
            raise(TypeError('Bad type: %s in __eq__ comparison' % (type(other)) ))

    def __gt__(self, other):
        """
        if the magnitude is greater the vector is greater
        """
        # done this way because diffMag is not signed
        m1 = self.magnitude()
        m2 = other.magnitude()
        if m1 > m2:
            return True
        else:
            return False

    def __lt__(self, other):
        """
        if the magnitude is greater the vector is greater
        """
        # done this way because diffMag is not signed
        m1 = self.magnitude()
        m2 = other.magnitude()
        if m1 < m2:
            return True
        else:
            return False

    def __le__(self, other):
        """
        if the magnitude is greater the vector is greater
        """
        # done this way because diffMag is not signed
        m1 = self.magnitude()
        m2 = other.magnitude()
        if m1 <= m2:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        if the magnitude is greater the vector is greater
        """
        # done this way because diffMag is not signed
        m1 = self.magnitude()
        m2 = other.magnitude()
        if m1 >= m2:
            return True
        else:
            return False

    def __str__(self):
        """
        print out the Lgm_Vector as a list

        @return: List repersentation of the components
        @rtype: str

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        return str([self.x, self.y, self.z])

    def __repr__(self):
        """
        print out the Lgm_Vector as a list

        @return: Name of the vector object
        @rtype: str

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        return str([self.x, self.y, self.z])

    def __getattr__(self, other):
        """
        getattr used for easy access to some methods (mag)

        @param other: attr to get from the object (mag)

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        if other == 'mag':
            self.mag = self.magnitude()
        else:
            raise AttributeError(other)

    def __add__(self, other):
        """
        add two vectors together or add a scaler to each component

        @param other: other vector or scalar to add to vector
        @type other: (Lgm_Vector, int, long, float)

        @return: new vector
        @rtype: Lgm_Vector

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        if isinstance(other, Lgm_Vector): # an other vector
            o_vec = Lgm_Vector()
            lib.Lgm_VecAdd(o_vec, self, other)
            return o_vec
        elif isinstance(other, (int, float, long)):
            x = self.x + other
            y = self.y + other
            z = self.z + other
            return  Lgm_Vector(x, y, z)
        else:
            raise(ArithmeticError("Cannot add type %s to a Lgm_Vector" % (type(other))))

    def __sub__(self, other):
        """
        subtract two vectors or subtract a scaler from each component

        @param other: other vector or scalar to subtract from vector
        @type other: (Lgm_Vector, int, long, float)

        @return: new vector
        @rtype: Lgm_Vector

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        if isinstance(other, Lgm_Vector): # an other vector
            o_vec = Lgm_Vector()
            lib.Lgm_VecSub(o_vec, self, other)
            return o_vec
        elif isinstance(other, (int, float, long)):
            x = self.x - other
            y = self.y - other
            z = self.z - other
            return  Lgm_Vector(x, y, z)
        else:
            raise(ArithmeticError("Cannot subtract %s from a Lgm_Vector" % (type(other))))

    def __mul__(self, other):
        """
        compute the cross product of two vectors or multi a scalar to each component

        @param other: other vector or scalar to cross product or multiply to vector
        @type other: (Lgm_Vector, int, long, float)

        @return: new vector
        @rtype: Lgm_Vector

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        if isinstance(other, Lgm_Vector): # an other vector
            return self.crossProduct(other)
        elif isinstance(other, (int, float, long)):
            x = self.x * other
            y = self.y * other
            z = self.z * other
            return Lgm_Vector(x, y, z)
        else:
            raise(ArithmeticError("Cannot subtract %s from a Lgm_Vector" % (type(other))))

    def __div__(self, other):
        """
        divide a scalar into each component

        @param other: scalar to divide into vector
        @type other: (int, long, float)

        @return: new vector
        @rtype: Lgm_Vector

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        if isinstance(other, (int, float, long)):
            x = self.x / other
            y = self.y / other
            z = self.z / other
            return Lgm_Vector(x, y, z)
        else:
            raise(ArithmeticError("Cannot subtract %s from a Lgm_Vector" % (type(other))))

    def tolist(self):
        """
        change an Lgm_Vector to a list
        """
        return [self.x, self.y, self.z]

    def crossProduct(self, other):
        """
        compute the cross product of two vectors

        @param other: other vector to cross prod (on the right)
        @type other: Lgm_Vector
        @return: the cross product of the 2 vectors
        @rtype: Lgm_Vector

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        o_vec = Lgm_Vector()
        lib.Lgm_CrossProduct(self, other, o_vec)
        return o_vec

    def magnitude(self):
        """
        return the magnitude of the vector

        @return: Magnitude of the vector
        @rtype: double

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        return lib.Lgm_Magnitude( self)

    def normalize(self):
        """
        Normalize the vector in place

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        lib.Lgm_NormalizeVector( self )

    def dotProduct(self, other):
        """
        compute the dot product of two vectors

        @param other: other vector to cross prod (on the right)
        @type other: Lgm_Vector
        @return: the cross product of the 2 vectors
        @rtype: Lgm_Vector

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        return lib.Lgm_DotProduct(self, other)

    def scale(self, val):
        """
        Scale a vector by a scalar

        @param val: the value to scale the vector by
        @type val: (int, long, float)

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        lib.Lgm_ScaleVector( self, val)

    def diffMag(self, other):
        """
        Find Magnitude of difference between to vectors

        @param other: other vector to compare
        @type other: Lgm_Vector
        @return: difference in magnitudes
        @rtype: float

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        return lib.Lgm_VecDiffMag(self, other)

    def forceMagnitude(self, val):
        """
        Force the vector to have a given magnitude inplace

        @param val: the value for the new magnitude
        @type val: (int, long, float)

        @author: Brian Larsen
        @organization: LANL
        @contact: balarsen@lanl.gov

        @version: V1: 22-Dec-2010 (BAL)
        """
        lib.Lgm_ForceMagnitude(self, val)

def SphToCart(lat, lon, rad):
    """takes an input Lat, Lon, Rad and returns x, y, z"""
    vec1 = Lgm_Vector()
    try:
        if len(lat) != len(lon) != len(rad):
            raise(ValueError('All input must be the same length'))
    except TypeError:
        lib.Lgm_SphToCartCoords(lat, lon, rad, vec1)
        return vec1
    else:
        ans = []
        for v1, v2, v3 in itertools.izip(lat, lon, rad):
            lib.Lgm_SphToCartCoords(v1, v2, v3, vec1)
            ans.append(copy.copy(vec1))
        return ans


Lgm_VectorP = ctypes.POINTER(Lgm_Vector)
