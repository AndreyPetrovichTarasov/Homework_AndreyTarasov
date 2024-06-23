import pytest
from src.decorators import log, my_function


def test_log():
    @log(filename=None)
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_err(capsys):
    my_function(1, "2")

    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_err2(capsys):
    my_function(1, "2")

    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''
