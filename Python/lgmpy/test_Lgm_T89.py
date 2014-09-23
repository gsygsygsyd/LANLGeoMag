#!/usr/bin/env python

"""
Test suite for the Lgm_T89 file

@author: Brian Larsen
@organization: LANL
@contact: balarsen@lanl.gov

@version: V1: 20-Dec-2010 (BAL)
"""

import unittest
import datetime
import itertools

import numpy

from lgmpy import Lgm_T89
from lgmpy import Lgm_Vector

class Lgm_T89_T89(unittest.TestCase):
    """
    Tests related to Lgm_T89.T89 wrapper
    @author: Brian Larsen
    @organization: LANL
    @contact: balarsen@lanl.gov

    @version: V1: 11-Jan-2011 (BAL)
    """
    def setUp(self):
        super(Lgm_T89_T89, self).setUp()
        self.pos = [-6.6, 0, 0]
        self.kp = 0
        self.dt = datetime.datetime(2005, 8, 31, 9, 0, 0)
    def tearDown(self):
        super(Lgm_T89_T89, self).tearDown()

    def test_T89(self):
        """the T89 simple static wrapper should work (regression)"""
        ans = [-18.926081,  -1.857515,  80.052116]
        numpy.testing.assert_allclose( Lgm_T89.T89(self.pos, self.dt, self.kp),
            [-18.926081,  -1.857515,  80.052116], rtol=1e-3, atol=0)
        ans = numpy.array([ans*2])
        numpy.testing.assert_allclose(Lgm_T89.T89([self.pos]*2,
                                    [self.dt]*2,
                                    [self.kp]*2) , ans.reshape(2,3), rtol=1e-3, atol=0)

