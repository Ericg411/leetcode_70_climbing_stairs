import unittest
from solution import Solution

class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_climb_stairs(self):
        # Test cases
        self.assertEqual(self.solution.climbStairs(0), 1)    # 1 way to stay at the ground
        self.assertEqual(self.solution.climbStairs(1), 1)    # 1 way to climb 1 step
        self.assertEqual(self.solution.climbStairs(2), 2)    # 2 ways to climb 2 steps (1+1, 2)
        self.assertEqual(self.solution.climbStairs(3), 3)    # 3 ways to climb 3 steps (1+1+1, 1+2, 2+1)
        self.assertEqual(self.solution.climbStairs(4), 5)    # 5 ways to climb 4 steps
        self.assertEqual(self.solution.climbStairs(5), 8)    # 8 ways to climb 5 steps

if __name__ == '__main__':
    unittest.main()
