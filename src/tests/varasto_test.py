"""Unit tests for varasto module."""

import unittest
from varasto import Varasto

class VarastoTest(unittest.TestCase):
    """Test class for Varasto."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Test that constructor creates an empty storage."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Test that new storage has correct capacity."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Test that addition increases balance."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Test that addition decreases free space."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Test that removal returns correct amount."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Test that removal increases space."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_liikaa(self):
        """Test removing more than available."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 8)
        
    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        """Test that negative addition does not change balance."""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_otto_palauttaa_nolla(self):
        """Test that negative removal returns zero."""
        saatu_maara = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_lisays_yli_tilavuuden_tayttaa_varaston(self):
        """Test that addition over capacity fills storage."""
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        
    def test_alkusaldo_ei_voi_olla_negatiivinen(self):
        """Test that initial balance cannot be negative."""
        varasto_negatiivisella_alkusaldo = Varasto(10, -5)
        self.assertAlmostEqual(varasto_negatiivisella_alkusaldo.saldo, 0)
    
    def test_alkusaldo_ei_voi_olla_suurempi_kuin_tilavuus(self):
        """Test that initial balance cannot exceed capacity."""
        varasto_suuremmalla_alkusaldo = Varasto(10, 15)
        self.assertAlmostEqual(varasto_suuremmalla_alkusaldo.saldo, 10)
    
    def test_tilavuus_ei_voi_olla_negatiivinen(self):
        """Test that capacity cannot be negative."""
        varasto_negatiivisella_tilavuudella = Varasto(-5)
        self.assertAlmostEqual(varasto_negatiivisella_tilavuudella.tilavuus, 0)
    
    def test_str_metodi_toimii(self):
        """Test that str method works."""
        self.varasto.lisaa_varastoon(7)
        odotettu_str = "saldo = 7, vielä tilaa 3"
        self.assertEqual(str(self.varasto), odotettu_str)
    
    def test_varasto_ei_hyvaksy_negatiivista_lisaysmaaraa(self):
        """Test that storage does not accept negative addition amount."""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)