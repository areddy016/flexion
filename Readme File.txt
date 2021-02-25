# React Unit Converter

## Problem

> Our users are science teachers who are comfortable
> using a browser. In their "Unit Conversion" science unit,
> they want to assign students unit-conversion problems on paper
> worksheets. After students turn in their completed worksheet, 
> the teachers want to be able to enter the questions and student 
> responses into a computer to be graded. Students will convert: 
> temperatures between Kelvin, Celsius, Fahrenheit, and Rakine.
> 

#### Technology Used

## Home Screen

> React Unit Converter welcomes you with a home screen where 
> teaches can choose what type of unit to convert.
> ![React Unit Converter Landing Screen](public/react-unit-converter-home.png "React Unit Converter Home screenshot")

## Coversion Screen

> Teachers are provided with a clean and simple page to convert units. 
> Teachers are given feedback if students are right or wrong.
> Teachers are provided with the correct answer.
> ![React Unit Converter Coversion Screen](public/react-unit-converter-convertsion-screen.png "React Unit Converter Coversion screenshot")


## CalculatorLibrary/
|
├── .git
├── .gitignore
├── README.md
├── calculator.py
├── requirements.txt
└── test_calculator.py


# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32 

## Define the main function to loop statement for given input value

def main():                                                # function definition
    print("This program illustrates a chaotic funciton.")  # output statement
    x = eval(input("Enter a number between 0 and 1: "))    # assignment statement wrapped around input statement
    for i in range(10):                                    # loop statement

##Creating Docker image file to make understand for other programs:

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
        x = 3.9 * x * (1 - x)                              # expression
        print(x)                                           # output statement

