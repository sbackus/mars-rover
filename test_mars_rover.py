from mars_rover_kata import mars_rover, turn, warp_drive
from pytest import mark

rover_params = [
    ("F", "0:1:N"),
    ("FF", "0:2:N"),
    ("FFF", "0:3:N"),
    ("R", "0:0:E"),
    ("RLL", "0:0:W"),
    ("RF", "1:0:E"),
    ("RFLFLF", "0:1:W"),
    ("LF", "9:0:W"),
    ("RFFFFFFFFFF", "0:0:E"),
    ("FFFFFFFFFF", "0:0:N"),
    ("RRF", "0:9:S"),
]

@mark.parametrize( ("command", "result"), rover_params)
def test_mars_rover_commands(command, result):
    assert mars_rover(command) == result

turn_params = [
    ("N", "R", "E"),
    ("N", "L", "W"),
    ("W", "R", "N"),
]

@mark.parametrize( ("current_heading", "turn_signal", "new_heading"), turn_params)
def test_turn(current_heading, turn_signal, new_heading):
    assert turn(current_heading, turn_signal) == new_heading

def test_warp_drive():
    assert warp_drive(-1)==9
    assert warp_drive(10)==0
    assert warp_drive(5) == 5
