# Spotify Data Science Project: 2021 Streaming History EDA

## This project is an exploratory data analysis into my Spotify streaming history for 2021. The goals of this project were to collect my own data, run an analysis with interactive charts, and find areas of optimization within my listening history.

## I request that anyone viewing my ipynb file should do so in a google colab or jupyter notebook to experience the interactive charts!

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
![Image 1]('readme images/newplot.png')
![Image 2]('readme images/artist_wc.png')
![Image 3]('readme images/newplot (1).png')
![Image 4]('readme images/newplot (2).png')
![Image 5]('readme images/newplot (3).png')
![Image 6]('readme images/newplot (4).png')
![Image 7]('readme images/newplot (5).png')
![Image 8]('readme images/newplot (6).png')


## Next Steps:
After performing an EDA on my streaming history for 2021, it was clear that there is a high skip percentage in my streams. The majority of my streams are skipped and with the goal in mind to reduce skip percentage and increase listening time, I have decided to pursue another project to meet my listening goals.

This next project will be an unsupervised learning project to cluster my saved songs into groups which can then be used to create playlists in my Spotify account. This will help meet my goal of maximizing listening time through the hypothesis that having playlists based on types of songs would allow me to narrow down my listening to be based on my mood but still allow me to have enough of my songs to shuffle through. Stay tuned for this next project on my github!

