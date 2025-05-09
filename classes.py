

class CHANSON:
    def __init__(self,isrc,title,artist,time,im,suivant=None):
        self.ISRC = isrc
        self.titre = title
        self.artiste = artist
        self.duree = time
        self.img = im
        self.next = suivant
    
class Noeud:
    def __init__(self, song: CHANSON, visited: bool = False):
        self.song = song
        self.visited = visited
class Graphe:
    def __innit__(self, liste_sommets:list,mat ):
        self.listeSommets = liste_sommets
        self.mat = mat
    def get_index_node(self, song=CHANSON):
        pass
        
        
    
class Playlist():
    def __init__(self):
        self.tete = None
    def est_vide(self)-> bool:
        return self.tete is None
  
        
    def insere(self,previous_song,new_song)-> None:
        """insère une nouvelle chanson juste après previous_song"""
        #cas où previous_song est en tête
        
        if self.tete is None:
            
            tmp = new_song
            tmp.next = self.tete
            self.tete = tmp
        #cas général  
        else:
            chansoncourante = self.tete
            while chansoncourante.next is not None and chansoncourante.next is not previous_song:
                chansoncourante = chansoncourante.next
            tmp = new_song
            tmp.next = chansoncourante.next
            chansoncourante.next = tmp
       
    

    def taille(self)-> int:
        
        if self.tete == None:
            return 0
        else:
            t = 1
            chansoncourante = self.tete
            while chansoncourante.next is not None:
                t = t + 1
                chansoncourante = chansoncourante.next
            return t

    def plus_long_texte(self):
        chansoncourante = self.tete
        plt=max(len(chansoncourante.titre),len(chansoncourante.artiste))
       
        while chansoncourante is not None:
                        
            tmp = max(len(chansoncourante.titre),len(chansoncourante.artiste)) 
            if tmp > plt:
                plt = tmp
            chansoncourante = chansoncourante.next
        
        return plt

        
    # fonction de test     
    def lit_tout(self):
        chansoncourante = self.tete
        while chansoncourante is not None:
            print(chansoncourante.titre)
            chansoncourante= chansoncourante.next

    ####################################""

class pile:
        def __init__(self):
            self.contenu = []

        def est_vide(self):
            return len(self.contenu)==0

        def empiler(self,v):
            self.contenu.append(v)
        
        def depiler(self):
            """retourne l'élément en heut de pile si celle-ci n'est pas vide"""
            if not self.est_vide():
                return self.contenu.pop() 
            
            else:
                raise Exception("saisie incorrecte") 

    ###################################





if __name__=="__main__":

        song1=CHANSON("FRZ019102280","Volutes","Alain Bashung","3:25","images/FRZ019102280.gif")
        song2=CHANSON("GBCJN7800001","Miss You","Rolling Stones","4:49","images/GBCJN7800001.gif")
        #song3=CHANSON("USQX90900760","Castles Made of Sand","Jimi Hendrix","2:47","images/USQX90900760.gif")
        #song4=CHANSON("USUM71021486","Take The Long Way Home","Supertramp","5:19","images/USUM71021486.gif")

        

        ########## instanciation ############

        maPL=Playlist()
        maPL.insere(None,song1)
        maPL.insere(None,song2)
        #maPL.insere(None,song4)
        #maPL.insere(song4,song3)

        maPL.lit_tout()
        

       

        

        


