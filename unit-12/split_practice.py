countries = "Nigeria, Ghana, Kenya, South Africa, Egypt"

date = "27/11/2026"

country_list = countries.split(",")

date_parts = date.split("/")

print("African Countries:")
print(country_list)

print("First Country:", country_list[0])
print("Second Country:", country_list[1])
print("Third Country:", country_list[2])
print("Fourth Country:", country_list[3])
print("Fifth country:", country_list[4])

print("Day:", date_parts[0])
print("Month:", date_parts[1])
print("year:", date_parts[2])

