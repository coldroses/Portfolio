#paul clear program status: complete


#use try and except to handle IOError, unspecified error exceptions

#main reads files content into a  string
#calls string_analysis function, pass string as argument
def main():
    readfile = open('text.txt', 'r')
    content = readfile.read()
    string_analysis(content)
    readfile.close()
    
#accepts string from main, use a loop to determine characters of each type
#display character summary
def string_analysis(content):
    upper = 0
    lower = 0
    dig = 0
    ws = 0
    try:
        for ch in content:
            if ch.isupper():
                upper += 1
            elif ch.islower():
                lower += 1
            elif ch.isdigit():
                dig += 1
            elif ch.isspace():
                ws +=1
        
        print("Uppercase letters: ", upper)
        print("Lowercase letters: ", lower)
        print("Whitespace characters: ",ws)
        print("Digits: ",dig)
    except IOError:
        print("Error reading the file.")
    except Exception:
        print('Error. Program terminated.')
main()

#output
#Uppercase letters: 60
#Lowercase letters: 970
#Whitespace characters: 134
#Digits: 7
