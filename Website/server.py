import asyncio
from websockets.server import serve
from predictor import predictor
import ast

async def echo(websocket):
    async for message in websocket:
        score = predictor(ast.literal_eval(message))
        await websocket.send(str(score))

async def main():
    async with serve(echo, "localhost", 6969):
        await asyncio.Future()
        
asyncio.run(main())
