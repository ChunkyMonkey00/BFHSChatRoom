import asyncio
import websockets

# Store connected clients
clients = set()

# Define a function to handle incoming messages
async def handle_client(websocket, path):
    # Add the client to the set
    clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to all connected clients
            for client in clients:
                await client.send(message)
    finally:
        # Remove the client when they disconnect
        clients.remove(websocket)

# Create a WebSocket server
start_server = websockets.serve(handle_client, "0.0.0.0", 8765)

# Start the server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
