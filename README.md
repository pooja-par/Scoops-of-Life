Scoops of Life Ice Cream Sales Optimization

## Description
The Scoops of Life Ice Cream Sales Optimization script is designed to help ice cream sellers optimize their sales and manage stock based on past order data. It leverages the Google Sheets API for data storage and analysis.

## Features

- Collects order data from the user.
- Identifies the most popular ice cream flavor of the day.
- Calculates surplus data by comparing orders with stock.
- Calculates stock data based on the average of the last 5 days entries.

## Future Features

- Temperature dependent icecream order to forecast future orders. 
- Optimize the staff allocation.



## Data Model

- 'order': Records daily ice cream orders for different flavors.
- 'favorit_flavor': Stores the most popular ice cream flavor and its contribution percentage.
- 'icecream_surplus': Tracks the surplus or unfulfilled orders for each flavor.
- 'stock': Maintains the stock levels for various ice cream flavors.

## Testing
I have manually tested  this project by doing the following:
-passed code through a PEP8 linter and confirmed there are no problems
-Tested in my local terminal and Code Instite Heroku terminal
-Check has been made by giving different numbers and also with empty field and random characters. With empty space and random characters, code return error and ask user to reenter the count again. 
-Where necessary, by print values are checked in terminal. 


## Bugs

- NO known bugs

## Remaining Bugs

No bugs remaining


## Validator Testing
Code has been checked in "https://pep8ci.herokuapp.com/". No errors identified. 
![Validator Check](https://github.com/pooja-par/Scoops-of-Life/blob/main/images/code_validate.png)




## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

 Steps for deployment:
 -Login to heroku and enter your detail
 -Fork or clone this repository 
 -Create a new heroku app
 -Create config-var : var-CREDS and var-PORT
 -Set the buildbacks to Python and NodeJs in that order
 -Select github for the deployment within deployment tab
 -Select manual deploy option
 -link heroku app to the repository
 -Click on Deploy

 ## Credits
  Code Institute for the deployment terminal
  

