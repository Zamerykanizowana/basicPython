def srednia(tablica_ocen, kolo_naukowe):
  suma = 0
  for ocena in tablica_ocen:
    if isNaN(ocena) == True:
      ocena = 0
    suma += ocena
  srednia = suma / len(tablica_ocen)
  if kolo_naukowe == "True":
    # TODO dodaj do sredniej 0,5 osceny jesli jest dzialalnosc w kole
  return srednia

def str_srednia_studenta(imie, nazwisko, srednia):
  # TODO (indeks) imie nazwisko: srednia, dzialnosc w kole TAK/NIE
  return imie + ' ' + nazwisko + ': ' + str(srednia)

def isNaN(cos):
  if cos == cos:
    return False
  else:
    return True
