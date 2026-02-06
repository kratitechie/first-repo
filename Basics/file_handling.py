message=input("Enter a text to be printed in a file:\n")

with open('output.txt', 'w') as f:
    f.write(message)
    
with open('output.txt', 'r') as f:
          print(f.read())
          
    