# Python Script for Generating Patch Lists


cli usage:

Input:
``python patcher.py --universe 1 --start_dmx 1 --fixture_start 2001 --quantity 16 --width 18 --mode "Mode 6" --name_prefix "Vortex"``

Output:
``Name, Fixture, Channel, Universe.DMXchannelStart, Universe.DMXchannelEnd, Width Mode
Vortex 2001, 2001, 2001, 1.001, 1.018, 18 "Mode 6"
Vortex 2002, 2002, 2002, 1.019, 1.036, 18 "Mode 6"
Vortex 2003, 2003, 2003, 1.037, 1.054, 18 "Mode 6"
Vortex 2004, 2004, 2004, 1.055, 1.072, 18 "Mode 6"
Vortex 2005, 2005, 2005, 1.073, 1.090, 18 "Mode 6"
Vortex 2006, 2006, 2006, 1.091, 1.108, 18 "Mode 6"
Vortex 2007, 2007, 2007, 1.109, 1.126, 18 "Mode 6"
Vortex 2008, 2008, 2008, 1.127, 1.144, 18 "Mode 6"
Vortex 2009, 2009, 2009, 1.145, 1.162, 18 "Mode 6"
Vortex 2010, 2010, 2010, 1.163, 1.180, 18 "Mode 6"
Vortex 2011, 2011, 2011, 1.181, 1.198, 18 "Mode 6"
Vortex 2012, 2012, 2012, 1.199, 1.216, 18 "Mode 6"
Vortex 2013, 2013, 2013, 1.217, 1.234, 18 "Mode 6"
Vortex 2014, 2014, 2014, 1.235, 1.252, 18 "Mode 6"
Vortex 2015, 2015, 2015, 1.253, 1.270, 18 "Mode 6"
Vortex 2016, 2016, 2016, 1.271, 1.288, 18 "Mode 6"``

Input:
``python patcher.py --universe 1 --start_dmx 289 --fixture_start 2017 --quantity 16 --width 20 --mode "Profile 7" --name_prefix "S360"``

Output:
``Name, Fixture, Channel, Universe.DMXchannelStart, Universe.DMXchannelEnd, Width Mode
S360 2017, 2017, 2017, 1.289, 1.308, 20 "Profile 7"
S360 2018, 2018, 2018, 1.309, 1.328, 20 "Profile 7"
S360 2019, 2019, 2019, 1.329, 1.348, 20 "Profile 7"
S360 2020, 2020, 2020, 1.349, 1.368, 20 "Profile 7"
S360 2021, 2021, 2021, 1.369, 1.388, 20 "Profile 7"
S360 2022, 2022, 2022, 1.389, 1.408, 20 "Profile 7"
S360 2023, 2023, 2023, 1.409, 1.428, 20 "Profile 7"
S360 2024, 2024, 2024, 1.429, 1.448, 20 "Profile 7"
S360 2025, 2025, 2025, 1.449, 1.468, 20 "Profile 7"
S360 2026, 2026, 2026, 1.469, 1.488, 20 "Profile 7"
S360 2027, 2027, 2027, 1.489, 1.508, 20 "Profile 7"
S360 2028, 2028, 2028, 2.001, 2.020, 20 "Profile 7"
S360 2029, 2029, 2029, 2.021, 2.040, 20 "Profile 7"
S360 2030, 2030, 2030, 2.041, 2.060, 20 "Profile 7"
S360 2031, 2031, 2031, 2.061, 2.080, 20 "Profile 7"
S360 2032, 2032, 2032, 2.081, 2.100, 20 "Profile 7"``