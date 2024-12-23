from fastapi import WebSocket, WebSocketDisconnect

from .. import app


@app.websocket("/chat/{room_id}")
async def chat(websocket: WebSocket, room_id: int):
    connection_manager = app.state.connection_manager
    await connection_manager.connect(websocket, room_id)

    try:
        while True:
            data = await websocket.receive_json()
            print(data)
            await connection_manager.broadcast(room_id, data)

    except WebSocketDisconnect:
        connection_manager.disconnect(websocket, room_id)
        await connection_manager.broadcast(room_id, {"msg": "Player left the chat"})
