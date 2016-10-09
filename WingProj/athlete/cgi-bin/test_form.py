import yate

print(yate.start_response("text/html"))
print(yate.do_form("add_timing_data.py",{"TimeValue":"80"},text="Send"))