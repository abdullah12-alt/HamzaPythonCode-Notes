import calculator
# from calculator import addition
import unittest

class TestMyCode(unittest.TestCase):
    
    def test_addition(self):
        result =calculator.addition(2,3)
        self.assertEqual(result,5)
    
    def test_subtract(self):
        result=calculator.subtract(2,3)
        self.assertEqual(result,-1)
      
    
        

if __name__=="__main__":
    unittest.main()
        