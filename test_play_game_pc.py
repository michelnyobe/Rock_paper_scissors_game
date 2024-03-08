"""Import the required modules and classes"""
from io import StringIO
from unittest.mock import patch
from rock_paper_scissors import play_game_pc

# Test the play_game_pc function with valid input
@patch('builtins.input', side_effect=['rock', 'no'])
def test_play_game_pc_valid_input(_mock_input):
    """Test play_game_pc function with valid input.

    This function tests the play_game_pc function to ensure that it behaves correctly 
    when valid input is provided. It uses a mocked input to simulate user input of 'rock',
    followed by 'no' to exit the game loop. It captures the output using a StringIO object 
    to check if the output contains any of the expected messages indicating a win, loss, or tie.

    Args:
        mock_input (Mock): A mocked input object to simulate user input.

    Returns:
        None
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        play_game_pc()
    output = fake_out.getvalue().strip()
    assert "YOU WIN!!!" in output or "YOU LOOSE!" in output or "IT'S A TIE!!!" in output

# Test the play_game_pc function with invalid input
@patch('builtins.input', side_effect=['invalid', 'rock', 'no'])
def test_play_game_pc_invalid_input(_mock_input):
    """Test play_game_pc function with invalid input.

    This function tests the play_game_pc function to ensure that it behaves correctly 
    when invalid input is provided. It uses a mocked input to simulate user input of 
    'invalid', 'rock', followed by 'no' to exit the game loop. It captures the output 
    using a StringIO object to check if the output contains the expected message indicating 
    an invalid choice.

    Args:
        mock_input (Mock): A mocked input object to simulate user input.

    Returns:
        None
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        play_game_pc()
    output = fake_out.getvalue().strip()
    assert "not a valid option" in output
