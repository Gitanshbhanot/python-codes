from translate import Translator
translator = Translator(to_lang="ja")
try:
    with open('exercise.txt', mode='r') as fp:
        text = fp.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test-ja.txt', mode='w') as my_file:
            my_file.write(translation)
except FileNotFoundError as e:
    print('check your file path silly')
