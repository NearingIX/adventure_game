class player_character:
    def __init__(self,character_name,level, occupation):
        self.character_name = character_name
        self.level = level
        self.occupation = occupation

def story_intoduction():
    print('Rumors of riches in the distant woods have lured you from your small village of Glenmist.\n' \
    'After a night of rainfall, you gather some items for the journey ahead and set out.')

def create_character():
    name_input = input("Enter your character's name:\n")
    choose_occupation = input("Choose your occupation:\n (A) Swordsman \n (B) Magician \n (C) Archer\n")
    if choose_occupation == 'A' or choose_occupation == 'a':
        occupation = 'Swordsman'
    elif choose_occupation == 'B' or choose_occupation == 'b':
        occupation = 'Magician'
    elif choose_occupation == 'C' or choose_occupation == 'c':
        occupation = 'Archer'
    else:
        print('Please enter A, B, or C for your occupation choice.')
    
    new_character = player_character(name_input,1, occupation)
    print('Welcome {0}!\nYou begin your new chapter as a level {1} {2}.'.format(
        getattr(new_character, 'character_name'), getattr(new_character, 'level'),
        getattr(new_character, 'occupation')))

    return new_character

story_intoduction()
new_character = create_character()
