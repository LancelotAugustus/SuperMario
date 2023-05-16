import pygame
from .. import setup, tools
from .. import constants as C


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.setup_state()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

    def setup_state(self):
        self.face_right = True
        self.dead = False
        self.big = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet = setup.GRAPHICS['mario_bros']
        self.right_frames = []
        self.left_frames = []
        self.up_frames = []
        self.down_frames = []
        frame_rects = [(178, 32, 12, 16), (80, 32, 15, 16), (96, 32, 16, 16), (112, 32, 16, 16)]
        for frame_rect in frame_rects:
            right_frame = tools.get_image(sheet, *frame_rect, (0, 0, 0), C.PLAYER_MULTI)
            left_frame = pygame.transform.flip(right_frame, True, False)
            up_frame = pygame.transform.rotate(right_frame, 90)
            down_frame = pygame.transform.rotate(right_frame, - 90)
            self.right_frames.append(right_frame)
            self.left_frames.append(left_frame)
            self.up_frames.append(up_frame)
            self.down_frames.append(down_frame)
        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self, keys):
        self.current_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
            self.y_vel = 0
            self.frames = self.right_frames
        elif keys[pygame.K_LEFT]:
            self.x_vel = - 5
            self.y_vel = 0
            self.frames = self.left_frames
        elif keys[pygame.K_UP]:
            self.x_vel = 0
            self.y_vel = - 5
            self.frames = self.up_frames
        elif keys[pygame.K_DOWN]:
            self.frames = self.down_frames
            self.x_vel = 0
            self.y_vel = 5
        if self.current_time - self.walking_timer > 100:
            self.walking_timer = self.current_time
            self.frame_index += 1
            self.frame_index %= 4
        self.image = self.frames[self.frame_index]
