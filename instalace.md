## Instalace modulů

V rámci kurzu budeme používat modul pro práci s daty `pandas`, moduly pro tvorbu grafů `matplotlib` a `seaborn` a moduly pro výpočty `scipy` a `statsmodels`. `pandas`, `matplotlib`, `seaborn` a `requests` jsou externí moduly, které musíme nejdříve nainstalovat.

Spusťte Visual Studio Code a otevřete si nový terminál (z horní lišty vyberte **Terminal → New Terminal**).

### Windows
Napište **postupně** následující příkazy a po každém z nich stiskni **Enter**:

```shell
pip install pandas
pip install matplotlib
pip install seaborn
pip install scipy
pip install statsmodels
```

### Mac OS, Linux
Napište **postupně** následující příkazy a po každém z nich stiskni **Enter**:

```shell
pip3 install pandas
pip3 install matplotlib
pip3 install seaborn
pip3 install scipy
pip3 install statsmodels
```

`pandas` je relativně veliký modul, který obsahuje mnoho dalších modulů, takže instalace bude nějakou chvíli trvat. Terminál během instalace vypíše spoustu textu. Někde na konci bychom pak měli vidět text podobný tomuto:

```shell
Successfully installed pandas-1.2.3
```

Čísla verzí se mohou lišit, záleží na tom, jaká verze je právě aktuální.
