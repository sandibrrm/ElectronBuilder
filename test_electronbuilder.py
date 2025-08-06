# test_electronbuilder.py
"""
Tests for ElectronBuilder module.
"""

import unittest
from electronbuilder import ElectronBuilder

class TestElectronBuilder(unittest.TestCase):
    """Test cases for ElectronBuilder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ElectronBuilder()
        self.assertIsInstance(instance, ElectronBuilder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ElectronBuilder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
