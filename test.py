text1 = "python developer with experience in machine learning and data analysis"
text2 = "skilled in python, data visualization, and machine learning projects"

words1 = text1.split()
words2 = text2.split()

common = set(words1) & set(words2)

print("Text 1 words:", words1)
print("Text 2 words:", words2)
print("Common words:", common)
print("Match count:", len(common))