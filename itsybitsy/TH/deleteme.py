import signalfx

sfx = signalfx.SignalFx()

program = "data('cpu.utilization').mean().publish()"
with signalfx.SignalFx().signalflow('SOME-TOKEN') as flow:
    print('Executing {0} ...'.format(program))
    computation = flow.execute(program)
    for msg in computation.stream():
        if isinstance(msg, signalfx.signalflow.messages.DataMessage):
            print('{0}: {1}'.format(msg.logical_timestamp_ms, msg.data))
        if isinstance(msg, signalfx.signalflow.messages.EventMessage):
            print('{0}: {1}'.format(msg.timestamp_ms, msg.properties))