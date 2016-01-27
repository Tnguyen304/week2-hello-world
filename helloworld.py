#Thuc Nguyen

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!
# This program will greet the user 
<<<<<<< HEAD
=======


# Ask for them to choose one from three different languages to greet them in.
# Display greeting in selected language
# Press spacebar to exit
#Print(Choose one of the following languages and I will greet you in that language)
#Print(Vietnamese, Korean, or Japanese.)

def hello_world():
    return 'Hello world!'
def language():
    return 'Choose one of the following languages and I will greet you in that language. :L'
def choice():
    return 'Vietnamese, Korean, or Japanese.'
print(hello_world())
print(language())
print(choice())

language = input('Select a language:')

if language == 'Vietnamese':
    print('Xin chào bạn!')
elif language == 'Korean':
    print('안녕하세요')
elif language == 'Japanese':
    print('こんにちは')
elif language != 'Vietnamese''Korean''Japanese':
    print('Something went wrong!')
>>>>>>> origin/master


# Ask for them to choose one from three different languages to greet them in.
# Display greeting in selected language
# Press spacebar to exit
#Print(Choose one of the following languages and I will greet you in that language)
#Print(Vietnamese, Korean, or Japanese.)

def hello_world():
    return 'Hello world!'
def language():
    return 'Choose one of the following languages and I will greet you in that language. :L'
def choice():
    return 'Vietnamese, Korean, or Japanese.'
print(hello_world())
print(language())
print(choice())

language = input('Select a language:')

if language == 'Vietnamese':
    print('Xin chào bạn!')
elif language == 'Korean':
    print('안녕하세요')
elif language == 'Japanese':
    print('こんにちは')
elif language != 'Vietnamese''Korean''Japanese':
    print('Something went wrong!')
