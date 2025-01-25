import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):              #метод проверяет работу метода walk в runner.py
        run = runner.Runner('Nick')   #создаётся объект класса Runner из runner.py
        for i in range(10):           # вызовите метод walk у этого объекта 10 раз
            run.walk()
                         # методом assertEqual сравните distance этого объекта со значением 50.
        self.assertEqual(run.distance, 50)

    def test_run(self):            #аналогично с test_walk
        run = runner.Runner('Bob')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run1 = runner.Runner('Dave')  #создаются 2 объекта класса Runner
        run2 = runner.Runner('Bill')
        for i in range(10):           #10 раз у объектов вызываются методы run и walk соответственно
            run1.run()
            run2.walk()
                                   #используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        self.assertNotEqual(run1.distance, run2.distance)






