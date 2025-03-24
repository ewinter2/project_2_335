#!/usr/bin/env python3

'''
Algorithm 2: Vibe Check - Card Shuffle
'''


def make_valid_groups(hand, group_size):
    '''
    Makes valid groups of cards from a
    hand that are group_size long
    and have consecutive values
    '''
    len_of_hand = len(hand)

    if len_of_hand % group_size != 0:
        print('Invalid group size.')
        return False

    hand.sort()

    hand_dict = {}
    for card in hand:
        if card in hand_dict:
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1

    while hand_dict:
        first_card = min(hand_dict.keys())
        for i in range(group_size):
            current_card = first_card + i
            if current_card not in hand_dict:
                return False
            hand_dict[current_card] -= 1
            if hand_dict[current_card] == 0:
                del hand_dict[current_card]
    return True


def main():
    '''Main function'''

    custom = input('''Welcome to Vibe Check - Card Shuffle! Would you like
    to use the example deck or enter in your own?
    Type "e" for the example or "c" for custom:''')

    if custom == 'e':
        sample_num = int(input('Sample 1 or Sample 2?'))
        if sample_num == 1:
            print('Sample 1: ')
            sample_1_hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
            sample_1_group_size = 3
            valid = make_valid_groups(sample_1_hand, sample_1_group_size)
        elif sample_num == 2:
            print('Sample 2: ')
            sample_1_hand = [1, 2, 3, 3, 4, 5, 6, 7]
            sample_1_group_size = 4
            valid = make_valid_groups(sample_1_hand, sample_1_group_size)
        else:
            print('Invalid sample number. Please enter 1 or 2.')
            return 1

    elif custom == 'c':
        print('You have chosen to enter in your own deck.')
        num_of_cards = int(input('How many cards are in your deck?'))
        custom_hand = []
        for i in range(num_of_cards):
            card = int(input(f'Enter the card {i + 1} value: '))
            custom_hand.append(card)

        custom_group_size = int(input('Enter the group size: '))
        valid = make_valid_groups(custom_hand, custom_group_size)

    else:
        print('Invalid choice. Please enter "e" or "c"')
        return 1

    if valid:
        print('True. You can make valid groups with this hand!')
    else:
        print('False. You cannot make valid groups with this hand')

    return valid


if __name__ == '__main__':
    main()
