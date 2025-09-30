
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# CRISP-DM: Business Understanding
st.header("Business Understanding")
st.write("The goal of this web application is to provide a visual and interactive tool for understanding simple linear regression. Users can adjust parameters to see how they affect the data and the resulting regression model. This helps in grasping the fundamental concepts of linear relationships and the impact of noise.")

# CRISP-DM: Data Understanding
st.header("Data Understanding")
st.write("The data is synthetically generated based on user-defined parameters. This allows for a controlled environment to study the behavior of linear regression models.")

# User Inputs
st.sidebar.header("Model Parameters")
a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.5, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 10.0, 2.0, 0.1)
num_points = st.sidebar.slider("Number of Points", 50, 500, 100, 10)

# CRISP-DM: Data Preparation
st.header("Data Preparation")
st.write("Based on the selected parameters, a dataset is generated. The data consists of a single independent variable (X) and a dependent variable (y), with a linear relationship defined by y = aX + b, where b is fixed at 10 for this example. Random noise is added to the 'y' values to simulate real-world data.")

# Generate Data
np.random.seed(42)
X = np.random.rand(num_points, 1) * 10
b = 10
y = a * X + b + np.random.randn(num_points, 1) * noise
df = pd.DataFrame(data=np.hstack([X, y]), columns=['X', 'y'])

st.subheader("Generated Data Sample")
st.write(df.head())

# CRISP-DM: Modeling
st.header("Modeling")
st.write("A simple linear regression model is trained on the generated data. The model learns the relationship between X and y to predict y from X.")

# Train the model
model = LinearRegression()
model.fit(X, y)

# Get model predictions
y_pred = model.predict(X)

# CRISP-DM: Evaluation
st.header("Evaluation")
st.write("The model's performance is evaluated by visualizing the regression line against the original data points. The learned model parameters (slope and intercept) are also displayed and compared to the true parameters used for data generation.")

# Display model parameters
st.subheader("Model Parameters")
st.write(f"Learned Slope (a): {model.coef_[0][0]:.2f}")
st.write(f"Learned Intercept (b): {model.intercept_[0]:.2f}")

# Plot the results
fig, ax = plt.subplots()
ax.scatter(X, y, label="Original Data")
ax.plot(X, y_pred, color='red', linewidth=2, label="Regression Line")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.set_title("Simple Linear Regression")
ax.legend()
st.pyplot(fig)

# CRISP-DM: Deployment
st.header("Deployment")
st.write("The application is deployed as a web service using Streamlit. This allows users to interact with the model through a web browser without needing to run the code locally. To deploy this application, you would typically use a service like Streamlit Cloud, Heroku, or AWS.")
st.code('''
# To run this app locally:
# 1. Make sure you have Python and pip installed.
# 2. Install the required libraries: pip install -r requirements.txt
# 3. Run the app: streamlit run app.py
''', language='bash')
