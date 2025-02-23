import requests
from bs4 import BeautifulSoup

# Рекорд Уэйна Гретцки
GRETZKY_GOALS = 894


# Функция для получения количества шайб Овечкина
def get_ovechkin_goals():
    # URL страницы с профилем Овечкина на ESPN
    url = "https://www.espn.com/nhl/player/stats/_/id/3101/alex-ovechkin"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем блок с общей статистикой Career
        stats_block = soup.find_all('span', class_='fw-bold clr-gray-01')
        if stats_block:
            # Ищем количество шайб
            goals = stats_block[2].text
            return int(goals)
        else:
            print("Не удалось найти блок со статистикой.")
            return None
    else:
        print("Ошибка при загрузке страницы.")
        return None


# Получаем текущее количество шайб Овечкина
ovechkin_goals = get_ovechkin_goals()

if ovechkin_goals is not None:
    # Вычисляем, сколько шайб осталось до рекорда
    goals_needed = GRETZKY_GOALS - ovechkin_goals

    # Выводим результат
    if goals_needed > 0:
        print(f"Александру Овечкину осталось забить {goals_needed} шайб до рекорда Уэйна Гретцки.")
    elif goals_needed == 0:
        print("Александр Овечкин достиг рекорда Уэйна Гретцки!")
    else:
        print("Александр Овечкин побил рекорд Уэйна Гретцки!")
else:
    print("Не удалось получить данные о количестве шайб.")