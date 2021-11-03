import pygame
import os, inspect
import random
from pygame.transform import scale

#recherche du répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")


# Setup
pygame.init()

# Definition de plusieur couleurs
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
RED = (255, 0, 0, 255)
GREY = (30, 30, 30, 255)
LIGHTGREY = (200, 200, 200, 255)
CYAN = (0, 255, 255, 255)
YELLOW = (255, 255, 0, 255)

# Definition d'une Police
police = pygame.font.SysFont("Stencil", 50)
 
 
# Definition de la hauteur et la largeur de l'écran [width,height]
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((2*screenWidth,screenHeight))
 
pygame.display.set_caption("Empire City")
 
# Boucle jusqu'à ce que l'utilisateur clique sur le bouton de fermeture.
done = False
 
# Utilisé pour gérer la vitesse de mise à jour de l'écran
clock = pygame.time.Clock()
 
# Cache le curseur de la sourie
pygame.mouse.set_visible(True) 
 
#Definition du fond
fond = pygame.image.load(os.path.join(assets, "map.png"))
fond2 = pygame.image.load(os.path.join(assets, "map2.png"))
dead = pygame.image.load(os.path.join(assets, "dead.png"))
won = pygame.image.load(os.path.join(assets, "win.png"))
bord_gauche = pygame.image.load(os.path.join(assets, "bord_gauche.png"))
bord_droit = pygame.image.load(os.path.join(assets, "bord_droit.png"))
#Definition des sprite


#viseur
viseur = pygame.image.load(os.path.join(assets, "viseur.png"))
viseur2 = pygame.image.load(os.path.join(assets, "viseurj2.png"))
#bandit

bandit_mitraillette = []
for i in range(12):
   bandit_mitraillette.append(pygame.image.load(os.path.join(assets, "mitra_"+str(i)+".png")))
bandit_mitraillette_hitbox = []
for i in range(10):
   bandit_mitraillette_hitbox.append(pygame.image.load(os.path.join(assets, "mitra_"+str(i)+"_hitbox.png")))

bandit_salto= []
for i in range(7):
   bandit_salto.append(pygame.image.load(os.path.join(assets, "saltofinestra_"+str(i+1)+".png")))
bandit_salto_hitbox = []
for i in range(5):
   bandit_salto_hitbox.append(pygame.image.load(os.path.join(assets, "saltofinestra_"+str(i+1)+"_hitbox.png")))
bandit_salto_x = [794,1034,1513,1755,4544]
bandit_salto_y = [1058,1058,1058,1058,291]
bandit_salto_x_map2 = [4422,5086]
bandit_salto_y_map2 = [1056,1104]

bandit_window_gauche= []
for i in range(4):
   bandit_window_gauche.append(pygame.image.load(os.path.join(assets, "sbircia_finestra_sx_"+str(i+1)+".png")))
bandit_window_gauche_hitbox = []
for i in range(2):
   bandit_window_gauche_hitbox.append(pygame.image.load(os.path.join(assets, "sbircia_finestra_sx_"+str(i+1)+"_hitbox.png")))
bandit_window_gauche_x = [874,1161,1449,1737,874,1161,1449,1737]
bandit_window_gauche_y = [618,618,618,618,235,235,235,235]
bandit_window_gauche_x_map2 = [96,625,2451,1249,4470,4847]
bandit_window_gauche_y_map2 = [621,284,525,1095,1103,192]

bandit_car= []
for i in range(5):
   bandit_car.append(pygame.image.load(os.path.join(assets, "sportello_"+str(i+1)+".png")))
bandit_car_hitbox = []
for i in range(3):
   bandit_car_hitbox.append(pygame.image.load(os.path.join(assets, "sportello_"+str(i+1)+"_hitbox.png")))
bandit_car_x = 91
bandit_car_y = 1012
bandit_car_x_map2 = 1880
bandit_car_y_map2 = 1079

bandit_window2= []
for i in range(4):
   bandit_window2.append(pygame.image.load(os.path.join(assets, "tenda_"+str(i+1)+".png")))
bandit_window2_hitbox = []
for i in range(2):
   bandit_window2_hitbox.append(pygame.image.load(os.path.join(assets, "tenda_"+str(i+1)+"_hitbox.png")))
bandit_window2_x = [2295,2490,2685,2685,3261,4029,2880,3837,5514]
bandit_window2_y = [624,624,624,624,291,291,291,291,438]
bandit_window2_x_map2 = [142,2489,4893]
bandit_window2_y_map2 = [624,527,195]

bandit_egout= []
for i in range(4):
   bandit_egout.append(pygame.image.load(os.path.join(assets, "tombino_"+str(i+1)+".png")))
bandit_egout_hitbox = []
for i in range(2):
   bandit_egout_hitbox.append(pygame.image.load(os.path.join(assets, "tombino_"+str(i+1)+"_hitbox.png")))
bandit_egout_x = [378,2134,3894,5690]
bandit_egout_y = [1422,1414,1406,1410]
bandit_egout_x_map2 = [381,2691]
bandit_egout_y_map2 = [1384,1379]

bandit_femme= []
for i in range(4):
   bandit_femme.append(pygame.image.load(os.path.join(assets, "ostaggio_"+str(i+1)+".png")))
bandit_femme_hitbox = []
for i in range(2):
   bandit_femme_hitbox.append(pygame.image.load(os.path.join(assets, "ostaggio_"+str(i+1)+"_hitbox.png")))
   
bandit_coureur = []
for i in range(7):
   bandit_coureur.append(pygame.image.load(os.path.join(assets, "corsadx_"+str(i+1)+".png")))
bandit_coureur_hitbox = []
for i in range(5):
   bandit_coureur_hitbox.append(pygame.image.load(os.path.join(assets, "corsadx_"+str(i+1)+"_hitbox.png")))
bandit_coureur_x = 0
bandit_coureur_y = 1185

bandit_gros= []
for i in range(4):
   bandit_gros.append(pygame.image.load(os.path.join(assets, "big_"+str(i+1)+".png")))
bandit_gros_hitbox = []
for i in range(2):
   bandit_gros_hitbox.append(pygame.image.load(os.path.join(assets, "big_"+str(i+1)+"_hitbox.png")))
   
bandit_esquive= []
for i in range(5):
   bandit_esquive.append(pygame.image.load(os.path.join(assets, "finta_"+str(i+1)+".png")))
bandit_esquive_hitbox = []
for i in range(3):
   bandit_esquive_hitbox.append(pygame.image.load(os.path.join(assets, "finta_"+str(i+1)+"_hitbox.png")))

bandit_mince= []
for i in range(4):
   bandit_mince.append(pygame.image.load(os.path.join(assets, "inpiedi_"+str(i+1)+".png")))
bandit_mince_hitbox = []
for i in range(2):
   bandit_mince_hitbox.append(pygame.image.load(os.path.join(assets, "inpiedi_"+str(i+1)+"_hitbox.png")))
   
