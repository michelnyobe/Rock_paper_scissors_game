""" Import the functions to test from the rock_paper_scissors.py file"""
from rock_paper_scissors import verify_input, winning_answers, anime

def test_verify_input():
    """Test the verify_input function
    """
    assert verify_input("rock") is True
    assert verify_input("paper") is True
    assert verify_input("scissors") is True
    assert verify_input("invalid") is False

def test_winning_answers():
    """Test the winning_answers function"""  
    assert winning_answers("rock", "scissors") is True
    assert winning_answers("paper", "rock") is True
    assert winning_answers("scissors", "paper") is True
    assert winning_answers("rock", "rock") is False
    assert winning_answers("paper", "paper") is False
    assert winning_answers("scissors", "scissors") is False

def test_anime():
    """Test the anime function"""
    assert anime("rock", "rock") is True
    assert anime("paper", "paper") is True
    assert anime("scissors", "scissors") is True
    assert anime("scissors", "paper") is None
    assert anime("paper", "scissors") is None
    assert anime("scissors", "rock") is None
