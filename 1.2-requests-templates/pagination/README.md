# Пагинация

Пагинация по csv-файлу с [портала открытых данных](https://data.mos.ru/datasets/752), содержащего список остановок наземного общественного транспорта.

Реализована функция отображения `stations.views.bus_stations`

Путь к файлу хранится в настройках `settings.BUS_STATION_CSV`.

Для чтения csv-файла используется [DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader).

![Пример результата](./res/result.png)
