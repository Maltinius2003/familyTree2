import gettext
import sys

gettext.bindtextdomain("messages", "locales")
gettext.textdomain("messages")

locale = sys.argv[1] if len(sys.argv) > 1 else "en"

try:
    lang = gettext.translation("messages", localedir="locales", languages=[locale])
    lang.install()
    _ = lang.gettext
except FileNotFoundError:
    # fallback to english, if the locale is not found
    print(f"Warning: No translation found for '{locale}'. Falling back to English.")

    gettext.install("messages", localedir="locales")
    _ = gettext.gettext

def main():
    print(_("Hello, world!"))

if __name__ == "__main__":
    main()