 # create a mapping of state to abbrevuation 
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# creat a basic set of states and some cities in them 
cities = {
    'CA':'San Arancisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has:",cities['NY']
print "OR State has:",cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is:",states['Michigan']
print "Florida's abbrevuation is:",states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has:",cities[states['Michigan']]
print "Florida has:",cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state,abbrev in states.items():
    print "%s is abbreviated %s " % (states,abbrev)

# print every city in state
print '-' * 10
for state,abbrev in states.items():
    print " %s state is abbreviated %s and has city %s" % (state,abbrev,cities[abbrev])

print '-' * 10
#safely get a abbreviaition by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry ,no Texas."

#get a city with a default value
city = cities.get('TX','Does Not Exist')
print "the city for the state 'TX' is : %s" % city

















