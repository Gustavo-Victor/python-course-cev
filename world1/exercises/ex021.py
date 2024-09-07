import pygame; 

# init game
pygame.init();

# load audio 
pygame.mixer.music.load("../assets/audios/desafinado.mp3"); 

# play audio
pygame.mixer.music.play(); 

# fix bugs
input(); 

# wait audio finish to stop executing the program
pygame.event.wait(); 