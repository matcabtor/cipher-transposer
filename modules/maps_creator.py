def build_dictionary(step):

    ordered_list = ['DO', 'DO#', 'RE', 'MIb', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'SIb', 'SI']
    dictionary = {}
    list_length = len(ordered_list)
    
    for i, item in enumerate(ordered_list):
        target_index = (i + step) % list_length
        dictionary[item] = ordered_list[target_index]
    
    # Create an extended version of the dictionary with lowercase keys and values
    lowercase_dictionary = {}
    for key, value in dictionary.items():
        lowercase_key = key.lower()
        lowercase_value = value.lower()
        lowercase_dictionary[lowercase_key] = lowercase_value
    
    # Update the original dictionary with the lowercase version
    dictionary.update(lowercase_dictionary)
    
    return dictionary

    






