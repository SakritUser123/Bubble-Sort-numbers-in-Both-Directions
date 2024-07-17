dir = input('up or down ')
if dir == 'up':
    values= []
    vert = input('Type out your list(seperated by commas): ')
    values = [int(num) for num in vert.split(',')]
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(values)-1):
            if values[i] > values[i+1]:
                sorted = True
                values[i],values[i+1] = values[i+1],values[i]
            
           
    print(values)
    
if dir == 'down':
    values= []
    vert = input('Type out your list(seperated by commas): ')
    values = [int(num) for num in vert.split(',')]
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(values)-1):
            if values[i] < values[i+1]:
                sorted = True
                values[i],values[i+1] = values[i+1],values[i]
            
           
    print(values)
        
