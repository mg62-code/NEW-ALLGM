import asyncio
from typing import List

class StreamingManager:
    """Manages active SSE client connections and broadcasts messages."""
    def __init__(self):
        # A list to hold asyncio.Queue objects for each client
        self.active_connections: List[asyncio.Queue] = []

    async def connect(self, queue: asyncio.Queue):
        """Adds a new client queue to the list of active connections."""
        self.active_connections.append(queue)

    async def disconnect(self, queue: asyncio.Queue):
        """Removes a client queue from the list of active connections."""
        try:
            self.active_connections.remove(queue)
        except ValueError:
            # This can happen if a client disconnects uncleanly
            # or is already removed. It's safe to ignore.
            pass

    async def broadcast(self, message: str):
        """Sends a message to all connected clients."""
        # Iterate over a copy of the list in case it gets modified
        # during the broadcast (e.g., a client disconnects).
        for queue in self.active_connections[:]:
            await queue.put(message)

# Create a single, shared instance of the manager
streaming_manager = StreamingManager()
