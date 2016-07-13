import redis
import mdl_shl1_msg_pb2
import mdl_szl1_msg_pb2

def mdl_time_str(x):
	return "%02d:%02d:%02d.%03d" % (x % 1000000000 / 10000000, x % 10000000 / 100000, x % 100000 / 1000, x % 1000)

def mdl_float_str(x):
	return "%f" % (x.Value / float(x.DecimalShift))

def on_shl1_indexes_msg(data):
        msg = mdl_shl1_msg_pb2.Indexes()
	msg.ParseFromString(data)
	print "%s XSHG.%s %s: %s" % (mdl_time_str(msg.UpdateTime), msg.IndexID, msg.IndexName, mdl_float_str(msg.LastIndex))
	return None

def on_shl1_equity_msg(data):
	msg = mdl_shl1_msg_pb2.Equity()
       	msg.ParseFromString(data)
        print "%s XSHG.%s %s: %s" % (mdl_time_str(msg.UpdateTime), msg.SecurityID, msg.SecurityName, mdl_float_str(msg.LastPrice))
	return None

def on_szl1_stock_msg(data):
	msg = mdl_szl1_msg_pb2.SZL1Stock()
        msg.ParseFromString(item['data'])
        print "%s XSHE.%s %s: %s" % (mdl_time_str(msg.UpdateTime), msg.SecurityID, msg.SecurityName, mdl_float_str(msg.LastPrice))
	return None

print "connect to redis..."
r = redis.Redis(host='feeder01-dev.datayes.com', port=9379, db=0) 
if r.execute_command('auth', 'mytoken') :
        print "redis auth succeeded"
else :
        print "redis auth failed"
        sys.exit()
p = r.pubsub()
p.subscribe(['mdl.3.3.000001', 'mdl.3.4.603600', 'mdl.5.2.*', 'mdl.2.4.*'])
print "receiving message..."
for item in p.listen():
	if str(item['type']) == 'message':
		channel = str(item['channel'])
		if channel[0:8] == "mdl.3.3.":
			on_shl1_indexes_msg(item['data'])
		elif channel[0:8] == "mdl.3.4.":
                        on_shl1_equity_msg(item['data'])
		elif channel[0:8] == "mdl.5.2.":
                        on_szl1_stock_msg(item['data'])
		elif channel[0:8] == "mdl.2.4.":
			print "heart beat"                        
		else:
			print "unknown channel: %s" % (channel)
