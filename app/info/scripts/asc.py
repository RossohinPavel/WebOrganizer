"""
    Скрипт для выявления просроченных заказов. 
    Фильтрует информацию на момент запуска фильтра. (системное время)
    Формирует 2 поля - просроченные заказы и горящие заказы 
    (срок исполнения которых меньше 1 дня)
    Работает с текстовым документом, который был экспортирован из ASC Control.
"""
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os import listdir as os_listdir, remove as os_remove
from .reporter import CheckOverdueReporter


def check_overdue(file):
    if file.name != 'OrdersReport.txt':
        return

    file_path = f'{settings.MEDIA_ROOT}/{file.name}'
    if file.name in os_listdir(settings.MEDIA_ROOT):
        os_remove(file_path)

    FileSystemStorage().save(file.name, file)
    
    return CheckOverdueReporter(file_path).as_dict()


REPORTS = {
    'Проверка на просроченные заказы': check_overdue
}