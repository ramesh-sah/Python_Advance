d={
    'course_id': 1,
    'course_name': 'Python Programming',
    'course_duration': '2 months',
    'course_instructor': 'John Doe',
    'course_price': 1500
}
c=d.get('course_id')
print(c)
c1=d['course_duration']
print(c1)
for a in d.keys():
    print(a)
for a in d.values():
    print(a)
for a in d.items():
    print(a)
del(d['course_id'])

print(d)

d['course_id'] = 100
print(d.pop('course_id'))
print(d)
