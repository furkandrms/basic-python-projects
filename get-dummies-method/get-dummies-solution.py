# Function to convert categorical variable to binary (dummy) variables
def convert_to_dummy_variable(n, variable, observations):
    # Perform the transformation using the get_dummies() function
    dummies = pd.get_dummies(observations[variable])
    
    # Print the result of the transformation
    print(dummies)

# Get input data
n = int(input("Enter the number of observations: "))
variable = input("Enter the name of the categorical variable: ")
observations = []
for i in range(n):
    obs = input(f"Enter the value of observation {i+1}: ")
    observations.append(obs)

# Call the function
convert_to_dummy_variable(n, variable, observations)
