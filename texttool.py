#!/usr/bin/env python3
"""
TextTool: small CLI text processor for uppercase, lowercase, length,
count-words, prefix, etc.
"""
def process_line(line):
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()

    if cmd == "length":
        return len(text)
    if cmd == "prefix":
        return text[:10]
    
    # Ajout de la commande manquante d'Alexis 
    if cmd == "count-words":
        return len(text.split())
    if cmd == "prefix":
        return text[:10]

    if cmd == "prefix":
        return text[:10]


    if cmd == "length":
        return len(text)


    return "Unknown command " + cmd


def main():
    """
    Main CLI loop of TextTool.
    Continuously reads user input and prints results from process_line().
    """
    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))


if __name__ == "__main__":
    main()