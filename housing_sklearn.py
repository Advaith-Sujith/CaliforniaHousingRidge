from sklearn.linear_model import Ridge
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True)

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()

xtrain = scaler.fit_transform(xtrain)
xtest = scaler.transform(xtest)

lr = Ridge(alpha=0.00000001)

lr.fit(xtrain, ytrain)
ypred = lr.predict(xtest)

r2 = r2_score(y_pred=ypred, y_true=ytest)
mse = mean_squared_error(ytest, ypred)

print(r2) #0.5757877066731295
print(mse) #0.5558915978556932