try:
    with open("H:\python projects\sample.txt.txt","r") as sample:
        b= sample.readlines()
        sample.seek(0)
        print("Reading file contents:")
        for i in range(len(b)):
            letter_counter=len(b[i])
            print("Line",i+1,":",sample.read(letter_counter),end="")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")