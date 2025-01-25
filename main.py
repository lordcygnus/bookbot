def main():
    filepath = "books/frankenstein.txt"
    text = reader(filepath)
    count = count_doc(text)
    count_char = count_character_frequency(text)
    report = count_character_frequency_report(filepath, count, count_char)
    print(report)

def reader(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_doc(text):
    word_count = len(text.split())
    return word_count

def count_character_frequency(text):
    char_frequency = {}
    for char in text.lower():  # Convert to lowercase
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency

def count_character_frequency_report(file_name, word_count, char_frequency):
    # Filter out special characters and spaces
    filtered_frequency = {char: count for char, count in char_frequency.items() if char.isalpha()}

    # Build the report as a list of strings
    report_lines = []
    report_lines.append(f"--- Begin report of {file_name} ---")
    report_lines.append(f"{word_count} words found in the document\n")

    for char, count in sorted(filtered_frequency.items()):  # Sort alphabetically by character
        report_lines.append(f"The '{char}' character was found {count} times")

    report_lines.append("--- End report ---")

    # Join the list into a single string and return it
    return "\n".join(report_lines)

# call entrypoint last
main()
