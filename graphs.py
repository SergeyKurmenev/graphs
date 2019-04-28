from my_queue import MyQueue


def find_distances(adjacency_list: [], start_point: int) -> []:
    """Поиск расстояния для всех точек, которые связаны с точкой начала поиска.
    Возвращает массив в котором для каждого элемента указано расстояние от стартовой точки или
    None если данная точка не связана со стартовой.
    Т.к. нумерация точек идёт с 1, а не с 0 и на вход принимаю номер точки в таком виде -
    появились паразитные '-1' в коде."""

    results = []
    start_point -= 1
    for i in range(len(adjacency_list)):
        results.append(None)

    queue = MyQueue()
    start_depth = 0
    queue.enqueue([start_point, start_depth])

    while not queue.empty():
        point = queue.dequeue().value
        if results[point[0]] is None:
            results[point[0]] = point[1]
        for connected_point in adjacency_list[point[0]]:
            if results[connected_point - 1] is None:
                queue.enqueue([connected_point - 1, point[1] + 1])

    return results


def find_connectivity_components(adjacency_list: []) -> []:
    """Поиск компонент связаности.
    Возвращает массив в котором для каждого элемента указан номер компоненты связаности.
    Основан на поиске расстояний:
    Шаг 1: Создаю массив для результатов(размер совпадает со списком смежности т.е. с количеством элементов)
      и заполняю его None элементами
    Шаг 2: Для первого None элемента делаю поиск расстояний
    Шаг 3: Всем найденным элементам(для которых было найдено расстояние) присваиваю номер компоненты
    Шаг 4: Увеличиваю номер компоненты
    Шаг 5: Повторяю действия 2-5 пока не дойду до конца(больше не будет None элементов в массиве результатов)"""

    connectivy_count = 1
    results = []
    for i in range(len(adjacency_list)):
        results.append(None)

    for point_number in range(len(results)):
        if results[point_number] is None:
            distances = find_distances(adjacency_list, point_number + 1)
            for point in range(len(distances)):
                if distances[point] is not None:
                    results[point] = connectivy_count
            connectivy_count += 1

    return results
