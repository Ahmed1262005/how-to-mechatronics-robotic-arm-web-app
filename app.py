from flask import Flask, render_template, request, redirect, url_for, make_response
import serial
ser = serial.Serial(
	port='/dev/ttyACM0',
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)
def serial_write_to_arduino(data):
 print(data)
 ser.write( bytes(data, 'utf-8'))
# Get server ip
S1list = list()
S2list = list()
S3list = list()
S4list = list()
S5list = list()
S6list = list()
SSlist = list()
app = Flask(__name__)
@app.route("/")
def redirectit():
 response = make_response(redirect(url_for('arm')))
 return response
@app.route("/arm/")
def arm():
    templateData = {
        'run': "Run"
    }
    return render_template('arm.html' , **templateData)
@app.route("/arm/test", methods=["POST"])
def test():
 templateData = {
		's1': "0",
	    's2': "0",
	    's3': "0",
	    's4': "0",
	    's5': "0",
	    's6': "0",
	    'speed': "0",
                 'run': "Run"
	}
 s1 = request.form["s1"]
 s2 = request.form["s2"]
 s3 = request.form["s3"]
 s4 = request.form["s4"]
 s5 = request.form["s5"]
 s6 = request.form["s6"]
 speed = request.form["speed"]

 templateData = {
 's1': s1,
 's2': s2,
 's3': s3,
 's4': s4,
 's5': s5,
 's6' : s6,
 'speed': speed
 }
 S1 = ("s1" + s1)
 S2 = ("s2" + s2)
 S3 = ("s3" + s3)
 S4 = ("s4" + s4)
 S5 = ("s5" + s5)
 S6 = ("s6" + s6)
 SS = ("ss" + speed)
 S1list.append(S1)
 S2list.append(S2)
 S3list.append(S3)
 S4list.append(S4)
 S5list.append(S5)
 S6list.append(S6)
 SSlist.append(SS)
 if len(S1list) > 1:
  if S1list[-2] != S1list[-1]:
   serial_write_to_arduino(S1list[-1])
 if len(S2list) > 1:
  if S2list[-2] != S2list[-1]:
   serial_write_to_arduino(S2list[-1])
 if len(S3list) > 1:
  if S3list[-2] != S3list[-1]:
   serial_write_to_arduino(S3list[-1])
 if len(S4list) > 1:
  if S4list[-2] != S4list[-1]:
   serial_write_to_arduino(S4list[-1])
 if len(S5list) > 1:
  if S5list[-2] != S5list[-1]:
   serial_write_to_arduino(S5list[-1])
 if len(S6list) > 1:
  if S6list[-2] != S6list[-1]:
   serial_write_to_arduino(S6list[-1])
 if len(SSlist) > 1:
  if SSlist[-2] != SSlist[-1]:
   serial_write_to_arduino(SSlist[-1])
 return render_template('arm.html' , **templateData )
app.run(debug=True, host='0.0.0.0', port=8000)