import Ship 
import Cruise
import Cargo

def test_Ship():
    barco1 = Ship(200, 10)
    assert barco1.is_worth_it() == 185

def test_Cruise():
    barco2 = Cruise(200 , 1000)
    assert barco2.is_worth_it() == 475

def test_Cargo():
    barco3 = Cargo(50, 1, 300, 25)
    assert barco3.is_worth_it() == 87.5