# ASCII characters mapping to upside version of those characters in Unicode strings.
# Could also pass as a commandline game for nerds.

def ascii_mapper():
    '''
    This function takes a string of ASCII characters and 
    returns the upside-down version of those characters in Unicode strings.
    '''
    ascii_dict = {
        'a':'\U00000250',
        'b':'\U00000071',
        'c':'\U00000254',
        'd':'\U00000070',
        'e':'\U000001DD',
        'f':'\U0000025F',
        'g':'\U00000183',
        'h':'\U00000265',
        'i':'\U00001D09',
        'j':'\U0000027E',
        'k':'\U0000029E',
        'l':'\U00000283',
        'm':'\U0000026F',
        'n':'\U00000075',
        'o':'\U0000006F',
        'p':'\U00000064',
        'q':'\U00000062',
        'r':'\U00000279',
        's':'\U00000073',
        't':'\U00000287',
        'u':'\U0000006E',
        'v':'\U0000028C',
        'w':'\U0000028D',
        'x':'\U00000078',
        'y':'\U0000028E',
        'z':'\U0000007A',
        'A':'\U00002200',
        'B':'\U00000042',
        'C':'\U00000186',
        'D':'\U00000044',
        'E':'\U0000018E',
        'F':'\U00002132',
        'G':'\U000005E4',
        'H':'\U00000048',
        'I':'\U00000049',
        'J':'\U0000017F',
        'K':'\U000022CA',
        'L':'\U00002142',
        'M':'\U0000004D',
        'N':'\U0000004E',
        'O':'\U0000004F',
        'P':'\U00000500',
        'Q':'\U00000051',
        'R':'\U00000052',
        'S':'\U00000053',
        'T':'\U00002534',
        'U':'\U00002229',
        'V':'\U0000039B',
        'W':'\U0000004D',
        'X':'\U00000058',
        'Y':'\U00002144',
        'Z':'\U0000005A',
        '0':'\U00000030',
        '1':'\U00000196',
        '2':'\U00001105',
        '3':'\U00000190',
        '4':'\U00003123',
        '5':'\U000003DB',
        '6':'\U00000039',
        '7':'\U00003125',
        '8':'\U00000038',
        '9':'\U00000036',
        ',':'\U0000002C',
        '.':'\U000002D9',
        '?':'\U000000BF',
        '!':'\U000000A1',
        '"':'\U00000022',
        '\'':'\U0000002C',
        '`':'\U0000002C',
        '(':'\U00000029',
        ')':'\U00000028',
        '[':'\U0000005D',
        ']':'\U0000005B',
        '{':'\U0000007D',
        '}':'\U0000007B',
        '<':'\U0000003E',
        '>':'\U0000003C',
        '&':'\U0000214B',
        '-':'\U0000203E',
        ' ':'\U00000020',
        
        }
    
    holder = []  # create an empty to hold translated characters
    
    user = True  # set user to True

    while user:
        get_string = input('Enter phrase, word or letter: ')
    
        for char in get_string:
            holder.append(ascii_dict[char])
        print('\n')
        print('\n')
        print('Game starting...','\U0000231B')
        print('>>> ',''.join(holder[:]))
        print('Press 1 to play again...or...Press 0 to quit')
        action = int(input('>> '))
        del(holder[:])
        if action == 1:
            continue
        elif action == 0:
            print('Game over!','\N{GRINNING FACE}')
            break
            
if __name__ == '__main__':
    ascii_mapper()
