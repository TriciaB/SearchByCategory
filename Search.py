print('Welcome to Search by Category')
print('What do you want to learn? ')
searchTopic = input()
print('Your topic is: ')
print('Please enter your search category: ')
print('1) Book')
print('2) Video')
print('3) Picture')
print('4) Article')
print('Enter the category number: ')
searchCategory = input()
if (searchCategory == "1"):
    categoryDesc = "Book"
if (searchCategory == "2"):
    categoryDesc = "Video"
if (searchCategory == "3"):
    categoryDesc = "Picture"
if (searchCategory == "4"):
    categoryDesc = "Article"
print('You selected to search for ' + str(searchTopic) + ' ' + str(categoryDesc))