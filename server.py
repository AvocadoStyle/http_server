import socket
import utilities_server

# # TO DO: set constants
# IP = '127.0.0.1'
# PORT = 80
# SOCKET_TIMEOUT = 0.1
#
# HTTP_OK_MSG = 'HTTP'
# ENCODE = 'ascii'
data = utilities_server.get_server_configuration()

def get_file_data(filename):
    """ Get data from file """
    if filename == '/':
        filename = 'index.txt'
    else:
        filename = filename.split('/')[1:]
        filename = ''.join(filename)
        if filename == 'favicon.ico':
            return "error fav"
    return utilities_server.get_file_content(filename)



def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    http_header_send = data["HTTP"]
    msg = ""
    msg += f'{http_header_send["HTTP_VERSION"]} {http_header_send["HTTP_VALID"]}{http_header_send["HTTP_END"]}'
    try:
        file_content = ''.join(get_file_data(resource))
        msg = f'{msg}\r\n{file_content}'
        client_socket.sendall(msg.encode())
    except:
        print("cannot get the file data")
        client_socket.send(b'error')
    return

    """
    if resource == '':
        url = DEFAULT_URL
    else:
        url = resource

    # TO DO: check if URL had been redirected, not available or other error code. For example:
    if url in REDIRECTION_DICTIONARY:
        # TO DO: send 302 redirection response

    # TO DO: extract requested file tupe from URL (html, jpg etc)
    if filetype == 'html':
        http_header = # TO DO: generate proper HTTP header
    elif filetype == 'jpg':
        http_header = # TO DO: generate proper jpg header
    # TO DO: handle all other headers

    # TO DO: read the data from the file
    data = get_file_data(filename)
    http_response = http_header + data
    client_socket.send(http_response.encode())
    """

def validate_http_request(request):
    """
    Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL
    """
    li_request = request.split()
    request_type = li_request[0]
    request_url = li_request[1]
    http_version = li_request[2]

    if request_type == data["HTTP"]["GET_REQUEST"] and \
        request_url.startswith('/') and \
        http_version == data["HTTP"]["HTTP_VERSION"]:
        return True, request_url

    return False, '/error'

def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    MESSAGE_SIZE = data["SERVER_DETAILS"]["MESSAGE_SIZE"]
    client_request = client_socket.recv(1024).decode()
    valid_http, resource = validate_http_request(client_request)

    if valid_http:
        print('valid HTTP request')
        handle_client_request(resource, client_socket)
    else:
        print("error - not a valid HTTP request")
        client_socket.send(b'error')

    print("close connection")
    client_socket.close()

def main():
    # Open a socket and loop forever while waiting for clients
    server_details = data["SERVER_DETAILS"]
    IP = server_details["IP"]
    PORT = server_details["PORT"]
    SOCKET_TIMEOUT = server_details["SOCKET_TIMEOUT"]
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()