from wsgiref.simple_server import sys_version
import pygame as pg

class Score:
 
    def __init__ (self):

        self.score = 0
        self.font  = pg.font.Font(None,30)
        self.font2  = pg.font.Font(None,50)

        self.context  = f"Score: {self.score}"
        self.text = self.font.render(self.context,True,(230,230,230))
        self.pre_high_score  = 0

        self.pre_hscore_surface = self.font.render(f"High Score: {self.pre_high_score}",True,(230,230,230))
        # self.show  = 0
    def add_score(self,is_colliding,can_add):
        if is_colliding  and can_add:
            self.score += 1    
            self.context  = f"Score: {self.score}"
            self.text = self.font.render(self.context,True,(230,230,230))
             
    def show_the_score(self,screen,y_of_your_arrow):
        screen.blit(self.text,(0,y_of_your_arrow + 70 + 10))
    
    def show_high_score(self,screen,width,file):
        with open(file) as f:
            self.pre_high_scor = f.read()

        self.pre_hscore_surface = self.font.render(f"High Score: {self.pre_high_scor}",True,(230,230,230))
        screen.blit(self.pre_hscore_surface,(width //2 - 122,1))

    def congrats(self,screen):
        congrats_surface = self.font2.render('You Win And Broke The High Score Record !!!!',True,(0,255,0)) 
        congrats_surface_pos = congrats_surface.get_rect()
        congrats_surface_pos.center = screen.get_rect().center
        screen.blit(congrats_surface,  congrats_surface_pos)

    def no_break_record(self,screen):
        congrats_surface2 = self.font2.render(' Good Game ! ',True,(0,255,0))
        congrats_surface2_pos = congrats_surface2.get_rect()
        congrats_surface2_pos.center = screen.get_rect().center
        screen.blit(congrats_surface2,congrats_surface2_pos)

    def new_high_score(self,time,screen,width,file): 
        saved_score = int(str(self.pre_high_score).split()[0].split('-')[0])
        if self.score > saved_score :
            with open(file,'w') as f:
                f.write(f"{str(self.score)} ({time}s)")

            self.pre_high_score  = str(self.score)+'-'+time
            pg.display.update(self.pre_hscore_surface.get_rect())
            self.pre_hscore_surface = self.font.render(f"High Score: {self.pre_high_score}",True,(230,230,230))
            self.show_high_score(screen,width,file) 
            self.congrats(screen)
            to_quit = self.font.render(f"Q = Quit",True,(230,230,230))
            to_replay = self.font.render(f"P = Replay",True,(230,230,230))
            screen.blit(to_quit,(width//2 - 50,350))
            screen.blit(to_replay,(width//2 - 50,400))
            pg.display.update()
            pg.time.wait(1000)

        else:
            self.show_high_score(screen,width,file) 
            self.no_break_record(screen)
            to_quit = self.font.render(f"Q = Quit",True,(230,230,230))
            to_replay = self.font.render(f"P = Replay",True,(230,230,230))
            screen.blit(to_quit,(width//2 - 50,350))
            screen.blit(to_replay,(width//2 - 50,400))


    def reset_score(self,screen,file,x,y):
        with open(file,'w') as f:
            f.write('0')
        reset_text  = self.font2.render('High Score Reset To 0',True,(0,255,0))
        screen.blit(reset_text,(x,y))
        pg.display.update()
        pg.time.delay(1000) 


            