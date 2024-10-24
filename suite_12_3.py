import unittest
import test_12_1
import test_12_2

tst_12_2 = unittest.TestSuite()
tst_12_2.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))
tst_12_2.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tst_12_2)