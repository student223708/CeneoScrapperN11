# CeneoScraper

## Analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Skladowa|Selektor|Zmienna|
|--------|--------|-------|
|opinia|div.js_product-review|review|
|identyfikator opinii|\[data-entry-id\]|review_id|
|autor|span.user-post__author-name|author|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|
|liczba gwiazdek|span.user-post__score-count|stars|
|tresc|div.user-post__text|content|
|data wystawienia|span.user-post__published > time:nth-child(1)\[datetime\]|publish_date|
|data zakupu|span.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|
|dla ilu przydatna|button.vote-yes[data-total-vote]<br>button.vote-yes > span<br>span[id^=votes-yes]|useful|
|dla ilu nieprzydatna|button.vote-no[data-total-vote]<br>button.vote-no > span<br>span[id^=votes-no]|useless|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--positives) > div.review-feature__item<br>div.review-feature__item:has( ~ div.review-feature__title--positives)|pros|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--negatives) > div.review-feature__item<br>div.review-feature__item:has( ~ div.review-feature__title--negatives)|cons|

## Etapy prac nad projektem (wersja strukturalna)

1) Pobranie skladowych pojedynczej opinii do niezaleznych zmiennych
2) Zapisanie wszystkich skladowych opinii do slownika
3) Pobranie wszystkich opinii z pojedynczej strony i zapisanie ich na liscie w postaci slownikow
4) Pobranie wszystkich opinii o wskazanym produkcie i zapisanie ich do pliku 
5) Wczytanie opinii o wskazanym produkcie z pliku do obiektu DataFrame
6) Wyliczenie podstawowych statystyk 
7) Przedstawienie struktury opinii o produkcie na wykresach
8) Stworzenie struktury wersji obiektowej
9) Implementacja i wykorzystanie micro Framework'a Flask

##  Etapy prac nad projektem (wersja obiektowa)

1)Zaktualizowanie tresci o wersje obiektowa
2)Dodanie routingu
3)Uruchomienie Flask i Jira
4)Dodanie poszczegolnych stron odwolujacych sie do bazy
5)Dodanie funkcjonalnosci
6)Dzialajacy eskalator
7)Otworzenie pliku README.md na stronie glownej

## Lista uzytych bibliotek oraz ich przeznaczenie

|Biblioteka|Zastosowanie|Dokumentacja|
|--------|--------|--------|
|Beautiful Soup|Pobieranie danych z plikow HTML i XML|https://www.crummy.com/software/BeautifulSoup/bs4/doc/|
|certifi|Walidacja certyfikatow i weryfikacja hosta|https://pypi.org/project/certifi/|
|charset-normalizer|Odczyt znakow ze wsparciem dekodowania nieznanych zestawow znakow|https://pypi.org/project/charset-normalizer/|
|cycler|Tworzenie wykresow i stosow danych|https://matplotlib.org/cycler/|
|fonttools|Zarzadzanie czcionka i konwersja formatow|https://pypi.org/project/fonttools/|
|idna|Wsparcie miedzynarodowych nazw domenowych|https://pypi.org/project/idna/|
|kiwisolver|Cassowary sluzacy do zarzadzania pamiecia|https://pypi.org/project/kiwisolver/|
|matplotlib|Tworzenie wizualizacji|https://matplotlib.org/|
|NumPy|Zestaw matematycznych narzedzi|https://numpy.org/|
|Packaging|Kontrola wersji, wymagania i specyfikacje|https://pypi.org/project/packaging/|
|pandas|Analiza i manipulacja danych|https://pandas.pydata.org/|
|Pillow|Zarzadzanie plikami formatow graficznych|https://pillow.readthedocs.io/en/stable/|
|pyparsing|Zarzadzanie wyrazeniami regularnymi|https://github.com/pyparsing/pyparsing|
|dateutil|Zarzadzanie data i strefami czasowymi|https://dateutil.readthedocs.io/en/stable/|
|pytz|Obliczenia uwzgledniajace daty i strefy czasowe|https://pypi.org/project/pytz/|
|requests|Wysylanie rzadan|https://pypi.org/project/requests/|
|six|Kontrola wersji Pythona|https://pypi.org/project/six/|
|soupsieve|Rozszerzenie Beautiful Soup o filtrowanie, selekcje i sprawdzanie danych|https://pypi.org/project/soupsieve/|
|urllib3|Zarzadzanie odnosnikami, polaczeniem i jego bezpieczenstwem|https://urllib3.readthedocs.io/en/stable/|
|markdown|Obsluga formatu plikow markdown|https://pypi.org/project/Markdown/|