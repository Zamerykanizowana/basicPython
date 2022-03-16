# Spotkanie nr 6: zabawa w bibliotekę!
## Przygotowanie do zadań
### Import danych
```
url = 'https://raw.githubusercontent.com/Zamerykanizowana/basicPython/main/books.csv'
df_books = pd.read_csv(url)
df_books
```
### Założenia
W zadaniach pracujemy z biblioteką **Pandas** na typie danych **dataframe**. Założenie jest takie, aby danych nie konwertować, np. na tablice, listy, czy numpy. Uzywamy funkcji z biblioteki Pandas.
## Zadania podstawowe
Zaproponowane rozwiązania nie są jedynymi z możliwych, a jedynie propozycją. Dlatego nie skreślaj swoich rozwiązań. Podziel się nimi na czacie, nawet jeśli nie do końca działają i potrzebujesz rady jak je naprawić.
#### Zadanie 1. Popraw literówkę w tytulę książki "Hatty Potter i Kamień Filozoficzny" &rarr; "Harry Potter i Kamień Filozoficzny"

```
df_books.at[3, "tytul"] = "Harry Potter i Kamień Filozoficzny"
```
Inną propozycją było rozwiązanie z `replace`, jadnak trzeba pamiętać, że choć człowiek intuicyjnie rozumie *zamień Hatty na Harry* to dla polecenia `raplace` nie ma dopasowania między ciągiem *Hatty* a *Hatty Potter i Kamień Filozoficzny*, bo są to dwa różne ciągi znaków, dlatego to rozwiązanie nie zadziała:
```
df_books.replace(to_replace ="Hatty",
                 value ="Harry")
```
A to zadziała:
```
df_books.replace(to_replace ="Hatty Potter i Kamień Filozoficzny",
                 value ="Harry Potter i Kamień Filozoficzny")
```
Jednak nie zaleca się funkcji `replece`, bo może zdarzyć się, że zmienimy nazwę, która mimo swojej niepoprawności stanowi orginalny tytuł (*W pustyni i w puszczy* zachowując poprawnośc językową powinen brzmieć *Na pustyni i w puszczy*). Dlatego lepiej wskazać konkretne miejsce w dataframie.
1. Posortuj dane datą (Pamiętaj, że format w pliku CSV to dd/mm/yyyy)
1. Wylistuj bez powtórzeń wszystkie książki (UWAGA! Jesli jest wiele egzemplarzy i tak wylistuj jedną pozycję)
1. Wylistuj status każdego egzemplarza książki.
1. Policz liczbę egzemplarzy każdego tytułu
1. Policz liczbę tytułów każdego autora
1. Wilistuj ksiązki wypożyczone wraz z liczbą dni od wypożyczenia
1. Posortuj ksiązki wypożyczone liczbą dni wypożyczenia
1. Wykonaj operację usunięcia wszystkich książek, których nie oddano od roku
1. Policz liczbę wypożyczeń danego egzmeplarza

## Zadanie rozbudowane
1. Dodaj możliwość dodania opracji poprzez wiersz poleceń (funkcja input)
