import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True)

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

ytrain = ytrain.reshape(-1, 1)
ytest = ytest.reshape(-1, 1)

xmin = np.min(xtrain, axis=0)
xmax = np.max(xtrain, axis=0)
xtrain = ( xtrain - xmin ) / ( xmax - xmin )
xtest = ( xtest - xmin ) / ( xmax - xmin )


W = np.random.rand(8, 1)
B = np.zeros((1,1))

def h(x):
    return np.dot(x, W) + B

def cost(H, Y, l):
    m = H.shape[0]
    mse = (1/m) * np.sum((H-Y)**2)
    l1 = l*np.sum(W**2)
    return mse+l1

print((h(xtrain)-ytrain).shape)

def w_grad(X, H, Y, l):
    m = X.shape[0]
    g = (2/m)*np.dot(X.T, (H-Y)) + l*2*W
    return g

def b_grad(H, Y):
    m = H.shape[0]
    g = (2/m) * np.sum(H-Y)
    return g


lr = 0.01
l = 0.00000001

for epoch in range(100000):
    H = h(xtrain)

    dW = w_grad(xtrain, H, ytrain, l)
    dB = b_grad(H, ytrain)

    W[:] = W - lr * dW
    B[:] = B - lr * dB

    if epoch % 100 == 0:
        print(cost(H, ytrain, l))


H = h(xtest)
ssres = np.sum((ytest-H)**2)
sstot = np.sum((ytest-np.mean(ytest))**2)

r2_score = 1-(ssres/sstot)

mse = (1/H.shape[0]) * np.sum((H-ytest)**2)

print("r2: ",r2_score) #0.5830657705545322
print("mse: ", mse) #0.5463543576012923