import json
import codecs
import os, glob
from newspaper import Article
from langdetect import detect


# Opening JSON file

for filename in glob.glob('*.json'):
	with codecs.open(os.path.join(os.getcwd(), filename), mode='r', encoding="utf-8") as f:

# returns JSON object as
# a dictionary

		data = json.load(f)
		list_url=[]

# Iterating through the json
# list
		for i in data['response_items']:
			list_url.append(i["linkToOriginalFile"])

		result_name="./Extracted_texts/"+filename+".txt"
		result = codecs.open(result_name, mode="w",encoding="utf-8")

		for url in list_url:
			article = Article(url)
			try:
				article.download()
				article.parse()
				if (len(article.text) > 1):
					lang=detect(article.text)

					if (lang=="fr"):
						result.write("#" + url + "\n\n")
						result.write (article.text)
						result.write("\n\n")
			except:
				pass
	# Closing file
	f.close()
