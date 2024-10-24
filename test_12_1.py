import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        test_obj = runner.Runner('test_name')
        for i in range(10):
            test_obj.walk()
        self.assertEqual(test_obj.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        test_obj = runner.Runner('test_name')
        for i in range(10):
            test_obj.run()
        self.assertEqual(test_obj.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        test_obj_1 = runner.Runner('test_name_1')
        test_obj_2 = runner.Runner('test_name_2')
        for i in range(10):
            test_obj_1.run()
            test_obj_2.walk()
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)

if __name__ == '__main__':
    unittest.main()
