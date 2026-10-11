import math
import unittest
from gradient import (
    finite_number, quadratic_loss, quadratic_gradient, central_difference,
    descend_quadratic, linear_mse_and_gradient, train_line,
)


class GradientTests(unittest.TestCase):
    def test_quadratic_example(self):
        self.assertEqual(quadratic_loss(0), 16)
        self.assertEqual(quadratic_gradient(0), -8)

    def test_quadratic_solution(self):
        self.assertEqual(quadratic_loss(4), 0)
        self.assertEqual(quadratic_gradient(4), 0)

    def test_three_steps(self):
        self.assertEqual(descend_quadratic(), ((0.0, 16.0), (2.0, 4.0), (3.0, 1.0), (3.5, 0.25)))

    def test_zero_steps(self):
        self.assertEqual(descend_quadratic(steps=0), ((0.0, 16.0),))

    def test_monotonic_quadratic_loss(self):
        histories = descend_quadratic(start=-2, target=3, learning_rate=0.1, steps=20)
        self.assertTrue(all(b[1] <= a[1] for a, b in zip(histories, histories[1:])))

    def test_numeric_gradient(self):
        for w in (-3.0, 0.0, 3.3, 10.0):
            self.assertAlmostEqual(central_difference(quadratic_loss, w), quadratic_gradient(w), places=6)

    def test_bad_step_rate(self):
        for rate in (-0.2, 0, 1, 1.1, float('nan')):
            with self.subTest(rate=rate), self.assertRaises(ValueError):
                descend_quadratic(learning_rate=rate)

    def test_bad_step_count(self):
        for steps in (-1, 0.5, True, 10001):
            with self.subTest(steps=steps), self.assertRaises(ValueError):
                descend_quadratic(steps=steps)

    def test_nonfinite_or_boolean_rejected(self):
        for x in (float('inf'), float('nan'), True, '1'):
            with self.subTest(x=x), self.assertRaises(ValueError):
                finite_number(x, 'x')

    def test_gradient_step_epsilon_checks(self):
        for h in (0, -0.01, float('nan'), 1e-200):
            with self.subTest(epsilon=h), self.assertRaises(ValueError):
                central_difference(quadratic_loss, 1, epsilon=h)

    def test_line_loss_at_zero(self):
        self.assertEqual(linear_mse_and_gradient((0,1,2,3), (1,3,5,7), 0, 0), (21, -17, -8))

    def test_line_exact_fit(self):
        self.assertEqual(linear_mse_and_gradient((0,1,2,3), (1,3,5,7), 2, 1), (0, 0, 0))

    def test_line_gradient_checks(self):
        xs, ys = (0,1,2,3), (1,3,5,7)
        _, dw, db = linear_mse_and_gradient(xs, ys, 0.8, 1.5)
        self.assertAlmostEqual(dw, central_difference(lambda w: linear_mse_and_gradient(xs,ys,w,1.5)[0], 0.8), places=5)
        self.assertAlmostEqual(db, central_difference(lambda b: linear_mse_and_gradient(xs,ys,0.8,b)[0], 1.5), places=5)

    def test_line_training(self):
        w, b, loss = train_line((0,1,2,3),(1,3,5,7))
        self.assertAlmostEqual(w, 2, places=4)
        self.assertAlmostEqual(b, 1, places=4)
        self.assertLess(loss, 1e-7)

    def test_reject_bad_dataset(self):
        for xs,ys in (((),()),((1,),(1,2)), ((float('inf'),),(2,)),((True,),(2,))):
            with self.subTest(xs=xs,ys=ys),self.assertRaises(ValueError):
                linear_mse_and_gradient(xs,ys,0,0)

    def test_train_line_invalid_rate(self):
        with self.assertRaises(ValueError):
            train_line((0,1),(1,3),rate=0)

    def test_train_line_invalid_steps(self):
        with self.assertRaises(ValueError):
            train_line((0,1),(1,3),steps=True)


    def test_chapter_05_finite_difference_derivation(self):
        loss = lambda w: 0.5 * (2 * w - 4) ** 2
        self.assertAlmostEqual(loss(1.01), 1.9602)
        self.assertAlmostEqual(loss(0.99), 2.0402)
        self.assertAlmostEqual(central_difference(loss, 1, epsilon=0.01), -4)
        self.assertAlmostEqual(central_difference(lambda w: w**3, 2, epsilon=0.1), 12.01)
        self.assertEqual(3 * 2**2, 12)


if __name__ == '__main__':
    unittest.main()
