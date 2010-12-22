# Generated by h2py from ../libLanlGeoMag/Lgm/Lgm_Sgp.h

#
# This structure contains raw lines for Two Line Elements (TLEs)
# and also the decoded values. Here is how the TLEs are formated;
#
#  Line 0:
#      Columns     Example                         Description
#      -------     -----------         ----------------------------------------------------------
#      1-24        ISS (ZARYA)         The common name for the object based on information from
#                                        the SatCat.
#
#  Line 1:
#      Columns     Example                         Description
#      -------     -----------         ----------------------------------------------------------
#      1           1                   Line Number
#      3-7         25544               Object Identification Number Search by object ID
#      8           U                   Elset Classification
#      10-17       98067A              International Designator Search by International Designator
#      19-32       04236.56031392      Element Set Epoch (UTC)
#      34-43       .00020137           1st Derivative of the Mean Motion with respect to Time
#      45-52(46-53??)       12345-7             2nd Derivative of the Mean Motion with respect to Time
#                                      NOTE: decimal point assumed.  This type of format is to be
#                                      read as: 0.12345e-7
#      54-61       16538-3             B* Drag Term
#      63  0       Element             Set Type
#      65-68       513                 Element Number
#      69          5                   Checksum
#
#  Line 2:
#      Columns     Example                         Description
#      -------     -----------         ----------------------------------------------------------
#      1           2                   Line Number
#      3-7         25544               Object Identification Number
#      9-16        51.6335             Orbit Inclination (degrees)
#      18-25       344.7760            Right Ascension of Ascending Node (degrees)
#      27-33       0007976             Eccentricity (decimal point assumed)
#      35-42       126.2523            Argument of Perigee (degrees)
#      44-51       325.9359            Mean Anomaly (degrees)
#      53-63       15.70406856         Mean Motion (revolutions/day)
#      64-68       32890               Revolution Number at Epoch
#      69          3                   Checksum
#
#


# Included from math.h
TRUE = 1
FALSE = 0
SGP_CK2 = 5.413080e-4
SGP_CK4 = 0.62098875e-6
SGP_E6A = 1.0e-6
SGP_QOMS2T = 1.88027916e-9
SGP_S = 1.01222928
SGP_TOTHRD = 0.66666667
SGP_XJ3 = (-0.253881e-5)
SGP_XKE = 0.743669161e-1
SGP_XKMPER = 6378.135
SGP_XMNPDA = 1440.0
SGP_AE = 1.0
SGP_DE2RA = 0.174532925e-1
SGP_PI = 3.14159265
SGP_PIO2 = 1.57079633
SGP_TWOPI = 6.2831853
SGP_X3PIO2 = 4.71238898
SGP_wgs72old = 0
SGP_wgs72 = 1
SGP_wgs84 = 2
M_PI = 3.141592653589793238462643
M_2PI = 6.283185307179586476925287


import ctypes
from _Lgm_Types import *


class _SgpTLE(ctypes.Structure):
    @classmethod
    def assign_fields(cls):
        cls._fields_ = [("Line0", ctypes.create_string_buffer(80) ), # Contains the common name for the object
            ("Line1", ctypes.create_string_buffer(80) ), # Contains identifiers derivatives of mean motion, drag term etc..
            ("Line2", ctypes.create_string_buffer(80) ), # Contains orbital elements (RA of Asc Node, mean anomaly, etc..)
            ("Name", ctypes.create_string_buffer(80) ), # Coman object name
            ("IdNumber", LgmInt), # Object identification number
            ("ElsetClass", ctypes.create_string_buffer(1)), # Elset Classification
            ("IntDesig", ctypes.create_string_buffer(20) ), # International designator
            ("ElementSetEpoch", LgmDouble), # Element Set Epoch Time
            ("dMMdT1", LgmDouble), # 1st Derivative of the Mean Motion with respect to Time
            ("dMMdT2", LgmDouble), # 2nd Derivative of the Mean Motion with respect to Time
            ("BstarDrag", LgmDouble), # B* Drag Term
            ("ElementSetType", LgmInt), # Element Set Type
            ("ElementSetNum", LgmInt), # Element Set Number
            ("Line1CheckSum", LgmInt), # Line1 Checksum
            ("Inclination", LgmDouble), # Orbit Inclination (degrees)
            ("RAofAscNode", LgmDouble), # Right Ascension of Ascending Node (degrees)
            ("Eccentricity", LgmDouble), # Eccentricity
            ("ArgOfPerigee", LgmDouble), # Argument of Perigee (degrees)
            ("MeanAnomaly", LgmDouble), # Mean Anomaly (degrees)
            ("MeanMotion", LgmDouble), # Mean Motion (revolutions/day)
            ("RevNumAtEpoch", LgmInt), # Revolution Number at Epoch
            ("Line2CheckSum", LgmInt), # Line2 Checksum
            ("Date", LgmLong), #
            ("UT", LgmDouble), #
            ("Year", LgmInt), #
            ("Month", LgmInt), #
            ("Day", LgmInt), #
            ("Doy", LgmInt), #
            ("Dow", ctypes.create_string_buffer(5) ), #
            ("JD", LgmDouble), # Julian Date of Epoch
            ("Period", LgmDouble), # in minutes
            ("IntDesig2", ctypes.create_string_buffer(20) ), # e.g. 1989-046A
            ("ObjectType", ctypes.create_string_buffer(20) ), # SAT, R/B or DEB
            ("EpochStr", ctypes.create_string_buffer(20) ), # A more readabl version of the epoch time...
            ("YYYYDDDdFRAC", LgmDouble) ] #  YYYYDDD.FRAC

