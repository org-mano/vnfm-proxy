
from cloudify import ctx
from cloudify.state import ctx_parameters as p
from requests import put, get, post, delete
vnfm_ip = '10.20.0.14'

#ctx.instance.runtime_properties['touched'] = p.touched_value
ctx.logger.info('Call do_command.py, command = {0}'.format(p.command))
ctx.logger.info('send command to vnfm')

if p.command == 'InstantiateVnf':
    resp = post('http://'+vnfm_ip+':5000/v1/vnfs', data={'vnfoid':'01234567', 'vnfmid':'12345678', 'vnfd':'sftp://vnfusr:vnfpswd@12.3.1.205/opt/vnf/zte-imsv4.10.10', 'vnfurl':'sftp://vnfusr:vnfpswd@12.3.1.205/opt/vnf/zte-imsv4.10.10/'})

elif p.command == 'QueryNfvOne':
    resp = get('http://' + vnfm_ip + ':5000/v1/vnfs/1222')

elif p.command == 'QueryNfvAll':
    resp = get('http://' + vnfm_ip + ':5000/v1/vnfs')

elif p.command == 'ScaleVnf':
    resp = put('http://'+vnfm_ip+':5000/v1/vnfs/100/scale', data={'nfvoid':'111', 'vnfmid':'222', 'scaletype':'1'})

elif p.command == 'UpdateVnf':
    resp = put('http://'+vnfm_ip+':5000/v1/vnfs/100/update', data={'nfvoid':'111', 'vnfmid':'222', 'VNFInstanceID':'1', 'VNFSoftwareVersion':'v2.3', 'vnfd':'<root/>', 'VNFGOSImageURL':'sftp://vnfusr:vnfpswd@12.3.1.205/opt/vnf/zte-imsv4.10.10/', 'VNFSoftwareURL':'sftp://vnfusr:vnfpswd@12.3.1.205/opt/vnf/zte-imsv4.10.10/'})

elif p.command == 'TerminateVnf':
    resp = delete('http://' + vnfm_ip + ':5000/v1/vnfs/1')
    
elif p.command == 'GetJobStatus':
    resp = get('http://' + vnfm_ip + ':5000/v1/jobs/1')

else:
    resp = {'msg': 'unknown command: ' + p.command}

ctx.logger.info(resp.json())
