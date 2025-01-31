# EXAMPLE 1 print a file with upper case letters (romeo.txt)
# text_file = input("Enter the file name: ")
# try:
#     fh = open(text_file)
# except:
#     print("File does not exists")
#     quit()
# for line in fh:
#     line = line.rstrip()
#     line= line.upper()
#     print(line)


# ////////////////////////////////////////////////////////////////////////////////////////////////////
# EXAMPLE 2 print only the unique words form a FILE and sort them
# fname = input("Enter file name: ")
# try:
#     fh = open(fname)
# except:
#     print("Wrong file name:",fname)
#     quit()
# lst = list()
# for line in fh:
#     line.rstrip()
#     words=line.strip()
#     el=words.split()
#     for item in el:
#         if item not in lst:
#             lst.append(item)
# lst.sort()
# print(lst)
# for ele  in range(len(lst)):
#     print(ele,lst[ele])


# ///////////////////////////////////////////////////////////////////////////////////////////////////////
# EXAMPLE 3 Iterate through a list of e-mail and find the sender with the most emails
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
# sender_dict={}
# sender_list=[]
# fh = open(fname)
# for text in fh:
#   line =  text.rstrip()
#   if "From:" not in line:
#       continue
#   else:
#       new_words = line.split()
#       sender_list.append(new_words[1])
# for sender in sender_list:
#     sender_dict[sender]= sender_dict.get(sender,0)+1
# biggest= 0
# sender=""
# for key, value in sender_dict.items():
#     if value >biggest:
#         biggest=value
#         sender= key
# print(sender,biggest)
# print(sender_dict)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#  EXAMPLE 4 Iterate through a list of e-mails and find the hour with the most emails
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
# hour_dict={}
# hour_list=[]
# fh = open(fname)
# for text in fh:
#   line =  text.rstrip()
#   if "From " not in line:
#       continue
#   else:
#       new_words = line.split()
#       hours= new_words[5][:2]
#       hour_dict[hours]= hour_dict.get(hours,0)+1
# for key,value in hour_dict.items():
#     newtup=(key,value)
#     hour_list.append(newtup)
# srtlst= sorted(hour_list)
# for value, key in srtlst:
#     print(value,key)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# EXAMPLE 5 Iterate through a file and get the values  for a specific attribute and calculate the average
# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# total =0
# counter=0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     line = line.rstrip()
#     values = line.split(":")
#     total=total+float(values[1])
#     counter= counter+1
# average= total/counter
# print("Average spam confidence: ",average)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# EXAMPLE 6 Import "re" package which helps for a very specific search
# import re
# number_sum=0
# try:
#     fh = open("all_numbers.txt")
# except:
#     print("File doesn't exist")
#     quit()
#
#
# for line in fh:
#     line= line.rstrip()
#     number=re.findall("[0-9]+",line)
#     # If on the current line we don't have any number, we will receive an empty list and the IF will be executed
#     if len(number)<1:
#         continue
#     else:
#         for element in number:
#             number_sum = number_sum+int(element)
# print(number_sum)
# # http://data.pr4e.org/intro-short.txt