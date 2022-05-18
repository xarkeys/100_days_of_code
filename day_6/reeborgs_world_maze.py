import explanation


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 6 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: None
    """
    expl_text = 'Today\'s challenge is not written in a Python file, we had to solve the maze challenge on the website'\
                'https://reeborg .ca/reeborg.html?'
    expl = explanation.Explanation(expl_text, 6)
    expl.print_explanation()

# the code to finish the maze was:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
