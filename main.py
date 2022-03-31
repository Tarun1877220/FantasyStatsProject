import csv

# Databse from Pro Football Reference
with open('All_years.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # The randomly selected years
    years = ["1993", "2000", "2011"]
  
    # The teams that made the playoffs
    teams = ["BUF", "HOU", "KAN", "RAI", "DEN", "PIT", "DAL", "SFO", "DET", "NYG", "MIN", "GNB", "TEN", "OAK", "MIA", "BAL","DEN","IND", "NYG", "MIN", "NOR", "PHI", "TAM", "STL", "NWE", "BAL", "HOU", "DEN", "PIT", "CIN", "GNB", "SFO", "NOR", "NYG", "ATL", "DET"]

    # The factors (nothing in quotes = whole team)
    positions = ["QB", "RB", "WR", "TE", ""]

    # Loops through the teams and the database
    k = 0
    for i in range(len(teams)):
      
      # Variables for averages
      div = 0
      total = 0
      line_count = 0

      # Resets the file position after each loop
      csv_file.seek(0)

      # Progresses through each set of 12 teams per each year
      if(i+1 == 13 or i+1 == 25):
        k += 1

      # Iterates over CSV
      for row in csv_reader:

        # If a team from a desired year at the desired position is found, add it to the average
        if line_count != 0:
          if(int(row[0]) == int(years[k]) and str(row[2]) == teams[i] and str(row[3]) == "enter position"):
            div += 1
            total += float(row[15])

        # Tracking where we are in the CSV
        line_count += 1

        # Taking the average
        format_float = "{:.2f}".format(total/div)

      # Printing out the result
      print(format_float)