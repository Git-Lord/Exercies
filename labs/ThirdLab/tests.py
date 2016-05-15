import unittest, main, itertools, sys, random

class CalculatorTests(unittest.TestCase):

    # Test a calculating the sums:
    def test_sums(self):
      # Calculates the sum:
      def sign_sum(array, signs):
        s = 0
        for i in range(len(array)):
            s += array[i] * signs[i]
        return s
      # Checks the different lengths
      for N in range(1, 20, 1):
        for j in range(0,10):
          # Checks the different arrays
          array = [random.randint(-100,100) for x in range(N)]

          # Generates the permutations:
          minimum = sys.maxsize
          multiple_signs = itertools.product([-1,1], repeat=N)
          # Checks the real minimum sum
          for sign in multiple_signs:
            s = abs(sign_sum(array, sign))
            if s < minimum:
              minimum = s
          # Checks the answer
          self.assertEqual(minimum, main.calculate(array))
          
if __name__ == '__main__':
    unittest.main()

