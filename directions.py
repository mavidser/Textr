import requests
import json
import re
import urllib

KEY = 'PRIVATE'

def clean_html(line):	
	line = re.sub(r"<b>","'",line)
	line = re.sub(r"</b>","'",line)
	line = re.sub(r"<div.*?>"," - ",line)
	line = re.sub(r"</div>","",line)
	line = line.replace("&nbsp;"," ")	
	return line

def getDirectionsWalking(source,destination):
	answer = ''
	req = requests.request('GET','https://maps.googleapis.com/maps/api/directions/json?origin='+source+'&destination='+destination+'&mode=walking&key='+KEY)
	obj = req.json()
	ans = obj["routes"][0]["legs"][0]["steps"]
	for i in ans:
		line = clean_html(i["html_instructions"])
		answer = answer + '\n' + line
	return answer

def getDirectionsDriving(source,destination):
	answer = ''
	req = requests.request('GET','https://maps.googleapis.com/maps/api/directions/json?origin='+source+'&destination='+destination+'&mode=driving&key='+KEY)
	obj = req.json()
	ans = obj["routes"][0]["legs"][0]["steps"]
	for i in ans:
		line = clean_html(i["html_instructions"])
		answer = answer + '\n' + line
	print answer
	return answer

def getDirectionsMetro(source,destination):
	answer = ''
	req = requests.request('GET','https://maps.googleapis.com/maps/api/directions/json?origin='+source+'&destination='+destination+'&mode=transit&transit_mode=subway&departure_time=1450&key='+KEY)
	obj = req.json()
	ans = obj["routes"][0]["legs"][0]["steps"]
	# print req.text
	for n,i in enumerate(ans):
		answer = answer + '\n' + 'Step '+str(n+1)
		line = i["html_instructions"]
		line = clean_html(line)
		answer = answer + '- '+line
		try:
			j = i['transit_details']
			answer = answer + '\n' + '  Total Stops: '+str(j['num_stops'])
			answer = answer + '\n' + '  From: '+j['departure_stop']['name']
			answer = answer + '\n' + '  To: '+j['arrival_stop']['name']
			answer = answer + '\n' + '  Line: '+j['line']['short_name']+' ('+j['line']['name']+')'
		except Exception as e:
			pass
		try:
			for j in i['steps']:
				answer = answer + '\n' + ' '+clean_html(j['html_instructions'])
		except:
			pass
		answer = answer + '\n'
	return answer

def placeSearch(query):
	req = requests.request('GET','https://maps.googleapis.com/maps/api/place/textsearch/json?'+urllib.urlencode({'query':query})+'&key='+KEY)
	obj = req.text
	obj = req.json()
	answer = ''
	for i in obj['results']:
		if 'opening_hours' not in i:
			answer = answer + '\n' + i['name']
			answer = answer + '\n' + i['formatted_address']
			answer = answer + '\n'
		elif i['opening_hours']['open_now']:
			answer = answer + '\n' + i['name']
			answer = answer + '\n' + i['formatted_address']
			answer = answer + '\n'
	return answer

# print getDirectionsMetro('connaught place, delhi','E-43/1, okhla phase 2, delhi')
# getDirectionsWalking('connaught place','lotus temple')
# getDirectionsDriving('connaught place','lotus temple')

# print requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=91springboard,+Delhi&key='+KEY).text
