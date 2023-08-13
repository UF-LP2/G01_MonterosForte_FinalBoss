import Cruise
import Cargo
import Ship
import archivos


def main() -> None:

 lista = archivos.readFile()
 
 for i in range(1, len(lista)):
    if lista[i][0] and lista[i][1] and lista[i][2] and lista[i][3]:
      # estan todas las columnas llenas en esa posicion --> CARGO
      barcoCargo = Cargo(lista[i][0], lista[i][1], lista[i][2], lista[i][3])

      try:
        barcoCargo.is_worth_it()
      except Exception as e:
        print(str(e))


    elif lista[i][0] and lista[i][1] and lista[i][2] and not lista[i][3]:
      # estan solo cargadas las primeras tres columnas --> CRUISE
      barcoCruise = Cruise(lista[i][0], lista[i][1], lista[i][2])

      try:
        barcoCruise.is_worth_it()
      except Exception as e:
        print(str(e))

    elif lista[i][0] and lista[i][1] and not lista[i][2] and not lista[i][3]:
      # estan solo cargadas las primeras dos columnas --> SHIP
      barcoShip = Ship(lista[i][0], lista[i][1])

      try:
        barcoShip.is_worth_it()
      except Exception as e:
        print(str(e))


if __name__ == "__main__":
  main()
