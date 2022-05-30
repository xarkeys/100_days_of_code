import explanation
import day_1.name_generator as day1
import day_2.split_the_bill as day2
import day_3.treasure_island as day3
import day_4.rock_paper_scissors as day4
import day_5.password_generator as day5
import day_6.reeborgs_world_maze as day6
import day_7.hangman as day7
import day_8.ceasar_cipher as day8


class ObjectManager:
    def __init__(self):
        self.__day = ''

    def run_day_01(self) -> str:
        city_name = input('What city did you grow up in?\n')
        hobby_name = input('What is your favourite hobby?\n')
        program = day1.BandName(city_name, hobby_name)
        return program.get_band_name()

    def run_day_02(self) -> str:
        bill_no_tip = float(input('What is the bill amount?\n'))
        tip_percentage = int(input('How much percent do you want to tip? (10, 12 or 15)\n'))
        num_diners = int(input('Among how many people do you want to split the bill?\n'))
        program = day2.Bill(bill_no_tip, tip_percentage)
        return program.split(num_diners)
