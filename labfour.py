#!/usr/bin/python37all
import cgi
import json
data = cgi.FieldStorage()

led = data.getvalue('option')
s1 = data.getvalue('Brightness')
data = {"option":led, "Brightness":s1}

with open('led-pwm.txt', 'w') as f:
  json.dump(data,f)
print("Content-type: text/html\n\n")
print('<html>')
print('<form action="/cgi-bin/labfour.py" method="POST">')
if led == "LED A":
  print('<input type="radio" name ="option" value="LED_A" checked> LED A <br>')
  print('<input type="radio" name ="option" value="LED_B"> LED B <br>')
  print('<input type="radio" name ="option" value="LED_C"> LED C <br>')
if led == "LED B":
  print('<input type="radio" name ="option" value="LED_A"> LED A <br>')
  print('<input type="radio" name ="option" value="LED_B" checked> LED B <br>')
  print('<input type="radio" name ="option" value="LED_C"> LED C <br>')
if led == "LED C":
  print('<input type="radio" name ="option" value="LED_A"> LED A <br>')
  print('<input type="radio" name ="option" value="LED_B"> LED B <br>')
  print('<input type="radio" name ="option" value="LED_C" checked> LED C <br>')
print('<input type="range" name="Brightness" min="0" max="100" value="50"/><br>')
print('<input type="submit" value="Submit">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')