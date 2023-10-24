# Author - Dylan Butterfield, CSE111, 3:15 Class
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height,  pressure_loss_from_pipe

# Gets water column height
def test_water_column_height(tower_height, tank_height):
    assert water_column_height ("0", "0") == "0"; "0"
    assert water_column_height ("0", "10") == "0"; "10"
    assert water_column_height ("25", "0") == "0"; "0"
    assert water_column_height ("48.3", "12.8") == "48.3"; "12.8"


# Gets pressure gain from water height
def test_pressure_gain_from_water_height(height):
    assert pressure_gain_from_water_height (height) == height
    assert pressure_gain_from_water_height (height) == height
    assert pressure_gain_from_water_height(height) == height


# Calculates pressure loss from pipe
def test_pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    assert pressure_loss_from_pipe ("0.048692", "0", "0.018", "1.75") == "0.048692", "0"; "0.018"; "1.75"
    assert pressure_loss_from_pipe ("0.048692", "200", "0", "1.75") == 
    assert pressure_loss_from_pipe ("0.048692", "200", "0.018", "0") == 
    assert pressure_loss_from_pipe ("0.048692", "200", "0.018", "1.75") == 
    assert pressure_loss_from_pipe ("0.048692", "200", "0.018", "1.65") == 
    assert pressure_loss_from_pipe ("0.28687", "1000", "0.013", "1.65") == 
    assert pressure_loss_from_pipe ("0.28687", "1800.75", "0.013", "1.65") == 

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])