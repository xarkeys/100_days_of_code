def name_generator():
    print('Welcome to the Band Name Generator.')
    city_name = input('What\'s the name of the city you grew up in? ')
    pet_name = input('What\'s your pet\'s name? ')
    band_name = city_name + pet_name
    return 'You band name could be: {}'.format(band_name)

