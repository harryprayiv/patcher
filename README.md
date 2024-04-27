# Python Script for Generating Patch Lists

This branch is dedicated to the reverse engineering and generation of a valid GMA2 patch file for use in the context of a rigging programmer.  I Intend to build a tool that can accomplish many of the tasks associated with my job without having to bring my computer or an expensive board.  I want to be able to hand a programmer a showfile that contains the entire patchlist, appropriately named and tagged on the fly from my smartphone.  I want this tool to be free, open source, and device agnostic for each of the programmers that may need this functionality wherever it may pop up.  

cli usage:

Input:
``python patcher.py --universe 1 --start_dmx 1 --fixture_start 2001 --quantity 16 --width 18 --mode "Mode 6" --name_prefix "Vortex"``

Output:
``[
    {
        "Name": "Vortex 2001",
        "Fixture": 2001,
        "Universe.DMXstart": "1.001",
        "Universe.DMXend": "1.018",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2002",
        "Fixture": 2002,
        "Universe.DMXstart": "1.019",
        "Universe.DMXend": "1.036",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2003",
        "Fixture": 2003,
        "Universe.DMXstart": "1.037",
        "Universe.DMXend": "1.054",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2004",
        "Fixture": 2004,
        "Universe.DMXstart": "1.055",
        "Universe.DMXend": "1.072",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2005",
        "Fixture": 2005,
        "Universe.DMXstart": "1.073",
        "Universe.DMXend": "1.090",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2006",
        "Fixture": 2006,
        "Universe.DMXstart": "1.091",
        "Universe.DMXend": "1.108",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2007",
        "Fixture": 2007,
        "Universe.DMXstart": "1.109",
        "Universe.DMXend": "1.126",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2008",
        "Fixture": 2008,
        "Universe.DMXstart": "1.127",
        "Universe.DMXend": "1.144",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2009",
        "Fixture": 2009,
        "Universe.DMXstart": "1.145",
        "Universe.DMXend": "1.162",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2010",
        "Fixture": 2010,
        "Universe.DMXstart": "1.163",
        "Universe.DMXend": "1.180",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2011",
        "Fixture": 2011,
        "Universe.DMXstart": "1.181",
        "Universe.DMXend": "1.198",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2012",
        "Fixture": 2012,
        "Universe.DMXstart": "1.199",
        "Universe.DMXend": "1.216",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2013",
        "Fixture": 2013,
        "Universe.DMXstart": "1.217",
        "Universe.DMXend": "1.234",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2014",
        "Fixture": 2014,
        "Universe.DMXstart": "1.235",
        "Universe.DMXend": "1.252",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2015",
        "Fixture": 2015,
        "Universe.DMXstart": "1.253",
        "Universe.DMXend": "1.270",
        "Width": 18,
        "Mode": "Mode 6"
    },
    {
        "Name": "Vortex 2016",
        "Fixture": 2016,
        "Universe.DMXstart": "1.271",
        "Universe.DMXend": "1.288",
        "Width": 18,
        "Mode": "Mode 6"
    }
]``

Input:
``python patcher.py --universe 1 --start_dmx 289 --fixture_start 2017 --quantity 16 --width 20 --mode "Profile 7" --name_prefix "S360"``

Output:
``[
    {
        "Name": "S360 2017",
        "Fixture": 2017,
        "Universe.DMXstart": "1.289",
        "Universe.DMXend": "1.308",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2018",
        "Fixture": 2018,
        "Universe.DMXstart": "1.309",
        "Universe.DMXend": "1.328",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2019",
        "Fixture": 2019,
        "Universe.DMXstart": "1.329",
        "Universe.DMXend": "1.348",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2020",
        "Fixture": 2020,
        "Universe.DMXstart": "1.349",
        "Universe.DMXend": "1.368",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2021",
        "Fixture": 2021,
        "Universe.DMXstart": "1.369",
        "Universe.DMXend": "1.388",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2022",
        "Fixture": 2022,
        "Universe.DMXstart": "1.389",
        "Universe.DMXend": "1.408",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2023",
        "Fixture": 2023,
        "Universe.DMXstart": "1.409",
        "Universe.DMXend": "1.428",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2024",
        "Fixture": 2024,
        "Universe.DMXstart": "1.429",
        "Universe.DMXend": "1.448",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2025",
        "Fixture": 2025,
        "Universe.DMXstart": "1.449",
        "Universe.DMXend": "1.468",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2026",
        "Fixture": 2026,
        "Universe.DMXstart": "1.469",
        "Universe.DMXend": "1.488",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2027",
        "Fixture": 2027,
        "Universe.DMXstart": "1.489",
        "Universe.DMXend": "1.508",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2028",
        "Fixture": 2028,
        "Universe.DMXstart": "2.001",
        "Universe.DMXend": "2.020",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2029",
        "Fixture": 2029,
        "Universe.DMXstart": "2.021",
        "Universe.DMXend": "2.040",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2030",
        "Fixture": 2030,
        "Universe.DMXstart": "2.041",
        "Universe.DMXend": "2.060",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2031",
        "Fixture": 2031,
        "Universe.DMXstart": "2.061",
        "Universe.DMXend": "2.080",
        "Width": 20,
        "Mode": "Profile 7"
    },
    {
        "Name": "S360 2032",
        "Fixture": 2032,
        "Universe.DMXstart": "2.081",
        "Universe.DMXend": "2.100",
        "Width": 20,
        "Mode": "Profile 7"
    }
]``