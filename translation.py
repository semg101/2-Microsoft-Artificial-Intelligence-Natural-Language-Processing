#pip install translate
from translate import Translator

translator= Translator(to_lang="German")
translation = translator.translate("Good Morning!")
print(translation)

print("---------------------------------")

from translate import Translator

translator= Translator(from_lang="german",to_lang="spanish")
translation = translator.translate("Guten Morgen")
print(translation)

print("-----------------------------------")
textToTranslate = input('Please enter a text: \n')
fromLangCode = input('What language is this?: \n')
toLangCode = input('To what language would you like to be translated?: \n')
translator= Translator(from_lang=fromLangCode,to_lang=toLangCode)
translation = translator.translate(textToTranslate)
print(translation)