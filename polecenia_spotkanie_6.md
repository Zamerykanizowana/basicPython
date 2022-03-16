# Spotkanie nr 6: zabawa w bibliotekę!
## Przygotowanie do zadań
### Import danych
```python
url = 'https://raw.githubusercontent.com/Zamerykanizowana/basicPython/main/books.csv'
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
1. Wylistuj status każdego egzemplarza książki.
1. Policz liczbę egzemplarzy każdego tytułu
1. Policz liczbę tytułów każdego autora
1. Wilistuj ksiązki wypożyczone wraz z liczbą dni od wypożyczenia
1. Posortuj ksiązki wypożyczone liczbą dni wypożyczenia
1. Wykonaj operację usunięcia wszystkich książek, których nie oddano od roku
1. Policz liczbę wypożyczeń danego egzmeplarza

## Zadanie rozbudowane
1. Dodaj możliwość dodania opracji poprzez wiersz poleceń (funkcja input)
