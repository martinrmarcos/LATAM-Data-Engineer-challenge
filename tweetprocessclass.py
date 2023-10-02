## importar libreria a usar

import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import re
import json
import re
from collections import Counter
import unidecode
import unicodedata
import emoji
from sqlalchemy import create_engine


class tweet_process():

	def json_to_df(self, file_name):
	### This function receives the file name and searches the current path for it
	### after that it iterates over all tweets adding them to a list using json_normalize
		current_directory = os.path.dirname(os.path.realpath('__file__'))
		file_name = file_name
		file_path = os.path.join(current_directory, file_name)
		normalized_data_list = []
		if os.path.exists(file_path):
			with open(file_path) as json_file:
				for line in json_file:
					try:
						data = json.loads(line)
						normalized_data_list.append(pd.json_normalize(data, max_level=1))
					except json.JSONDecodeError as e:
						print(f"Error decoding JSON: {e}")
		else:
			print(f"File not found: {file_path}")
		return pd.concat(normalized_data_list, ignore_index=True)

	def convert_lowercase(self, df):
	### Just a basic function in order to normalize the data by getting all values 
	### to lowercase and extracting all accentuation
		def strip_accents(s):
			return ''.join(c for c in unicodedata.normalize('NFD', s)
							if unicodedata.category(c) != 'Mn')
		df.columns = map(str.lower, df.columns)
		df.columns = map(strip_accents, df.columns)
		df = df.apply(lambda x: x.astype(str).str.lower())
		return df

	def topX_most_retweeted(self, df, top = 10, retweetcount_column = 'retweetcount'):
	### This function receives the df and retrieves a new df with the most retweeted tweets
	### using the function sort_values
		df[retweetcount_column] = pd.to_numeric(df[retweetcount_column])
		topX_retweeted_tweets = df.sort_values(by=retweetcount_column, ascending=False).head(top)
		return topX_retweeted_tweets

	def topX_tweets_per_person(self, df, top = 10, username_column = 'user.username'):
	### This function receives the df and retrieves a new df with the people with the most tweets
	### using a value_counts over the username
		return pd.DataFrame(df[username_column].value_counts().head(top))

	def topX_tweets_per_day(self, df, top = 10, date_columns = 'date'):
	### This function receives the df and retrieves a new df with the days were 
	### there were the most ammount of tweets, using a value_counts over the transformed 'day' value
		df[date_columns] = pd.to_datetime(df[date_columns])
		df['day'] = df['date'].dt.date
		return pd.DataFrame(df['day'].value_counts().head(top))

	def topX_most_used_hashtags(self, df, top = 10, tweet_column = 'renderedcontent'):
	### This function receives the df and retrieves a new df with the most used hashtags
	### using a value_count() over the hashtags extracted by using the REGEX '#\w+' and findall
		all_text = ' '.join(df[tweet_column])
		hashtags = re.findall(r'#\w+', all_text)
		return pd.DataFrame(pd.Series(hashtags).value_counts().head(top))

	def topX_most_used_emoji(self, df, top = 10, tweet_column = 'renderedcontent'):
	### This function receives the df and retrieves a new df with the most used emojis
	### using emoji.UNICODE_EMOJI to find all emojies within all tweets, and sorting them to get the most used
		all_text = ' '.join(df[tweet_column])
		emojislist = [c for c in all_text if c in emoji.UNICODE_EMOJI['en']]
		#emoji_counts = Counter(emojislist)
		top_X_emojis = dict(sorted(Counter(emojislist).items(), key=lambda x: x[1], reverse=True)[:top])
		return pd.DataFrame(list(top_X_emojis.items()), columns=['emoji', 'count'])

	def topX_most_influential(self, df, top = 10, retweetcount_column = 'retweetcount', username_column = 'user.username'):
	### This function receives the df and retrieves a new df with the most influential users according to ther retweets
	### using a groupby on retweetcount over username and then reordering them Descending
		df[retweetcount_column] = pd.to_numeric(df[retweetcount_column])
		user_retweet_counts = df.groupby(username_column)[retweetcount_column].sum()
		return pd.DataFrame(user_retweet_counts.sort_values(ascending=False).head(top))

################## The following function can only be used if the postgres docker steps were completed
################## Please check readme file


	def upload_to_sql(self, df, columns_to_sql, table_name):
	### This function will upload certain df with its seelcted columns into a selected table on the created DB
	### Using sqlalchemy we can acces a DB and perform changes to it
		username = 'postgres'
		password = 'Latam2023'
		host = '0.0.0.0'  
		port = '5432'  
		database_name = 'LATAMDB'
		engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database_name}')
		connection = engine.connect()
		return df[columns_to_sql].to_sql(table_name, engine, if_exists='replace', index=False)


































