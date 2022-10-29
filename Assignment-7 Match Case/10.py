user_liking_color = input("Enter the color you like: ")
match user_liking_color:
    case user_liking_color if 'yellow' in user_liking_color:
        print('Yellow - Monday')
    case user_liking_color if 'blue' in user_liking_color:
        print('Blue - Tuesday')
    case user_liking_color if 'orange' in user_liking_color:
        print('Orange - Wednesday')
    case user_liking_color if 'white' in user_liking_color:
        print('White - Thursday')
    case user_liking_color if 'black' in user_liking_color:
        print('Black - Friday')
    case user_liking_color if 'red' in user_liking_color:
        print('Red - Saturday')
    case _:
        print('All other colours - Sunday')