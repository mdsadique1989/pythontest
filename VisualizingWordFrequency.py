import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Get input from the user
text = input("Enter sentence for word cloud: ")

# Generate the word cloud
wordcloud = WordCloud().generate(text)

# Display the word cloud using matplotlib
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# Save the plot as an image file
plt.savefig("/workspaces/pythontest/wordcloud.png")

print("Word cloud saved as 'wordcloud.png'")
