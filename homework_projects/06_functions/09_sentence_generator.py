def make_sentence(word: str, part_of_speech: int):
   
    
    sentence_templates = {

        0: f"I am excited to learn more about {word} and its impact on technology!",  
        
        1: f"AI can {word} data faster than humans!", 
        
        2: f"This new AI model is very {word} and powerful!" 
    }

    
    print(sentence_templates.get(part_of_speech, "Part of speech must be 0, 1, or 2! Can't make a sentence."))


    
    word = input("Please type a noun, verb, or adjective: ")

    print("Is this a noun, verb, or adjective?")
    
    try:

        part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))

        make_sentence(word, part_of_speech)

    except ValueError:

        print("Invalid input! Please enter 0, 1, or 2.")