bandit_loin= []
for i in range(4):
   bandit_loin.append(pygame.image.load(os.path.join(assets, "lontano_"+str(i+1)+".png")))
bandit_loin_hitbox = []
for i in range(2):
   bandit_loin_hitbox.append(pygame.image.load(os.path.join(assets, "lontano_"+str(i+1)+"_hitbox.png")))
bandit_loin_x = [905,1197,1486]
bandit_loin_y = [666,666,666]
bandit_loin_x_map2 = [145,2494,4895]
bandit_loin_y_map2 = [670,574,235]

bandit_loin_2= []
for i in range(4):
   bandit_loin_2.append(pygame.image.load(os.path.join(assets, "lontanomancino_"+str(i+1)+".png")))
bandit_loin_2_hitbox = []
for i in range(2):
   bandit_loin_2_hitbox.append(pygame.image.load(os.path.join(assets, "lontanomancino_"+str(i+1)+"_hitbox.png")))
bandit_loin_2_x = [905,1197,1486]
bandit_loin_2_y = [666,666,666]
bandit_loin_2_x_map2 = [102,1678,2454,4848]
bandit_loin_2_y_map2 = [672,959,573,237]


#compteur pour affichage bandit
n=0
m=0
#tire
bang = []
for i in range(25):
   bang.append(pygame.image.load(os.path.join(assets, "esplosione_"+str(i+1)+".png")))
pan=0
pan2=0
#Definition des flèche
   #Joueur1
fleche_gauche = pygame.image.load(os.path.join(assets, "fleche_gauche.png"))
fleche_gauche_x = 40
fleche_gauche_y = 300-(fleche_gauche.get_height()/2)

fleche_droite = pygame.image.load(os.path.join(assets, "fleche_droite.png"))
fleche_droite_x = 760-(fleche_droite.get_width())
fleche_droite_y = 300-(fleche_droite.get_height()/2)
   #Joueur2
   
fleche_gauche2 = pygame.image.load(os.path.join(assets, "fleche_gauchej2.png"))
fleche_gauche2_x = 40
fleche_gauche2_y = 300-(fleche_gauche.get_height()/2)

fleche_droite2 = pygame.image.load(os.path.join(assets, "fleche_droitej2.png"))
fleche_droite2_x = 760-(fleche_droite.get_width())
fleche_droite2_y = 300-(fleche_droite.get_height()/2)

#evenement
death=False
loose=False
loose2=False
esquive=False
esquive2=False
win=False
win2=False

#BALLE
bullet = pygame.image.load(os.path.join(assets, "bullet.png"))
bullet_y = screenHeight-50

nbrball2=12
#Page d'accueil
thank = pygame.image.load(os.path.join(assets, "thank.png"))
message = pygame.image.load(os.path.join(assets, "message.png"))
titre_map1 = pygame.image.load(os.path.join(assets, "titre_map1.png"))
titre_map2 = pygame.image.load(os.path.join(assets, "titre_map2.png"))
titre_map1_2 = pygame.image.load(os.path.join(assets, "titre_map1_2.png"))
titre_map2_2 = pygame.image.load(os.path.join(assets, "titre_map2_2.png"))
joueur = pygame.image.load(os.path.join(assets, "1_joueur.png"))
joueur_2 = pygame.image.load(os.path.join(assets, "1_joueur_2.png"))
joueurs = pygame.image.load(os.path.join(assets, "2_joueurs.png"))
joueurs_2 = pygame.image.load(os.path.join(assets, "2_joueurs_2.png"))

Map2 = False
Joueur2 = False
afficheMap = False
afficheMessage = -20
choixJoueur = False
choixMap = True
newhighscore=False
bord=400
TimelineReset=pygame.time.get_ticks()

#Compteur
compteur = 0
plusScore = 0 
plusScore2 = 0 
taillePlusScore = 30
taillePlusScore2 = 30

#Esquive
hide = pygame.image.load(os.path.join(assets, "schiva.png"))

with open(os.path.join(assets, "score.txt"), "r") as fichier:
	highscore=float(fichier.read())

