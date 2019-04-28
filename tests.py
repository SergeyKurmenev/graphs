import unittest
import graphs


class TestMethods(unittest.TestCase):

    def setUp(self) -> None:
        """Графы и ожидаемые результаты составлял в тетради"""

        # три списка смежности
        self.first_adjacency_list = [[2, 5], [1, 3, 8], [2, 4], [3, 8], [1, 6, 7], [5], [5, 8], [2, 4, 7, 9],
                                     [8, 10], [9], [12, 13], [11, 13], [11, 12], [], []]
        self.second_adjacency_list = [[2, 9], [1, 3, 4], [2, 4], [2, 3, 5], [4, 6, 7], [5, 7, 8],
                                      [5, 6, 8], [6, 7, 10], [1, 10], [9, 8]]
        self.third_adjacency_list = [[2], [1], [4], [3], [6], [5, 7], [6], [], [], []]

        # ожидаемые результаты поиска компонент связности для этих списков
        self.expected_1_components = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
        self.expected_2_components = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.expected_3_components = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6]

        # ожидаемые результаты поиска расстояний для 1го списка (старт из 3х точек)
        self.expected_1_dist_from_2 = [1, 0, 1, 2, 2, 3, 2, 1, 2, 3, None, None, None, None, None]
        self.expected_1_dist_from_12 = [None, None, None, None, None, None, None, None, None, None, 1, 0, 1, None, None]
        self.expected_1_dist_from_10 = [4, 3, 4, 3, 4, 5, 3, 2, 1, 0, None, None, None, None, None]

        # ожидаемые результаты поиска расстояний для 2го списка (старт из 3х точек)
        self.expected_2_dist_from_3 = [2, 1, 0, 1, 2, 3, 3, 4, 3, 4]
        self.expected_2_dist_from_6 = [4, 3, 3, 2, 1, 0, 1, 1, 3, 2]
        self.expected_2_dist_from_10 = [2, 3, 4, 4, 3, 2, 2, 1, 1, 0]

        # ожидаемые результаты поиска расстояний для 3го списка (старт из 3х точек)
        self.expected_3_dist_from_6 = [None, None, None, None, 1, 0, 1, None, None, None]
        self.expected_3_dist_from_9 = [None, None, None, None, None, None, None, None, 0, None]
        self.expected_3_dist_from_1 = [0, 1, None, None, None, None, None, None, None, None]

    def test_find_distances(self):
        # поиск дистанций для первого списка смежности из 3х точек
        self.assertEqual(graphs.find_distances(self.first_adjacency_list, 2), self.expected_1_dist_from_2)
        self.assertEqual(graphs.find_distances(self.first_adjacency_list, 12), self.expected_1_dist_from_12)
        self.assertEqual(graphs.find_distances(self.first_adjacency_list, 10), self.expected_1_dist_from_10)

        # поиск дистанций для второго списка смежности из 3х точек
        self.assertEqual(graphs.find_distances(self.second_adjacency_list, 3), self.expected_2_dist_from_3)
        self.assertEqual(graphs.find_distances(self.second_adjacency_list, 6), self.expected_2_dist_from_6)
        self.assertEqual(graphs.find_distances(self.second_adjacency_list, 10), self.expected_2_dist_from_10)

        # поиск дистанций для третьего списка смежности из 3х точек
        self.assertEqual(graphs.find_distances(self.third_adjacency_list, 6), self.expected_3_dist_from_6)
        self.assertEqual(graphs.find_distances(self.third_adjacency_list, 9), self.expected_3_dist_from_9)
        self.assertEqual(graphs.find_distances(self.third_adjacency_list, 1), self.expected_3_dist_from_1)

    def test_find_connectivity_components(self):
        # поиск компонент связности для 3х списков смежности
        self.assertEqual(graphs.find_connectivity_components(self.first_adjacency_list), self.expected_1_components)
        self.assertEqual(graphs.find_connectivity_components(self.second_adjacency_list), self.expected_2_components)
        self.assertEqual(graphs.find_connectivity_components(self.third_adjacency_list), self.expected_3_components)


if __name__ == '__main__':
    unittest.main()
