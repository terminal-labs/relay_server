import time
import piplates.RELAYplate as RELAY
from flask import Flask

t = .2

app = Flask(__name__)

@app.route('/on/<int:relay_id>')
def on(relay_id):
    print relay_id
    RELAY.relayON(0,relay_id)
    return str(relay_id)+' on'
    
@app.route('/all_on')
def all_on():
    for i in range(1,8):
        RELAY.relayON(0,i)
        time.sleep(t)
    return 'all on'

@app.route('/off/<int:relay_id>')
def off(relay_id):
    RELAY.relayOFF(0,relay_id)
    return str(relay_id)+' off'

@app.route('/all_off')
def all_off():
    for i in range(1,8):
        RELAY.relayOFF(0,i)
        time.sleep(t)
    return 'all off'                        
