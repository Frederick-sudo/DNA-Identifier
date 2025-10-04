import csv
import sys


def main():
    if len(sys.argv) != 3: #Checks for proper command-line usage
        print("Error: Incorrect usage")
        exit(1)

    with open(sys.argv[1],"r") as csv_database: #Opens the database (.csv) file into a variable
        with open(sys.argv[2],"r") as txt_sequence: #Opens the DNA sequence (.txt) file into a variable

            csv_dictionary = csv.DictReader(csv_database) #Reads the CSV file and converts each row into a dictionary
                                                          #(where the keys are the column headers and the values are the row data)

            txt_string = txt_sequence.read() #Reads the database (.txt) file into a variable
                                             #Convers the (.txt) file into a SINGLE LINE OF STRING

            seq = len(txt_string)  #Get the length of the string

            str_list = csv_dictionary.fieldnames[1:] #Create a list that contains all the column headers from the CSV file then stores it in the variable "str_list"
                                                     #.fieldnames is the key that lets you access all the column headers from a CSV file when using csv.DictReader
                                                     #Uses LIST SLICING ([1:]) to start from the 1ST INDEX skipping the 0TH INDEX

            STR_dict = {} #Create an empty dictionary called "STR_dict"

            for str_seq in str_list: #For each STR in the list, compute the longest run in the DNA string
                STR_dict[str_seq] = longest_match(txt_string, str_seq)  #Stores the result in the STR_dict with STR name as the key and its count as the value


            for row in csv_dictionary: #Loop through each person (row) in the CSV database
                match = True  # Assume it's a match unless proven wrong


                for str_seq in str_list:  #For each STR, check if the count in the DNA sequence matches the count in the current row
                    if STR_dict[str_seq] != int(row[str_seq]):
                        match = False  #If any STR doesn't match, it's not a match
                        break  #No need to check further

                if match: #If all STR counts matched (match is still True), then this is the person we're looking for
                    print(row["name"]) #Print the name of the matching person
                    break
            else:
                print("No match")  # This runs if no break happened (no matches found)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
