x=[1,2,3,4,5]
y=[2,4,5,4,5]
n=len(x)
sum_x=sum(x)
sum_y=sum(y)
sum_xy=sum([x[i]*y[i] for i in range(n)])
sum_x2=sum([x[i]**2 for i in range(n)])
m=(n*sum_xy-sum_x*sum_y)/(n*sum_x2-sum_x**2)
b=(sum_y-m*sum_x)/n
print(f"Linear Regression Model: y = {m:.2f} * x + {b:.2f}")
x_new=6
y_pred=m*x_new+b
print(f"Predicted y for x={x_new}: {y_pred:.2f}")

