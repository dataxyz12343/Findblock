import pygame as pg
import random
from colors import Therect,get_random_rgb
from score import Score
from pongsound import Sound
from clash import Clash

pg.init()

width = 800
height = 600
screen = pg.display.set_mode((width,height))
pg.display.set_caption(('FIND THE BLOCKS'))


#NOTE : MIND-BLOWING FACTS 😅
# rect = pg.Rect((800//2,600//2,300,300)) # module pygame has a CLASS called Rect( which has attributes)
# rect.center = screen.get_rect().center  # .center (midtop/midbottom,...) is a attribute of the class Rect
# #                   >>>>>>>>>>>>> .get_rect() returns a pg.Rect

#rect 1
rect = Therect()
# a random block > rect 2
rect2  = pg.Rect((0,0,70,70))
rect2.center = screen.get_rect().center
rgb2 = (230,230,230)
def draw_rect2():
    pg.draw.rect(screen,rgb2,rect2,5)

# negotiate by an arrow
arrow = pg.image.load('arrow.png')
arrow_pos= arrow.get_rect(topleft = (0,10))
def draw_arrow():
    screen.blit(arrow,arrow_pos)
# sound
pong_sound = Sound()
angle = 0
def rotate_arrow(rect1,rect2):
    global angle
    if  rect2.y + rect2.height >= rect1.y >= rect2.y - 50:
        if rect1.x < rect2.x:
            angle = -90
            rotated_arrow = pg.transform.rotate(arrow,angle)
            screen.blit(rotated_arrow,arrow_pos)   
        else:
            angle = 90
            rotated_arrow = pg.transform.rotate(arrow,angle)
            screen.blit(rotated_arrow,arrow_pos)
    elif rect2.y - 50 > rect1.y :
        angle = 180
        rotated_arrow  = pg.transform.rotate(arrow,angle)
        screen.blit(rotated_arrow,arrow_pos)         
    else:
        screen.blit(arrow,arrow_pos)

def stay_in_range():
    if 0 <= rect.rect.x + rect.rectx <= screen.get_rect().width - rect.rect.width:#rect.x + rectx predict if will go outside         
        rect.rect.x += rect.rectx
    else:
        pong_sound.play_sound_touch_limit()
    if 0 <= rect.rect.y + rect.recty <= screen.get_rect().height - rect.rect.height:
        rect.rect.y += rect.recty 
    else:
        pong_sound.play_sound_touch_limit()
# score 
is_colliding = False
player_score  = Score()
#clash and collision
clash  = Clash()
# clash.clash_xy.center = rect2.center
counter =  0
def collision():
    global is_colliding,rgb2,counter
    if rect.rect.colliderect(rect2):
        is_colliding = True
        counter  = 10
        rect2.x = random.randint(0,730)
        rect2.y = random.randint(0,530)
        rgb2 = get_random_rgb()
        rect.rgb = rgb2
        pong_sound.play_ping_sound()


#text take time
text_surface =  player_score.font.render(f'Enter seconds to play :',True,(230,230,230) ) 
the_top_left = (width//2 + 80,0)
text_xy = text_surface.get_rect(topleft = the_top_left)
def show_text_time():
    screen.blit(text_surface,text_xy) 

rect_take_time  =  pg.Rect(0,0,90,30)
rect_take_time.x = text_xy.right
def draw_rect_take_time():
    pg.draw.rect(screen,(230,230,230),rect_take_time,2)

#TAKE SECONDS

sec_entered =  ''
sec_context =  player_score.font.render(sec_entered,True,(230,230,230))
def blit_time():
    screen.blit(sec_context,rect_take_time)

can_add = False
active = False
ti = 10

def write_time(event):
    global sec_entered,active,can_add,ti,time1,show
    if active:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                sec_entered = sec_entered[:-1]
            elif event.key == pg.K_RETURN:
                    try:
                        time1 = pg.time.get_ticks()
                        ti = int(sec_entered)
                        active = False
                        player_score.score = 0
                        player_score.context  = f"Score: {player_score.score}"
                        player_score.text = player_score.font.render(player_score.context,True,(230,230,230))
                        show = True
                        can_add = True
                        pg.display.flip()
                    
                    except ValueError:
                        no_letter_message = player_score.font.render('ERROR!',True,(255,0,0))
                        screen.blit(no_letter_message,(rect_take_time.x,rect_take_time.y  + 30))

            else:
                if not event.key == pg.K_r:
                    sec_entered += event.unicode            

def check_events(event,aclass):
    global ti,active,can_add,time1,show
    if event.type == pg.QUIT:
        exit()
    if event.type == pg.MOUSEBUTTONDOWN:
        if rect_take_time.collidepoint(event.pos):
            active = True
            pg.display.update()
    write_time(event)
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            aclass.rectx = -rect.speed_move
        if event.key == pg.K_RIGHT:
            aclass.rectx = rect.speed_move
        if event.key == pg.K_UP:
            aclass.recty = -rect.speed_move
        if event.key == pg.K_DOWN:
            aclass.recty = rect.speed_move
        if event.key == pg.K_q:
           exit()
        if event.key == pg.K_p:
           show = False
        if event.key == pg.K_r:
            if not can_add:
               player_score.reset_score(screen, 'highscore.txt', width // 2 - 150 , 100)
               player_score.show_high_score(screen,width,'highscore.txt')
    elif event.type == pg.KEYUP:
        if event.key in [pg.K_LEFT, pg.K_RIGHT]:
            aclass.rectx = 0
        if event.key in [pg.K_UP, pg.K_DOWN]:
            aclass.recty = 0
        if event.key == pg.K_q:
           exit()

def guide_reset():
    guide_reset = player_score.font.render('R = Reset',True,(230,230,230))
    screen.blit(guide_reset,(width//2 - 80,30))
running = True
# fps
clock = pg.time.Clock()
# Countdown for the end
time_to_stop = 1000
time_here =  0
show = True
#last

while running :
    screen.fill((0,0,0))
    is_colliding = False
    for event in pg.event.get():
        check_events(event,rect)

    
    sec_context =  player_score.font.render(sec_entered,True,(230,230,230))
    blit_time()

    draw_rect_take_time()
    show_text_time()
    stay_in_range()
    collision() 
    if counter >0:
       clash.show_clash(screen,(rect.rect.x-30,rect.rect.y-30))
       counter  -= 1 

    rotate_arrow(rect.rect,rect2)
    if can_add:
        time2  = pg.time.get_ticks() 
        time_past = (time2 - time1) //1000
        time_here  = ti-time_past
        time_context = player_score.font.render(f'Time Left: {time_here}',True,(230,230,230))              
        screen.blit(time_context,(0,arrow_pos.y + 100))
        player_score.add_score(is_colliding,can_add)
        player_score.show_the_score(screen,arrow_pos.y)

    if time_here < 0 and show :
        player_score.new_high_score(sec_entered,screen,width,'highscore.txt')
        player_score.score = 0
        rgb2 = rect.rgb = (0,255,255)
        can_add = False
    player_score.show_high_score(screen,width,'highscore.txt')
    guide_reset()
    pg.draw.rect(screen,rect.rgb, rect.rect,3)
    draw_rect2()

    clock.tick(60)
    pg.display.flip()


