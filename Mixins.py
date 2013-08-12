import servers
class SafeTCPFileHandler(TCPFileHandler,SafeFileHandlerMixIn):
    "'Soup' of TCPFileHandler and SafeFileHandlerMixIn"
    suffix = "<hr><i>Python TCPFileServer .1 with SafeFileHandlerMixIn</i>"
