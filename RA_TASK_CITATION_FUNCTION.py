# Author-specific information
import pybliometrics


from pybliometrics.scopus import AuthorRetrieval, \
    config  # Use to get author-specific information
from pybliometrics.scopus import CitationOverview  # Use to get citation records
import pandas as pd  # Data manipulation
from itertools import chain
import urllib3, socket
from urllib3.connection import HTTPConnection

# Helper for WebScrapping, help remove runTimeError
HTTPConnection.default_socket_options = (
        HTTPConnection.default_socket_options + [
    (socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000), #1MB in byte
    (socket.SOL_SOCKET, socket.SO_RCVBUF, 1000000)
])
# API Key
# You can use this API Key

# APIKey = "bbbdbb95250305656923e48510d48f8d"
# a = "2c780a1e190e8aebe29a37c14883668a"
# print(config['Authentication']['APIKey'])
# pybliometrics.scopus.utils.create_config()

# pybliometrics.scopus.utils.create_config()
# Load dataset


# Helperfunction for Get citation
def catch_citation(lst, year):
    cc = CitationOverview(lst,  # The Scopus identifier
                          start=1950,  # Insert some really early year
                          end=year - 1,  # Insert some year before conference,
                          citation="exclude-self",
                          # No self-citations counted (this is when an author cites themselves)
                          id_type="scopus_id",  # We're using Scopus ID
                          refresh=True)
    return cc.grandTotal


df = pd.read_excel
def get_citation(year, file_address):

    df = pd.read_excel(file_address)
    print(df)
    author_to_docu = {}
    for i in range(0, len(df['Scopus identifier'])): # loop over the name file
        auth_ret = pd.DataFrame(list(chain.from_iterable([AuthorRetrieval(
            df['Scopus identifier'][i]).get_documents()]))) # get author's documents id
        temp = []
        for item in auth_ret.eid: # get the documents id without prefix
            temp.append(item[7:])
        author_to_docu[df['Scopus identifier'][i]] = temp
    scopus_id_and_citation = pd.DataFrame(
        columns=["author_id", "year", "citation"])

    for key in author_to_docu: # loop over all the documents to get citations
        i = 0
        count = 0
        lst = author_to_docu[key]
        while i <= len(lst) - 1:
            count = count + catch_citation(lst[i:i + 25], year)
            i = i + 25
            print(count)
        new_row = pd.DataFrame(
            {"author_id": [key], "year": [year], "citation": [count]})
        scopus_id_and_citation = pd.concat([scopus_id_and_citation, new_row]
                                           , ignore_index = True)
    return scopus_id_and_citation


# get_citation(2022, '/Users/zhuxichen/Desktop/RA data/2022_unique_scopus_id.xlsx').to_excel("2022_author_citation.xlsx")
# get_citation(2021, '/Users/zhuxichen/Desktop/RA data/2021_unique_scopus_id.xlsx').to_excel("2021_author_citation.xlsx")
# get_citation(2020, '/Users/zhuxichen/Desktop/RA data/2020_unique_scopus_id.xlsx').to_excel("2020_author_citation.xlsx")
# get_citation(2019, '/Users/zhuxichen/Desktop/RA data/2019_unique_scopus_id.xlsx').to_excel("2019_author_citation.xlsx")
# get_citation(2018, '/Users/zhuxichen/Desktop/RA data/2018_unique_scopus_id.xlsx').to_excel("2018_author_citation.xlsx")
# get_citation(2017, '/Users/zhuxichen/Desktop/RA data/2017_unique_scopus_id.xlsx').to_excel("2017_author_citation.xlsx")
# get_citation(2016, '/Users/zhuxichen/Desktop/RA data/2016_unique_scopus_id.xlsx').to_excel("2016_author_citation.xlsx")
# get_citation(2015, '/Users/zhuxichen/Desktop/RA data/2015_unique_scopus_id.xlsx').to_excel("2015_author_citation.xlsx")
# get_citation(2014, '/Users/zhuxichen/Desktop/RA data/2014_unique_scopus_id.xlsx').to_excel("2014_author_citation.xlsx")