class Lgm_T89Tests(unittest.TestCase):
    """
    Tests related to Lgm_T89
    @author: Brian Larsen
    @organization: LANL
    @contact: balarsen@lanl.gov

    @version: V1: 04-Jan-2011 (BAL)
    """
    def setUp(self):
        super(Lgm_T89Tests, self).setUp()
        self.pos = [-6.6, 0, 0]
        self.kp = 0
        self.dt = datetime.datetime(2005, 8, 31, 9, 0, 0)
    def tearDown(self):
        super(Lgm_T89Tests, self).tearDown()

    def test_T89_1(self):
        """First simple in/out tests of T89 (regression)"""
        ans = [[-18.92608102838227, -1.8575154402941223, 80.05211611259763],
            [-20.783024662565946, -1.8575154402941223, 74.2809609414084 ],
            [-22.512615841596073, -1.8575154402941223, 70.18331903086782],
            [-26.36648155861654, -1.8575154402941223,  64.30381088411946 ], ]
        for i, kp in enumerate(range(4)):
            B = Lgm_T89.Lgm_T89(self.pos, self.dt, kp)
            self.assertAlmostEqual(ans[i][0], B['B'].x, 5)
            self.assertAlmostEqual(ans[i][1], B['B'].y, 5)
            self.assertAlmostEqual(ans[i][2], B['B'].z, 5)

    def test_kp_checking(self):
        """for T89 Kp is between 0 and 5 inclusive"""
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89, self.pos, self.dt, 10)
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89, self.pos, self.dt, 6)
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89, self.pos, self.dt, -1)
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89, self.pos, self.dt, [-1, 0])
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89, self.pos, self.dt, [7, 0])

    def test_list_in(self):
        """Make sure that list inputs work correctly (regression)"""
        ans = [[-18.92608102838227, -1.8575154402941223, 80.05211611259763],
            [-20.783024662565946, -1.8575154402941223, 74.2809609414084 ],
            [-22.512615841596073, -1.8575154402941223, 70.18331903086782],
            [-26.36648155861654, -1.8575154402941223, 64.30381088411946 ], ]
        for i, kp in enumerate(range(4)):
            a = Lgm_T89.Lgm_T89([self.pos]*2, [self.dt]*2, [kp]*2)
            B = a.calc_B()
            B = [val.tolist() for val in B]
            Bv = list(itertools.chain.from_iterable(B))
            Av = list(itertools.chain.from_iterable([ans[i]]*2))
            for i, val in enumerate(Bv):
                self.assertAlmostEqual(Av[i], val, 5)
        self.assertEqual(len(B), 2)

    def test_pos_checking(self):
        """Lgm_T89 pos agrument has checking"""
        self.assertRaises(TypeError, Lgm_T89.Lgm_T89, 'bad', self.dt, self.kp)

    def test_time_checking(self):
        """Lgm_T89 time agrument has checking"""
        self.assertRaises(TypeError, Lgm_T89.Lgm_T89, self.pos, 'bad', self.kp)

    def test_internal_model(self):
        """Lgm_T89 internal_model agrument has checking"""
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89, self.pos, self.dt,
                          self.kp, INTERNAL_MODEL=4)
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89, self.pos, self.dt,
                          self.kp, INTERNAL_MODEL='bla')
        a = Lgm_T89.Lgm_T89(self.pos, self.dt, self.kp, INTERNAL_MODEL=1)
        self.assertEqual(a.attrs['internal_model'], 1)
        a = Lgm_T89.Lgm_T89(self.pos, self.dt, self.kp, INTERNAL_MODEL='LGM_CDIP')
        self.assertEqual(a.attrs['internal_model'], 0)
        a = Lgm_T89.Lgm_T89(self.pos, self.dt, self.kp, INTERNAL_MODEL='LGM_EDIP')
        self.assertEqual(a.attrs['internal_model'], 1)
        a = Lgm_T89.Lgm_T89(self.pos, self.dt, self.kp, INTERNAL_MODEL='LGM_IGRF')
        self.assertEqual(a.attrs['internal_model'], 2)

    def test_internal_model_values(self):
        """Lgm_T89 internal_model agrument changes the ouput values"""
        # values form C test run
        #        Date = 20090101; UTC  = 0.0; mInfo->Kp = 2; 
        #        u.x = 3.0; u.y = 4.0; u.z = 3.0
        #        IGRF: -124.3951334579, -73.9980630146, 78.2480922689
        #        CDIP: -123.6039064198, -75.2663431204, 77.7392286024
        #        EDIP: -123.5566489251, -72.5155639973, 79.1393833267
        ans = {}
        ans['IGRF'] = [-123.99486 ,  -73.758075,   77.98547 ]
        ans['CDIP'] = [-123.6039064198, -75.2663431204, 77.7392286024]
        ans['EDIP'] = [-123.5566489251, -72.5155639973, 79.1393833267]
        pos = [3.0, 4.0, 3.0]
        dt = datetime.datetime(2009, 1, 1, 0)
        kp = 2
        a = Lgm_T89.T89(pos, dt, kp, INTERNAL_MODEL='LGM_IGRF')
        numpy.testing.assert_allclose(ans['IGRF'], a)
        a = Lgm_T89.T89(pos, dt, kp, INTERNAL_MODEL='LGM_CDIP')
        numpy.testing.assert_allclose(ans['CDIP'], a)
        a = Lgm_T89.T89(pos, dt, kp, INTERNAL_MODEL='LGM_EDIP')
        numpy.testing.assert_allclose(ans['EDIP'], a)

    def test_coord_system(self):
        """Lgm_T89 only inpout GSM for now (regression)"""
        self.assertRaises(NotImplementedError, Lgm_T89.Lgm_T89, self.pos,
                          self.dt, self.kp, coord_system='SM')

    def test_lengths(self):
        """all scalars or all lists"""
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89,
                          [self.pos, self.pos], self.dt, self.kp)
        self.assertRaises(ValueError, Lgm_T89.Lgm_T89,
                          [self.pos]*2, [self.dt]*2, [self.kp]*3)



if __name__ == '__main__':
    unittest.main()
