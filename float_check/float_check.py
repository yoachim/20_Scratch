import numpy as np
import pandas as pd
import sqlite3

# Generate some numbers to see if different hardware setups treat float differently

def data_generate(seed=42):
    float1 = 310.3930573237407
    float2 = 310.39305732374066
    float3 = 310.393057323740656

    num_floats = np.array([float1, float2, float3])

    np.random.seed(seed)
    rand_floats = np.random.random(100)

    print('float1=', float1)
    print('float2=', float2)
    print('float3=', float3)

    print('from the numpy array')
    for num in num_floats:
        print(num)

    # Let's dump the data to numpy save and sqlite

    np.savez('test_data.npz', float1=float1, float2=float2, float3=float3,
             num_floats=num_floats, rand_float=rand_floats)

    conn = sqlite3.connect('test_data.sqlite')
    df1 = pd.DataFrame(num_floats)
    df2 = pd.DataFrame(rand_floats)

    df1.to_sql('num_floats', conn)
    df2.to_sql('rand_floats', conn)

if __name__ == "__main__":
    data_generate()