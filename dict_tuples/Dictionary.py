# d = {'a': 10, 'b': 20, 'c': 30}
# print (d['a'])  #print value from dict
# del d['a']   #delete
# d['d'] = 100 #add value to dict
# print(d)
# #print all values
# for i in d:
#     print ("keys :", i , "value:", d[i])

#
# book = {}
# book['tom'] = {'name':  'Tom', 'age': 10 }
# book['john'] = {'name': 'John', 'age': 15}
# book['mary'] = {'name': 'Mary', 'age': 25}
# import  json
# s = json.dumps(book)
# with open("/Users/anuhyasamudrala/Documents/book.txt", "w") as f:
#     f.write(s)
#     f.close()
#
# f = open("/Users/anuhyasamudrala/Documents/book.txt" , "r")
# s = json.loads(f.read())
# age = s['tom'] ['name']
# print(age)
#
# for name in s:
#     print(s[name])
#
#

school = {}
school['abc'] = {'name' : 'abc' , 'place' : 'clt'}
school['def'] = {'name' : 'def' , 'place' : ' texas' }
import  json
s = json.dumps(school)
with open("/Users/anuhyasamudrala/Documents/school.txt" , "w") as f :
      f.write(s)

f = open("/Users/anuhyasamudrala/Documents/school.txt" , "a")
school['ghi'] = {'name' : 'ghi' , 'place' : 'clt1'}




