class dictionarydi:
    def Dictionary(self):
        d = { 'course_name':'Python','course_duration':'2 month'}
        print(d, type(d))
        print(d['course_name'])
if __name__=="__main__":
    obj = dictionarydi()
    obj.Dictionary()
    obj.Dictionary()