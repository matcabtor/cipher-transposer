from modules.utils import add_space_around_colons

def substitute_text(input_text, dictionary):
    lines = input_text.splitlines()  # Split input text into lines
    
    result = []
    for line in lines:
        line = add_space_around_colons(line) # Add space around ritornelos to prevent it to come with notes
        words = line.split()  # Split line into words
        substituted_words = []
        
        for word in words:
            if word.upper().replace('B', 'b') in dictionary:
                word = word.upper().replace('B', 'b') # Make the whole note uppercase
            if word in dictionary:
                substituted_words.append(dictionary[word])  # Substitute if in dictionary
            else:
                substituted_words.append(word)  # Keep the original word
        
        substituted_line = ' '.join(substituted_words)  # Join words back into a line
        result.append(substituted_line)
    
    output_text = '\n'.join(result)  # Join lines back into text with preserved line breaks
    return output_text