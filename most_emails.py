#9.4 Write a program to read through the mbox-short.txt and figure out who
#has sent the greatest number of mail messages. The program looks for 'From '
#lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to
#a count of the number of times they appear in the file. After the dictionary
#is produced, the program reads through the dictionary using a maximum loop to
#find the most prolific committer.

#fname = input("Enter file name:")
fh = open("mbox-short.txt")

lst = list()
counts = dict()

for line in fh:
    if line.startswith("From "):
        split_line = line.split()
        emails = split_line[1]
        lst.append(emails)

for email in lst:
    counts[email] = counts.get(email, 0) + 1

big_email = None
big_count = None

#items = counts.items()
#print(items)

for email, count, in counts.items(): 
    if big_count is None or count > big_count:
        big_count = count
        big_email = email
    else:
        continue

print(big_email, big_count)

#Desired Output
#cwen@iupui.edu 5
