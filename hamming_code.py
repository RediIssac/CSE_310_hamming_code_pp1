# CSE_310_hamming_code_pp1
import numpy as np
def encode(parity_bits, data):
    n = len(data) + parity_bits
    assert 2 ** parity_bits == n + 1

    # copy data to code
    code = np.zeros(n, dtype=int)
    code[np.arange(n) & np.arange(n) + 1 > 0] = data
    print("code", code)
    # parity mask
    mask = np.zeros(n, dtype=int)
    mask[::2] = 1

    # compute parity
    #START YOUR CODE
    i = 0
    while i < n:
        # mask the bits that are needed for calculation
        masked_bit = code[i:]*mask
        num_ones = 0
        
        # add number of ones for the masked bit
        for index in range(len(masked_bit)):
            num_ones += masked_bit[index]
            
        # check if there is odd number of ones
        if (num_ones % 2 == 0):
            # add parity 0 if number of ones is even
            code[i] = 0
            
        else:
            # add parity 1 if number of ones is odd
            code[i] = 1
        i += i+1
        # update the mask for the next parity computation
        mask = np.repeat(mask,2)[:n-i]
    #END OF YOUR CODE    
  
    # result
    return code
    
    
    
def decode(code):
    n = len(code)

    # parity mask
    mask = np.zeros(n, dtype=int)
    mask[::2] = 1

    # compute parity
    # START YOUR CODE
    error = -1
    i = 0
    while i < n:
        # mask the skipped bits and add number of ones
        masked_bit = code[i:]*mask
        num_ones = 0
       
        for index in range(len(masked_bit)):
            num_ones += masked_bit[index]
        # if there is an error num_ones will be odd so anding it with one gives the error bit
        error += (i+1)*(num_ones & 1)
        i += i + 1
        mask = np.repeat(mask,2)[:n-i]
        
    # END OF YOUR CODE
    
    # fix error
    if error >= 0:
        code[error] ^= 1

    # get data from code
    data = code[np.arange(n) & np.arange(n) + 1 > 0]

    # result
    return error, data
    
    
# test code    
parity_bits = 3
data = np.random.randint(0, 2, 4)


# generate code
code = encode(parity_bits, data)
print('hamming code', data, '->', code)

# make error
code[3] ^= 1
print('with error', code)

# reconstruct
error, recon = decode(code)
print('error @', error, '->', recon)



parity_bits = 4
data = np.random.randint(0, 2, 11)

# generate code
code = encode(parity_bits, data)
print('hamming code', data, '->', code)

# make error
code[14] ^= 1
print('with error', code)

# reconstruct
error, recon = decode(code)
print('error @', error, '->', recon)
