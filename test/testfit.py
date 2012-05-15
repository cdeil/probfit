import unittest
from dist_fit.cdist_fit import *
from dist_fit.cdist_func import *
from numpy.random import randn
from math import log,pi,sqrt
class TestFit(unittest.TestCase):

    def setUp(self):
        self.ndata = 20000
        self.data = randn(self.ndata)
        self.analytic = self.ndata*0.5*(log(2*pi)+1)
        
    def test_UnbinnedML(self):
        f = gaussian
        blh = UnbinnedML(gaussian,self.data)
        self.assertAlmostEqual(blh(0,1),self.analytic,delta=self.analytic*0.01)
    
    def test_BinnedLH_poisson(self):
        analytic = 0.5*(log(2*pi)+1)
        f = gaussian
        nbins = 1000
        blh = BinnedLH(gaussian,self.data,bins=nbins,range=(-5,5))
        #self.assertAlmostEqual(blh(0,2),self.analytic,delta=self.analytic*0.01)
        self.assertAlmostEqual(2.*blh(0,1)/nbins,1.,delta=0.5)

if __name__ == '__main__':
    unittest.main()