#Tirage aux sort du bandit
def SelectionBandit() :
   dnumero_bandit = random.randint(0,12)
   if Map2 :
      if dnumero_bandit == 0:
         dbandit_x=random.randint(0,fond.get_width()-bandit_mitraillette[0].get_width())
         dbandit_y=1185
         dbandit=bandit_mitraillette
         dbandit_hitbox=bandit_mitraillette_hitbox
      elif dnumero_bandit ==1:
         numero_coord=random.randint(0,1)
         dbandit_x=bandit_salto_x_map2[numero_coord]
         dbandit_y=bandit_salto_y_map2[numero_coord]
         dbandit=bandit_salto
         dbandit_hitbox=bandit_salto_hitbox
      elif dnumero_bandit ==2:
         numero_coord=random.randint(0,5)
         dbandit_x=bandit_window_gauche_x_map2[numero_coord]
         dbandit_y=bandit_window_gauche_y_map2[numero_coord]
         dbandit=bandit_window_gauche
         dbandit_hitbox=bandit_window_gauche_hitbox
      elif dnumero_bandit ==3:
         dbandit_x=bandit_car_x_map2
         dbandit_y=bandit_car_y_map2
         dbandit=bandit_car
         dbandit_hitbox=bandit_car_hitbox
      elif dnumero_bandit ==4:
         numero_coord=random.randint(0,2)
         dbandit_x=bandit_window2_x_map2[numero_coord]
         dbandit_y=bandit_window2_y_map2[numero_coord]
         dbandit=bandit_window2
         dbandit_hitbox=bandit_window2_hitbox
      elif dnumero_bandit ==5:
         numero_coord=random.randint(0,1)
         dbandit_x=bandit_egout_x_map2[numero_coord]
         dbandit_y=bandit_egout_y_map2[numero_coord]
         dbandit=bandit_egout
         dbandit_hitbox=bandit_egout_hitbox
      elif dnumero_bandit ==6:
         dbandit_x=random.randint(0,fond.get_width()-bandit_femme[0].get_width())
         dbandit_y=1185
         dbandit=bandit_femme
         dbandit_hitbox=bandit_femme_hitbox 
      elif dnumero_bandit ==7:
         dbandit_x=bandit_coureur_x
         dbandit_y=bandit_coureur_y
         dbandit=bandit_coureur
         dbandit_hitbox=bandit_coureur_hitbox
      elif dnumero_bandit ==8:
         dbandit_x=random.randint(0,fond.get_width()-bandit_gros[0].get_width())
         dbandit_y=1185
         dbandit=bandit_gros
         dbandit_hitbox=bandit_gros_hitbox
      elif dnumero_bandit ==9:
         dbandit_x=random.randint(0,fond.get_width()-bandit_esquive[0].get_width())
         dbandit_y=1185
         dbandit=bandit_esquive
         dbandit_hitbox=bandit_esquive_hitbox
      elif dnumero_bandit ==10:
         dbandit_x=random.randint(0,fond.get_width()-bandit_mince[0].get_width())
         dbandit_y=1185
         dbandit=bandit_mince
         dbandit_hitbox=bandit_mince_hitbox
      elif dnumero_bandit ==11:
         numero_coord=random.randint(0,2)
         dbandit_x=bandit_loin_x_map2[numero_coord]
         dbandit_y=bandit_loin_y_map2[numero_coord]
         dbandit=bandit_loin
         dbandit_hitbox=bandit_loin_hitbox
      elif dnumero_bandit ==12:
         numero_coord=random.randint(0,3)
         dbandit_x=bandit_loin_2_x_map2[numero_coord]
         dbandit_y=bandit_loin_2_y_map2[numero_coord]
         dbandit=bandit_loin_2
         dbandit_hitbox=bandit_loin_2_hitbox
   else:
      if dnumero_bandit == 0:
         dbandit_x=random.randint(0,fond.get_width()-bandit_mitraillette[0].get_width())
         dbandit_y=1085
         dbandit=bandit_mitraillette
         dbandit_hitbox=bandit_mitraillette_hitbox
      elif dnumero_bandit ==1:
         numero_coord=random.randint(0,2)
         dbandit_x=bandit_salto_x[numero_coord]
         dbandit_y=bandit_salto_y[numero_coord]
         dbandit=bandit_salto
         dbandit_hitbox=bandit_salto_hitbox
      elif dnumero_bandit ==2:
         numero_coord=random.randint(0,5)
         dbandit_x=bandit_window_gauche_x[numero_coord]
         dbandit_y=bandit_window_gauche_y[numero_coord]
         dbandit=bandit_window_gauche
         dbandit_hitbox=bandit_window_gauche_hitbox
      elif dnumero_bandit ==3:
         dbandit_x=bandit_car_x
         dbandit_y=bandit_car_y
         dbandit=bandit_car
         dbandit_hitbox=bandit_car_hitbox
      elif dnumero_bandit ==4:
         numero_coord=random.randint(0,8)
         dbandit_x=bandit_window2_x[numero_coord]
         dbandit_y=bandit_window2_y[numero_coord]
         dbandit=bandit_window2
         dbandit_hitbox=bandit_window2_hitbox
      elif dnumero_bandit ==5:
         numero_coord=random.randint(0,3)
         dbandit_x=bandit_egout_x[numero_coord]
         dbandit_y=bandit_egout_y[numero_coord]
         dbandit=bandit_egout
         dbandit_hitbox=bandit_egout_hitbox
      elif dnumero_bandit ==6:
         dbandit_x=random.randint(0,fond.get_width()-bandit_femme[0].get_width())
         dbandit_y=1085
         dbandit=bandit_femme
         dbandit_hitbox=bandit_femme_hitbox
      elif dnumero_bandit ==7:
         dbandit_x=bandit_coureur_x
         dbandit_y=bandit_coureur_y
         dbandit=bandit_coureur
         dbandit_hitbox=bandit_coureur_hitbox
      elif dnumero_bandit ==8:
         dbandit_x=random.randint(0,fond.get_width()-bandit_gros[0].get_width())
         dbandit_y=1085
         dbandit=bandit_gros
         dbandit_hitbox=bandit_gros_hitbox
      elif dnumero_bandit ==9:
         dbandit_x=random.randint(0,fond.get_width()-bandit_esquive[0].get_width())
         dbandit_y=1200
         dbandit=bandit_esquive
         dbandit_hitbox=bandit_esquive_hitbox
      elif dnumero_bandit ==10:
         dbandit_x=random.randint(0,fond.get_width()-bandit_mince[0].get_width())
         dbandit_y=1085
         dbandit=bandit_mince
         dbandit_hitbox=bandit_mince_hitbox
      elif dnumero_bandit ==11:
         numero_coord=random.randint(0,2)
         dbandit_x=bandit_loin_x[numero_coord]
         dbandit_y=bandit_loin_y[numero_coord]
         dbandit=bandit_loin
         dbandit_hitbox=bandit_loin_hitbox
      elif dnumero_bandit ==12:
         numero_coord=random.randint(0,2)
         dbandit_x=bandit_loin_2_x[numero_coord]
         dbandit_y=bandit_loin_2_y[numero_coord]
         dbandit=bandit_loin_2
         dbandit_hitbox=bandit_loin_2_hitbox
   banditselec = []      
   banditselec.append(dnumero_bandit)
   banditselec.append(dbandit_x)
   banditselec.append(dbandit_y)
   banditselec.append(dbandit)
   banditselec.append(dbandit_hitbox)
   return banditselec
# -------- Main Program Loop -----------


