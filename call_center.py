from datetime import datetime

class Call(object):
    unique_id = 1000
    def __init__(self, caller_name, call_number, reason):
        self.caller_name = caller_name
        self.call_number = call_number
        self.time_of_call = datetime.now()
        self.reason = reason

        Call.unique_id += 1

    def display(self):
        print "ID: " + str(Call.unique_id)
        print "Caller Name: " + self.caller_name
        print "Call Number: " + self.call_number
        print "Time of call: " + self.time_of_call
        print "Reason for call: " + self.reason
        return self


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.queue_size()

    def queue_size(self):
        return len(self.calls)

    def add_call(self, obj):
        self.calls.append(obj)
        print self.calls

    def remove_call(self):
        if self.queue_size > 0:
            self.calls.remove([0])
        else:
            print "none to remove"

    def info(self):
        for attr,val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)



index_call_1 = Call('Jane Doe', '213-555-5555','wrong number...thought it was Pizza Hut')

Dojo_Call_Center = CallCenter()

Dojo_Call_Center.add_call(index_call_1)