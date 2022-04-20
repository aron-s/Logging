"""Testing logs being created"""
import os

def test_info_log():
    """test log.info"""
    assert os.path.exists('./app/logs/info.log') == True

def test_debug_log():
    """test debug.info"""
    assert os.path.exists('./app/logs/debug.log') == True

def test_random_log():
    assert os.path.exists('./app/logs/random.log') == False