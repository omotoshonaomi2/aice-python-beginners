name = "  nAOMI oMOTOSHO  "
country = "  nIGERIA   "

clean_name = name.strip().title()
clean_country = country.strip().title()

course = "History and Political Science"
clean_course = course.replace("Political Science", "International Relations")

print("Original name:", name)
print("Cleaned name:", clean_name)

print("Original country:", country)
print("Cleaned country:", clean_country)

print("Original course:", course)
print("Cleaned course:", clean_course)

