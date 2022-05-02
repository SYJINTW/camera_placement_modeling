import os
import numpy as np
import pandas as pd
import random
from pathlib import Path

def generate_tv(max_lim: list, min_lim: list, num_of_tv: int):
    '''
    max_lim = [x,y,z,yaw,pitch,roll]
    min_lim = [x,y,z,yaw,pitch,roll]
    '''
    random.seed(1)

    random.random()
    results = []
    for i in range(num_of_tv):
        x = round(random.uniform(min_lim[0],max_lim[0]),3)
        y = round(random.uniform(min_lim[1],max_lim[1]),3)
        z = round(random.uniform(min_lim[2],max_lim[2]),3)
        yaw = round(random.uniform(min_lim[3],max_lim[3]),3)
        pitch = round(random.uniform(min_lim[4],max_lim[4]),3)
        roll = round(random.uniform(min_lim[5],max_lim[5]),3)
        while ((-0.5 < x < 0.5 and (-0.5 < z < 0.5)) or (-0.5 < y < 0.5 and (-0.5 < z < 0.5))):
            x = round(random.uniform(min_lim[0],max_lim[0]),3)
            y = round(random.uniform(min_lim[1],max_lim[1]),3)
            z = round(random.uniform(min_lim[2],max_lim[2]),3)
            yaw = round(random.uniform(min_lim[3],max_lim[3]),3)
            pitch = round(random.uniform(min_lim[4],max_lim[4]),3)
            roll = round(random.uniform(min_lim[5],max_lim[5]),3)
        results.append([i,x,y,z,roll,pitch,yaw])
    
    df = pd.DataFrame(results)
    df.to_csv('regression_tv0.csv', header=['idx','x','y','z','roll','pitch','yaw'], index=False)




def main():
    max_lim = [10,10,4,180,180,180]
    min_lim = [-10,-10,-4,-180,-180,-180]
    num_of_tv = 10
    generate_tv(max_lim, min_lim, num_of_tv)

if __name__ == '__main__':
    main() 