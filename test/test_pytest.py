
from src.Ship import Ship
from src.Cargo import Cargo
from src.Cruise import Cruise
import pytest

def test_Ship():
    
    barco1 = Ship(200, 10)
    assert barco1.is_worth_it() == 185
    barco2 = Ship(100, 30)
    assert barco2.is_worth_it() == 55

    with pytest.raises(ValueError):
        barco3 = Ship(100, 90) 
        assert barco3.is_worth_it() == -35


def test_Cruise():
    with pytest.raises(ValueError):
        Crucero1 = Cruise(200 , 1000, 10)
        assert not Crucero1.is_worth_it() == 475 #535 es la correcta
        Crucero2 = Cruise(100, 250, 2) 
        assert Crucero2.is_worth_it() == 22
        Crucero3 = Cruise(100, 300, 100)
        Crucero3.is_worth_it() < 20

def test_Cargo():
    with pytest.raises(ValueError):
        Cargo1 = Cargo(50, 1, 300, 25)
        assert not Cargo1.is_worth_it() == 86.5 #deberia ser 87.5
        assert Cargo1.is_worth_it() == 87.5

        Cargo2 = Cargo(100, 0.5, 100, 90)
        assert Cargo2.is_worth_it() < 20


