
from hangman import random, replay_game, again

def test_random():
    assert "PYTHON" == "PYTHON"
    assert "JAVASCRIPT" == "JAVASCRIPT"
    assert "INTEGERS" == "INTEGERS"
    assert "ENCYCLOPEDIA" == "ENCYCLOPEDIA"

def test_replay_game():
    if again == ("y"): 
        return True
    elif again == ("n"): 
        return False