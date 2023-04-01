def underline(text: str, color="white"):
    if color == "white":
        return "\x1b[4;37;40m" + text + "\x1b[0m"
    elif color == "pink":
        return "\x1b[4;35;40m" + text + "\x1b[0m"
    return text


def italic(text: str, color="while"):
    if color == "white":
        return "\x1b[3;37;40m" + text + "\x1b[0m"
    elif color == "pink":
        return "\x1b[3;35;40m" + text + "\x1b[0m"
    elif color == "yellow":
        return "\x1b[3;33;40m" + text + "\x1b[0m"
    return text


def yellow(text: str):
    return "\x1b[1;33;40m" + text + "\x1b[0m"


def red(text: str):
    return "\x1b[1;31;40m" + text + "\x1b[0m"


def green(text: str):
    return "\x1b[1;32;40m" + text + "\x1b[0m"


def pink(text: str):
    return "\x1b[1;35;40m" + text + "\x1b[0m"

def white(text: str):
    return "\x1b[1;37;40m" + text + "\x1b[0m"
