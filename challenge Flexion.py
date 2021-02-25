#!/usr/bin/env python
# coding: utf-8

# In[1]:


temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")


# In[ ]:


pip install -r requirements.txt
pip install codecov
pip install pytest-cov
pip install .


# ### language: python
# python:
#   - "3.6"
#   - "3.7"
# install:
#   - pip install -r requirements.txt
#   - pip install codecov
#   - pip install pytest-cov
#   - pip install .
# script:
#   - pytest --cov-report=xml --cov=deeptabular tests/
# 
# after_success:
#   - codecov
# 
# deploy:
#   provider: pypi
#   user: __token__
#   password: $TEST_PYPI_TOKEN
#   distributions: "sdist bdist_wheel"
#   skip_existing: true
#   on:
#     branch: staging

# In[2]:


pip install tensorflow


# In[3]:


import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import accuracy_score


def test_build_classifier():
    classifier = DeepTabularClassifier(
        cat_cols=["C1", "C2"], num_cols=["N1", "N2"], n_targets=1, num_layers=1
    )
    df = pd.DataFrame(
        {
            "C1": np.random.randint(0, 10, size=5000),
            "C2": np.random.randint(0, 10, size=5000),
            "N1": np.random.uniform(-1, 1, size=5000),
            "N2": np.random.uniform(-1, 1, size=5000),
            "target": np.random.uniform(-1, 1, size=5000),
        }
    )
    df["target"] = df.apply(
        lambda x: 1 if (x["C1"] == 4 and x["N1"] < 0.5) else 0, axis=1
    )

    test = pd.DataFrame(
        {
            "C1": np.random.randint(0, 10, size=5000),
            "C2": np.random.randint(0, 10, size=5000),
            "N1": np.random.uniform(-1, 1, size=5000),
            "N2": np.random.uniform(-1, 1, size=5000),
            "target": np.random.uniform(-1, 1, size=5000),
        }
    )
    test["target"] = test.apply(
        lambda x: 1 if (x["C1"] == 4 and x["N1"] < 0.5) else 0, axis=1
    )

    classifier.fit(df, target_col="target", epochs=100, save_path=None)

    pred = classifier.predict(test)

    acc = accuracy_score(test["target"], pred)

    assert isinstance(classifier.model, tf.keras.models.Model)
    assert acc > 0.9


# In[ ]:


## CalculatorLibrary/
|
├── .git
├── .gitignore
├── README.md
├── calculator.py
├── requirements.txt
└── test_calculator.py


# In[4]:



# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32 


# In[5]:


def main():                                                # function definition
    print("This program illustrates a chaotic funciton.")  # output statement
    x = eval(input("Enter a number between 0 and 1: "))    # assignment statement wrapped around input statement
    for i in range(10):                                    # loop statement
        x = 3.9 * x * (1 - x)                              # expression
        print(x)                                           # output statement


# In[7]:



def main():
    print("This program coverts a temperature in Celsius to a temperature in Fahrenheit.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()


# In[ ]:


$ pip freeze > requirements.txt


# In[ ]:


flake8 --statistics
./calculator.py:3:1: E302 expected 2 blank lines, found 1
./calculator.py:6:1: E302 expected 2 blank lines, found 1
2     E302 expected 2 blank lines, found 1


# In[ ]:


## Unit tests for the calculator library


import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)


# In[ ]:


collected 2 items

test_calculator.py::TestCalculator::test_addition PASSED [50%]

test_calculator.py::TestCalculator::test_subtraction PASSED [100%]


# In[ ]:


# Python CircleCI 2.0 configuration file
version: 2
jobs:
  build:
    docker:
      - image: circleci/python:3.7

    working_directory: ~/repo

    steps:
      # Step 1: obtain repo from GitHub
      - checkout
      # Step 2: create virtual env and install dependencies
      - run:
          name: install dependencies
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
      # Step 3: run linter and tests
      - run:
          name: run tests
          command: |
            . venv/bin/activate
            flake8 --exclude=venv* --statistics
            pytest -v --cov=calculator


# In[ ]:


deploy:
  provider: pypi
  user: __token__
  password: $TEST_PYPI_TOKEN
  distributions: "sdist bdist_wheel"
  skip_existing: true
  on:
    branch: staging


# In[ ]:


def test_multiplication(self):
    assert 100 == calculator.multiply(10, 10)


# In[ ]:


def multiply(first_term, second_term):
    return first_term * second_term


# In[ ]:





# In[ ]:




