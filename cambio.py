import time


if __name__=='__main__':
    
    corriente = 0
    prev_val = 0
    error = 1
    
    while True:
        tecla = input()
        
        #modificacion de corriente

        if tecla == "+":
            corriente += 10
        elif tecla == "-":
            corriente -= 10


        if corriente > (prev_val - error) and corriente < (prev_val + error):
            print("No cambio")            
        else:
            print("Cambio")
            prev_val = corriente

        print(corriente)
        time.sleep(.5) 

