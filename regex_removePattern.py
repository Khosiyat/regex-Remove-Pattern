                                                                    #Copywrite Warning: Owner of the code is Gulcheera Academy(Khosiyat Sabirova)
                                                        #This code can be used by anyone for free, but the name "Gulcheera Academy" must be acknowledged 
import pandas as pd
import numpy as np
import matplotlib as plt
import re
import warnings
#%matplotlib inline


example_textData=["@this is great post, #IT @my godfather http://bit.ly/3h63x  he did not deserve this","#culture_art Here is a post of modern art"]
#remove special patterns
def remove_pattern(inputText,inputPattern):
  all_patterns=re.findall(inputPattern,inputText)
  for lexUnit in all_patterns:
    inputText=re.sub(lexUnit, "", inputText)

    return inputText

#You may change the regular expression patterns
cleaned_text=np.vectorize(remove_pattern)(example_textData[0:4],["@"])

print(cleaned_text)
