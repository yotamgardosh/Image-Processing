import numpy as np

def batch_1():

    # 1. Create a numpy array of shape [9, 1] and fill it with random values.
    # 2. Turn it into a 3 × 3 matrix.
    # 3. Print the shape and type of the matrix.
    # 4. Get the first column of the matrix and multiply it by the third column of the matrix.
    # 5. Create a new matrix of size [9, 9] and fill it with the value from the previous section.
    # 6. Create a new matrix of size [9, 9] and fill it with random values.
    # 7. Stack the two matrices along a new dimension to form a tensor of shape [9, 9, 2].
    # 8. Get the mean, sum, and standard deviation of the new matrices along the third dimension.
    # 9. Get all the indices of the array for which the value is greater than the mean.
    # 10. Replaces the values of items in these indices by 0.

    #1
    print("Q1")
    a = np.random.rand(9, 1)
    print(a.shape)
    print(a)

    #2
    print("Q2")
    b = a.reshape(3,3)
    print(b.shape)
    print(b)

    #3
    print("Q3")
    print(b.dtype)

    #4
    print("Q4")
    col_1 = b[:,0]
    col_2 = b[:,2]
    mul = np.multiply(col_1,col_2)
    print(mul)

    #5
    print("Q5")
    # np.tile is a NumPy function that allows you to construct a new array
    # by repeating an existing array along specified dimensions.
    # It takes the array you want to repeat and a tuple specifying the
    # number of times to repeat the array in each dimension.
    c = np.tile(mul,(9,3))
    print(c.shape)

    #6
    print("Q6")
    d = np.random.rand(9,9)

    #7
    print("Q7")
    e = np.stack((c,d),axis=2)
    print(e.shape)
    print(e)

    #8
    print("Q8")
    mean = np.mean(e,axis=2)
    sum = np.sum(e,axis=2)
    std = np.std(e,axis=2)
    print("mean: ", mean)
    print("mean: ", sum)
    print("mean: ", std)

    #9
    print("Q9")
    greater_then_mean = np.where(e > mean[:,:,np.newaxis])
    print(greater_then_mean)

    #10
    print("Q10")
    e[greater_then_mean] = 0
    print(e)




def benchmark():
    import time
    a = np.random.rand(512,512,3)
    b = np.random.rand(512, 512, 3)

    start = time.time()
    for _ in range(1000):
        c = np.multiply(a,b)

    end = time.time()
    print("total time np function: ", end-start)

    start = time.time()
    for _ in range(1000):
        for i in range(512):
            for j in range(512):
                for k in range(3):
                    c = a[i, j, k] * b[i, j, k]

    end = time.time()
    print("total time 3 loops: ", end-start)










def main():
    # batch_1()
    benchmark()

if __name__ == "__main__":
    main()
