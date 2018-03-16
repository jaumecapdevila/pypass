import click
import random
import string

def gen_password(length, withSpecialCharacters):
    charactersToUse = get_character_list(withSpecialCharacters)
    secureRandom = random.SystemRandom()
    finalPassword = ''
    i = 0
    while i < int(length):
        character = secureRandom.choice(charactersToUse)
        finalPassword += character
        i += 1
    return finalPassword

def get_character_list(withSpecialCharacters):
    availableChars = list(string.ascii_lowercase + string.ascii_uppercase)
    if withSpecialCharacters:
        specialCharsList = list('!#%^&{}[].-_')
        availableChars += specialCharsList
    return availableChars


@click.command()
@click.argument('length')
@click.option('--special', is_flag=True, help='define if the password should contain special characters or not')
def cli(length, special):
    print special
    generatedPassword = gen_password(length, special)
    click.echo(generatedPassword)

