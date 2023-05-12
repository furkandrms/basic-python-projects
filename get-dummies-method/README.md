# Question:

Given a dataset containing a categorical variable, write a function that converts this categorical variable into binary (dummy) variables by creating a separate column for each category.


# Input:
The first line contains two integers, n representing the number of observations in the dataset, and variable representing the name of the categorical variable. The next n lines contain the categorical variable value for each observation in the dataset.

# Output:
For each observation in the dataset, print the transformed dataset by creating a separate column for each category. The columns take the values of 0 or 1, where 1 indicates membership in the corresponding category, and 0 indicates non-membership.



**Input:**

| Input                    | Description                                 |
|--------------------------|---------------------------------------------|
| 5                        | Number of observations                       |
| color                    | Categorical variable name                    |
| red                      | Value of 1st observation                     |
| blue                     | Value of 2nd observation                     |
| green                    | Value of 3rd observation                     |
| red                      | Value of 4th observation                     |
| yellow                   | Value of 5th observation                     |

**Output:**

| Output       |  red   | blue  | green | yellow |
|--------------|--------|-------|-------|--------|
| 1st observation   |   1    |   0   |   0   |   0    |
| 2nd observation   |   0    |   1   |   0   |   0    |
| 3rd observation   |   0    |   0   |   1   |   0    |
| 4th observation   |   1    |   0   |   0   |   0    |
| 5th observation   |   0    |   0   |   0   |   1    |

