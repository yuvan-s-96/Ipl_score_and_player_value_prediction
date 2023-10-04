# IPL Score Prediction

This project aims to predict the final score of an Indian Premier League (IPL) cricket match based on various input parameters such as venue, batting team, bowling team, overs, runs, wickets, runs in the previous 5 overs, and wickets in the previous 5 overs.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)


## Project Overview

The IPL Score Prediction project uses a Ridge Regression model to predict the final score of an IPL cricket match. It takes into account both categorical and numerical features to make predictions.

- Categorical Features: Venue, Batting Team, Bowling Team
- Numerical Features: Overs, Runs, Wickets, Runs in the Previous 5 Overs, Wickets in the Previous 5 Overs

The project is built using Flask, a micro web framework, to create a web interface for users to input match details and receive score predictions.

## Getting Started

To get started with this project, follow these steps:
- Clone the repository to your local machine:
`https://github.com/yuvan-s-96/Ipl_score_and_player_value_prediction.git  `
- Install the required libraries:
`pip install flask joblib numpy`
- Run the Flask app:
`python app.py`
- Open a web browser and go to http://localhost:5000 to use the IPL Score Prediction interface.

## Usage
- Enter the match details: Venue, Batting Team, Bowling Team, Overs, Runs, Wickets, Runs in the Previous 5 Overs, Wickets in the Previous 5 Overs.
- Click the "Predict" button.
- The predicted final score will be displayed on the webpage.

## Dependencies
- Flask
- Joblib
- Numpy
- License


