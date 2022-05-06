"""Test for time_of_day method"""
from freezegun import freeze_time
from python_advanced.unittesting.to_test import time_of_day


@freeze_time('2017-05-21 11:24:15', auto_tick_seconds=18000)
def test_time_of_day():
    """Check the correctness of the returned value"""
    assert time_of_day() == "morning"
    assert time_of_day() == "afternoon"
    assert time_of_day() == "night"
    assert time_of_day() == "night"
