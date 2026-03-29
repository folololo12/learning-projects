  show_id     type                  title         director  ... rating   duration                                          listed_in                                        description
0      s1    Movie   Dick Johnson Is Dead  Kirsten Johnson  ...  PG-13     90 min                                      Documentaries  As her father nears the end of his life, filmm...
1      s2  TV Show          Blood & Water              NaN  ...  TV-MA  2 Seasons    International TV Shows, TV Dramas, TV Mysteries  After crossing paths at a party, a Cape Town t...
2      s3  TV Show              Ganglands  Julien Leclercq  ...  TV-MA   1 Season  Crime TV Shows, International TV Shows, TV Act...  To protect his family from a powerful drug lor...
3      s4  TV Show  Jailbirds New Orleans              NaN  ...  TV-MA   1 Season                             Docuseries, Reality TV  Feuds, flirtations and toilet talk go down amo...
4      s5  TV Show           Kota Factory              NaN  ...  TV-MA  2 Seasons  International TV Shows, Romantic TV Shows, TV ...  In a city of coaching centers known to train I...

[5 rows x 12 columns]
<class 'pandas.DataFrame'>
RangeIndex: 8807 entries, 0 to 8806
Data columns (total 12 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   show_id       8807 non-null   str
 1   type          8807 non-null   str
 2   title         8807 non-null   str
 3   director      6173 non-null   str
 4   cast          7982 non-null   str
 5   country       7976 non-null   str
 6   date_added    8797 non-null   str
 7   release_year  8807 non-null   int64
 8   rating        8803 non-null   str
 9   duration      8804 non-null   str
 10  listed_in     8807 non-null   str
 11  description   8807 non-null   str
dtypes: int64(1), str(11)
memory usage: 825.8 KB
None
       release_year
count   8807.000000
mean    2014.180198
std        8.819312
min     1925.000000
25%     2013.000000
50%     2017.000000
75%     2019.000000
max     2021.000000
show_id            0
type               0
title              0
director        2634
cast             825
country          831
date_added        10
release_year       0
rating             4
duration           3
listed_in          0
description        0
dtype: int64
type
Movie      6131
TV Show    2676
Name: count, dtype: int64
country
United States     2818
India              972
United Kingdom     419
Japan              245
South Korea        199
Canada             181
Spain              145
France             124
Mexico             110
Egypt              106
Name: count, dtype: int64
