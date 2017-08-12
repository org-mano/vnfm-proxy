from cloudify.workflows import ctx
from cloudify.workflows import parameters as p

ctx.logger.info('Get command : {0}'.format(p.command))

for node in ctx.nodes:
    for instance in node.instances:
        instance.execute_operation('custom.do_command', kwargs={'command': p.command})
