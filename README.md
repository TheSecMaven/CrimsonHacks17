# CrimsonHacks17

![alt text](/Atrocious_Apartments.png "Logo Title Text 1")
## Check it Out!
Visit our website (https://atrociousapartments.com/)

## Inspiration
When you begin your search for the perfect apartment, you can view information about the security of inside the apartment. However, there isn't a way to view the surrounding area of the apartment, until now! With our hack you can select an apartment and view the crime around the area. They can see a description of what happened as well as when it happened. In addition, we have allowed for the viewing of nearby construction, through the use of building permits, for those of us who take the 2-5 daily nap and have a deep distaste for construction noise/ traffic problems. All of our data came from Tuscaloosa's Open Data Portal (https://data.tuscaloosa.com/). All of these things make the apartment hunting experience much simpler, and allows students to get all of the information that goes into an apartment decision much easier.

## What it does
Upon entrance to our site, the user is able to view all apartments in a given city on a Google map. From here, the user is able to view all building permits and crime data in the area. They can then click on individual apartment complexes and view the crimes that occurred within a .25 mile radius as well as the construction permits within a .20 mile radius. Furthermore, upon click the view shrinks down to only the relevant building permits and crime data, to provide a clearer viewpoint for the user.

## How we built it
We built it on a Amazon EC2 Ubuntu Server running Apache using Flask. We used the Google Maps API to show the data for apartment locations and compared it with area crime statistics and building construction permits. To export our data that we needed we created json files from python scripts. We also used Geopy to geocode all of the addresses that came off of the open data portal. We also used vincenty to calculate distances between the latitude and longitude of all events, so you can see what crimes and construction that are relevant to a given apartment complex.

## Challenges we ran into
We had a problem with how bad the data we exported was and cleaning it up for what we needed. Tuscaloosa's portal proved more than difficult in garnering all relevant information. All apartment complexes were obtained from offcampushousing.ua.edu, which also proved difficult. When we pulled the data we couldn't figure out which permits were active and nonactive.  Another issue we had was configuring apache to work with flask.

## Accomplishments that we're proud of
This is a very relevant tool for a college community. Not only does it help parents search for apartments that are historically safe, but it allows for more personalized decisions when picking an apartment. This web app also has the potential to spur positive change, in that a complex that has countless crimes/building permits in the nearby area might be encouraged to improve their standards to better meet the demands of apartment renters. Ultimately this tool simplifies a very complicated searching process, and allows for the visualization of important data that was previously difficult to access/discern.

## What we learned
* How to set up and debug apache.
* How to attach a domain name to a EC2 instance.
* Exporting data as a json file.
* Cleaning data is very difficult. "lol"

## What's next for Atrocious Apartments
* The incorporation of  311 call data is our next big feature. 311 calls that are placed within a certain radius of an apartment complex that refer to things such as trash, rats, or cockroaches could prove to be something that apartment hunters want to be informed about before they make a decision.
* Adding the ability for customization of preferences. Perhaps some users are more cautious and want a wider crime data radius around their complex of choice; or maybe users have an outrageous fear of cockroaches and can't handle a single report of roaches in the area. This, among other things, are our future goals.
* The implementation of a login system for users to save certain apartments, download data on an apartment, and even customize their preferences for construction/crime and, eventually, 311 call data.
