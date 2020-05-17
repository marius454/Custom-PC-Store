# Custom-PC-Store

## Projekto paleidimo instrukcija:

1.Jei neturima, reikia įsidiegti Python. Kodas buvo rašomas su Python 3.6 versija, o ši instrukcija išbandyta ir veikianti su python 3.8.3 versija.
  *	Parsisiųsti iš šio puslapio - https://www.python.org/downloads/
  *	Pagal naudojama aplinka pasirinkti tinkama versiją/instaliavimo būdą.
  *	Įdiegti Python pasirenkant, kad kartu būtų instaliuojama pip ir python kelias įrašomas į PATH/environment variables.

2.	Nusiklonuoti arba tiesiog parsisiusti projekto gtihub repozitorija į norimą direktoriją (https://github.com/marius454/Custom-PC-Store )
*	git clone https://github.com/marius454/Custom-PC-Store

3.Jeigu norima galima susikurti virtualią aplinką, kad instaliuojamos python bibliotekos nebūtų išsaugotos globaliai. Tai galima padaryti komandinėje eilutėje panaudojus šias komandas (naudojau CMD, nes su PowerShell buvo problem įeinant į virtualią aplinką)
*	pip install virtualenvwrapper-win
*	mkvirtualenv venv

4.Įsidiegti reikalingas bibliotekas.
*	cd Custom-PC-Store (jei ne klonuota, o parsisiųsta tiesiog nuveskite komandinę eilutę į direktoriją kurioje turite requirements.txt failą)
*	pip install –r requirements.txt

5.Įjungti django projekto serverį.
*	cd PC_Store
*	python manage.py runserver (turėtų veikti, bet jei kyla problemų jas lengviau spresti naudojant “python manage.py migrate”, nes šita komanda išves python interpretatoriaus klaidas kode ir lengviau pamatyti kas vyksta pvz. truksta bibliotekų, nes instaliavime kilo klaidų, jei su migrate klaidų nėra pabandykite runserver dar kartą)  
*	Norint baigus išjungti serverį reikia esant komandinėje eilutėje paspausti ctrl+c

6.Atverti sukurtą svetainę
*	Per naršyklę į URL skiltį įrašyti http://localhost:8000/ arba http://127.0.0.1:8000/ taip pat parašyta komandinėje eilutė panaudojus runserver:

7.Sukurti administratoriaus paskyra kad būtų galima pamatyti administratoriaus skiltį http://localhost:8000/admin
*	python manage.py createsuperuser
*	Panaudojus komandą sekti instrukcija ir sukurti naudotojo paskyra
*	Vėl įjungti serverį, nueiti į http://localhost:8000/admin ir prisijungti.
