import pytest
from src.decorators import log, my_function
from src.config import ROOT_PATH
from pathlib import Path


def test_log():
    @log(filename=None)
    def myfunction(x, y):
        return x + y

    result = myfunction(1, 2)
    assert result == 3


@log(filename="log_file.txt")
#@log()
def add(x, y):
    return x + y


def test_log_err3():

    with pytest.raises(TypeError):
        log_file = Path(ROOT_PATH, "log_file.txt")
        print(log_file)

        add(1, "2")

    assert log_file.exists()

    with open(log_file, 'r') as f:
        log_contents = f.read()
        assert "add error:unsupported operand type(s) for +: 'int' and 'str' . Inputs: (1, '2'), {}" in log_contents