class _SgpInfo(ctypes.Structure):
    @classmethod
    def assign_fields(cls):
        cls._fields_ = [ \
            #THESE WERE FOR THGE STR3 codes
            ("IFLAG", LgmInt), #
            ("XMO", LgmDouble), #
            ("XNODEO", LgmDouble), #
            ("OMEGAO", LgmDouble), #
            ("EO", LgmDouble), #
            ("XINCL", LgmDouble), #
            ("XNO", LgmDouble), #
            ("XNDT2O", LgmDouble), #
            ("XNDD6O", LgmDouble), #
            ("BSTAR", LgmDouble), #
            ("XDOT", LgmDouble), #
            ("YDOT", LgmDouble), #
            ("ZDOT", LgmDouble), #
            ("EPOCH", LgmDouble), #
            ("DS50", LgmDouble), #
            # new vars
            ("argpdot", LgmDouble),
            ("argpo", LgmDouble),
            ("atime", LgmDouble),
            ("aycof", LgmDouble),
            ("bstar", LgmDouble),
            ("cc1", LgmDouble),
            ("cc4", LgmDouble),
            ("cc5", LgmDouble),
            ("con41", LgmDouble),
            ("d2", LgmDouble),
            ("d2201", LgmDouble),
            ("d2211", LgmDouble),
            ("d3", LgmDouble),
            ("d3210", LgmDouble),
            ("d3222", LgmDouble),
            ("d4", LgmDouble),
            ("d4410", LgmDouble),
            ("d4422", LgmDouble),
            ("d5220", LgmDouble),
            ("d5232", LgmDouble),
            ("d5421", LgmDouble),
            ("d5433", LgmDouble),
            ("dedt", LgmDouble),
            ("del1", LgmDouble),
            ("del2", LgmDouble),
            ("del3", LgmDouble),
            ("delmo", LgmDouble),
            ("didt", LgmDouble),
            ("dmdt", LgmDouble),
            ("dnodt", LgmDouble),
            ("domdt", LgmDouble),
            ("e3", LgmDouble),
            ("ecco", LgmDouble),
            ("ee2", LgmDouble),
            ("error", LgmDouble),
            ("eta", LgmDouble),
            ("gsto", LgmDouble),
            ("inclo", LgmDouble),
            ("mdot", LgmDouble),
            ("mo", LgmDouble),
            ("no", LgmDouble),
            ("nodecf", LgmDouble),
            ("nodedot", LgmDouble),
            ("nodeo", LgmDouble),
            ("omgcof", LgmDouble),
            ("peo", LgmDouble),
            ("pgho", LgmDouble),
            ("pho", LgmDouble),
            ("pinco", LgmDouble),
            ("plo", LgmDouble),
            ("se2", LgmDouble),
            ("se3", LgmDouble),
            ("sgh2", LgmDouble),
            ("sgh3", LgmDouble),
            ("sgh4", LgmDouble),
            ("sh2", LgmDouble),
            ("sh3", LgmDouble),
            ("si2", LgmDouble),
            ("si3", LgmDouble),
            ("sinmao", LgmDouble),
            ("sl2", LgmDouble),
            ("sl3", LgmDouble),
            ("sl4", LgmDouble),
            ("t", LgmDouble),
            ("t2cof", LgmDouble),
            ("t3cof", LgmDouble),
            ("t4cof", LgmDouble),
            ("t5cof", LgmDouble),
            ("x1mth2", LgmDouble),
            ("x7thm1", LgmDouble),
            ("xfact", LgmDouble),
            ("xgh2", LgmDouble),
            ("xgh3", LgmDouble),
            ("xgh4", LgmDouble),
            ("xh2", LgmDouble),
            ("xh3", LgmDouble),
            ("xi2", LgmDouble),
            ("xi3", LgmDouble),
            ("xl2", LgmDouble),
            ("xl3", LgmDouble),
            ("xl4", LgmDouble),
            ("xlamo", LgmDouble),
            ("xlcof", LgmDouble),
            ("xli", LgmDouble),
            ("xmcof", LgmDouble),
            ("xni", LgmDouble),
            ("zmol", LgmDouble),
            ("zmos", LgmDouble),
            ("GravConst", LgmInt), #
            ("irez", ctypes.create_string_buffer(1) ), #
            ("init", ctypes.create_string_buffer(1) ), #
            ("method", ctypes.create_string_buffer(1) ), #
            ("isimp", ctypes.create_string_buffer(1) ), #
            ("X", ), #
            ("Y", ), #
            ("Z", ), #
            ("VX", ), #
            ("VY", ), #
            ("VZ", ) ]
