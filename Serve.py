def serve(handler,t=SocketServer.TCPServer,HOST="localhost",PORT=0):
    "Serve forever, given a handler, a\
t(default=SocketServer.TCPServer) a HOST(default = \
localhost) a PORT(default = 0)"
    server = t((HOST,PORT),handler)
    server.serve_forever()
    
