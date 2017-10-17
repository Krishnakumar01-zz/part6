def json_encode(data):
	'''implements the json code'''
	if isinstance(data, bool):
        	if data:
            		return "true"
        	else:
            		return "false"
    	elif isinstance(data, (int, float)):
        	return str(data)
    	elif isinstance(data, str):
        	return '"' + escape_string(data) + '"'
    	elif isinstance(data, list):
        	return "[" + ", ".join(json_encode(d) for d in data) + "]"
	elif isinstance(data,dict):
		return "{" + ",".join(json_encode(i)+":" + json_encode(j) for i,j in data.items())+ "}"
	else:
        	raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s


a={'x':1,'y':2,'z':3}
print(json_encode(a))
