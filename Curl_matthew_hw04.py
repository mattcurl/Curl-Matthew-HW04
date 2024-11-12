# Matt Curl
# 13
# 11/12/2024
#Sources, help given to/received from: 
# Lucas Dillon
# Googled "Can you multiply a string in python" 
# Got: https://www.codechef.com/learn/course/python/LTCPY08/problems/PYTHCL37A#:~:text=In%20Python%2C%20you%20can%20multiply,a%20specified%20number%20of%20times.
# import path library so we can read the prompt and output a file
from pathlib import Path
inputs = Path('prompt.txt')
outputs = Path('out.txt')

# set up the prompt for reading
prompt = inputs.read_text()
lines = prompt.splitlines()

#initialize output string for later
output_str = ""

# have it read each new line
for line in lines:
#split each line by space so we get each command
    commands = line.split()
    

    # have it iterate through each command
    for func in commands:
    #split each command into a list
        
        parts = func.split(":")

        # turn the value into an int so it can be used for calculations later
        value = int(parts[1])
        
# use if operator to check the value of the key
        if parts[0] == "w":

            # append output with the character asscoiated with key times the value number
            output_str += " " * value
           
        # repeat for other character/ key pair
        if parts[0] == "*":

            output_str += "*" * value
    # add a new line at the end of each line
    output_str += "\n"
    
        
# write the final string into the output file
outputs.write_text(output_str)

