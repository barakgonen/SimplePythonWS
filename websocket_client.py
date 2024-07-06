import os
import asyncio
import websockets

async def send_message_periodically():
    server_url = os.getenv("WS_SERVER_URL")
    port = os.getenv("WS_SERVER_PORT")
    interval = int(os.getenv("SEND_INTERVAL"))
    message_size = int(os.getenv("MESSAGE_PAYLOAD_SIZE"))
    protocol = "ws://"

    uri = f"{protocol}{server_url}:{port}"
    print("URI is: " + uri)

    async with websockets.connect(uri) as websocket:
        while True:
            message = "a" * message_size
            await websocket.send(message)
            print(f"Sent message: {message}")
            await asyncio.sleep(interval)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_message_periodically())
