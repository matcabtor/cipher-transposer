from modules.maps_creator import build_dictionary
from modules.tranposer import substitute_text
from unidecode import unidecode
import sys

def main():
    input_text_path, output_text_path, steps = sys.argv[1], sys.argv[2], int(sys.argv[3])

    # Read document
    with open(input_text_path, 'r') as file:
        input_text = file.read()
    
    normalized_text = unidecode(input_text)  # Remove diacritics

    # Normalize notes to get a 1:1 relation
    standard_notes_dict = {
        'REb': 'DO#',
        'RE#': 'MIb',
        'SOLb': 'FA#',
        'LAb': 'SOL#',
        'LA#': 'SIb',
    }

    # Lowercase version
    lowercase_standard = {}
    for key, value in standard_notes_dict.items():
        lowercase_key = key.lower()
        lowercase_value = value.lower()
        lowercase_standard[lowercase_key] = lowercase_value
    
    standard_notes_dict.update(lowercase_standard)

    # Normalization
    text_standard = substitute_text(normalized_text, standard_notes_dict)

    # Transposition
    transpose_dict = build_dictionary(steps)

    final_text = substitute_text(text_standard, transpose_dict)

    with open(output_text_path, 'w') as file:
        file.write(final_text)

if __name__ == "__main__":
    main()

    