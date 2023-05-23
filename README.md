# Musical-Time-Machine

This Python script allows you to generate a playlist on Spotify containing the top 100 songs from the Billboard chart for a specific date.
It utilizes web scraping to extract the song titles and artist names from the Billboard chart and then searches for the corresponding tracks on Spotify using the Spotify API. Finally, it creates a new playlist on your Spotify account and adds the tracks to the playlist.
Prerequisites

Before running the script, make sure you have the following:

    Python 3 installed on your machine.
    Spotify developer account: You need to create a Spotify developer account and register a new application to obtain the client ID and client secret required for authentication.

Installation

    Clone this repository to your local machine or download the ZIP file.

    Navigate to the project directory.

    Install the required Python libraries by running the following command:

    pip install -r requirements.txt

    Set up environment variables:
        Rename the .env.example file to .env.
        Open the .env file and replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your actual Spotify client ID and client secret.

Usage

    Open a terminal or command prompt and navigate to the project directory.

    Run the following command to execute the script:

    python playlist_generator.py

    Enter the desired date in the format YYYY-MM-DD when prompted.

    The script will scrape the Billboard chart for that date, search for the corresponding tracks on Spotify, create a new playlist on your Spotify account, and add the tracks to the playlist.

    Once the process is complete, the script will print the snapshot ID of the playlist modification.

License

This project is licensed under the MIT License. Feel free to modify and use it according to your needs.
