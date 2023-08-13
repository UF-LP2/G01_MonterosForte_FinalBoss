
from src.archivos import readFile
from src.Ship import Ship
from src.Cruise import Cruise
from src.Cargo import Cargo


def main() -> None:

 lista = readFile()
 for i in range(1, len(lista)):
   if lista[i][0] and lista[i][1] and lista[i][2] and lista[i][3]:
      # estan todas las columnas llenas en esa posicion --> CARGO
      barcoCargo = Cargo(float(lista[i][0]), float(lista[i][1]), float(lista[i][2]), float(lista[i][3]))
      try:
        barcoCargo.is_worth_it()
      except Exception as e:
        print(str(e))   
        
   elif lista[i][0] and lista[i][1] and lista[i][2] and not lista[i][3]:
      # estan solo cargadas las primeras tres columnas --> CRUISE
      barcoCruise = Cruise(float(lista[i][0]), float(lista[i][1]), float(lista[i][2]))

      try:
        barcoCruise.is_worth_it()
      except Exception as e:
        print(str(e))

   elif lista[i][0] and lista[i][1] and not lista[i][2] and not lista[i][3]:
      # estan solo cargadas las primeras dos columnas --> SHIP
      barcoShip = Ship(float(lista[i][0]), float(lista[i][1]))

      try:
        barcoShip.is_worth_it()
      except Exception as e:
        print(str(e))


if __name__ == "__main__":
  main()
