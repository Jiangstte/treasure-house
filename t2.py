people = {
    'lg' : {
         'phone': '12345',
         'add': '71905',
         },

    'lh' : {
         'phone' : '23456',
	 'add'   : '71904',
	 },

    'lj' : {
	 'phone' : '34567',
	 'add'   : '71903',
	 },
}

#jieshi = {

#'p' : 'phone',
#'a' : 'addres',

#}

name = raw_input('the name is:')
request = raw_input('phone(p) number or address(a):')

if request == 'p': key = 'phone'
if request == 'a': key = 'add'

if name in people: print "%s's %s is %s." % (name,key,people[name][key],)
