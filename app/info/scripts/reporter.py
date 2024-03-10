"""
    Скрипт для выявления просроченных заказов. 
    Фильтрует информацию на момент запуска фильтра. (системное время)
    Формирует 2 поля - просроченные заказы и горящие заказы 
    (срок исполнения которых меньше 1 дня)
    Работает с текстовым документом, который был экспортирован из ASC Control.
"""
from datetime import datetime, timedelta


class CheckOverdueReporter:
    NAMES = ('Просроченные заказы', 'Должны быть скоро готовы', 'Должны быть скоро готовы')
    FORMAT = r'%d.%m.%Y %H:%M:%S'
    DELTA_4 = timedelta(days=4)
    DELTA_3 = timedelta(days=3)
    STATUSES = ('В печати', 'Отпечатан', 'На упаковке')
    HEADERS = ('№ заказа', 'Статус сменился (Оплачен)', 'Клиент', 'Текущий статус')


    def __init__(self, file_path: str):
        self.__NOW = datetime.now()
        self.overdue = []
        self.hot = []
        self.normal = []
        self.__analyze(file_path)

    def as_dict(self) -> dict:
        report = {}
        for i, lst in enumerate((self.overdue, self.hot, self.normal)):
            if lst:
                lst.insert(0, self.HEADERS)
                report[self.NAMES[i]] = lst
        return report

    def __analyze(self, file_path: str):
        with open(file_path, 'r', encoding='cp1251') as file:
            lines = file.readlines()

        for line in lines:
            line = line[:-2].split('\t')

            # Разбираем линию по статусу
            status = line[-2]
            if status in self.STATUSES:
                # Убираем ненужные столбики
                line.pop(1)
                line.pop(-1)
                line.pop(-2)
            else:
                continue

            # Распределяем по спискам
            diff = self.__NOW - datetime.strptime(line[1], self.FORMAT)

            if diff > self.DELTA_4:
                self.overdue.append(line)
                continue

            if self.DELTA_3 <= diff <= self.DELTA_4:
                self.hot.append(line)
                continue
            
            self.normal.append(line)
