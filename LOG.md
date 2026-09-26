## 21/9/2026  2.5hrs
Finalised repo setup and began work on coordinate translation math. Used Dr T.S. Kelso's articles on CelesTrak (Orbital
Coordinate Systems Series). Completed equations under spherical assumption, next will move onto oblate spheroid math.

## 21/9/2026 1hr (Late)
Picked it back up later. Finished coordinate translation equation for an oblique spheroid. Next move is twofold; start 
tinkering around in python for coding coordinates/positional stuff, and work on velocity (need to figure out maximum 
angular speed for ISS).

## 23/9/2026 0.5hrs
Didn't have much time today so just did some research on how to properly pull ISS coords. Currently thinking I'll 
utilise SGP4 for ECI coords, then handwrite a script to convert to elevation and azimuth from Sydney. SGP4 requires the
TLE set though, will need to figure how to update it hands-free. Next is work on code.

## 26/9/2026 2hrs
Wrote the code for finding elevation/azimuth from Sydney, completely handwritten. Needs quite a bit of streamlining and 
cleaning though, is pretty inefficient as-is. This first session can be found in "preliminary_code.py". Spoke to a 4th 
year mech student this morning who gave me some great advice on motor schematics; researching that is what comes next.