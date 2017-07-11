def store(data,full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1,' ')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data,label,name):
    return data[label].get(name)

MyNames = {}
init(MyNames)
myname = raw_input('please input your name:')
store(MyNames,myname)
first = raw_input('please input the guanian ci,first,middle,or last:')
guanjian = raw_input('the guanjian ci of the name:')
c = lookup(MyNames,first,guanjian)
print c
