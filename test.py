def alien_to_integer(alien_numeral):
    alien_map = {'A': 1, 'B': 5, 'Z': 10, 'L': 50, 'C': 100, 'D': 500, 'R': 1000}
    result = 0
    i = 0
    while i < len(alien_numeral):
        current_val = alien_map[alien_numeral[i]]
        if i + 1 < len(alien_numeral):
            next_val = alien_map[alien_numeral[i + 1]]
            if current_val < next_val:
                result += next_val - current_val
                i += 2  # Skip the next character
            else:
                result += current_val
                i += 1
        else:
            result += current_val
            i += 1
    return result

def main():
    while True:
        alien_numeral = input("Enter an Alien numeral (or 'exit' to quit): ").upper()
        if alien_numeral == 'EXIT':
            break
        integer_equivalent = alien_to_integer(alien_numeral)
        print(f"The integer equivalent of '{alien_numeral}' is: {integer_equivalent}")

if __name__ == "__main__":
    main()