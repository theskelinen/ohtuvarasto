import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):ddd
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)
        
    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_otto_palauttaa_nolla(self):
        saatu_maara = self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_lisays_yli_tilavuuden_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)
        
    def test_alkusaldo_ei_voi_olla_negatiivinen(self):
        varasto_negatiivisella_alkusaldo = Varasto(10, -5)

        self.assertAlmostEqual(varasto_negatiivisella_alkusaldo.saldo, 0)
    
    def test_alkusaldo_ei_voi_olla_suurempi_kuin_tilavuus(self):
        varasto_suuremmalla_alkusaldo = Varasto(10, 15)

        self.assertAlmostEqual(varasto_suuremmalla_alkusaldo.saldo, 10)
    
    def test_tilavuus_ei_voi_olla_negatiivinen(self):
        varasto_negatiivisella_tilavuudella = Varasto(-5)

        self.assertAlmostEqual(varasto_negatiivisella_tilavuudella.tilavuus, 0)
    
    def test_str_metodi_toimii(self):
        self.varasto.lisaa_varastoon(7)
        odotettu_str = "saldo = 7, vielä tilaa 3"
        self.assertEqual(str(self.varasto), odotettu_str)

