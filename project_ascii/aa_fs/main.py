def symbols(file_path):
    with open(file_path, "r") as f:
        lines = f.read().splitlines()





    ascii = {}
    word = []  
    curr_symbol = 32  




    for line in lines:
        if len(word) == 8:
            



            ascii[chr(curr_symbol)] = word
            curr_symbol += 1
            word = []  



        else:
            
            word.append(line)

    



    if len(word) == 8:

        ascii[chr(curr_symbol)] = word

    return ascii

def art_ascii(string, banner):
    
    lines = [""] * 8  



    for char in string:
        ascii_char = banner.get(char, [" " * 8] * 8)  
        for i in range(8):
            lines[i] += ascii_char[i]
    return "\n".join(lines)

def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: python3 main.py <STRING> <BANNER>")
        return

    input_string = sys.argv[1]
    banner_type = sys.argv[2].lower()

    
    banner_files = {
        "standard": "standard.txt",
        "shadow": "shadow.txt",
        "thinkertoy": "thinkertoy.txt"
    }

    if banner_type not in banner_files:
        print("Error: Напишите 'shadow' или 'standard' или 'thinkertoy'.")
        return

    banner_path = banner_files[banner_type]

    
    banner = symbols(banner_path)
    
    
    ascii_art = art_ascii(input_string, banner)
    print(ascii_art)

if __name__ == "__main__":
    main()