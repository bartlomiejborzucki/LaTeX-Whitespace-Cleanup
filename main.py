import os
import sys

def fix_tex_file(filename):
    with open(filename, "r+", encoding="utf-8") as f:
        content = f.read()

        # replace single space after short prepositions with non-breaking space
        # Polish
        content = content.replace(" w ", " w~")
        content = content.replace(" z ", " z~")
        content = content.replace(" o ", " o~")
        content = content.replace(" a ", " a~")
        content = content.replace(" u ", " u~")
        content = content.replace(" i ", " i~")
        content = content.replace(" W ", " W~")
        content = content.replace(" Z ", " Z~")
        content = content.replace(" O ", " O~")
        content = content.replace(" A ", " A~")
        content = content.replace(" U ", " U~")
        content = content.replace(" I ", " I~")
        
        # English
        content = content.replace(" a ", " a~")
        content = content.replace(" an ", " an~")
        content = content.replace(" the ", " the~")
        content = content.replace(" in ", " in~")
        content = content.replace(" on ", " on~")
        content = content.replace(" at ", " at~")
        content = content.replace(" for ", " for~")
        content = content.replace(" and ", " and~")
        content = content.replace(" or ", " or~")
        content = content.replace(" but ", " but~")
        content = content.replace(" A ", " A~")
        content = content.replace(" An ", " An~")
        content = content.replace(" The ", " The~")
        content = content.replace(" In ", " In~")
        content = content.replace(" On ", " On~")
        content = content.replace(" At ", " At~")
        content = content.replace(" For ", " For~")
        content = content.replace(" And ", " And~")
        content = content.replace(" Or ", " Or~")
        content = content.replace(" But ", " But~")

        # German
        content = content.replace(" An ", " an~")
        content = content.replace(" Auf ", " auf~")
        content = content.replace(" In ", " in~")
        content = content.replace(" Mit ", " mit~")
        content = content.replace(" Nach ", " nach~")
        content = content.replace(" Seit ", " seit~")
        content = content.replace(" Von ", " von~")
        content = content.replace(" Zu ", " zu~")
        content = content.replace(" Über ", " Über~")
        content = content.replace(" Und ", " Und~")
        content = content.replace(" Oder ", " Oder~")
        
        f.seek(0)
        f.write(content)
        f.truncate()

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".tex"):
                fix_tex_file(os.path.join(root, file))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: This script expects exactly one argument, the directory to process.")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: The given argument is not a directory.")
        sys.exit(1)

    process_directory(directory)
    