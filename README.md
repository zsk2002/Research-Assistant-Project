# Research Project Report for Summer 2022 with Prof. Dhuey
Group Members: Shangkai Zhu, Rong Zhang, Miao Han

#1. Table 1: Economic noConference Data.xlsx
It is a dataset containing information of associations and their invited speakers from 2014 to 2022, and it has three sheets. The first sheet shows the information of invited speakers for each association and in each year, including the gender information for each speaker. The second sheet is an association list, specifying whether each association is included in our first sheet. For those associations we fail to fill the speaker information into the first sheet, there is a reason for why we cannot find the invitation information. You can also find the website link for each association and links to their conference pages in the second sheet. The third sheet is the colour code.


#2. Data cleaning for Economic noConference Data in R

- Reformat the speakers’ names and clean the dataset.

- See process in: data_clean.Rmd

#### Output: cleaned_name /non_matched_speaker_name.xlsx

#### Cleaned_name.xlsx:
    a cleaned dataset for Economic noConference Data.xlsx, it contains 6 
    columns, Association_Name, Year, First_Name, Last_Name, Sex, 
    name(Full name, include both Fisrt_Name, and Last_Name)

#### Non_matched_speaker_name.xlsx: 
    It is a subset of cleaned_name data that get rid of the names that have 
    already had a speaker id, and it only contains two columns, Last_Name 
    and First_Name. They are all the speakers that have not had a speaker 
id yet.

# 3. Get author id in Python

#### See python file: GetIdentifier.py

    We imported non_matched_speaker_name.xlsx into python, and used the 
    AuthorSearch function in pybliometrics.scopus Package to get the 
    speaker cid for those authors. Due to Web Scraping Protection, 
    we kept getting Scopus401error, so we split the non_matched_speaker_name 
    into two parts to get the author’s cid, 0 - 3000 and 3000 - rest, which 
    we get two output files, Output_0-3000_unique.xlsx, the first 3000 names 
    of speaker id and output_3000_rest_unique, the rest names of speaker id. 
    Then, we combined the two dataset, and named it as all_name.xlsx. It 
    contains 12 columns, Count (the number of times for the same 
    name with different eid), eid (eid of each individual), orcid, surname, 
    initials, givenname, affiliation, documents, city, country, and areas.

# 4. Work on the Un-unique Speakers

    After we got all speakers with their corresponding scopus id (about 5000 
    more, both unique speakers and un-unique speakers all together), there’re 
    many speakers with repeated search results of speaker names from different 
    associations.
    For unique speakers, their count is 0. For un-unique ones, their counts 
    are greater than 0. We need to know which speaker is correct for counts 
    more than 0.
    Therefore, using both the gender database and the speaker sheet, 
    we manually find the correct speakers based on the information of 
    various meetings of the association.
    Several problems are indicated in the “notes” column, such as the website 
    is broken or scopus produces the wrong search results.
    For the second sheet, the correct speakers are not fully copied from the 
    first sheet, since we add “unique” and “correct” columns in the first 
    sheet, shown as the indicator of “0=no” and “1=yes”.

#### Output: non_matched_manually_checked_speakers.xlsx

#5. Data cleaning for non_matched_manually_checked_speakers.xlsx in R

#### See process in: data_clear.Rmd

- Get rid of the prefix in the eid
- Select only three columns, Scopus identifier, Last_Name, and First_Name
- Add previously matched speakers
- Combine the dataset with cleaned to split author’s with years

Output:
- 2014_unique_scopus_id.xlsx,
- 2015_unique_scopus_id.xlsx,
- 2016_unique_scopus_id.xlsx,
- 2017_unique_scopus_id.xlsx,
- 2018_unique_scopus_id.xlsx,
- 2019_unique_scopus_id.xlsx,
- 2020_unique_scopus_id.xlsx,
- 2021_unique_scopus_id.xlsx,
- 2022_unique_scopus_id.xlsx.

#Useless for now


## 6. Extract their documents id and citations from Scopus on Python

#### See file: RA_TASK_CITATION_FUNCTION.py

    Originally, we only wanted to get the total citations of each author 
    before a given year, and the whole process is in the 
    RA_TASK_CITATION_FUNCTION.py

    We mainly used two functions from the pybliometrics.scopus package, 
    AuthorRetrival and CitationOverview
