from threading import Thread

import tornado.ioloop
import tornado.web
import json

import discord
import asyncio

with open("config.json", "r") as f:
	config = json.load(f)

def sawait(coro, loop):
	return asyncio.run_coroutine_threadsafe(coro, loop).result()

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

async def send_message(channel, msg):
	#Grrrrrrrrrrrrrrrrrr
	return "AAAAAAAA"

class MainHandler(tornado.web.RequestHandler):
	def get(self, channel = None):
		ip = self.request.remote_ip
		if len(config["allow"]) > 0 and ip not in config["allow"]:
			self.write("Unauthorized")
			self.set_status(401)
			return

		statuscode = 200
		try:
			message = self.get_argument("message", None, True)

			if channel is None or len(channel) is 0:
				raise Exception("Missing channel name")
			if message is None or len(message) is 0:
				raise Exception("Missing message")

			sawait(send_message(channel, message), client.loop)
			self.write("OK")
		except Exception as e:
			self.write("Exception: {}".format(e))
			statuscode = 500
		finally:
			self.set_status(statuscode)

if __name__ == "__main__":
	app = tornado.web.Application([
		(r"/(.*)", MainHandler),
	])
	app.listen(config["port"])

	Thread(target=client.run, args=(config["token"],)).start()
	tornado.ioloop.IOLoop.current().start()