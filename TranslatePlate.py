from translate import Translator
languages = ['de', 'ru', 'tr']
text = input('Enter text to translate: ')

for language in languages:
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    print(f'Translated {language} text: {translation}')