import pandas as pd
# Author-specific information
from pybliometrics.scopus import AuthorSearch, config
# Use to get author-specific information

df = pd.read_excel(r'/Users/zhuxichen/Desktop/RA data/non_matched_speaker_name.xlsx')
# pybliometrics.scopus.utils.create_config()
# API Key
# Request an API Key from the Elsevier Developer Portal.
# (https://dev.elsevier.com/)
# I'm inputting my APIKey here but please don't use this just now.
# (There are quotas for how much I can use this in a week)

APIKey = "97f0be3ade7211e3e79dbb23981a12be"
# Load dataset
# This dataset should have the following characteristics:
# A column for first names, ideally titled First_Name.
# A column for last names, ideally titled Last_Name.
# Here is an example:
# Create an empty list to collect all the identifier
print(config['Authentication']['APIKey'])

# Get first 3000 author scopus id, run separately
Name = []
for i in range(0, 3000):
    temp = []
    temp.append(df.Last_Name[i])
    temp.append(df.First_Name[i])
    Name.append(temp)

df = pd.DataFrame(Name, columns= ["Last_Name", "First_Name"])

# Get author scopus id
count = 0
ids = []
for i in range(0, len(df)):
    auth = AuthorSearch(query = "AUTHLAST(%s) AND AUTHFIRST(%s) AND SUBJAREA(ECON)" % (df.Last_Name[i], df.First_Name[i]))
    ids.insert(i, auth)
    count += 1
     # Other data
data = []
for i in range(0, len(ids)):
    data.insert(i, 'data' + str(i))
for i in range(0, len(ids)):
    data[i] = pd.DataFrame(ids[i].authors)
frames = []
for i in range(0, len(ids)):
    frames.insert(i, data[i])
result = pd.concat(frames) # Save the dataset
result.to_excel("output_0-3000_unique.xlsx", index = True, index_label = "Count")



Name_3000_rest = []
for i in range(3000, len(df)):
    temp = []
    temp.append(df.Last_Name[i])
    temp.append(df.First_Name[i])
    Name_3000_rest.append(temp)

df_3000_rest = pd.DataFrame(Name_3000_rest, columns= ["Last_Name", "First_Name"])
print(df_3000_rest)

count = 0
ids = []
for i in range(0, len(df_3000_rest)):
    auth = AuthorSearch(query = "AUTHLASTNAME(%s) AND AUTHFIRST(%s) AND SUBJAREA(ECON)" % (df_3000_rest.Last_Name[i], df_3000_rest.First_Name[i]))
    ids.insert(i, auth)
    count += 1
# Other data
data = []
for i in range(0, len(ids)):
    data.insert(i, 'data' + str(i))
for i in range(0, len(ids)):
    data[i] = pd.DataFrame(ids[i].authors)
frames = []
for i in range(0, len(ids)):
    frames.insert(i, data[i])
result = pd.concat(frames) # Save the dataset
result.to_excel("output_3000_rest_unique.xlsx", index = True, index_label = "Count")








# The number of eid retrieved will exceed the api, may split into two xlsx
#############################################################################
# Useless
#############################################################################
# HTTPConnection.default_socket_options = (
#         HTTPConnection.default_socket_options + [
#     (socket.SOL_SOCKET, socket.SO_SNDBUF, 100000000), #1MB in byte
#     (socket.SOL_SOCKET, socket.SO_RCVBUF, 100000000)
# ])
# df = pd.read_excel(r'/Users/zhuxichen/Desktop/RA data/non_matched_speaker_name.xlsx')
# pybliometrics.scopus.utils.create_config()
# API Key
# Request an API Key from the Elsevier Developer Portal.
# (https://dev.elsevier.com/)
# I'm inputting my APIKey here but please don't use this just now.
# (There are quotas for how much I can use this in a week)

# APIKey = "97f0be3ade7211e3e79dbb23981a12be"
# Load dataset
# This dataset should have the following characteristics:
# A column for first names, ideally titled First_Name.
# A column for last names, ideally titled Last_Name.
# Here is an example:
# Create an empty list to collect all the identifier
# print(config['Authentication']['APIKey'])

# Name = []
# for i in range(0, len(df)):
#     temp = []
#     temp.append(df.Last_Name[i])
#     temp.append(df.First_Name[i])
#     Name.append(temp)
#
# df = pd.DataFrame(Name, columns= ["Last_Name", "First_Name"])
# count = 0
# ids = []
# for i in range(0, len(df)):
#     auth = AuthorSearch(query = "AUTHLASTNAME(%s) AND AUTHFIRST(%s) AND SUBJAREA(ECON)" % (df.Last_Name[i], df.First_Name[i]))
#     ids.insert(i, auth)
#     count += 1
# data = []
# for i in range(0, len(ids)):
#     data.insert(i, 'data' + str(i))
# for i in range(0, len(ids)):
#     data[i] = pd.DataFrame(ids[i].authors)
# frames = []
# for i in range(0, len(ids)):
#     frames.insert(i, data[i])
# result = pd.concat(frames) # Save the dataset
# result.to_excel("scopus_id_author.xlsx", index = True, index_label = "Count")
