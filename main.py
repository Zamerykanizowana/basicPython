url = 'https://raw.githubusercontent.com/Zamerykanizowana/basicPython/main/data.csv'
df = pd.read_csv(url)
print(df)


def srednia(tablica_ocen, kolo_naukowe):
  suma = 0
  for ocena in tablica_ocen:
    if isNaN(ocena) == True:
      ocena = 0
    suma += ocena
  srednia = suma / len(tablica_ocen)
  if kolo_naukowe == "True":
      srednia = srednia
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


def generuj_raport_mock(df, liczba_stypendystow):
  short_df = df[["imie", "nazwisko", "semestr_studiow", "srednia", "kolo_naukowe"]].sort_values(by = "srednia", ascending = False)
  ile_studentow_ma_stypendium = liczba_studentow_do_stypendium(df, 0.2)
  with open('/content/report.txt', 'w') as f:
    f.write("Stypendyści: \n")
    for index, row in short_df.iterrows():
      if row["semestr_studiow"] != 1:
        # TODO jakis if, ktory sprawdzi, czy nadal możemy przyznac stypendium
        if ... :
          f.write(str_srednia_studenta(row["imie"], row["nazwisko"], row["srednia"], row["kolo_naukowe"]))
          f.write('\n')
          ile_studentow_ma_stypendium = ile_studentow_ma_stypendium - 1
    f.write('----------------\n')
    f.write('Pozostali studenci:\n')
    for index, row in short_df.iterrows():
      if row["semestr_studiow"] == 1:
        f.write(str_srednia_studenta(row["imie"], row["nazwisko"], row["srednia"], row["kolo_naukowe"]))
        f.write('\n')
    f.close()

# Test no 1
student = ["Monika", "Testowa", "111222", 2,2,3,4,5,2,5,5, "True", "False", 2]
student2 = ["Aleksandra", "Testowa", "111333", 2,2,3,4,5,2,5,5, "False", "False", 2]
studenci = [student, student2]
if srednia(student[3:11], student[11]) == 4.0 and srednia(student2[3:11], student2[11]) == 3.5:
    print("test pozytywny")
else:
    print("test negatywny")
    print(str_srednia_studenta(student[0], student[1], srednia(student[3:11],student[11])))
    print(str_srednia_studenta(student2[0], student2[1], srednia(student2[3:11],student2[11])))
