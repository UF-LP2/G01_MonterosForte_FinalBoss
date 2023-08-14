
from src.archivos import readFile
from src.Ship import Ship
from src.Cruise import Cruise
from src.Cargo import Cargo


def main() -> None:

 lista = readFile()
 for i in range(1, len(lista)):
   if lista[i][0] and lista[i][1] and lista[i][2] and lista[i][3] and (lista[i][3] == "0.25" or lista[i][3] == "0.5" or lista[i][3] == "1"):
      # estan todas las columnas llenas en esa posicion --> CARGO
      print(lista[i][0])
      barcoCargo = Cargo(float(lista[i][2]), float(lista[i][3]), float(lista[i][0]), float(lista[i][1]))
      try:
        pesoFinal = barcoCargo.is_worth_it()
        if pesoFinal < 20:
          print("No merece ser saqueado.") #"Se deberá elevar un error de cantidad"
        else:
          print("Merece ser saqueado.")
      except Exception as e:
        print(str(e))   
        
   elif lista[i][0] and lista[i][1] and lista[i][2] and  (lista[i][3] != "0.25" or lista[i][3] != "0.5" or lista[i][3] != "1"):
      # estan solo cargadas las primeras tres columnas --> CRUISE
      print(lista[i][0])
      barcoCruise = Cruise(float(lista[i][2]), float(lista[i][0]), float(lista[i][1]))

      try:
        pesoFinal = barcoCruise.is_worth_it()
        if pesoFinal < 20:
          print("No merece ser saqueado.") #"Se deberá elevar un error de cantidad"
        else:
          print("Merece ser saqueado.")

      except Exception as e:
        print(str(e))

   elif lista[i][0] and lista[i][1] and not lista[i][2] and not lista[i][3]:
      # estan solo cargadas las primeras dos columnas --> SHIP
      print(lista[i][0])
      barcoShip = Ship(float(lista[i][0]), float(lista[i][1]))

      try:
        pesoFinal = barcoShip.is_worth_it()
        if pesoFinal < 20:
          print("No merece ser saqueado.") #"Se deberá elevar un error de cantidad"
        else:
          print("Merece ser saqueado.")
      except Exception as e:
        print(str(e))


if __name__ == "__main__":
  main()