while not done:
   
   # récupère la liste des touches claviers appuyeées sous la forme liste bool
   pygame.event.pump()
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
   n+=1

   # LOGIQUE
   KeysPressed = pygame.key.get_pressed()
   
   #Sélection map
   
   if KeysPressed[pygame.K_LEFT] and choixMap :
      Map2 = False
        
   if KeysPressed[pygame.K_RIGHT] and choixMap :
      Map2 = True
      
   if KeysPressed[pygame.K_LEFT] and choixJoueur :
      Joueur2 = False
        
   if KeysPressed[pygame.K_RIGHT] and choixJoueur :
      Joueur2 = True
      
   if KeysPressed[pygame.K_DOWN] and choixMap :
      choixMap=False
      choixJoueur=True
      
   if KeysPressed[pygame.K_UP] and choixJoueur :
      choixMap=True
      choixJoueur=False
      
   if (KeysPressed[pygame.K_SPACE] or KeysPressed[pygame.K_RETURN]) and (choixMap or choixJoueur) and pygame.time.get_ticks()-TimelineReset>1000:
      afficheMap = True
      choixMap=False
      choixJoueur=False 
      #différente Timeline
      TimelineBandit=pygame.time.get_ticks()
      TimelineEsquive=-15000
      TimelineTire=pygame.time.get_ticks()
      TimelineEsquive2=-15000
      TimelineTire2=pygame.time.get_ticks()
      TimelineReset=pygame.time.get_ticks()
      TimelineScore=-2000
      TimelineScore2=-2000
      J_xdecor = 1050
      J_ydecor = 510
      nbrball=12
      score = 0
      V_xecran = screenWidth//2
      V_yecran = screenHeight//2
      if Joueur2 :
         bord=0
         nbrball2=12
         viseur = pygame.image.load(os.path.join(assets, "viseurj1.png"))
         J_xdecor2 = 1050
         J_ydecor2 = 510
         score2 = 0
         V_xecran2 = screenWidth//2
         V_yecran2 = screenHeight//2
      else:
         viseur = pygame.image.load(os.path.join(assets, "viseur.png"))
      banditselectione = SelectionBandit()
      numero_bandit = banditselectione[0]
      bandit_x = banditselectione[1]
      bandit_y = banditselectione[2]
      bandit = banditselectione[3]
      bandit_hitbox = banditselectione[4]

   if (KeysPressed[pygame.K_SPACE] or KeysPressed[pygame.K_RETURN]) and ((loose and not Joueur2 and pygame.time.get_ticks()-TimelineTire>500) or ((loose or win) and (loose2 or win2)  and Joueur2 and pygame.time.get_ticks()-TimelineTire>500 and pygame.time.get_ticks()-TimelineTire2>500)):
      bord=400
      afficheMap = False
      choixMap=True
      loose=False
      loose2=False
      newhighscore=False
      win=False
      win2=False
      TimelineReset=pygame.time.get_ticks()

   #Déplacement du viseur
   if afficheMap :
      if KeysPressed[pygame.K_w] and V_yecran>(viseur.get_height()) :
         V_yecran -= 25
         
      if KeysPressed[pygame.K_s] and V_yecran<(screenHeight-viseur.get_height()) :
         V_yecran += 25
         
      if KeysPressed[pygame.K_a] and V_xecran>(viseur.get_width()) :
         V_xecran -= 25
         
      if KeysPressed[pygame.K_d] and V_xecran<(screenWidth-viseur.get_width()):
         V_xecran += 25
      
      if Joueur2:
         if KeysPressed[pygame.K_UP] and V_yecran2>(viseur2.get_height()) :
            V_yecran2 -= 25
            
         if KeysPressed[pygame.K_DOWN] and V_yecran2<(screenHeight-viseur2.get_height()) :
            V_yecran2 += 25
            
         if KeysPressed[pygame.K_LEFT] and V_xecran2>(viseur2.get_width()) :
            V_xecran2 -= 25
            
         if KeysPressed[pygame.K_RIGHT] and V_xecran2<(screenWidth-viseur2.get_width()) :
            V_xecran2 += 25
      #Déplacement de l'écran
   
      if V_yecran<(viseur.get_height()) and J_ydecor-20>0 and not (loose or win):
         J_ydecor -= 25
         
      if V_yecran>(screenHeight-viseur.get_height()) and J_ydecor+20<fond.get_height()-screenHeight and not (loose or win):
         J_ydecor += 25
         
      if V_xecran<(viseur.get_width()) and J_xdecor-20>0 and not (loose or win):
         J_xdecor -= 25
         
      if V_xecran>(screenWidth-viseur.get_width()) and J_xdecor+20<fond.get_width()-screenWidth and not (loose or win):
         J_xdecor += 25
      
      if Joueur2:
         if V_yecran2<(viseur2.get_height()) and J_ydecor2-20>0 and not (loose2 or win2):
            J_ydecor2 -= 25
            
         if V_yecran2>(screenHeight-viseur2.get_height()) and J_ydecor2+20<fond.get_height()-screenHeight and not (loose2 or win2):
            J_ydecor2 += 25
            
         if V_xecran2<(viseur2.get_width()) and J_xdecor2-20>0 and not (loose2 or win2):
            J_xdecor2 -= 25
            
         if V_xecran2>(screenWidth-viseur2.get_width()) and J_xdecor2+20<fond.get_width()-screenWidth and not (loose2 or win2):
            J_xdecor2 += 25
      #Esquive
         #Joueur1
      if KeysPressed[pygame.K_e] and not (loose or win) and pygame.time.get_ticks()-TimelineEsquive>15000 and nbrball > 3:
         esquive=True
         plusScore=-100
         score+=plusScore
         nbrball-=3
         TimelineEsquive = pygame.time.get_ticks()
      if pygame.time.get_ticks()-TimelineEsquive >= 1000 :
         esquive=False
         #Joueur2
      if KeysPressed[pygame.K_KP1 ] and not (loose2 or win2) and pygame.time.get_ticks()-TimelineEsquive2>15000 and nbrball2 > 3:
         esquive2=True
         plusScore2=-100
         score2+=plusScore2
         nbrball2-=3
         TimelineEsquive2 = pygame.time.get_ticks()
      if pygame.time.get_ticks()-TimelineEsquive2 >= 1000 :
         esquive2=False
      #Tire
         #Joueur1
      if KeysPressed[pygame.K_SPACE] and bandit_x-J_xdecor<V_xecran<bandit_x-J_xdecor+bandit[0].get_width() and bandit_y-J_ydecor<V_yecran<bandit_y-J_ydecor+bandit[0].get_height() and pygame.time.get_ticks()-TimelineBandit>3000 and not (loose or win) and pygame.time.get_ticks()-TimelineTire>200 and not esquive:
         if bandit_hitbox[m].get_at(((J_xdecor+V_xecran-bandit_x), (J_ydecor+V_yecran-bandit_y)))==BLUE:
            plusScore=100*((9000-(pygame.time.get_ticks()-TimelineBandit))/1000)
            score+=plusScore
            TimelineBandit=pygame.time.get_ticks()
            death=True
            nbrball+=2
         if bandit_hitbox[m].get_at(((J_xdecor+V_xecran-bandit_x), (J_ydecor+V_yecran-bandit_y)))==GREEN:
            plusScore=300*((9000-(pygame.time.get_ticks()-TimelineBandit))/1000)
            score+=plusScore
            TimelineBandit=pygame.time.get_ticks()
            death=True
            nbrball+=4
         if bandit_hitbox[m].get_at(((J_xdecor+V_xecran-bandit_x), (J_ydecor+V_yecran-bandit_y)))==RED:
            plusScore=-300
            score+=plusScore
            TimelineBandit=pygame.time.get_ticks()
            death=True
            if nbrball > 5:
               nbrball-=4
            else:
               nbrball =1
               death=False
         if bandit_hitbox[m].get_at(((J_xdecor+V_xecran-bandit_x), (J_ydecor+V_yecran-bandit_y)))==CYAN:
            plusScore=-1000
            score+=plusScore
            TimelineBandit=pygame.time.get_ticks()
            death=True
            if nbrball > 10:
               nbrball-=9
            else:
               nbrball =1
               death=False
         tire_x=V_xecran-(50)
         tire_y=V_yecran-(50)
         if V_yecran>=54:
            V_yecran -= 30
         nbrball-=1
         fire = pygame.mixer.Sound(os.path.join(assets, "gun_fire.wav"))
         fire.play()
         TimelineTire=pygame.time.get_ticks()
      elif KeysPressed[pygame.K_SPACE] and not loose and pygame.time.get_ticks()-TimelineTire>200 :
         tire_x=V_xecran-(50)
         tire_y=V_yecran-(50)
         if V_yecran>viseur.get_height():
            V_yecran -= 30
         nbrball-=1
         fire = pygame.mixer.Sound(os.path.join(assets, "gun_fire.wav"))
         fire.play()
         TimelineTire=pygame.time.get_ticks()
         #Joueur2
      if Joueur2 :
         if KeysPressed[pygame.K_KP0] and bandit_x-J_xdecor2<V_xecran2<bandit_x-J_xdecor2+bandit[0].get_width() and bandit_y-J_ydecor2<V_yecran2<bandit_y-J_ydecor2+bandit[0].get_height() and pygame.time.get_ticks()-TimelineBandit>3000 and not (loose2 or win2) and pygame.time.get_ticks()-TimelineTire2>200 and not esquive:
            if bandit_hitbox[m].get_at(((J_xdecor2+V_xecran2-bandit_x), (J_ydecor2+V_yecran2-bandit_y)))==(0,0,255,255):
               plusScore2 = 100*((9000-(pygame.time.get_ticks()-TimelineBandit))/1000)
               score2+=plusScore2
               TimelineBandit=pygame.time.get_ticks()
               death=True
               nbrball2+=2
            if bandit_hitbox[m].get_at(((J_xdecor2+V_xecran2-bandit_x), (J_ydecor2+V_yecran2-bandit_y)))==(0,255,0,255):
               plusScore2=300*((9000-(pygame.time.get_ticks()-TimelineBandit))/1000)
               score2+=plusScore2
               TimelineBandit=pygame.time.get_ticks()
               death=True
               nbrball2+=4
            if bandit_hitbox[m].get_at(((J_xdecor2+V_xecran2-bandit_x), (J_ydecor2+V_yecran2-bandit_y)))==(255,0,0,255):
               plusScore2=-300
               score2+=plusScore2
               TimelineBandit=pygame.time.get_ticks()
               death=True
               if nbrball2 > 5:
                  nbrball2-=4
               else:
                  nbrball2 =1
                  death=False
            if bandit_hitbox[m].get_at(((J_xdecor2+V_xecran2-bandit_x), (J_ydecor2+V_yecran2-bandit_y)))==(0,255,255,255):
               plusScore2=-1000
               score2+=plusScore2
               TimelineBandit=pygame.time.get_ticks()
               death=True
               if nbrball2 > 10:
                  nbrball2-=9
               else:
                  nbrball2 =1
                  death=False
            
            tire2_x=V_xecran2-(50)
            tire2_y=V_yecran2-(50)
            if V_yecran2>=54:
               V_yecran2 -= 30 
            nbrball2-=1
            fire = pygame.mixer.Sound(os.path.join(assets, "gun_fire.wav"))
            fire.play()
            TimelineTire2=pygame.time.get_ticks()
         elif KeysPressed[pygame.K_KP0] and not loose2 and pygame.time.get_ticks()-TimelineTire2>200 :
            tire2_x=V_xecran2-(50)
            tire2_y=V_yecran2-(50)
            if V_yecran2>viseur.get_height():
               V_yecran2 -= 30
            fire = pygame.mixer.Sound(os.path.join(assets, "gun_fire.wav"))
            fire.play()
            nbrball2-=1
            TimelineTire2=pygame.time.get_ticks()
      if pygame.time.get_ticks()-TimelineBandit>500 and death and not esquive:
         banditselectione = SelectionBandit();
         numero_bandit = banditselectione[0]
         bandit_x = banditselectione[1]
         bandit_y = banditselectione[2]
         bandit = banditselectione[3]
         bandit_hitbox = banditselectione[4]
         death= False
      if nbrball <= 0:
         nbrball=0
         loose= True
         bandit_fin_1=bandit[len(bandit)-2]
         if Joueur2 :
            win2=True
            bandit_fin_2=bandit[len(bandit)-1]
         J_xdecor = bandit_x+bandit[0].get_width()/2-screenWidth/2
         J_ydecor = bandit_y+bandit[0].get_height()/2-screenHeight/2
         if J_xdecor < 0:
            J_xdecor=0
         elif J_xdecor > fond.get_width()-screenWidth:
            J_xdecor = fond.get_width()-screenWidth
         if J_ydecor < 0:
            J_ydecor = 0
         elif J_ydecor > fond.get_height()-screenHeight:
            J_ydecor = fond.get_height()-screenHeight
         J_xdecor2 = J_xdecor
         J_ydecor2 = J_ydecor
         if score>highscore and not Joueur2:
            with open(os.path.join(assets, "score.txt"), "w") as fichier:
               fichier.write(str(score))
               newhighscore=True
               highscore=score
      if nbrball2 <= 0:
         nbrball2=0
         loose2= True
         win=True
         bandit_fin_1=bandit[len(bandit)-1]
         bandit_fin_2=bandit[len(bandit)-2]
         J_xdecor = bandit_x+bandit[0].get_width()/2-screenWidth/2
         J_ydecor = bandit_y+bandit[0].get_height()/2-screenHeight/2
         if J_xdecor2 < 0:
            J_xdecor2=0
         elif J_xdecor2 > fond.get_width()-screenWidth:
            J_xdecor2 = fond.get_width()-screenWidth
         if J_ydecor2 < 0:
            J_ydecor2 = 0
         elif J_ydecor2 > fond.get_height()-screenHeight:
            J_ydecor2 = fond.get_height()-screenHeight
         J_xdecor = J_xdecor2
         J_ydecor = J_ydecor2
         if score>highscore and not Joueur2:
            with open(os.path.join(assets, "score.txt"), "w") as fichier:
               fichier.write(str(score))
               highscore=score
               newhighscore=True
      #Tire bandit
      
   
         
      if pygame.time.get_ticks()-TimelineBandit>9000 and not (esquive or esquive2):
         if Joueur2 and not (loose2 or win2 or loose or win) :
            if score > score2 :
               win=True
               loose2=True
               bandit_fin_1=bandit[len(bandit)-1]
               bandit_fin_2=bandit[len(bandit)-2]
            elif score < score2 :
               win2 = True
               loose = True
               bandit_fin_1=bandit[len(bandit)-2]
               bandit_fin_2=bandit[len(bandit)-1]
            else :
               loose2=True
               loose=True
               bandit_fin_1=bandit[len(bandit)-2]
               bandit_fin_2=bandit[len(bandit)-2]
         elif not (loose2 or win2 or loose or win) :
            loose = True
            bandit_fin_1=bandit[len(bandit)-2]
         J_xdecor = bandit_x+bandit[0].get_width()/2-screenWidth/2
         J_ydecor = bandit_y+bandit[0].get_height()/2-screenHeight/2
         if J_xdecor < 0:
            J_xdecor=0
         elif J_xdecor > fond.get_width()-screenWidth:
            J_xdecor = fond.get_width()-screenWidth
         if J_ydecor < 0:
            J_ydecor = 0
         elif J_ydecor > fond.get_height()-screenHeight:
            J_ydecor = fond.get_height()-screenHeight
         J_xdecor2 = J_xdecor
         J_ydecor2 = J_ydecor
         if score>highscore and not Joueur2:
            with open(os.path.join(assets, "score.txt"), "w") as fichier:
               fichier.write(str(score))
               highscore=score
               newhighscore=True
      elif pygame.time.get_ticks()-TimelineBandit>9000 and not esquive:
         loose= True
         bandit_fin_1=bandit[len(bandit)-2]
         if Joueur2 :
            win2=True
            bandit_fin_2=bandit[len(bandit)-1]
         J_xdecor = bandit_x+bandit[0].get_width()/2-screenWidth/2
         J_ydecor = bandit_y+bandit[0].get_height()/2-screenHeight/2
         if J_xdecor < 0:
            J_xdecor=0
         elif J_xdecor > fond.get_width()-screenWidth:
            J_xdecor = fond.get_width()-screenWidth
         if J_ydecor < 0:
            J_ydecor = 0
         elif J_ydecor > fond.get_height()-screenHeight:
            J_ydecor = fond.get_height()-screenHeight
         J_xdecor = J_xdecor2
         J_ydecor = J_ydecor2
         if score>highscore and not Joueur2:
            with open(os.path.join(assets, "score.txt"), "w") as fichier:
               fichier.write(str(score))
               highscore=score
               newhighscore=True
      elif pygame.time.get_ticks()-TimelineBandit>9000 and not esquive2 and Joueur2:
         loose2= True
         bandit_fin_2=bandit[len(bandit)-2]
         win=True
         bandit_fin_1=bandit[len(bandit)-1]
         J_xdecor2 = bandit_x+bandit[0].get_width()/2-screenWidth/2
         J_ydecor2 = bandit_y+bandit[0].get_height()/2-screenHeight/2
         if J_xdecor2 < 0:
            J_xdecor2=0
         elif J_xdecor2 > fond.get_width()-screenWidth:
            J_xdecor2 = fond.get_width()-screenWidth
         if J_ydecor2 < 0:
            J_ydecor2 = 0
         elif J_ydecor2 > fond.get_height()-screenHeight:
            J_ydecor2 = fond.get_height()-screenHeight
         J_xdecor = J_xdecor2
         J_ydecor = J_ydecor2
         if score>highscore and not Joueur2:
            with open(os.path.join(assets, "score.txt"), "w") as fichier:
               fichier.write(str(score))
               highscore=score
               newhighscore=True
      elif pygame.time.get_ticks()-TimelineBandit>9000 and afficheMap:
         death=True
         TimelineBandit=pygame.time.get_ticks()
      
      if Joueur2 :
         if (score > 5523) :
            loose2= True
            bandit_fin_2=bandit[len(bandit)-2]
            win=True
            bandit_fin_1=bandit[len(bandit)-1]
            J_xdecor2 = bandit_x+bandit[0].get_width()/2-screenWidth/2
            J_ydecor2 = bandit_y+bandit[0].get_height()/2-screenHeight/2
            if J_xdecor2 < 0:
               J_xdecor2=0
            elif J_xdecor2 > fond.get_width()-screenWidth:
               J_xdecor2 = fond.get_width()-screenWidth
            if J_ydecor2 < 0:
               J_ydecor2 = 0
            elif J_ydecor2 > fond.get_height()-screenHeight:
               J_ydecor2 = fond.get_height()-screenHeight
            J_xdecor = J_xdecor2
            J_ydecor = J_ydecor2
         elif (score2 > 5523) :
            loose= True
            bandit_fin_2=bandit[len(bandit)-1]
            win2=True
            bandit_fin_1=bandit[len(bandit)-2]
            J_xdecor2 = bandit_x+bandit[0].get_width()/2-screenWidth/2
            J_ydecor2 = bandit_y+bandit[0].get_height()/2-screenHeight/2
            if J_xdecor2 < 0:
               J_xdecor2=0
            elif J_xdecor2 > fond.get_width()-screenWidth:
               J_xdecor2 = fond.get_width()-screenWidth
            if J_ydecor2 < 0:
               J_ydecor2 = 0
            elif J_ydecor2 > fond.get_height()-screenHeight:
               J_ydecor2 = fond.get_height()-screenHeight
            J_xdecor = J_xdecor2
            J_ydecor = J_ydecor2
      # DESSIN
   
   # affiche la zone de rendu au dessus de fenetre de jeu
      zonejaune = pygame.Rect( J_xdecor, J_ydecor, screenWidth, screenHeight )
      fondj1=pygame.Surface((screenWidth, screenHeight))
      if Map2 :
         fondj1.blit(fond2,(0,0),area = zonejaune)
      else :
         fondj1.blit(fond,(0,0),area = zonejaune)
      
      if Joueur2 :
         bord=0
         zonejaune = pygame.Rect( J_xdecor2, J_ydecor2, screenWidth, screenHeight )
         fondj2=pygame.Surface((screenWidth, screenHeight))
      
         if Map2 :
            fondj2.blit(fond2,(bord+0,0),area = zonejaune)
         else :
            fondj2.blit(fond,(bord+0,0),area = zonejaune)
      # BALLES
      s = police.render(str(nbrball)+"X", True,WHITE)
      fondj1.blit(s,(0, screenHeight-s.get_height()+6))
      fondj1.blit(scale(bullet,(10*2, 23*2)),(s.get_width()+6, screenHeight-bullet.get_height()-6))
      
      
      #Compteur
      compteur=(int((9000-pygame.time.get_ticks()+TimelineBandit)/100))/10
      if compteur < 0 :
         compteur = 0
      cpt = police.render(str(int(compteur*10)/10), True,WHITE)
      if compteur<=6:
         fondj1.blit(cpt,(screenWidth-75, screenHeight-50))
   
      #bandit
      if 3000<pygame.time.get_ticks()-TimelineBandit<9000 and not (death or (loose or win) or not afficheMap) :
         if numero_bandit==0:
            if pygame.time.get_ticks()-TimelineBandit<4500:
               m=(n%2)
            elif pygame.time.get_ticks()-TimelineBandit<6000:
               m=2+(n%2)
            elif pygame.time.get_ticks()-TimelineBandit<7500:
               m=4+(n%2)
            else:
               m=6+(n%2)
         if numero_bandit==1:
            if pygame.time.get_ticks()-TimelineBandit<5500:
               m=0
            elif pygame.time.get_ticks()-TimelineBandit<5833:
               m=1
            elif pygame.time.get_ticks()-TimelineBandit<6166:
               m=2
            elif pygame.time.get_ticks()-TimelineBandit<6500:
               m=3
            else:
               m=4
         if numero_bandit==2:
            if pygame.time.get_ticks()-TimelineBandit<5500:
               m=0
            else:
               m=1
         if numero_bandit==3:
            if pygame.time.get_ticks()-TimelineBandit<4500:
               m=0
            elif pygame.time.get_ticks()-TimelineBandit<5000:
               m=1
            else:
               m=2
         if numero_bandit==4:
            if pygame.time.get_ticks()-TimelineBandit<5500:
               m=0
            else:
               m=1
         if numero_bandit==5:
            if pygame.time.get_ticks()-TimelineBandit<5500:
               m=0
            else:
               m=1
         if numero_bandit==6:
            if pygame.time.get_ticks()-TimelineBandit<6000:
               m=0
            else:
               m=1
         if numero_bandit==7:
            if pygame.time.get_ticks()-TimelineBandit<3500:
               T6 = pygame.time.get_ticks()
               m = 0
            elif pygame.time.get_ticks()-TimelineBandit>3700 :
               bandit_x+=10
            if 3700<pygame.time.get_ticks()-TimelineBandit<7000:
               m=1+((n//6)%2)
            if pygame.time.get_ticks()-TimelineBandit>=7000:
               m=3+((n//6)%2)
         if numero_bandit==8:
            if pygame.time.get_ticks()-TimelineBandit<6000:
               m=0
            else:
               m=1
         if numero_bandit==9:
            if pygame.time.get_ticks()-TimelineBandit<8000:
               m=((n//30)%2)
            else:
               m=2
         if numero_bandit==10:
            if pygame.time.get_ticks()-TimelineBandit<6000:
               m=0
            else:
               m=1
         if numero_bandit==11:
            if pygame.time.get_ticks()-TimelineBandit<6000:
               m=0
            else:
               m=1
         if numero_bandit==12:
            if pygame.time.get_ticks()-TimelineBandit<6000:
               m=0
            else:
               m=1
         fondj1.blit(bandit[m],(bandit_x-J_xdecor,bandit_y-J_ydecor))
         #bandit
         if Joueur2 and not (death or (loose2 or win2)) :
            fondj2.blit(bandit[m],(bord+bandit_x-J_xdecor2,bandit_y-J_ydecor2))
   
                  
      if death and not loose and not esquive:
         fondj1.blit(bandit[len(bandit)-1],(bandit_x-J_xdecor,bandit_y-J_ydecor))
      if loose :
         fondj1.blit(bandit_fin_1,(bandit_x-J_xdecor,bandit_y-J_ydecor))
         fondj1.blit(dead,(0,0))
         if not Joueur2:
            H1=police.render("highscore : "+str(int(highscore)), True,WHITE)
            fondj1.blit(H1,(400-(H1.get_width()/2),400))
            if newhighscore:
               H2=police.render("Nouveau highscore", True,YELLOW)
               fondj1.blit(H2,(400-(H2.get_width()/2),410+H1.get_height()))
      if win :
         fondj1.blit(bandit_fin_1,(bord+bandit_x-J_xdecor,bandit_y-J_ydecor))
         fondj1.blit(won,(bord+0,0))
      if death and esquive :
         fondj1.blit(bandit[len(bandit)-2],(bandit_x-J_xdecor,bandit_y-J_ydecor))
      
      #tire
      if pygame.time.get_ticks()-TimelineTire<500 and pygame.time.get_ticks()-TimelineReset>500 and not (loose or win):
         pan+=1
         fondj1.blit(scale(bang[pan%23],(100,100)),(tire_x,tire_y))
      #fleche
      if bandit_x+bandit[0].get_width()//2>J_xdecor+screenWidth and 3000<pygame.time.get_ticks()-TimelineBandit<9000 :
         if J_ydecor+screenHeight-(40+fleche_droite.get_height())>bandit_y+bandit[0].get_height()//2>J_ydecor+40:
            fondj1.blit(fleche_droite,(fleche_droite_x,bandit_y-J_ydecor+bandit[0].get_height()//2))
         if bandit_y+bandit[0].get_height()//2<J_ydecor+40:
            fondj1.blit(fleche_droite,(fleche_droite_x,40))
         if J_ydecor+screenHeight-(40+fleche_droite.get_height())<bandit_y+bandit[0].get_height()//2:
            fondj1.blit(fleche_droite,(fleche_droite_x,screenHeight-(40+fleche_droite.get_height())))
      if bandit_x+bandit[0].get_width()//2<J_xdecor and 3000<pygame.time.get_ticks()-TimelineBandit<9000 :
         if J_ydecor+screenHeight-(40+fleche_gauche.get_height())>bandit_y+bandit[0].get_height()//2>J_ydecor+40:
            fondj1.blit(fleche_gauche,(fleche_gauche_x,bandit_y-J_ydecor+bandit[0].get_height()//2))
         if bandit_y+bandit[0].get_height()//2<J_ydecor+40:
            fondj1.blit(fleche_gauche,(fleche_gauche_x,40))
         if J_ydecor+screenHeight-(40+fleche_gauche.get_height())<bandit_y+bandit[0].get_height()//2:
            fondj1.blit(fleche_gauche,(fleche_gauche_x,screenHeight-(40+fleche_gauche.get_height())))
      #viseur
      if not (loose or win):
         fondj1.blit(scale(viseur,(100,100)),(0+V_xecran-(viseur.get_width()//2),V_yecran-(viseur.get_height()//2)))
      
      #Score j1
      
      sc = police.render("SCORE : "+str(int(score)), True,WHITE)
      fondj1.blit(sc,(0, 0))
      if pygame.time.get_ticks()-TimelineScore<2000 and plusScore!= 0 :
         
            policePlusScore = pygame.font.SysFont("Stencil", taillePlusScore)
            taillePlusScore+=1
            if plusScore>0 :
               plusSc = policePlusScore.render("+"+str(int(plusScore)), True,WHITE)
            else :
               plusSc = policePlusScore.render(""+str(int(plusScore)), True,WHITE)
            fondj1.blit(plusSc,(300, 0))
      else :
         TimelineScore = pygame.time.get_ticks()
         taillePlusScore=30
         plusScore=0
      
      #Esquive
      if pygame.time.get_ticks()-TimelineEsquive>15000 and pygame.time.get_ticks()-TimelineBandit>3000 and not (loose or win):
         message_esquive = police.render("ESQUIVE", True,WHITE)
         fondj1.blit(message_esquive,(0+screenWidth-message_esquive.get_width(), 0))
      elif pygame.time.get_ticks()-TimelineEsquive>15000 :
         message_esquive = police.render("ESQUIVE", True,LIGHTGREY)
         fondj1.blit(message_esquive,(0+screenWidth-message_esquive.get_width(), 0))
      else :
         message_esquive = police.render("ESQUIVE", True,GREY)
         fondj1.blit(message_esquive,(0+screenWidth-message_esquive.get_width(), 0))
      
      if esquive :
         fondj1.blit(hide,(0,0))
   
      #dessin joueur 2
      if Joueur2 and afficheMap:
            
         # BALLES
         police = pygame.font.SysFont("Stencil", 50)
         
         s = police.render(str(nbrball2)+"X", True,WHITE)
         fondj2.blit(s,(bord+0, screenHeight-s.get_height()+6))
         fondj2.blit(scale(bullet,(10*2, 23*2)),(bord+s.get_width()+6, screenHeight-bullet.get_height()-6))
         
         #Compteur
         
         if compteur < 0 :
            compteur = 0
         cpt = police.render(str(int(compteur*10)/10), True,WHITE)
         if compteur<=6:
            fondj2.blit(cpt,(bord+screenWidth-75, screenHeight-50))
   
         #bandit

         if death and not (loose2 or win2) and not esquive:
            fondj2.blit(bandit[len(bandit)-1],(bord+bandit_x-J_xdecor2,bandit_y-J_ydecor2))
         if loose2 :
            fondj2.blit(bandit_fin_2,(bord+bandit_x-J_xdecor2,bandit_y-J_ydecor2))
            fondj2.blit(dead,(bord+0,0))
         if win2 :
            fondj2.blit(bandit_fin_2,(bord+bandit_x-J_xdecor2,bandit_y-J_ydecor2))
            fondj2.blit(won,(bord+0,0))
         if death and esquive :
            fondj2.blit(bandit[len(bandit)-2],(bord+bandit_x-J_xdecor2,bandit_y-J_ydecor2))
         
         #tire
         if pygame.time.get_ticks()-TimelineTire2<500 and pygame.time.get_ticks()-TimelineReset>500 and not (loose2 or win2):
            pan+=1
            fondj2.blit(scale(bang[pan%23],(100,100)),(bord+tire2_x,tire2_y))
         
         #fleche
         
         if bandit_x+bandit[0].get_width()//2>J_xdecor2+screenWidth and 3000<pygame.time.get_ticks()-TimelineBandit<9000 :
            if J_ydecor2+screenHeight-(40+fleche_droite2.get_height())>bandit_y+bandit[0].get_height()//2>J_ydecor2+40:
               fondj2.blit(fleche_droite2,(bord+fleche_droite2_x,bandit_y-J_ydecor2+bandit[0].get_height()//2))
            if bandit_y+bandit[0].get_height()//2<J_ydecor2+40:
               fondj2.blit(fleche_droite2,(bord+fleche_droite2_x,40))
            if J_ydecor2+screenHeight-(40+fleche_droite2.get_height())<bandit_y+bandit[0].get_height()//2:
               fondj2.blit(fleche_droite2,(bord+fleche_droite2_x,screenHeight-(40+fleche_droite2.get_height())))
         if bandit_x+bandit[0].get_width()//2<J_xdecor2 and 3000<pygame.time.get_ticks()-TimelineBandit<9000 :
            if J_ydecor2+screenHeight-(40+fleche_gauche2.get_height())>bandit_y+bandit[0].get_height()//2>J_ydecor2+40:
               fondj2.blit(fleche_gauche2,(bord+fleche_gauche2_x,bandit_y-J_ydecor2+bandit[0].get_height()//2))
            if bandit_y+bandit[0].get_height()//2<J_ydecor2+40:
               fondj2.blit(fleche_gauche2,(bord+fleche_gauche2_x,40))
            if J_ydecor2+screenHeight-(40+fleche_gauche2.get_height())<bandit_y+bandit[0].get_height()//2:
               fondj2.blit(fleche_gauche2,(bord+fleche_gauche2_x,screenHeight-(40+fleche_gauche2.get_height())))
         #viseur
         if not (loose2 or win2):
            fondj2.blit(scale(viseur2,(100,100)),(bord+V_xecran2-(viseur2.get_width()//2),V_yecran2-(viseur2.get_height()//2)))
         
         #Score j2
         
         sc = police.render("SCORE : "+str(int(score2)), True,WHITE)
         fondj2.blit(sc,(bord+0, 0))
         if pygame.time.get_ticks()-TimelineScore2<2000 and plusScore2!= 0 :
            policePlusScore2 = pygame.font.SysFont("Stencil", taillePlusScore2)
            taillePlusScore2+=1
            if plusScore2>0 :
               plusSc2 = policePlusScore2.render("+"+str(int(plusScore2)), True,WHITE)
            else :
               plusSc2 = policePlusScore2.render(""+str(int(plusScore2)), True,WHITE)
            fondj2.blit(plusSc2,(bord+300, 0))
         else :
            TimelineScore2 = pygame.time.get_ticks()
            taillePlusScore2=30
            plusScore2=0
         
         #Esquive
         if pygame.time.get_ticks()-TimelineEsquive2>15000 and pygame.time.get_ticks()-TimelineBandit>3000 and not (loose2 or win2):
            message_esquive = police.render("ESQUIVE", True,WHITE)
            fondj2.blit(message_esquive,(bord+screenWidth-message_esquive.get_width(), 0))
         elif pygame.time.get_ticks()-TimelineEsquive2>15000 :
            message_esquive = police.render("ESQUIVE", True,LIGHTGREY)
            fondj2.blit(message_esquive,(bord+screenWidth-message_esquive.get_width(), 0))
         else:
            message_esquive = police.render("ESQUIVE", True,GREY)
            fondj2.blit(message_esquive,(bord+screenWidth-message_esquive.get_width(), 0))
            
         if esquive2 :
            fondj2.blit(hide,(bord,0))
         
         screen.blit(fondj2,(screenWidth,0))
         bord=0
      screen.blit(fondj1,(bord,0))
    # Page d'acceuil
   if not Joueur2 or choixJoueur or choixMap :
      screen.blit(bord_droit,(bord+screenWidth,0))
      screen.blit(bord_gauche,(0,0))
   if not afficheMap :

        screen.blit(scale(thank,(screenWidth,screenHeight)),(bord+0,0))
        
        afficheMessage += 1
        if afficheMessage >= 0 and afficheMessage <= 30 :
            
            screen.blit(scale(message,(767,60)),(bord+20,20))
            
        if afficheMessage > 30 :
        
            afficheMessage = -20
        if choixMap :
         if not Map2 :
            screen.blit(scale(titre_map1_2,(396,203)),(bord+20,50))
            screen.blit(scale(titre_map2,(323,156)),(bord+430,100))
            
         if Map2 :
            screen.blit(scale(titre_map1,(305,156)),(bord+20,100))
            screen.blit(scale(titre_map2_2,(420,203)),(bord+360,50))
        else :
         if not Map2 :
            screen.blit(scale(titre_map1,(396,203)),(bord+20,50))
            screen.blit(scale(titre_map2,(323,156)),(bord+430,100))
            
         if Map2 :
            screen.blit(scale(titre_map1,(305,156)),(bord+20,100))
            screen.blit(scale(titre_map2,(420,203)),(bord+360,50))
            
        if choixJoueur:
         if not Joueur2 :
            screen.blit(joueur_2,(bord+25,225))
            screen.blit(joueurs,(bord+screenWidth-joueurs.get_width()-25,250))
            
         if Joueur2 :
            screen.blit(joueur,(bord+50,250))
            screen.blit(joueurs_2,(bord+screenWidth-joueurs_2.get_width()-25,225))
        else :
         if not Joueur2 :
            screen.blit(joueur,(bord+25,225))
            screen.blit(joueurs,(bord+screenWidth-joueurs.get_width()-25,250))
            
         if Joueur2 :
            screen.blit(joueur,(bord+50,250))
            screen.blit(joueurs,(bord+screenWidth-joueurs.get_width()-25,225))
      
    # Go ahead and update the screen with what we've drawn.
   pygame.display.flip()
 
    # Limit frames per second
   clock.tick(30)
 
# Close the window and quit.
pygame.quit()