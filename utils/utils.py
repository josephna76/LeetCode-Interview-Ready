def print_colored(text, status):
    colors = {
        "pass": "\033[92m",  # Green
        "fail": "\033[91m",  # Red
        "end": "\033[0m",
    }
    symbols = {
        "pass": "\u2714",  # Checkmark
        "fail": "\u2716",  # Cross
    }
    color = colors.get(status, "")
    symbol = symbols.get(status, "")
    print(f"{color}{symbol} {text}{colors['end']}")
