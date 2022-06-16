from lib2to3.pytree import _Results
from unittest import result
from dearpygui_demo import first_run

def test_version():
    assert first_run == '0.1.0'

    def test_calculate_windchill():
        excpeted = 36.0
        Results = first_run.calculate_windcill(5,40)
        assert excpeted == result
def test_calculate_windchill_forextreme():
    expected = -98
    _Results = first_run.calculate_windchill(60,-45)