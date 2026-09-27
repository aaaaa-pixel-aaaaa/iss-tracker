import numpy as np
from astropy.time import Time
from astropy.coordinates import EarthLocation
from sgp4.api import Satrec
import math

psi = float(-33) #lat, update specificity later
rad_psi = np.deg2rad(psi)
long = float(151) #long, update specificity later
f = float(1 / 298.26)
C = float(1 / np.sqrt(1+f*(f-2)*(np.sin(rad_psi)**2)))
S = float(1-f)**2*C
a = 6378.135
t = Time.now()
tle1 = "1 25544U 98067A   26269.01266413  .00010261  00000-0  19655-3 0  9997" #remember to put this back to an input later
tle2 = "2 25544  51.6303 161.0895 0007829 186.0461 174.0434 15.48628597587381"
# I know its poor form to just blunty list all my variables upfront, I'll clean the code down the line
time = Time(t, location=EarthLocation(lat=psi, lon=long))
lst = time.sidereal_time('apparent')
theta = lst.radian
x_ob = a*C*np.cos(rad_psi)*np.cos(theta)
y_ob = a*C*np.sin(theta)*np.cos(rad_psi)
z_ob = a*S*np.sin(rad_psi)
jd1 = t.jd1
jd2 = t.jd2
sat = Satrec.twoline2rv(tle1, tle2)
e, sat_pos, v = sat.sgp4(jd1, jd2)
x_sat, y_sat, z_sat = sat_pos
relx = x_sat - x_ob
rely = y_sat - y_ob
relz = z_sat - z_ob
S = np.sin(rad_psi)*np.cos(theta)*relx+np.sin(rad_psi)*np.sin(theta)*rely-np.cos(rad_psi)*relz
E = -np.sin(theta)*relx+np.cos(theta)*rely
Z = np.cos(rad_psi)*np.cos(theta)*relx + np.cos(rad_psi)*np.sin(theta)*rely+np.sin(rad_psi)*relz
range = np.sqrt(S**2+E**2+Z**2)
elevation = np.rad2deg(np.arcsin(Z / range))
azimuth = np.rad2deg(np.arctan2(-E, S))

print(elevation, azimuth)