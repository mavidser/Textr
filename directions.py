import requests
import json
import re

KEY = 'AIzaSyDAOVghqgpiIdbJ2CRKnlVqcnF2hQ6o62k'

def clean_html(line):	
	line = re.sub(r"<b>","'",line)
	line = re.sub(r"</b>","'",line)
	line = re.sub(r"<div.*?>"," - ",line)
	line = re.sub(r"</div>","",line)
	line = line.replace("&nbsp;"," ")	
	return line

def getDirectionsWalking(source,destination):
	req = requests.request('GET','https://maps.googleapis.com/maps/api/directions/json?origin='+source+'&destination='+destination+'&mode=walking&key='+KEY)
	obj = req.json()
	ans = obj["routes"][0]["legs"][0]["steps"]
	for i in ans:
		line = clean_html(i["html_instructions"])
		print line

def getDirectionsDriving(source,destination):
	req = requests.request('GET','https://maps.googleapis.com/maps/api/directions/json?origin='+source+'&destination='+destination+'&mode=driving&key='+KEY)
	obj = req.json()
	ans = obj["routes"][0]["legs"][0]["steps"]
	for i in ans:
		line = clean_html(i["html_instructions"])
		print line

def getDirectionsMetro(source,destination):
	req = requests.request('GET','https://maps.googleapis.com/maps/api/directions/json?origin='+source+'&destination='+destination+'&mode=transit&transit_mode=subway&departure_time=1450&key='+KEY)
	obj = req.json()
	ans = obj["routes"][0]["legs"][0]["steps"]
	# print req.text
	for n,i in enumerate(ans):
		print 'Step',n+1,
		line = i["html_instructions"]
		line = clean_html(line)
		print '-',line
		try:
			j = i['transit_details']
			print '  Total Stops:',j['num_stops']
			print '  From:',j['departure_stop']['name']
			print '  To:',j['arrival_stop']['name']
			print '  Line:',j['line']['short_name'],'(',j['line']['name'],')'
		except:
			pass
		try:
			for j in i['steps']:
				print ' ',clean_html(j['html_instructions'])
		except:
			pass
		print

getDirectionsMetro('connaught place, delhi','E-43/1, okhla phase 2, delhi')
# getDirectionsWalking('connaught place','lotus temple')
# getDirectionsDriving('connaught place','lotus temple')

# print requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=91springboard,+Delhi&key='+KEY).text
