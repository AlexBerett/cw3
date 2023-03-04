import requests
from datetime import datetime


def get_data(url):
    """
    Функция получает адрес ссылки json файла с данными бакновских транзакций и
    возвращает статус получения данных и список данных из json файла
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "info: Данные получены успешно!\n"
        return None, f"warning: Статус ответа {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "error: requests.exceptions.ConnectionError"


def get_filtered_data(data, filtered_empty_from=False):
    """
    Функция фильтрует данные списка (data)
    :param data: список данных
    :param filtered_empty_from: булево значение, True в случае наличия "from" в data
    :return: отфильтрованный список data, содержащий данные о проведенных операциях "EXECUTED"
    """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_data(data, count_last_values):
    """
    Функция сортирует список данных по убыванию даты совершенных операций ("date"),
    возвращает срез отсортированного по дате списка, где count_last_values - количество элементов списка
    """
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


def get_formatted_data(data):
    """
    Функция форматирует данные в списке data
    :param data: список данных
    :return: список данных в требуемом по ТЗ формате
    """
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        # Проверка наличия данных отправителя "from" в списке data
        if "from" in row:
            sender = row["from"].split()
            sender_bill = sender.pop(-1)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            sender_info = " ".join(sender)
        else:
            sender_bill, sender_info = "", "[СКРЫТО]"

        recipient = f"**{row['to'][-4:]}"
        amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{sender_info} {sender_bill} -> Счет {recipient}
{amount}
""")

    return formatted_data
