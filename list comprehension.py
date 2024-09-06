"""sqauring of no.s from 1 to 10 and then store it in list using for loop"""
# square=[]
# for i in range(1,11):
#     square.append(i**2)
# print(square)

"""    now using list comprehension   """
# square=[i**2 for i in range(1,11)]
# print(square)

""" selecting movies applying condition """
# movies=[("iron man",2008),("spiderman",2011),("avengers",2012),("the nun",2009)]
# movies_list=[title for title , year in movies if year>2010]
# print(movies_list)