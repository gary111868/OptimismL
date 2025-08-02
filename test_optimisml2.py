# test_optimisml2.py
"""
Tests for OptimismL2 module.
"""

import unittest
from optimisml2 import OptimismL2

class TestOptimismL2(unittest.TestCase):
    """Test cases for OptimismL2 class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OptimismL2()
        self.assertIsInstance(instance, OptimismL2)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OptimismL2()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
