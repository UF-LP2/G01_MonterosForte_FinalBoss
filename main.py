import prueba
import random

def main() -> None:

  random.seed()
  dado = random.randint(1,3)

  draft_aux = random.randint(1, 200)
  crew_aux = random.randint(1, 100)
  cargo_aux = random.randint(1, 100)
  passengers_aux = random.randint(1,100)

  if dado == 1:
    Barco1 = prueba.Ship(draft_aux, crew_aux)
    Barco1.is_worth_it()

    
if __name__ == "__main__":
  main()
