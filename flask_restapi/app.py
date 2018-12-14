from flask import Flask, jsonify, make_response, request
from mymodules.fibonacci import get_fib_sequence
from mymodules.health import endpointhealth, SRM

app = Flask(__name__)

@app.route('/fib/<int:start_idx>/<int:end_idx>/', methods=['GET'])
def fibnacci_sequence (start_idx, end_idx):
    response = {
        'data': None,
        'status': 200,
        'error_message': None
    }

    try:
        start_idx = int(start_idx)
        end_idx = int(end_idx)
    except Exception as err:
        response['status'] = 500
        response['error_message'] = str(err)
        return jsonify(response)


    if start_idx >= end_idx or start_idx < 0 or end_idx < 0:
        response['status'] = 500
        response['error_message'] = 'Start index should be less than end index and both of them positive numbers'
        return jsonify(response)

    try:
        response['data'] = {
            'fibonacci_sequence': get_fib_sequence(start_idx, end_idx),
            'start_idx': start_idx,
            'end_idx': end_idx
        }
    except Exception as err:
        response['status'] = 500
        response['error_message'] = str(err)
        return jsonify(response)


    response = make_response(jsonify(response))

    response.cache_control.max_age = 31536000 # for a year

    return response


@app.route('/health/', methods=['GET'])
def health_check():

    data = SRM.get_datas()
    data['service_health'] = []

    path = request.host

    try:
        data['service_health'].append(endpointhealth(path + '/fib/5/60/'))
    except Exception as err:
        data['service_health'].append(str(err))

    response = make_response(jsonify(data))
    response.cache_control.max_age = 31536000 # for a year

    return response

if __name__ == '__main__':
    import socket, fcntl, struct, subprocess

    def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_fileno = s.fileno()
        SIOCGIFADDR = 0x8915

        structpack = struct.pack('256s', ifname[:15])
        ioctl = fcntl.ioctl(socket_fileno, SIOCGIFADDR, structpack)
        ntoa = socket.inet_ntoa(ioctl[20:24])
        
        return ntoa

    for ni in socket.if_nameindex():
        ifname = ni[1].encode()
        
        if not ifname == b'lo':
            try:
                ip = get_ip_address(ifname)
            except OSError as err:
                ip = None
            
            break

    app.run(host='localhost', port=5000, debug=True)