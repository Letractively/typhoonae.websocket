all: proto/websocket_service_pb2.py

proto/websocket_service_pb2.py: src/proto/websocket_service.proto
	@mkdir -p proto
	bin/protoc -I src/proto/ --python_out=proto/ $<

clean:
	rm -rf proto
