# Hepterakt

Invoices and tasks management application 

## Installation

```
git clone `this repo`
pip -r requirements.txt install
```

## Requirements

```
Django==2.2.1
python-dateutil==2.8.0
```

## Building and running

```
cd Hepterakt
python manage.py runserver
```

## Features

### To do app 
 
 - tasks that can be rescheduled for the nest month,
 - all task may be set to undone by one click.
 
### Payments app

 - adding payments with thick to indicate if it is paid,
 - separating payments in categories,
 - ability to upload and download invoices,
 - payments separation by year and month, history of payments,
 - warning will appear when close to deadline.

### Hour report

 - adding monthly work hours and vacation hours.
 
### Backend

 - login required middleware - only registered users may surf the app

## ToDo tasks / changelog

- [x] lista terminw "todo" do odchaczania w ramach danego msc / opcja zamknij miesic
- [x] dodawanie wydatków w kategoriach + faktury
- [x] przeglądanie historii wydatków
- [x] filtrowanie wydatków - domyślnie po year/mth, możliwość zmiany (poprzedni, następny)
- [x] middleware
- [x] h tracking
- [x] view only file name not whole path
- [x] fix setting paid
- [x] add month hours tracking tool
- [x] installation instruction in readme and requirements, 
- [x] list features
- [x] warning fot deadline approaching
- [x] podsumowanie wydatków per mth