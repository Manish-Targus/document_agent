from qdrant_client import QdrantClient
import pprint
client = QdrantClient(":memory:")
pprint.pprint([m for m in dir(client) if not m.startswith("_")])
