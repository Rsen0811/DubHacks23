import asyncio
from websockets.sync.client import connect

def calculateScore(answers):
    with connect("ws://localhost:6969") as websocket:
        websocket.send(answers)        
        message = websocket.recv()
        print(f"Received: {message}")

s = input("scores?")

calculateScore(s)

