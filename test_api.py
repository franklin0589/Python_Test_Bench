from pydoc import resolve
import requests
import json
import pyglet

from test_pyglet import on_draw

response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
window = pyglet.window.Window()

if response.status_code == 200:
    # Display all Api information recovered
    # def jprint(obj):
    #     # create a formatted string of the Python JSON object
    #     text = json.dumps(obj, sort_keys=True, indent=4)
    #     print(text)
        
    # jprint(response.json())
    #Investigate specific information
    #print(response.json()["iss_position"]["latitude"])
    fact = response.json()["text"]
    label = pyglet.text.Label(fact, font_name='Times New Roman', font_size=12, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
    @window.event
    def on_draw():
        window.clear()
        label.draw()
    pyglet.app.run()
else:
    print("Error: Status Code is", response.status_code)