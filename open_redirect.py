print("*****" * 15)
print("-----" * 15)
print("\tBy Boaz Kodjo BoazAK, aka KodjoDoDjango, aka InfoSecKodjo")
print("\t\t\thttps://twitter.com/BoazakK")
print("-----" * 15)
print("*****" * 15)

# Take the input from user
site = input("\n\nExample :\ngoogle.com\nor\n*.google.com\n\nEnter website:")
# Show the input in terminal
print("The website you're looking fo is: " + site + "\n\n")

# Read the file containing the Google Dorks keywords
file1 = open('dork.txt', 'r')
Lines = file1.readlines()

# Strips the newline character
for line in Lines:
    print("site:{}: {}".format(site, line.strip()))


    # Search with Google