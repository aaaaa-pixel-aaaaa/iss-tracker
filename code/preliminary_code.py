import numpy as np
from astropy.time import Time
from astropy.coordinates import EarthLocation
from sgp4.api import Satrec
import math

psi = float(-33.87) #lat
rad_psi = np.deg2rad(psi)
long = float(151.27) #long
f = float(1 / 298.26)
C = float(1 / np.sqrt(1+f*(f-2)*(np.sin(rad_psi)**2)))
S = float(1-f)**2*C
a = 6378.135
t = Time.now()
tle1 = "1 25544U 98067A   26268.43198945  .00011731  00000-0  21853-3 0  9992" #remember to put this back to an input later
tle2 = "2 25544  51.6316 163.9608 0004776 179.9710 180.1280 15.49288785587293"
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



