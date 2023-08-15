
from src.archivos import readFile
from src.Ship import Ship
from src.Cruise import Cruise
from src.Cargo import Cargo


def main() -> None:

 lista = readFile()
 for i in range(1, len(lista)):
   if lista[i][0] and lista[i][1] and lista[i][2] and lista[i][3] and (lista[i][3] == "0.25" or lista[i][3] == "0.5" or lista[i][3] == "1"):
      # estan todas las columnas llenas en esa posicion --> CARGO

      barcoCargo = Cargo(float(lista[i][2]), float(lista[i][3]), float(lista[i][0]), float(lista[i][1]))
      print(f"Barco N°{barcoCargo.contador} - TIPO: Cargo")
      try:
        pesoFinal = barcoCargo.is_worth_it()
        if pesoFinal >= 20:
          print("Merece ser saqueado.")
      except Exception as e:
        print(str(e))   
        
   elif lista[i][0] and lista[i][1] and lista[i][2] and  (lista[i][3] != "0.25" or lista[i][3] != "0.5" or lista[i][3] != "1"):
      # estan solo cargadas las primeras tres columnas --> CRUISE

      barcoCruise = Cruise(float(lista[i][2]), float(lista[i][0]), float(lista[i][1]))
      print(f"Barco N°{barcoCargo.contador} - TIPO: Cruise")

      try:
        pesoFinal = barcoCruise.is_worth_it()
        if pesoFinal >= 20:
          print("Merece ser saqueado.")

      except Exception as e:
        print(str(e))

   elif lista[i][0] and lista[i][1] and not lista[i][2]: #Asumimos que si la lista[i][3] esta llena con algun valor, es error.
      # estan solo cargadas las primeras dos columnas --> SHIP

      barcoShip = Ship(float(lista[i][0]), float(lista[i][1]))
      print(f"Barco N°{barcoCargo.contador} - TIPO: Ship")

      try:
        pesoFinal = barcoShip.is_worth_it()
        if pesoFinal >= 20:
          print("Merece ser saqueado.")
      except Exception as e:
        print(str(e))


if __name__ == "__main__":
  main()

#Segunda prueba