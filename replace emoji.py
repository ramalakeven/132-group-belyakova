def replace_character_with_emoji(string, character):
    ns = string.replace(character, '😎')
    return ns

string = input("Введите предложение: ")
character = input("Введите символ для замены: ")
ns = replace_character_with_emoji(string, character)
print("Новое предложение:", ns)