import unittest
from prova_escrita_03 import trobar_min_max_rendiment, comptar_estudiants, comptar_estudiants_matèria
from prova_escrita_04 import cercar_el, sumar_fila, sumar_matriu, transformar

class TestProvaEscrita03(unittest.TestCase):

    def test_trobar_min_max_rendiment(self):
        resultat = trobar_min_max_rendiment(10.5, 12.0, 15.0)
        self.assertEqual(resultat, (10.5, 15.0))

    def test_comptar_estudiants(self):
        notes = {
            "Anna": {"Matemàtiques": 8, "Història": 7},
            "Marc": {"Matemàtiques": 6},
            "Laura": {"Ciències": 9, "Matemàtiques": 10},
            "Jordi": {"Història": 5},
        }
        self.assertEqual(comptar_estudiants(notes), 4)

    def test_comptar_estudiants_materia(self):
        notes = {
            "Anna": {"Matemàtiques": 8},
            "Marc": {"Matemàtiques": 6},
            "Laura": {"Matemàtiques": 10},
            "Jordi": {"Història": 5},
        }
        self.assertEqual(comptar_estudiants_matèria(notes, "Matemàtiques"), 3)


class TestProvaEscrita04(unittest.TestCase):

    def test_cercar_el(self):
        matriu = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(cercar_el(matriu, 10), (False, None))
        self.assertEqual(cercar_el(matriu, 1, True), (True, (0,0)))

    def test_sumar_fila(self):
        matriu = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(sumar_fila(matriu, 2), 24)
        self.assertIsNone(sumar_fila(matriu, 10))

    def test_sumar_matriu(self):
        matriu = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(sumar_matriu(matriu), 45)

    def test_transformar(self):
        matriu = [[1,2,3],[4,5,6],[7,8,9]]
        transformar(matriu, 10, "+")
        self.assertEqual(matriu, [[11,12,13],[14,15,16],[17,18,19]])

if __name__ == '__main__':
    unittest.main()