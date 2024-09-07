d={
    'course_name':'Python',
    'course_duration':'2 months',
    'instructor':'ramesh',
    'location':'bangalore',
    'date':'2022-08-15',
    'time':'10:00 AM'
}
del(d['course_name'])
print(d)
a=d.pop('date')
print(a)
print(d)


# n=d.get('course_name')
# print(n)
# n=d['course_duration']
# print(n)
# for a in d.keys():
#     print(a)
    
# for a in d.values():
#     print(a)
# #get both key and values 
# for a in d.keys():
#     print(a,":",d[a])
    
# for a,b in d.items():
#     print(a,":",b)
