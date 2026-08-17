"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

        Parameters:
            elapsed_bake_time (int): The baking time already elapsed.
    
        Returns:
            int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    
        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes (number_of_layers):
    """Calculate the preparation time in minutes.

        Parameters:
            number_of_layers (int): The number of layers you want to add to the lasagna.
    
        Returns:
            int: The preparation time (in minutes) derived from 'preparation_time_in_minutes'.
    
        Function that takes the actual minutes it takes to prepare in minutes depending on the number of layers and preparation time.
    """
    preparation_time_in_minutes = PREPARATION_TIME * number_of_layers
    return preparation_time_in_minutes


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

        Parameters:
             number_of_layers(int): the number of layers added to the lasagna.
            elapsed_bake_time(int): the number of minutes the lasagna has spent baking in the oven already.
    
        Returns:
            int: The elapsed time (in minutes) derived from 'elapsed_time_in_minutes'.
    
        Function that takes the number of layers and time the lasagna has been in the oven and gives you the elapsed time in minutes.
    """
    elapsed_time_in_minutes = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elapsed_time_in_minutes

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
