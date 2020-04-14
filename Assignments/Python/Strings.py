import re
s = " I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"

print("Given String is :"+s)

#1)Consider the above text as a string, figure out the average length of the string.
len_of_string = len(s)
words = s.split()
len_of_words = len(words)
avg_len_of_string= round((len_of_string/len_of_words),2)
print("1) avg_len_of_string "+ str(avg_len_of_string))


# 2: Lower the text in the string.
print("2) Lower the string \n"+s.lower())

# 3 Try to get the clean text removing the punctuation from the string.

pattern=r"[.,! ]"
clean_text = re.sub(pattern,"",s)
print("3) clean text is \n"+clean_text)

