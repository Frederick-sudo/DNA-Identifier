DNA Identification Project

Project Description:

A program that identifies a person based from their DNA sequence by, utilizing python logic and analyzing their DNA's Short Tandem Repeats (STRs). The program takes two inputs which are the csv file that contains the database of multiple individuals alongside their STR counts, and a text file that contains a specific DNA sequence.

Features:

The program finds the longest consecutive repeats of specific STRs in the DNA sequence and matches them against the database to identify the person. If no match is found, it outputs "No match." 

Reads a CSV file with names and STR counts (e.g., AGATC, AATG, TATC).

Processes a DNA sequence from a text file to count the longest consecutive STR repeats.

Compares STR counts with the database to find a match.

Outputs the name of the matching person or "No match" if no match is found.

Files Included:

dna.py: The main Python script that performs the DNA identification.

databases/: A folder containing CSV files with STR data for individuals (e.g., small.csv, large.csv).

sequences/: A folder containing text files with DNA sequences (e.g., 1.txt, 2.txt, etc.).

README.md: This file, explaining the project and how to run it.

