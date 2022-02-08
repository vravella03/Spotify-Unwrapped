# Spotify Data Science Project: 2021 Streaming History EDA

## This project is an exploratory data analysis into my Spotify streaming history for 2021. The goals of this project were to collect my own data, run an analysis with interactive charts, and find areas of optimization within my listening history.

### I request that anyone viewing my ipynb file should download and open it in a google colab or jupyter notebook to experience the interactive charts!

### Steps Completed in Project:
- Requested streaming history from Spotify (Spotify allow you to request your streaming history for 1 year)
- Used trackIds from streaming history json files to access Spotify API and extract audio features
- Analysed trends in listening history and produced interactive charts
- Brainstormed solutions for optimized listening which led to next project (Unsupervised Learning)

## Findings:
- ~71% of my streams are skipped.
- The goal for my Spotify listening, in the future, is to reduce skipped percentage and maximize listening.
- I've streamed 636 unique artists and 2130 unique songs.
- My most streamed artists were Drake, Travis Scott, Kanye West, ASAP Rocky and Post Malone.
- The artists I skipped the most were Lil Uzi Vert and XXXTentacion.
- My most listened to songs were Laugh Now Cry Later, Forever, and The Bigger Picture.
- The songs I skipped the most are Mo Bamba and Myself.
- I tend to skip less popular songs than more popular songs, on average.
- All of my top 10 songs had an average listen percentage of ~50% or higher.
- I spent more time listening to Donda by Kanye West than Certified Lover Boy by Drake.
- I listened to music the most at night.
- I listened to a stream for longer, on average, in the mornings and on the weekends.

## Some cool charts:
![Image 1](https://github.com/vravella03/Spotify-Unwrapped/blob/main/readme%20images/newplot.png)
![Image 2](https://github.com/vravella03/Spotify-Unwrapped/blob/main/readme%20images/artist_wc.png)
![Image 3](https://github.com/vravella03/Spotify-Unwrapped/blob/main/readme%20images/newplot%20(1).png)
![Image 4](https://github.com/vravella03/Spotify-Unwrapped/blob/main/readme%20images/newplot%20(2).png)
![Image 5](https://github.com/vravella03/Spotify-Unwrapped/blob/main/readme%20images/newplot%20(3).png)
![Image 6](https://github.com/vravella03/Spotify-Unwrapped/blob/main/readme%20images/newplot%20(4).png)
![Image 7](https://github.com/vravella03/Spotify-Unwrapped/blob/main/readme%20images/newplot%20(5).png)
![Image 8](https://github.com/vravella03/Spotify-Unwrapped/blob/main/readme%20images/newplot%20(6).png)


## Next Steps:
After performing an EDA on my streaming history for 2021, it was clear that there is a high skip percentage in my streams. The majority of my streams are skipped and with the goal in mind to reduce skip percentage and increase listening time, I have decided to pursue another project to meet my listening goals.

This next project will be an unsupervised learning project to cluster my saved songs into groups which can then be used to create playlists in my Spotify account. This will help meet my goal of maximizing listening time through the hypothesis that having playlists based on types of songs would allow me to narrow down my listening to be based on my mood but still allow me to have enough of my songs to shuffle through. Stay tuned for this next project on my github!

## Resources

Thanks to all of these articles and people that have made this project much easier to do!

- https://www.section.io/engineering-education/spotify-python-part-1/
- https://medium.com/@rafaelnduarte/how-to-retrieve-data-from-spotify-110c859ab304
- https://github.com/rafaelnduarte/Spotify_K-Means_Clustering/blob/master/Spotify_Clulstering.ipynb
- https://towardsdatascience.com/spotify-data-project-part-1-from-data-retrieval-to-first-insights-f5f819f8e1c3
- https://medium.com/web-mining-is688-spring-2021/preliminary-data-analysis-on-spotify-data-using-api-a84bb0aae00c
- https://datascientistdiary.com/index.php/2021/03/04/how-to-use-spotify-api-and-what-data-science-opportunities-can-it-open-up/
- https://jovian.ai/odiesta/spotify-streaming-history-exploratory-data-analysis-project
- https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b
