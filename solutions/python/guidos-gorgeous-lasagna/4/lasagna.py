#!/usr/bin/env python 

from datetime import datetime, timezone, timedelta

"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40 
PREPARATION_TIME = 1
#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    print(f"The bake time remaining is: {bake_time_remaining}")
    return bake_time_remaining

def preparation_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the preparation time.
    :param number_of_layers: int - the number of layers that will be in the lasagna
    :elapsed_bake_time: int - elapsed cooking time
    """

    print("How many layers will your lasagna have?")
    number_of_layers = int(input())
    PREPARATION_TIME = number_of_layers * 2
    

    print(f"The total preparation time in minutes is: {PREPARATION_TIME}")
    return PREPARATION_TIME


def elapsed_time_in_minutes(elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    elapsed_cooking_time = elapsed_bake_time + PREPARATION_TIME
    print(f"The total time that has passed (in minutes) preparing and cooking is: {elapsed_cooking_time}")
    return elapsed_cooking_time 

def main():
    number_of_layers = 1
    print("What is your expected bake time?")
    EXPECTED_BAKE_TIME = int(input())
    
    elapsed_bake_time = 0
    
    # Assign value to PREPARATION_TIME
    preparation_time_in_minutes(number_of_layers, elapsed_bake_time)
    
    elapsed_time_in_minutes(elapsed_bake_time)

    remaining_bake_time = bake_time_remaining(elapsed_bake_time)
    print(f"Total bake time remaining is: {remaining_bake_time}")
    time_now_utc = datetime.now(timezone.utc)
    print(f"The time is now: {time_now_utc}")
    print(f"The lasagna should be ready at: {(time_now_utc + timedelta(minutes=remaining_bake_time))}")

#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO: define the 'elapsed_time_in_minutes()' function below.



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

if __name__ == "__main__":
    main()
