def draw_hangman(mistake_count: int) -> str:
    """
    Draw a specific step of the hangman game progress. Depending on the number of mistakes have already been made.
    :param mistake_count: The number of mistakes the player has made so far.
    :type mistake_count: int
    :return: The hangman ASCII art, depending on the number of mistakes made.
    :rtype: str
    """
    stages = ['''
    +---+
     |   |
         |
         |
         |
         |
    ======
    ''', '''
    +---+
     |   |
     0   |
         |
         |
         |
    ======
    ''', '''
    +---+
     |   |
     0   |
     |   |
         |
         |
    ======
    ''', '''
    +---+
     |   |
     0   |
    /|   |
         |
         |
    ======
    ''', '''
    +---+
     |   |
     0   |
    /|\  |
         |
         |
    ======
    ''', '''
    +---+
     |   |
     0   |
    /|\  |
    /    |
         |
    ======
    ''', '''
     +---+
     |   |
     0   |
    /|\  |
    / \  |
         |
    ======     
    '''
              ]
    return stages[mistake_count]
