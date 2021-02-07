View it in action at gwrisk.tech

# Hacklytics 2021

## Inspiration
On January 27th, 2021, the Pentagon declared climate change a national security issue--this shows the sheer importance of the issue at hand and how it impacts various aspects of our lives.
The impact isn’t just at the global and national level. Each location will have different risks to account for.
With so much data and areas of impact, it’s hard to know what your local level concerns should be.

How do you do anything to prepare and lesson the impact if you don’t know how it’s going to impact you locally. There are many visualizations out there showing that climate change is real and that it will fundamentally change many areas of the country and world, but they don’t make it easy for local areas to know what specifically they should be focused on. gwRisk is designed as a planning tool which helps counties (and the people who live in them) understand the risks specific to them. Once they understand what their local risks are, they can better focus on being prepared for them before the problems hit.

## What it does
gwRisk outputs information about a specific county the user that can help the user in global warming planning.
## How we built it
We used pandas, numpy, and mathplotlib to clean, combine, and visualize different data, all in Google Colab. We used flask to serve our data into a website as well.
## Challenges we ran into
The challenges we ran into is that of our teammates had an emergency, so we had to find a replacement. Another challenge was deploying the website and making sense of the various data sets.
## Accomplishments that we're proud of

## What we learned
We learned about data cleaning and visualization.
## What's next for gwRisk
There are a few items from the jupyter notebook that didn't get added to the webpage yet. Once they are added then people can start their local preparations. After that we would like to add some secondary risks to supplement the direct risks so each county can have even more areas to be aware of and prepare for.
## Resources
CSV and Excel files used are from:
http://www.globalpolicy.science/econ-damage-climate-change-usa
_italics_This file contains median damages for each sector shown in Fig 2 of the main article (agriculture, mortality, energy, low-risk labor, high-risk labor, coastal damages, property crime, violent crime, total damages).  These impacts are the central estimate for average annual damage during 2080-2099 under a business-as-usual scenario (RCP8.5). UPDATE: This file has been updated (6/26/17) to include avg county income and population in 2012, as well as to replace 4 missing values._italics_

http://www.impactlab.org/map/#usmeas=absolute&usyear=2020-2039&gmeas=absolute&gyear=1986-2005

https://hazards.geoplatform.gov/portal/apps/MapSeries/index.html?appid=ddf915a24fb24dc8863eed96bc3345f8 (2020 Data)

http://www.impactlab.org/map/#usmeas=absolute&usyear=2020-2039&gmeas=absolute&gyear=1986-2005
