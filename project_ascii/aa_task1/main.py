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

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <STRING>")
        return

    input_string = sys.argv[1]
    banner_path = "standard.txt"  

    
    banner = symbols(banner_path)
    
    
    ascii = art_ascii(input_string, banner)
    print(ascii)

if __name__ == "__main__":
    main()

