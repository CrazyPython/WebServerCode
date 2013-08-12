import SocketServer
import sys
import traceback
import os
html = ""
disallowed_prefixes=["C:/Users"]
class BaseTCPHandler(SocketServer.BaseRequestHandler):
    def getdata(self):
        self.data = self.request.recv(1024).strip()
    def handle(self):
        self.getdata()
        self.handle_fake()
    def __getatr__(self,attr):
        if attr == "handle":
            return self.handle_fake
class SingleHandler(BaseTCPHandler):
    def handle_fake(self): #So that the Inherited ones can acsess the handle fuction
        global html
        self.request.sendall(html)
class TCPFileHandler(BaseTCPHandler):
    suffix = "<hr><i>Python TCPFileServer .1</i>"
    def handle_fake(self):
        try:
            send = open("SERVER/"+self.data).read()
        except IOError:
            send = "<b>404 Page not Found.</b>"+self.suffix
        except:
            send = "<b>404 Internal Server Error</b>"+self.suffix
            print "500:"
            traceback.print_exc()
        self.request.sendall(t)
class SafeFileHandlerMixIn(BaseTCPHandler):
    
    def getdata(self):
        global disallowed_prefixes
        data = self.request.recv(1024).strip()
        data = os.normpath(data)
        for prefix in disallowed_prefixes:
            if data.startswith(prefix):
                self.request.sendall("<b>403 Forbidden(Security Breach Detected!)</b>")
                break
        else:
            self.data = data
            self.handle_fake()
