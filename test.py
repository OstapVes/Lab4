import unittest
from models.country import Country
from models.Repairs import Repairs
from manager.repairs_manager import RepairsManager
from models.parquet import Parquet
from models.tile import Tile
from models.linoleum import Linoleum
from models.conducts import Conducts
from models.rosette import Rosette
from models.lamp import Lamp


class TestRepairsManager(unittest.TestCase):

    def setUp(self):
        self.parquet = Parquet()
        self.tile = Tile()
        self.linoleum = Linoleum()
        self.conducts = Conducts()
        self.rosette = Rosette()
        self.lamp = Lamp()
        materials = [self.parquet, self.tile, self.linoleum, self.conducts, self.rosette, self.lamp]
        self.manager = RepairsManager(materials)


class TestRepairs(unittest.TestCase):

    def setUp(self):
        self.repairs = Repairs(20, "Repairs", Country.USA)

    def test_init(self):
        self.assertEqual(20, self.repairs.price)
        self.assertEqual("Repairs", self.repairs.brand)
        self.assertEqual(Country.USA, self.repairs.origin_country)

    def test_str(self):
        self.assertEqual(str(self.repairs),
                         f" Price: {self.repairs.price}\n Brand: {self.repairs.brand}\n ")


if __name__ == '__main__':
    unittest.main()
