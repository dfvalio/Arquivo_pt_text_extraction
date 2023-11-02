# Arquivo_pt_text_extraction
Python script to extract language-specific texts concerning a list of key words. 

1) search_key_words.py --> this script creates a .json file for each key word listed as input. The .json files concerns the results from the query in Arquivo.pt database.
2) text_extraction_url_newspaper_lang_detect.py --> for each .json file created with the preceding script, it extract the texts from all URL's (using newspaper3k) and verify the language (using langdetect). 
