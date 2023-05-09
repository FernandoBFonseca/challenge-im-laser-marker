import pandas as pd

def import_plan(filename):
    #Receives the file with the plan and return the height, width and 
    #a list with the points to go
    df = pd.read_csv(filename, sep=';')
   
    w=df[df['Nom'] == 'tr0x']['Valeur'].values[0]
    h=df[df['Nom'] == 'tr0y']['Valeur'].values[0]  

    points_lists = []

    for i in range(1,13):
        x = df[df['Nom'] == f'tr{i}x']['Valeur'].values[0]
        y = df[df['Nom'] == f'tr{i}y']['Valeur'].values[0] 
        point = [x,y]
        points_lists.append(point)

    return w,h,points_lists