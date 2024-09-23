import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.array(list).reshape(3, 3)
    
    calculations = { 
        'mean': [
            np.mean(matriz, axis=0).tolist(), 
            np.mean(matriz, axis=1).tolist(), 
            np.mean(matriz).tolist()
        ],
        'variance': [
            np.var(matriz, axis=0).tolist(), 
            np.var(matriz, axis=1).tolist(), 
            np.var(matriz).tolist()
        ], 
        'standard deviation': [
            np.std(matriz, axis=0).tolist(), 
            np.std(matriz, axis=1).tolist(), 
            np.std(matriz).tolist()
        ], 
        'max': [
            np.max(matriz, axis=0).tolist(), 
            np.max(matriz, axis=1).tolist(), 
            np.max(matriz).tolist()
        ],
        'min': [
            np.min(matriz, axis=0).tolist(), 
            np.min(matriz, axis=1).tolist(), 
            np.min(matriz).tolist()
        ],
        'sum': [
            np.sum(matriz, axis=0).tolist(), 
            np.sum(matriz, axis=1).tolist(), 
            np.sum(matriz).tolist()
        ]
    }
    
    return calculations
