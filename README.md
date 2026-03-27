<img width="782" height="103" alt="image" src="https://github.com/user-attachments/assets/8a8e9030-6cd5-4b96-94b9-f5ceccc0d9ea" />**GraphHopper Route Planner**

&#x09;A Python-based Command Line Interface (CLI) tool that provides turn-by-turn navigation, distance, and travel time between two locations. It utilizes the GraphHopper Geocoding API to resolve location names and the Routing API to calculate the best path based on different vehicle profiles.


**Features**
* Geocoding: Convert city names or addresses into geographic coordinates.
* Multiple Profiles: Support for car, bike, and foot travel modes.
* Turn-by-Turn Directions: Detailed instructions for every leg of the journey.
* Dual Metrics: Displays distances in both Kilometer[GraphHopper Route Planner.md]
s (km) and Miles (mi).
* Smart Formatting: Calculates trip duration in a clean HH:MM:SS format.



Setup \& Installation

1\. Get your API Key

To use this application, you must have a GraphHopper API key:

1. Go to the GraphHopper Directions API Dashbaord.
2. Sign up for a free account or log in.
3. Navigate to the API Keys section and generate a new key.



2\. Configure the Project

1. Clone this repository to your local machine.
2. Create a file named config.py in the root directory.
3. Add your API key and the base URLs to config.py:

<img width="782" height="103" alt="image" src="https://github.com/user-attachments/assets/d10341a7-fc68-48e2-a76f-aa88a50e4ac0" />




3\. Install Dependencies

Ensure you have the requests library installed:

<img width="815" height="55" alt="image" src="https://github.com/user-attachments/assets/988ea058-b493-409d-b2d2-bd61c3ea9be7" />



**Usage**
Run the main application script:

<img width="820" height="59" alt="image" src="https://github.com/user-attachments/assets/58ca30b6-7e7d-47b0-aaf9-b23e86fc684e" />

Instructions:

1. Select Profile: Enter car, bike, or foot.
2. Input Locations: Enter your "Starting Location" and "Destination".
3. Review Trip: The script will output the total distance, estimated time, and specific directions.
4. Quit: Type q or quit at any prompt to exit.


