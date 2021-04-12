import csv;
rows = []
with open("main.csv","r") as file:
    read = csv.reader(file)
    for r in read:
        rows.append(r)
planet_data_rows = rows[1:]
planet_mass = []
planet_radius = []
planet_names = []
for datas in planet_data_rows:
    planet_mass.append(datas[4])
    planet_radius.append(datas[5])
    planet_names.append(datas[2])
def g(m,r,nm):
    Gravity = []
    for index in enumerate(nm):
        g = (float(m[index])*5.972e+24) / (float(r[index])*float(r[index])*6371000*6371000) * 6.674e-11
        Gravity.append(g)
    print(Gravity)
g(planet_mass,planet_radius,planet_names)