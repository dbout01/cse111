# Author - Dylan Butterfield, CSE111, 3:15 Class
import math

# Calculates water column height
def water_column_height(tower_height, tank_height):
    height = tower_height + 3 * tank_height / 4
    return height

# Calculates pressure gain from water column height
def pressure_gain_from_water_height(height):
    rho = 998.2  # Density of water in kg/m^3
    g = 9.80665  # Acceleration due to gravity in m/s^2
    pressure_gain = rho * g * height / 1000 # Convert pressure to kilopascals (kPa)
    return pressure_gain

# Calculates the pressure loss from pipe
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    rho = 998.2  # Density of water in kg/m^3
    pressure_loss = -friction_factor * pipe_length * rho * \
        fluid_velocity ** 2 / (2000 * pipe_diameter)
    return pressure_loss

# Calculates the water pressure lost due to fittings in a pipeline
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_water = 998.2  # Density of water in kg/m^3
    lost_pressure = (-0.04 * density_water * fluid_velocity **
                     2 * quantity_fittings) / 2000
    return lost_pressure


# Calculates the Reynolds number for water flowing through a pipe
def reynolds_number(hydraulic_diameter, fluid_velocity):
    density_water = 998.2 # Density of water in kg/m^3
    dynamic_viscosity = 0.0010016    # Dynamic viscosity of water in Pascal seconds
    reynolds = (density_water * hydraulic_diameter *
                fluid_velocity) / dynamic_viscosity
    return reynolds



# Calculates the water pressure lost due to water moving from a pipe with a large diameter to a pipe with a smaller diameter.
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density_water = 998.2  # Density of water in kg/m^3
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** (1 / 4 - 1))
    lost_pressure = -k * density_water * fluid_velocity ** 2 / 2000
    return lost_pressure



# Puts together everything & calls main for file to run
PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(
        diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()
