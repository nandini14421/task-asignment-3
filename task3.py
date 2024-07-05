import lyricsgenius
api_key="IwyCis0QFvqjl94X-zB4BnFED4uOkhMqt-RG6K_Pn0wRwMs1sYuAYk3yoVGPV1Md"
genius = lyricsgenius.Genius(api_key) 
name = input("enter atrist name: ")
artist =genius.search_artist(name)
song = input("type your song for lyrics : ")
song = artist.song(song)
print(song.lyrics)