import sys
sys.path.append(r"C:\Users\thmon\OneDrive\Documents\Universidad\Labo Progra 2\Final Boss Final\G01_MonterosForte_FinalBoss")
from src.Ship import Ship
from src.Cargo import Cargo
from src.Cruise import Cruise

def test_Ship():
    barco1 = Ship(200, 10)
    assert barco1.is_worth_it() == 185

def test_Cruise():
    barco2 = Cruise(200 , 1000)
    assert barco2.is_worth_it() == 474 #475

def test_Cargo():
    barco3 = Cargo(50, 1, 300, 25)
    assert barco3.is_worth_it() == 86.5 #deberia ser 87.5