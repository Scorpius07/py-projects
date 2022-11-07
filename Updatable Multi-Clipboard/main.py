# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:
# python mcb.pyw save <key> - Saves clipboard to keyword.
# python mcb.pyw <key> - Loads keyword to clipboard.
# python mcb.pyw list - Loads all keywords to clipboard.
# python mcb.pyw del <key> - Deletes key from the 'shelve' file.
# python mcb.pyw del all - Deletes all keys from the 'shelve' file.

# Example Text: Hello, World!
from pyperclip import copy, paste
import sys
import shelve

cmdLine = sys.argv
del cmdLine[0]

if cmdLine[0].lower() == "save":
    del cmdLine[0]
    text = paste()
    if text == "":
        print("Blank input not allowed."), exit()
    with shelve.open('Details') as file:
        file[cmdLine[0]] = text
        print(f"Clipboard's text ({text}) has been written to the backup file with the key: {cmdLine[0]}.\n")

elif cmdLine[0].lower() == "list":
    with shelve.open('Details') as file:
        keys = list(file.keys())
    print(f"The backup file contains {keys} (consider it empty if no value is in it).\n")

elif ' '.join(cmdLine).lower() == "del all":  # python mcb.pyw del all
    with shelve.open('Details') as file:
        file.clear()
    print("All cleared\n")

elif cmdLine[0].lower() == "del":
    with shelve.open('Details') as file:
        try:
            to_be_deleted = file[cmdLine[1]]
            del file[cmdLine[1]]
        except KeyError:
            print("Invalid key"), exit()

        print(f"'{to_be_deleted}' key deleted successfully. The file now contains:\n> {list(file.keys())}\n")

else:
    with shelve.open('Details') as file:
        value = file.get(cmdLine[0])
        to_copy = input(f"'{value}' is present inside '{file.get(cmdLine[0])}'. Do you want to copy it into the clipboard?\n"
                        "(Y)es | (N)o  > ")
        if to_copy.lower() == "y":
            copy_text = copy(value)
            print(f"\n'{value}' has been copied to your clipboard. Use CTRL + V to paste it anywhere.")


