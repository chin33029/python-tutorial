"""Assignment 3"""


def welcome_statement():
    print('Welcome to Python Bar.')
    print(f'We have {bottle_total} shot(s) for sale')



if __name__ == '__main__':
 

    bottle_total = 32
    shots = 0  
    
        
    welcome_statement() 


    while int(shots) < int(bottle_total):
        
        shots = input('How many shots do you want (type exit to leave)')
                      
        if str(shots).lower().strip(' ') == 'exit':
            print('Thank you for being a Python Bar Customer.')
            break          

        if int(shots) == bottle_total:
            print('Closing up the bar because we have no more shots left.')
            break 
                                
        if int(shots) < bottle_total:
            bottle_total = bottle_total - int(shots)
            print(f'Sold {shots} shots(s) {bottle_total} shots left')
        if int(shots) > bottle_total:
            print(f'Not enough in bottle for {shots} [ {bottle_total} shots left]' )    
            shots = 0
        

