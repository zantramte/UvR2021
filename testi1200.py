def odstrani_enake(a, b):
    for elementa in a:
        for elementb in b:
            if elementa == elementb and b.index(elementb) == a.index(elementa):
                a.pop(a.index(elementa))
                b.pop(b.index(elementb))



import unittest
import warnings


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_01_odstrani_enake(self):
        a = [1, 3, 2, 13, 2, 4, 1]
        b = [8, 3, 13, 8, 2, 4, 5]
        self.assertIsNone(odstrani_enake(a, b))
        self.assertEqual([1, 2, 13, 1], a)
        self.assertEqual([8, 13, 8, 5], b)

        a = [1, 1, 1, 1, 1]
        b = [1, 1, 1, 1, 1]
        self.assertIsNone(odstrani_enake(a, b))
        self.assertEqual([], a)
        self.assertEqual([], b)

    def test_02_diff(self):
        with open("f1.txt", "wt") as f:
            f.write("""Ana
Berta
Cecilija
Dani
Ema""")
        with open("f2.txt", "wt") as f:
            f.write("""Ana
Berta
Cilka
Dani
Eva Ema""")
        self.assertEqual([(3, 'Cecilija', 'Cilka'), (5, 'Ema', 'Eva Ema')], diff("f1.txt", "f2.txt"))

    def test_03_mesta(self):
        self.assertEqual(
            [["Ana"], ["Berta"], ["Cilka"]],
            mesta([("Ana", 15), ("Berta", 13), ("Cilka", 5)]))
        self.assertEqual(
            [["Ana"], ["Berta"], ["Cilka", "Dani"], [], ["Ema"],
             ["Fanči", "Greta"], []],
            mesta([("Ana", 15), ("Berta", 13), ("Cilka", 12), ("Dani", 12),
             ("Ema", 8), ("Fanči", 6), ("Greta", 6)]))
        self.assertEqual(
            [["Ana"], ["Berta"], ["Cilka", "Dani", "Ema"], [], [],
             ["Fanči", "Greta"], []],
            mesta([("Ana", 15), ("Berta", 13), ("Cilka", 12), ("Dani", 12),
             ("Ema", 12), ("Fanči", 6), ("Greta", 6)]))
        self.assertEqual(
            [["Ana"], ["Berta"], ["Cilka", "Dani", "Ema", "Fanči"], [], [], [],
             ["Greta"]],
            mesta([("Ana", 15), ("Berta", 13), ("Cilka", 12), ("Dani", 12),
             ("Ema", 12), ("Fanči", 12), ("Greta", 6)]))
        self.assertEqual(
            [["Ana"], ["Berta"], ["Cilka", "Dani", "Ema", "Fanči", "Greta"],
             [], [], [], []],
            mesta([("Ana", 15), ("Berta", 13), ("Cilka", 12), ("Dani", 12),
             ("Ema", 12), ("Fanči", 12), ("Greta", 12)]))
        self.assertEqual(
            [["Ana", "Berta"], [], ["Cilka", "Dani", "Ema", "Fanči", "Greta"],
             [], [], [], []],
            mesta([("Ana", 15), ("Berta", 15), ("Cilka", 12), ("Dani", 12),
             ("Ema", 12), ("Fanči", 12), ("Greta", 12)]))
        self.assertEqual(
            [["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"],
             [], [], [], [], [], []],
            mesta([("Ana", 12), ("Berta", 12), ("Cilka", 12), ("Dani", 12),
             ("Ema", 12), ("Fanči", 12), ("Greta", 12)]))

    def test_04_dovolj_lihih(self):
        self.assertTrue(dovolj_lihih([], 0))
        self.assertFalse(dovolj_lihih([], 1))
        self.assertTrue(dovolj_lihih([4, 1, 3, 5, 6, 8, 7, 1, 3], 6))
        self.assertTrue(dovolj_lihih([4, 1, 3, 5, 6, 8, 7, 1, 3], 5))
        self.assertTrue(dovolj_lihih([4, 1, 3, 5, 6, 8, 7, 1, 3], 4))
        self.assertTrue(dovolj_lihih([4, 1, 3, 5, 6, 8, 7, 1, 3], 3))
        self.assertTrue(dovolj_lihih([4, 1, 3, 5, 6, 8, 7, 1, 3], 2))
        self.assertTrue(dovolj_lihih([4, 1, 3, 5, 6, 8, 7, 1, 3], 1))
        self.assertTrue(dovolj_lihih([4, 1, 3, 5, 6, 8, 7, 1, 3], 0))
        self.assertFalse(dovolj_lihih([4, 1, 3, 5, 6, 8, 7, 1, 3], 7))


    def test_05_parkirisce(self):
        parkirisce = Parkirisce(3)

        self.assertTrue(parkirisce.prosto())
        self.assertEqual(0, parkirisce.zasluzek())

        self.assertIsNone(parkirisce.parkiraj("A123", 8.25))
        self.assertTrue(parkirisce.prosto())  # parkiran je A123
        self.assertEqual(0, parkirisce.zasluzek())

        parkirisce.parkiraj("Z234", 8.50)
        self.assertTrue(parkirisce.prosto())  # parkirana A123 in Z234
        self.assertEqual(0, parkirisce.zasluzek())

        self.assertEqual(1, parkirisce.odpelji("Z234", 8.75))
        self.assertTrue(parkirisce.prosto())  # parkirana je A123
        self.assertEqual(1, parkirisce.zasluzek())

        parkirisce.parkiraj("B345", 10.30)
        self.assertTrue(parkirisce.prosto())  # parkirana A123 in B345
        self.assertEqual(1, parkirisce.zasluzek())

        parkirisce.parkiraj("C567", 10.50)
        self.assertFalse(parkirisce.prosto())  # parkirani A123, B345, C567
        self.assertEqual(1, parkirisce.zasluzek())

        parkirisce.parkiraj("D567", 11.00)  # ne more parkirati
        self.assertFalse(parkirisce.prosto())  # parkirani A123, B345, C567
        self.assertEqual(1, parkirisce.zasluzek())

        self.assertEqual(3, parkirisce.odpelji("A123", 11.20))
        self.assertTrue(parkirisce.prosto())  # parkirani B345, C567
        self.assertEqual(4, parkirisce.zasluzek())


if __name__ == "__main__":
    unittest.main()
