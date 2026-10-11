import math
import unittest
from attention import attention, causal_mask, stable_softmax


class AttentionTests(unittest.TestCase):
    def test_pedagogical_weights(self):
        weights, output = attention(((1,0),), ((1,0),(0,1)), ((2,0),(0,2)))
        expected = math.exp(1/math.sqrt(2)) / (math.exp(1/math.sqrt(2)) + 1)
        self.assertAlmostEqual(weights[0][0], expected)
        self.assertAlmostEqual(weights[0][1], 1 - expected)
        self.assertAlmostEqual(output[0][0], 2 * expected)
        self.assertAlmostEqual(output[0][1], 2 * (1-expected))

    def test_weights_sum_to_one(self):
        weights,_ = attention(((1,0),(0,1)),((1,0),(0,1)),((2,0),(0,2)))
        for row in weights:
            self.assertAlmostEqual(sum(row),1)

    def test_zero_query_uniform(self):
        weights,_ = attention(((0,0),),((1,0),(0,1)),((10,),(20,)))
        self.assertEqual(weights,((0.5,0.5),))

    def test_mask_excludes_key(self):
        weights,output = attention(((1,0),),((1,0),(0,1)),((3,4),(5,6)),mask=((True,False),))
        self.assertEqual(weights,((1.0,0.0),))
        self.assertEqual(output,((3.0,4.0),))

    def test_causal_mask(self):
        self.assertEqual(causal_mask(3), ((True,False,False),(True,True,False),(True,True,True)))

    def test_causal_attention(self):
        q=k=((1,0),(0,1))
        v=((1,),(9,))
        weights,_=attention(q,k,v,mask=causal_mask(2))
        self.assertEqual(weights[0],(1.0,0.0))
        self.assertGreater(weights[1][1],0)

    def test_mask_all_blocked(self):
        with self.assertRaises(ValueError):
            attention(((1,),),((1,),),((1,),),mask=((False,),))

    def test_mask_shape(self):
        with self.assertRaises(ValueError):
            attention(((1,),),((1,),),((1,),),mask=((True,True),))

    def test_mask_requires_boolean(self):
        with self.assertRaises(ValueError):
            attention(((1,),),((1,),),((1,),),mask=((1,),))

    def test_empty_matrix(self):
        with self.assertRaises(ValueError):
            attention((), ((1,),),((1,),))

    def test_jagged_matrix(self):
        with self.assertRaises(ValueError):
            attention(((1,),(1,2)),((1,),),((1,),))

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            attention(((1,2),),((1,),),((1,),))

    def test_mismatched_kv_lengths(self):
        with self.assertRaises(ValueError):
            attention(((1,),),((1,),(2,)),((1,),))

    def test_nonfinite_values(self):
        for bad in (float('inf'),float('nan')):
            with self.subTest(value=bad),self.assertRaises(ValueError):
                attention(((bad,),),((1,),),((1,),))

    def test_bools_rejected_as_numbers(self):
        with self.assertRaises(ValueError):
            attention(((True,),),((1,),),((1,),))

    def test_softmax_stable_large_values(self):
        self.assertEqual(stable_softmax((1000,1000)),(0.5,0.5))
        a,b=stable_softmax((1000,999))
        self.assertAlmostEqual(a+b,1)
        self.assertGreater(a,b)

    def test_softmax_rejects_empty(self):
        with self.assertRaises(ValueError):
            stable_softmax(())

    def test_softmax_rejects_nonfinite(self):
        with self.assertRaises(ValueError):
            stable_softmax((0.0,float('nan')))

    def test_causal_mask_bad_length(self):
        for value in (0,-1,True,1.5):
            with self.subTest(value=value),self.assertRaises(ValueError):
                causal_mask(value)

    def test_multiple_value_dimensions(self):
        weights, outputs=attention(((1,),), ((1,),(1,)), ((0,3,7),(2,5,9)))
        self.assertEqual(outputs,((1.0,4.0,8.0),))
        self.assertEqual(weights,((0.5,0.5),))


    def test_chapter_06_two_token_worked_example(self):
        # Independent regression check for the numerical derivation in chapter 06.
        queries = ((1,), (0,))
        keys = ((1,), (0,))
        values = ((2,), (4,))
        weights, outputs = attention(queries, keys, values)
        first = math.e / (math.e + 1)
        self.assertAlmostEqual(weights[0][0], first)
        self.assertAlmostEqual(weights[0][1], 1 - first)
        self.assertAlmostEqual(outputs[0][0], 4 - 2 * first)
        self.assertAlmostEqual(outputs[1][0], 3)
        masked_weights, masked_outputs = attention(
            queries, keys, values, mask=causal_mask(2)
        )
        self.assertEqual(masked_weights[0], (1.0, 0.0))
        self.assertEqual(masked_outputs[0], (2.0,))
        self.assertAlmostEqual(masked_outputs[1][0], 3)


if __name__ == '__main__':
    unittest.main()
