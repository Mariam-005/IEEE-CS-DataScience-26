### =>Building a Decision Tree
#### =>Steps
-> How to choose which feature to split on at each node?
    Choose the feature that maximizes purity

-> When to stop splitting?
 if:
- The node is 100% one class
- Splitting would make the tree exceed the Maximum Depth (number of hops from the root)
- The improvement in purity is below a threshold.
- The number of training examples in the node is below a threshold

### =>Measuring Purity

#### Entropy
Let:
- p1 = fraction of positive examples.
      `p0 = 1 - p1`

**binary entropy function** 
 ` H(p₁) = -p₁ log₂(p₁) - p₀ log₂(p₀) `

> **Note**
> If `p0 = 0` or `p1 = 0`, then `0 × log(0)` is defined as **0** (even though `log(0)` is actually `-∞`)

Looks very similar to the Logistic Loss formula


 Entropy
  = 0 -> the node is completely pure (all examples belong to one class)
  = 1 -> maximum uncertainty (50%-50% split).
 Lower entropy = better


### Choosing a Split

#### Information Gain
 => Reduction in Entropy

Formula:
  `= H(p_root) - (w_left H(p_left) + w_right H(p_right))
where
-> w_left = number of examples in the left node / number of examples in the parent node
-> w_right = number of examples in the right node / number of examples in the parent node


so with higher Information Gain
-> Better split
-> More reduction in uncertainty
#### Steps
1. Start with all training examples
2. Calculate the information gain for every possible feature
3. Pick the feature with the highest Information Gain
4. Split the dataset into left and right branches
5. Repeat recursively until one of the stopping conditions is met:
   - Node becomes 100% one class
   - Maximum Depth is reached
   - Information Gain is below a threshold
   - Number of examples is below a threshold

#### Recursive Splitting:
The way we build a decision tree is by creating smaller decision trees in the left and right branches.

### Maximum Depth

The larger the maximum depth:
   ->The bigger the tree becomes.
   ->The more complex the model becomes.
   ->Higher chance of overfitting

Small Maximum Depth
-> Simpler tree
-> May cause underfitting

----
### Decision Trees with Continuous Features
decision trees also work with continuous features.
Instead of splitting on categories => we split using a threshold.

Example:
Age:
   20  , 25  , 30,   35
->Possible thresholds
   22.5 ,  27.5 ,  32.5
   
For every threshold:
- Calculate the Information Gain
- Choose the threshold with the **highest Information Gain**

---
### Regression with Decision Trees

Regression Tree
- Predicts continuous values
- Tries to reduce the **Variance**
`Variance Reduction = Var(root) - (w_left·Var(left) + w_right·Var(right))`

---
### Tree Ensembles
A single decision tree is highly sensitive to small changes in the training data
To make it more "robust" -> we use multiple decision trees 
(Tree Ensembles)

Examples:
- Random Forest
- XGBoost

but how can we build multiple different trees from the same dataset without them all turning out identical?
#### ->Sampling with Replacement
- Randomly sample the training examples with replacement
- This creates a new training set that is similar to, but not exactly the same as, the original dataset

as sampling is done with replacement
- The same training example may appear multiple times.
- Some examples may not appear at all

as a result:
each decision tree is trained on a slightly different dataset making the overall model more robust