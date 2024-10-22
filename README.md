# familyTree2

Generate messages.pot:
xgettext -d messages -o locales/messages.pot test_locales.py --from-code UTF-8

Generate message.po's:
msginit -l de_DE.UTF8 -o locales/de/LC_MESSAGES/messages.po -i locales/messages.pot --no-translator

Generate messages.mo's:
msgfmt locales/en/LC_MESSAGES/messages.po -o locales/en_GB/LC_MESSAGES/messages.mo