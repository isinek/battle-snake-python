import os
import random

import cherrypy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""

class Battlesnake(object):
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self):
		return {
			"apiversion": "1",
			"author": "sinek",
			"color": "#888888",
			"head": "default",
			"tail": "default",
		}

	@cherrypy.expose
	@cherrypy.tools.json_in()
	def start(self):
		data = cherrypy.request.json

		print("START")
		return "ok"

	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	def move(self):
		data = cherrypy.request.json

		print(data)

		# Choose a random direction to move in
		possible_moves = ["up", "down", "left", "right"]
		move = random.choice(possible_moves)

		print(f"MOVE: {move}")
		return {"move": move}

	@cherrypy.expose
	@cherrypy.tools.json_in()
	def end(self):
		data = cherrypy.request.json

		print("END")
		return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
