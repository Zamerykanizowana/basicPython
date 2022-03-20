# Spotkanie nr 6: zabawa w bibliotekę!
## Przygotowanie do zadań
### Import danych
```python
url = 'https://raw.githubusercontent.com/Zamerykanizowana/basicPython/main/6_spotkanie/books.csv'
df_books = pd.read_csv(url)
df_books
```
### Założenia
W zadaniach pracujemy z biblioteką **Pandas** na typie danych **dataframe**. Założenie jest takie, aby danych nie konwertować, np. na tablice, listy, czy numpy. Uzywamy funkcji z biblioteki Pandas.
## Zadania podstawowe
Zaproponowane rozwiązania nie są jedynymi z możliwych, a jedynie propozycją. Dlatego nie skreślaj swoich rozwiązań. Podziel się nimi na czacie, nawet jeśli nie do końca działają i potrzebujesz rady jak je naprawić.
#### Zadanie 1. Popraw literówkę w tytulę książki "Hatty Potter i Kamień Filozoficzny" &rarr; "Harry Potter i Kamień Filozoficzny"

```python
df_books.at[3, "tytul"] = "Harry Potter i Kamień Filozoficzny"
```
Inną propozycją było rozwiązanie z `replace`, jadnak trzeba pamiętać, że choć człowiek intuicyjnie rozumie *zamień Hatty na Harry* to dla polecenia `raplace` nie ma dopasowania między ciągiem *Hatty* a *Hatty Potter i Kamień Filozoficzny*, bo są to dwa różne ciągi znaków, dlatego to rozwiązanie nie zadziała:
```python
df_books.replace(to_replace ="Hatty",
                 value ="Harry")
```
A to zadziała:
```python
df_books.replace(to_replace ="Hatty Potter i Kamień Filozoficzny",
                 value ="Harry Potter i Kamień Filozoficzny")
```
Ważną różnicą miedzy poleceniem pierwszym a trzecim, jest fakt, że pierwsze trwale ingeruje w w oryginał danych, zaś trzecie zamieni dane tylko w ramach polecenia, oryginał się nie zmieni. Aby polecenie pierwsze i trzecie zadziałało tak samo do `replace` należy dodać argument (ang. *named argument*) `inplace` o którym szerzej powiemy w dalszej części tego instruktażu. <br>
Jednak nie zaleca się funkcji `replece`, bo może zdarzyć się, że zmienimy nazwę, która mimo swojej niepoprawności stanowi orginalny tytuł (*W pustyni i w puszczy* zachowując poprawnośc językową powinen brzmieć *Na pustyni i w puszczy*). Dlatego lepiej wskazać konkretne miejsce w dataframie.
#### Zadanie 2. Posortuj dane datą **(Pamiętaj, że format w pliku CSV to dd/mm/yyyy)**
W pierwszej kolejności należy przekonwertować datę, która dla człowieka pozostaje czytelna, ale dla programu pozostaje ciągiem znaków. Tu pułapką jest format znany w naszym regionie `dd/mm/yyyy`, jednak standardowy format dla Pythona to `mm/dd/yyyy`, dlatego należy wskazać jak czytać poprawnie datę przez argument (ang. *named argument*) `format`. W kolejnym etapie wystarczy posortować choć oczywiście nie stoi na przeszkodzie, aby zrobić to w jednym poleceniu (jednej liniki kodu).
```python
df_books["data_operacji"] = pd.to_datetime(df_books["data_operacji"], format="%d/%m/%Y")
df_books.sort_values(by="data_operacji", inplace=True)
```
#### Zadanie 3. Wylistuj bez powtórzeń wszystkie książki (UWAGA! Jesli jest wiele egzemplarzy i tak wylistuj jedną pozycję)
W pierwszej kolejności można stworzyć kopię samej kolumny tytułów, a następnie usunąć z kopii wszystkie powtórki.
```python
df_books_title = df_books["tytul"].copy(deep=True)
df_books_title.drop_duplicates(inplace=True)
```
Warto zatrzymać się na moment przy arumentach `deep` i `inplace`. Argument `deep` nastawiony na `True` powoduje w przypadku funkcji `copy` "głębokie" skopiowanie dataframe'u, czyli rzeczywiście kopiujemy dataframe (dane), które stanowią osobny byt. W przypadku `False` (który jest wartością domyślą = czyli jak nie nastawimy nic, to wykona się `deep=False`) w rzeczywistości kopiujemy wskaźnik do komórki pamięci, czyli modyfikując kopię modyfikująmy także oryginał. `inplace` nastawiony na `True` modyfikuje oryginał, czyli w podanym przypadku trwale usuwa duplikaty, zaś nastawiony na `False` (domyślnie) zwraca dane z usuniętymi duplikatami, ale nie modyfikuje oryginału. Żadko kiedy używamy `inplace`, ale na potrzeby ćwiczeń, będzie on używany, gdyż często wykorzystujemy dane do jednaego zadania z poprzedniego i checmy zachować modyfikację. Dla testów wykonaj polecenie:
```python 
df_books.drop_duplicates()
```
A nastepnie sprawdź, czy Twój dataframe został trwale zmodyfikowany przez wykonanie:
```
df_books
```
Duplikaty powinny być widoczne, bo nie zostały trawle usunięte poprzednim poleceniem.
#### Zadanie 4. Wylistuj status każdego egzemplarza książki.
W pierwszej części kopiujemy `df_books`, dla przypomnienia `df_books` jest posortowany datami. Kolejnym krokiem jest usunięcie duplikatów po numerze (indywidualny numer egzemplarzy książek) i zachowujemy najbardziej ostatni (niepoprawnie językowo, ale oddaje trafne stwierdzenie po angielsku *the most recent value*).
```python
df_books_status = df_books.copy(deep=True)
df_books_status.drop_duplicates("numer", keep="last", inplace=True)
df_books_status[["tytul", "numer", "status"]].sort_values(by="tytul")
```
#### Zadanie 5. Policz liczbę egzemplarzy każdego tytułu
W pierwszej częsci kopiujemy oryginalne dane, ale tylko kolumny z tytułem i numerem. Usuwamy duplikaty numerów, Grupujemy i zliczamy wartości, na końcu przedstawiając je tabelarycznie zmianiamy nazwę kolumny na `liczba_egzemplarzy`, żeby wartość w kolumnie była dobrze zinterpretowana przez odbiorcę tabeli. 
```python
df_books_per_title = df_books[["tytul", "numer"]].copy(deep=True)
df_books_per_title.drop_duplicates("numer", inplace=True)
df_books_per_title.groupby('tytul').count().rename(columns={"numer":"liczba_egzemplarzy"})
```
#### Zadanie 6. Policz liczbę tytułów każdego autora
W pierwszym poleceniu kopiujemy z `df_books` kolumną z aoutorami tytułami, następnie usuwamy powtórzenia. W ostatnim ktroku grupujemy po autorze i liczymy liczbę wsytąpień, po czym zamieniamy nazwę kolumny na `liczba_tytułów` by tabela stała się bardziej czytelna dla kogoś kto widzi ją pierwszy raz. 
```python
df_books_per_author = df_books[["autor", "tytul"]].copy(deep=True)
df_books_per_author.drop_duplicates("tytul", keep="last", inplace=True)
df_books_per_author.groupby('autor').count().rename(columns={"autor":"liczba_tytułów"})
```
#### Zadanie 7.  Wilistuj ksiązki wypożyczone wraz z liczbą dni od wypożyczenia
Do wykonania zadania wykonamy napisaną przez nas funkcję `policz_dni_od_operacji`, która zwraca liczbę dni od wypożyczenia do dzisiaj.
```python
def policz_dni_od_operacji(df):
  return (datetime.today() - df['data_operacji']).days
```
W pierwszej kolejności kopiujemy z `df_books_status` (z zadania 4 - jest to lista wszystkich egzemplarzy książek z najbardziej aktualnymi statusami), których status jest `wypozyczona`. Następnie do nowej kolumny o nazwie `liczba_dni_od_wypozyczenia` aplikujemy (ang. *apply*) obliczoną za pomocą wcześniej opisanej funkcji liczbę dni od wypożyczenia. 
```python
df_books_borrowed = df_books_status.loc[df_books_status['status'] == 'wypozyczona'].copy(deep=True)
df_books_borrowed["liczba_dni_od_wypozyczenia"] = df_books_borrowed.apply(policz_dni_od_operacji, axis=1)
df_books_borrowed
```
#### Zadanie 8. Posortuj ksiązki wypożyczone liczbą dni wypożyczenia
```python
df_books_borrowed.sort_values(by="liczba_dni_od_wypozyczenia")
```
W zalezności od zapotrzebowania można posortować także malejąco przez użycie argumentu `ascending=False`.
#### Zadanie 9. Wykonaj operację usunięcia wszystkich książek, których nie oddano od roku
```python
df_books_borrowed[df_books_borrowed["liczba_dni_od_wypozyczenia"] < 365]
```
Operacja powyżej nie jest trwała, czyli z `df_books_borrowed` nie usunęliśmy trwale książek w ponad rocznym wypożeczniem, a jedynie je wyświtliliśmy.
#### Zadanie 10. Policz liczbę wypożyczeń danego egzmeplarza
W pierwszej kolejności kopiujemy z `df_books` wszystkie opracje wypozyczenia, następnie je grupujemy (dla czytelności) po autorze, tytule i numerze, zliczamy i dla czytlności zmieniamy nazwę kolumny. Widzimy, że najwięcej razy wypożaczanym egzemplarzem była książka o numerze **12567**, czyli *Harry Potter i Kamień Filozoficzny*.
```python
df_borrow_operation = df_books.loc[df_books['status'] == 'wypozyczona'].copy(deep=True)
df_borrow_operation[['autor', 'tytul', 'numer', 'status']].groupby(['autor', 'tytul', 'numer']).count().rename(columns={"status":"liczba_wypożyczeń"})
```
## Zadanie rozbudowane
1. Dodaj możliwość dodania opracji poprzez wiersz poleceń (funkcja input)
