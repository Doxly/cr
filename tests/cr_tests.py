from nose.tools import *
import copy

#from NAME.app import MyApplication
import cr.app
import cr.model


class Cr_Cubic_tests(object):
    """docstring for NAME_tests"""

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_rotate(self):
        # Угловой кубик
        cubic = cr.model.Cubic((1, 1, 1), (0, 0, 0))

        new_position = cubic.rotate(cubic.position, axe=0, angle=90)
        assert_equals([1, -1, 1], new_position,
            'крутим вокруг x против часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=0, angle=-90)
        assert_equals([1, 1, -1], new_position,
            'крутим вокруг x по часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=1, angle=90)
        assert_equals([1, 1, -1], new_position,
            'крутим вокруг y против часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=1, angle=-90)
        assert_equals([-1, 1, 1], new_position,
            'крутим вокруг y по часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=2, angle=90)
        assert_equals([-1, 1, 1], new_position,
            'крутим вокруг z против часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=2, angle=-90)
        assert_equals([1, -1, 1], new_position,
            'крутим вокруг z по часовой на 90')

        # кубик на грани
        cubic = cr.model.Cubic((1, 0, 1), (0, 0, 0))
        new_position = cubic.rotate(cubic.position, axe=0, angle=90)
        assert_equals([1, -1, 0], new_position,
            'крутим вокруг x против часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=0, angle=-90)
        assert_equals([1, 1, 0], new_position,
            'крутим вокруг x по часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=1, angle=90)
        assert_equals([1, 0, -1], new_position,
            'крутим вокруг y против часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=1, angle=-90)
        assert_equals([-1, 0, 1], new_position,
            'крутим вокруг y по часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=2, angle=90)
        assert_equals([0, 1, 1], new_position,
            'крутим вокруг z против часовой на 90')

        new_position = cubic.rotate(cubic.position, axe=2, angle=-90)
        assert_equals([0, -1, 1], new_position,
            'крутим вокруг z по часовой на 90')


    def test_swap_colors(self):
        # Угловой кубик
        source_cubic = cr.model.Cubic((1, 1, 1), (1, 2, 3))

        cubic = copy.deepcopy(source_cubic)
        cubic.swap_colors(0)
        assert_equals([1, 3, 2], cubic.colors, 'Вращаем вокруг x')

        cubic = copy.deepcopy(source_cubic)
        cubic.swap_colors(1)
        assert_equals([3, 2, 1], cubic.colors, 'Вращаем вокруг y')

        cubic = copy.deepcopy(source_cubic)
        cubic.swap_colors(2)
        assert_equals([2, 1, 3], cubic.colors, 'Вращаем вокруг z')

        # кубик на ребре
        source_cubic = cr.model.Cubic((1, 0, 1), (1, 0, 3))

        cubic = copy.deepcopy(source_cubic)
        cubic.swap_colors(0)
        assert_equals([1, 3, 0], cubic.colors, 'Вращаем вокруг x')

        cubic = copy.deepcopy(source_cubic)
        cubic.swap_colors(1)
        assert_equals([3, 0, 1], cubic.colors, 'Вращаем вокруг y')

        cubic = copy.deepcopy(source_cubic)
        cubic.swap_colors(2)
        assert_equals([0, 1, 3], cubic.colors, 'Вращаем вокруг z')

class Cr_Model_Tests(object):
    """Набор тестов для cr.model.Model"""

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_build_cubics(self):
        dimension = 3
        model = cr.model.Model(dimension)
        assert_equals(dimension **3, len(model.cubics),
            'Количество кубиков в модели')
        print('model:{}'.format(model.cubics))