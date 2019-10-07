student = {1:{'name':'Pooja', 'age':29,'Country':'New Zealand'},
           2:{'name':'Amay', 'age':31,'Country':'New Zealand'},
           3:{'name':'Ashwini', 'age':29,'Country':'India'}}

for key, value in student.items():
        print('ID:', key)

        for key in value:
                print(key,':',value[key])
##for p_id, p_info in student.items():
##    print("\nPerson ID:", p_id)
##    
##    for key in p_info:
##        print(key + ':', p_info[key])
##
