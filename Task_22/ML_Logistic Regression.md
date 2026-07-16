
# => Supervised Learning
Logistic Regression belongs to Supervised Learning

| Hours Studied | Passed |
|---------------|--------|
| 2 | No |
| 4 | No |
| 6 | Yes |
| 8 | Yes |

The model learns the relationship between the input and the output, then predicts the class for new data.

## ->Classification
Classification predicts categories (classes)
Ex:
- Spam / Not Spam
- Pass / Fail

### Why don't we use Linear Regression?
if we have a binary classification problem
0 = Fail
1 = Pass

Linear Regression predicts using

```
y = wx + b
```

The problem is that this equation can produce any value ->these values don't represent probabilities

As a probability must always satisfy

```
0 ≤ Prob ≤ 1
```

So Linear Regression is not suitable for classification.


#### the main idea:

Instead of predicting the class directly ->
Logistic Regression predicts the probability that an observation belongs to a class.

### =>Step 1: Build a Linear Equation
starts with the same linear equation used in Linear Regression.

```
z = wx + b
```

For multiple features,

```
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

//The value of **z** can be anything
->so we still have the same problem :
need to convert this value into a probability.


### =>Step 2: Apply the Sigmoid Function
Sigmoid Function solves the problem.
It converts any real number into a value between 0 and 1

```
σ(z) = 1/(1+e^(-z))
```

so every prediction can be interpreted as a probability.

# Properties of the Sigmoid Function

-> Output is always between 0 and 1
-> Very large positive values become close to 1
-> Very large negative values become close to 0

ex:
z = -10  -> ≈ 0.000045
almost impossible to belong to Class 1.
 
---

# Decision Boundary

After calculating the probability ->need to convert it into a class
This is done using a "threshold".

Usually,

```
Threshold = 0.5
```

Rule:
if probability ≥ 0.5
predict Class 1
else
predict Class 0


Can the Threshold Change?
->Yes

Choosing the threshold affects
- Precision
- Recall
- False Positives
- False Negatives

---

How does it know whether its prediction is good or bad?
We compare the predicted probability with the actual answer using a Cost Function

The goal is simple: small cost = good model
   the model updates its weights until the cost becomes as small as possible.

---
Why doesn't MSE work well?
After the Sigmoid Function the prediction is no longer linear

When MSE is combined with the Sigmoid function
    Cost Function becomes "non-convex"

so it may contain several local minima
->Gradient Descent may get stuck before reaching the best solution

so =>Logistic Regression uses "Log Loss"
``` Cost = -[y log(p) + (1-y) log(1-p)] ```
keeping the Cost Function convex this allows Gradient Descent to reach the global minimum more efficiently
____
##### => When to use Logistic Regression?
- when the relationship between the features and the target is approximately linear
- when you want a strong baseline model before trying more complex algorithms.