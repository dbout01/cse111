# Author: Dylan Butterfield <- contain name for credit

def main(): #<- main script/function
    """
    ...
    """
    print(f"I'm feeling cold{cold()}") #<- will call function that contains "cold"
    print(f"I'm feeling extra cold{snow()}")
    print(f"I'm feeling hot{hot()}")

def cold():
    """ 
    Gives the cold emoji

    Returns: 
        str: the emoji for cold
    """
    return "🥶"

def hot():
    return "🔥"

def snow():
    return "⛄❄️"

main() #<- calls "main"




# MAIN STRUCTURE OF ASSIGNMENTS FOR REST OF CLASS
# LOOK OVER ASSINGMENTS AND SEE WHERE PLACEMENT IS NEEDED