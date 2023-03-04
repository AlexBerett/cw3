### Задача:
<aside>
IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает пять последних успешных (EXECUTED) банковских операций клиента. Вам доверили реализовать алгоритм, который на бэкенде будет готовить данные для отображения в новом виджете.
</aside>

### Формат данных:
```commandline
<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>
```

### Пример вывода одной операций:
```commandline
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
```

### *зависимости проекта: см файл requirements.txt
