RULES = {3: "Fizz", 5: "Buzz" }  

def is_divisible_by(number: int, word: str) -> bool:

    for divisor, replacement in RULES.items():
        if replacement == word:
            return number % divisor == 0
    raise ValueError(f"Word '{word}' is not defined in RULES.")

def generate_fizzbuzz(start: int = 1, end: int = 100) -> list[str]:

    if end < start:
        raise ValueError("end needs to be >= start .")
    output: list[str] = []
    for number in range(start, end + 1):
        replacement = "".join(
            word for divisor, word in RULES.items() if number % divisor == 0
        )
        output.append(replacement or str(number))
    return output

def print_fizzbuzz(start: int = 1, end: int = 100) -> None:
    for line in generate_fizzbuzz(start, end):
        print(line)

if __name__ == "__main__":
    print_fizzbuzz()
