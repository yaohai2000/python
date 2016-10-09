import cgi
import yate
import athletemodle

form_data=cgi.FieldStorage()
athlete_name=form_data['which_athlete'].value
athlete=athletemodle.get_from_store()[athlete_name]
print(yate.start_response())
print(yate.include_header(athlete_name + " 's timing: " + "  " + athlete.dob))
print(yate.u_list(athlete.top3()))

the_links={"Home":"/index.html","Choose another athlete":"/cgi-bin/generate_list.py"}
print(yate.include_footer(the_links))
