"""
  ITSC 1212 - Putting the pieces together! #2
"""
######################################################
#            |\
#     -------|-\\-----
#     ------0---\|----
#     -----------|----
#     -----------0-----
######################################################

'''
    Reads a CSV file containing information about songs and returns a list of songs,
     where each song is a sublist in the format [title, artist, duration].

    filename (string): The name of the CSV file to read.
    header (boolean): Indicates whether the file has a header row that should be skipped.
'''
import csv
 
def load_data(filename, header):
    playlist = [ ]  # Initialize an empty list to store song data
    file_ref = open(filename, 'r')  # Open the file for reading

    # If there is a header row, skip it
    if header:
        file_ref.readline()  # Skip the header line by reading it and doing nothing with it

    # Read each line (song) in the file
    for info in file_ref:
        row = info.strip().split(",")  # Remove any surrounding whitespace and split by comma
        title = row[0]                 # First column is the song title
        artist = row[1]                # Second column is the artist name
        rank = int(row[2])         # Third column is the rank, converted to integer
        playlist.append([title, artist, rank])  # Append song data as a sublist
        
    file_ref.close()
    return playlist   # Return the list of songs


def display_menu():
    """
    Displays the menu options to the user.
    """
    #TODO: Print the menu options to the user.
    print('Menu: \n 1. Show song by rank \n 2. Show top 10 songs \n 3. Show top 20 songs \n 4. Quit')

    
def get_user_choice(songs):
    get_user_quit = True
    while get_user_quit:
       user_input = int(input('enter the number for your menu item: '))
       if user_input == 1:
          with open('/Users/Berha/OneDrive/Desktop/csv/songs.csv', 'r') as f:
             new_playlist = []
             rank_input = int(input('enter a random intger to display song rank: '))
             f.readline()
             for info in f:
                row = info.strip().split(",") 
                title = row[0]                
                artist = row[1]                
                rank = int(row[2]) 
                new_playlist.append([title, artist, rank]) 
                for songs in new_playlist:
                   sorted_list = sorted(new_playlist, key=lambda rank: rank[2]) 
          print(f'the song that is ranked in the {rank_input} place is {sorted_list[rank_input - 1][0]} by {sorted_list[rank_input - 1][1]} ')
       elif user_input == 2:
           with open('/Users/Berha/OneDrive/Desktop/csv/songs.csv', 'r') as newfile:
              top_n = 10
              new_playlist = []
              sorted_list = []
              newfile.readline()
              for info in newfile:
                 row = info.strip().split(",") 
                 title = row[0]                
                 artist = row[1]                
                 rank = int(row[2]) 
                 new_playlist.append([title, artist, rank]) 
                 for song in new_playlist:
                    sorted_list = sorted(new_playlist, key=lambda rank: rank[2]) 
           print(f'Here is the rank list ranging from {top_n}: {sorted_list[:top_n]}')
       elif user_input == 3:
          with open('/Users/Berha/OneDrive/Desktop/csv/songs.csv', 'r') as newfile:
              top_n = 20
              new_playlist = []
              sorted_list = []
              newfile.readline()
              for info in newfile:
                 row = info.strip().split(",") 
                 title = row[0]                
                 artist = row[1]                
                 rank = int(row[2]) 
                 new_playlist.append([title, artist, rank]) 
                 for song in new_playlist:
                    sorted_list = sorted(new_playlist, key=lambda rank: rank[2]) 
          print(f'Here is the rank list ranging from {top_n}: {sorted_list[:top_n]}')
       elif user_input == 4:
          get_user_quit == False
          print('Thank you for using our services')
          break          
       else:
          print('Invalid Option')
          
          
def add_list(songs):
 with open(songs , 'r') as file_output:
    new_playlist = []
    sorted_list = []
    readfile = file_output.readline()
    for info in file_output:
      row = info.strip().split(",") 
      title = row[0]                
      artist = row[1]                
      rank = int(row[2]) 
      new_playlist.append([title, artist, rank]) 
      for song in new_playlist:
        sorted_list = sorted(new_playlist, key=lambda rank: rank[2])
    ask_user = input('Do you want to store the list in accending or decending order? (put + for accending or - for decending): ')
    if ask_user == ('+'):
       with open('top_ranked_songs.csv', 'w+') as file_input:
        input_file = csv.writer(file_input)
        input_file.writerow(readfile.split())
        input_file.writerows(sorted_list)
    if ask_user == ('-'):
       with open('top_ranked_songs.csv', 'w+') as file_input:
        reversed_list = sorted_list.reverse()
        input_file = csv.writer(file_input)
        input_file.writerow(readfile.split())
        input_file.writerows(sorted_list)         
          
          
   
    
"""
Main logic to run the Song Management Application.

The logic should:
1. Load the songs from the CSV file.
2. Display the menu and prompt the user to select an option.
3. Call the appropriate function based on the user’s choice.
4. Keep displaying the menu until the user chooses to quit.
"""
# TODO: Load the songs by calling load_data()
load_data('/Users/Berha/OneDrive/Desktop/csv/songs.csv', True)

# TODO: Implement a loop to keep displaying the menu until the user chooses to quit
# - Call display_menu() to show the menu options
# - Get the user's choice with get_user_choice()
display_menu()
get_user_choice('/Users/Berha/OneDrive/Desktop/csv/songs.csv')

add_list('/Users/Berha/OneDrive/Desktop/csv/songs.csv')