import unittest
import module_12_2 as mod


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.alls_results = {}

    def setUp(self):
        self.runner_1 = mod.Runner('Usein', 10)
        self.runner_2 = mod.Runner('Andrey', 9)
        self.runner_3 = mod.Runner('Nick', 3)

    def test1(self):
        go = mod.Tournament(90, self.runner_1, self.runner_3)
        end = go.start()
        self.assertTrue(end[2] == 'Nick')
        self.__class__.alls_results['1й забег'] = end

    def test2(self):
        go = mod.Tournament(90, self.runner_2, self.runner_3)
        end = go.start()
        self.assertTrue(end[2] == 'Nick')
        self.__class__.alls_results['2й забег'] = end

    def test3(self):
        go = mod.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        end = go.start()
        self.assertTrue(end[3] == 'Nick')
        self.__class__.alls_results['3й забег'] = end

    @classmethod
    def tearDownClass(cls):
        for number, result in cls.alls_results.items():
            print(number, ':')
            for i, j in result.items():
                print('    ', i, j)


if __name__ == '__main__':
    unittest.main()
