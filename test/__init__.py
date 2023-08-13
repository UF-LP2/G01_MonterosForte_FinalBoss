
from prueba import Ship

def test_ship():
    barco1 = Ship(200, 10)
    assert barco1.is_worth_it() == 185
