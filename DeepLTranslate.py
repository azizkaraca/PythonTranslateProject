import requests

# Enter the DeepL API key here
api_key = 'd4329109-647b-49c7-adae-da0baf47b3b4:fx'  # this is free API version of DeepL

# Specify the text and target languages you want to translate
text = input('Enter text to translate: ')
languages = ['EN', 'DE', 'RU', 'TR']  # define languages code here

# Define DeepL API URL here
url = "https://api-free.deepl.com/v2/translate"

for language in languages:
    # Required parameters for API request
    params = {
        'auth_key': api_key,
        'text': text,
        'target_lang': language
    }

    # Send the API request
    response = requests.post(url, data=params)

    # Check the response and print the translation
    if response.status_code == 200:
        result = response.json()
        translation = result['translations'][0]['text']
        print(f'Translated {language} text: {translation}')
    else:
        print(f"Error: {response.status_code}, {response.text}")

