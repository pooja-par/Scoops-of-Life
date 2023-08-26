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
-


## Bugs

- Surplus data calculation may not be accurate in certain scenarios.

## Remaining Bugs

No bugs remaining

- 
## Validator Testing





## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

 Steps for deployment:
 Fork or clone this repository
 Create a new heroku app
 Set the buildbacks to Python and NodeJs in that order
 link heroku app to the repository
 Click on Deploy

 ## Credits
  Code Institute for the deployment terminal
  

