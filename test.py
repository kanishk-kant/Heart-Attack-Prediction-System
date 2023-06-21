# data type
# 1 int
#   float
# 2 bool
# 3 str
# 4 list
# 5 tuple
# 6 dict

"""
OPERATORS
addition                      +
subtraction                   -
multiplication                *
division                      /
exponential (to the power)    **
modulus (remainder)           %
floor division                //
"""

# nm = 'Harry'
# print(nm[-4:-2])
#
# list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# print(list1)
#
# tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# print(tuple1)
#
#
# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("ishh"))
# print(str1.index("is"))



n="NaNdInI"

# upper()
# print(n.upper())
# u = n.upper()
# print(u)

# lower()
# print(n.lower())
#
# n = " nandini is a girl "
# print(n.strip())
#
# n = "nandini is a girlllllllll"
# print(n.rstrip("l"))
#
# str3 = "Hello !!!"
# print(str3.rstrip("!"))
#
# n = "nandini is bad a girl"
# print(n.replace('bad','good'))
#
# n = "nandini is a girl"
# print(n.split(" "))
#
# n = "nandinI iS a Girl"
# print(n.capitalize())
# c = n.capitalize()
# print(c)
#
# n = "nandinI iS a Girl"
# print(n.center(100))
# print(n.center(100, "~"))

# n = "nandini is a good girl"
# print(n.count("i"))
# c = n.count("i")
# print(c)

# n = "nandini is a girl"
# print(n.endswith("a girl"))

# n = "nandini is a girl"
# print(n.find("is"))
# print(n.find("k"))
# print(n.index("is"))
# print(n.index("k"))

# n = "NandiniIsaGirl00000"
# print(n.isalnum()) #A-Z,a-z,0-9
# print(n.isalpha()) #a-z,A-Z

# n = "Nandini"
# print(n.islower())
# print(n.isupper())

# n = "Nandini"
# print(n.isprintable())
# print(n.isspace())

# n = "Nandini Is A Good Girl"
# print(n.title())
# print(n.istitle())

# n = "nandini is a girl"
# print(n.startswith("nan"))

# n = "Nandini Is A Good Girl"
# print(n.swapcase())


##############if-else###############

# a = int(input("Enter your age: "))
# print("Your age is:", a)
#
# if(a==18):
#   print("APPLY FRESH DL")
# elif(28>a>18):
#     print("apply DL")
# elif(a>28):
#     print("renew dl")
# else:
#   print("You cannot APPLY DL")
#
# print("done")


# n = 18
# if (n < 0):
#     print("Number is negative.")
# elif (n > 0):
#     if (n <= 10):
#         print("Number is between 1-10")
#     elif (n>10 and n<=20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")


# string_a = "fcfl2n0k7pax"
# string_b = "wrf8mqanxs6g"
#
# def calculate_levenshtein_distance(string_a, string_b):
#
#     matrix = [[0] * (len(string_b) + 1) for _ in range(len(string_a) + 1)]
#
#
#     for i in range(len(string_a) + 1):
#         matrix[i][0] = i
#     for j in range(len(string_b) + 1):
#         matrix[0][j] = j
#
#
#     for i in range(1, len(string_a) + 1):
#         for j in range(1, len(string_b) + 1):
#             if string_a[i - 1] == string_b[j - 1]:
#                 cost = 0
#             else:
#                 cost = 1
#             matrix[i][j] = min(
#                 matrix[i - 1][j] + 1,  # deletion
#                 matrix[i][j - 1] + 1,  # insertion
#                 matrix[i - 1][j - 1] + cost  # substitution
#             )
#
#     return matrix[-1][-1]
#
# distance = calculate_levenshtein_distance(string_a, string_b)
# print("Levenshtein distance:", distance)

#
# import re
#
# txt_record = "v=spf1 ip4:40.113.200.201 ip6:2001:db8:85a3:8d3:1319:8a2e:370:7348 include:thirdpartydomain.com ~all"
#
# ipv4_pattern = r"\bip4:([0-9]{1,3}(?:\.[0-9]{1,3}){3})\b"
# ipv4_match = re.search(ipv4_pattern, txt_record)
#
# if ipv4_match:
#     ipv4_address = ipv4_match.group(1)
#     print("Extracted IPv4 address:", ipv4_address)
# else:
#     print("No IPv4 address found in the TXT record.")

#
# import requests
# from bs4 import BeautifulSoup
#
#
# def find_string_in_webpage(url, item_index):
#     # Send a GET request to the webpage
#     response = requests.get(url)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Create a BeautifulSoup object to parse the HTML content
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         # Find all the items on the webpage
#         items = soup.find_all('item')
#
#         # Check if the requested index is within the range of the available items
#         if 0 <= item_index < len(items):
#             # Get the string value of the specified item
#             target_item = items[item_index].get_text()
#
#             return target_item
#         else:
#             return "Invalid item index."
#     else:
#         return "Failed to retrieve webpage content."
#
#
# # Provide the URL of the webpage and the index of the item you want to retrieve
# webpage_url = 'https://www.example.com'  # Replace with your webpage link
# target_index = 2663  # Replace with the desired item index
#
# # Call the function to find the string in the specified item
# result = find_string_in_webpage(webpage_url, target_index)
#
# print(f"The string at index {target_index} is: {result}")
#
# import dns.resolver
# import re
#
#
# def get_txt_dns_record(url):
#     try:
#         # Query the TXT DNS record
#         answers = dns.resolver.resolve(url, 'TXT')
#
#         for rdata in answers:
#             # Extract the TXT record value
#             txt_record = rdata.to_text()
#
#             return txt_record
#     except dns.resolver.NXDOMAIN:
#         return "Domain does not exist."
#     except dns.resolver.NoAnswer:
#         return "No TXT record found."
#
#
# def extract_ipv4_address(txt_record):
#     # Use regex to extract the IPv4 address from the TXT record
#     ipv4_regex = r"ip4:([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"
#     match = re.search(ipv4_regex, txt_record)
#
#     if match:
#         return match.group(1)
#     else:
#         return "No IPv4 address found."
#
#
# # Provide the URL for the TXT DNS record lookup
# url = 'quest.squadcast.tech'
#
# # Get the TXT DNS record
# txt_record = get_txt_dns_record(url)
#
# # Extract the IPv4 address from the TXT record using regex
# ipv4_address = extract_ipv4_address(txt_record)
#
# print(f"The IPv4 address for {url} is: {ipv4_address}")


n = int(input('enter'))
print(n)