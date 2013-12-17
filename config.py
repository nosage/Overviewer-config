# Define the path to your world here. 'My World' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['My World'] = "C:\Minecraft Server 1.7\Minecraft\world"

def factoryFilter(poi):
    if poi['id'] == 'Factory':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def townFilter(poi):
    if poi['id'] == 'Town':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def structureFilter(poi):
    if poi['id'] == 'Structure':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
		
manualpoisList = [
	{'id':'Structure','x':-211,'y':100,'z':120,'name':'the Castle'},
	{'id':'Factory','x':-110,'y':100,'z':229,'name':'Iron Foundry'},
	{'id':'Factory','x':46,'y':150,'z':188,'name':'the Lab'},
	{'id':'Town','x':1785,'y':100,'z':814,'name':'Desert Village'}
]		

markerList = [
	dict(name="Towns", filterFunction=townFilter, icon="icons/marker_town.png", checked=True),
	dict(name="Factories", filterFunction=factoryFilter, icon="icons/marker_factory.png", checked=True),
	dict(name="Structure", filterFunction=structureFilter, icon="icons/marker_tower.png", checked=True),
	dict(name="Players", filterFunction=playerIcons, checked=True)
]

# Define where to put the output here.
outputdir = "C:\wamp\www"

# This is an item usually specified in a renders dictionary below, but if you
# set it here like this, it becomes the default for all renders that don't
# define it.
# Try "smooth_lighting" for even better looking maps!
rendermode = "lighting"

renders["render1"] = {
        'world': 'My World',
        'title': 'A regular render',
		'showlocationmarker': False,
		'manualpois': manualpoisList,
		'markers': markerList,
}

# This example is the same as above, but rotated
renders["render2"] = {
        'world': 'My World',
        'northdirection': 'upper-right',
        'title': 'Upper-right north direction',
		'showlocationmarker': False,
		'manualpois': manualpoisList,
		'markers': markerList,
}

# Here's how to do a nighttime render. Also try "smooth_night" instead of "night"
renders["render3"] = {
        'world': 'My World',
        'title': 'Nighttime',
        # Notice how this overrides the rendermode default specified above
        'rendermode': 'night',
		'showlocationmarker': False,
		'manualpois': manualpoisList,
		'markers': markerList,
}

