# Spotkanie nr 7: operacje na plikach łączonych w bibliotece
## Przygotowanie do zadań
### Założenia 
Plik `list_of_books.csv` zawiera listę egzamplarzy książek w biblitece. W kolumnach znajdują się takie informacje jak:
- **tytul**
- **autor**
- **rok_wydania**
- **numer** unikalny numer identyfikacyjny egzemplarz książki

Plik `list_of_users.csv` zawiera liste użytkowników zapisanych w biblitece. W kolumnach znajdują się takie informacje jak:
- **imie**
- **nazwisko**
- **numer_uzytkownika** unikalny numer identyfikujacy użytkonika
Specyficznym przypadkiem jest użytkownik **Konto Bibliotekarza**, które przeprowadza takie operacje **zakup**.

Plik `operations.csv` zawiera listę operacji wykonanych na egzemplarzach książek w bibliotece przez danych użytkowników.
- **numer_uzytkownika**
- **numer** referancja do egzemplarza książki
- **operacja** wyróżnia się trzy operacje `wypozyczenie`, `oddanie` i `zakup`
- **data_operacji**
### Import bibliotek
W rozwiązaniach nie użyto biblioteki `numpy` jednak można wykonać zadania z użyciem tejże biblioteki.
```python
import pandas as pd
import numpy as np
from datetime import datetime
``` 
### Import danych 
```python
url = 'https://raw.githubusercontent.com/Zamerykanizowana/basicPython/main/7_spotkanie/list_of_books.csv'
df_list_of_books = pd.read_csv(url)
df_list_of_books

url = 'https://raw.githubusercontent.com/Zamerykanizowana/basicPython/main/7_spotkanie/list_of_users.csv'
df_list_of_users = pd.read_csv(url)
df_list_of_users

url = 'https://raw.githubusercontent.com/Zamerykanizowana/basicPython/main/7_spotkanie/operations.csv'
df_operations = pd.read_csv(url)
df_operations
```
## Zadania
#### Zadanie 1. Policz liczbę egzemplarzy książek każdego tytuły. Tabele powinna zawierać w kolumnie pierwszej autora, w drugiej tytuł, w trzeciej liczbę egzemplarzy danej pozycji książkowej.
```python
df_list_of_books[['autor','tytul','numer']].drop_duplicates("numer").groupby(['autor','tytul']).count().rename(columns={"numer":"liczba_egzemplarzy"})
```
#### Zadanie 2. Wylistuj egzemplarze książek wraz z aktualnym statusem. Tabela ma przedstawiać kolumny autor, tytuł, numer, operacja i jej data.
```python
df_operations["data_operacji"] = pd.to_datetime(df_operations["data_operacji"], format="%Y-%m-%d")
df_list_of_books[['autor', 'tytul', 'numer']].merge(df_operations[['numer','operacja','data_operacji']], on="numer", how="right").\
  sort_values(by="data_operacji").drop_duplicates("numer", keep="last")
```
#### Zadanie 3. Wylistuj użytkowników i liczbę wypożyczeń (przyjmuj, że wypożczenie się liczy nawet jeśli użytkownik jeszcze nie oddał jakiejś książki)
```python
df_list_of_users.merge(df_operations[['numer_uzytkownika','operacja']].loc[df_operations['operacja'] == 'wypozyczenie'], on="numer_uzytkownika", how="right").\
  groupby(['imie','nazwisko','numer_uzytkownika']).count().rename(columns={"operacja":"liczba_wypozyczen"})
```
#### Zadanie 4. Wylistuj książki i liczbę ich wypożyczeń (przyjmuj, że wypożczenie się liczy nawet jeśli użytkownik jeszcze nie oddał jakiejś książki). Jako książki rozumiemy konkretny egzemplarz. Tabela powinna zawierać informacje o autorze, tytule, numerze egzemplarzu i liczbie wypożyczeń.
```python
df_list_of_books[['autor', 'tytul', 'numer']].merge(df_operations[['numer','operacja']].\
  loc[df_operations['operacja'] == 'wypozyczenie'], on="numer", how="right").\
  groupby(['autor', 'tytul', 'numer']).count().rename(columns={"operacja":"liczba_wypozyczen"})
```
#### Zadanie 5. Wylistuj użytkowników z liczbą książek aktualnie wypożyczonych.
W pierwszej kolejności sortujemy `df_operations` datą, następnie usuwamy duplikaty z zachowaniem najaktualniejszego i pozostawiamy tylko operacje dotyczące wypożyczenia. To wszytko zapisujemy do roboczego `df_copy`. Następnie łączymy (`merge`) `df_copy` i `df_list_of_users`, wycinając tylko interesujące nas kolumny i grupujemy zliczając licznę wierszy i podmieniając nazœ kolumny.
```python
df_copy = df_operations.sort_values(by=["numer_uzytkownika","numer","data_operacji"]).drop_duplicates(["numer_uzytkownika", "numer"], keep="last").loc[df_operations['operacja'] == 'wypozyczenie']
df_list_of_users.merge(df_copy, on="numer_uzytkownika", how="right")[["imie", "nazwisko", "numer_uzytkownika", "numer"]].groupby(['imie','nazwisko','numer_uzytkownika']).count().rename(columns={"operacja":"liczba_wypozyczanych_obecnie_ksiazek"})
```
#### Zadanie 6. Wylistuj użytkowników z liczbą wypożyczonych-zwróconych książek i średnią dni wypożecznia.
W pierwszej kolejności sortujemy operacje dla połaczonych tabel `df_list_of_users` i `df_operations`. Sortowanie najpierw jest po użytkowniku, później po numerze [egzemplarza], a nastepnie po dacie, co spowoduje, że korepondujące opracje wypożyczenie-oddanie będą obok siebie w wierszach. Później liczymy różnicę dla wierszy obok siebie (dla wiersza pierwszego będzie NaN, gdyż nie ma się do czego porównać). W kolejnym kroku bieżamy pod uwagę tylko dane z wierszy `wypozyczenie`. Grupujemy i liczymy średnią ze zgrupowania, następnie nadajemy nową [jasną] nazwę kolumny. 
```python
df_tmp = df_list_of_users.merge(df_operations, on="numer_uzytkownika", how="right").sort_values(by=["numer_uzytkownika","numer","data_operacji"])
df_tmp['roznica'] = df_tmp['data_operacji'].diff()
df_tmp[["imie", "nazwisko", "numer_uzytkownika", "operacja", "roznica"]].loc[df_tmp['operacja'] == 'oddanie']
pd.DataFrame(df_tmp[["imie", "nazwisko", "numer_uzytkownika", "operacja", "roznica"]].loc[df_tmp['operacja'] == 'oddanie']\
  .groupby(["imie", "nazwisko", "numer_uzytkownika"])["roznica"].mean()).rename(columns={"roznica":"srednia_dni_wypozyczenia"})
```
