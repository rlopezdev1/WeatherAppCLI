#! python3
import sys, json, requests
# Passes first argument as the name of the script
#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print ("The arguments are: ", str(sys.argv))


APPID = '7883e31cc02aa2a476dc5d016ad54b27'


if len(sys.argv)<2:
    print('Usage weather.py city_name, 2-letter_country_code')
    sys.exit()
# Combines arguments such as San Francisco(two words) into 1 string
location = ''.join(sys.argv[1:])


url = url ='https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&APPID=%s' % (location,
APPID)



#Stores results of url 
response = requests.get(url);
#This stores a response object, which checks for errors.
response.raise_for_status();

#print(response.text)

#load JSON data into a Python variable.
weatherData = json.loads(response.text)

w = weatherData['list']
kelvin = w[0]['main']['temp']
convertToF = (kelvin - 273.15) * 9/5 + 32
print('Current weather in %s: '  %(location))
print w[0]['weather'][0]['main'], '-',w[0]['weather'][0]['description']
print "Humidity", w[0]['main']['humidity'], "%"
print "Temperature: ", convertToF, u"\N{DEGREE SIGN}"
print
print('Tomorrow:')
print w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description']
print
print('Day after tomorrow:')
print w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description']

