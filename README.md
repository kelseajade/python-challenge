# python-challenge
I created at folder for pybank and pypoll. 

For Pybank, I used the csv budget_data. 
My variables were defined as the total months, total profit loss, previous profit, changes in profit, and the dates. 
To count the months I started to count rows after the header in row 0. This counted 86 months of data based on number of rows. 
I changed the profits to take the previous months profit from the current profits to get the change in profit. 
The average change was calculated by the sum  of changes in profit divided by the number of months. This was Total Months: 86
Total: $22564198 which came to -8311.11. To find the increase and decrease I used the max and min functions from a python functions sheet. I printed the values and then used 'write' to put them in a text file called analysis. I tried to print as a list but I kept getting an error saying I forgot a comma and Stack Overflow showed two ways as individual codes or commas so I printed individually. 

For Pypoll, I used the csv election_data.
My variables were total votes, candidates, and candidate votes. I skipped the header again and counted votes. There were 369711 votes. I created a dictionary to apend vote counts. I used the percentage code from class for percentage of total votes. The max function was from the python functions. I then chose to print the results as individual lines again because it worked when I did Pybank. 
