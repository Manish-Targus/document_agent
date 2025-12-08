from qdrant_client import QdrantClient
print(dir(QdrantClient))
try:
    client = QdrantClient(":memory:")
    print("Client created")
    print(hasattr(client, "search"))
except Exception as e:
    print(e)
