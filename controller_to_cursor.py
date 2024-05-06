import pygame
import pyautogui


pygame.init()
pygame.joystick.init()

xbox_controllers = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

if xbox_controllers:
    controller = xbox_controllers[0]
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    while True:
        time = clock.tick(320)
        pygame.event.pump()

        left_x = controller.get_axis(0)
        left_y = controller.get_axis(1)

        mouse_pos = pyautogui.position()
        new_pos = (mouse_pos[0] + (left_x * 10), mouse_pos[1] + (left_y * 10))

        pyautogui.moveTo(new_pos[0], new_pos[1])

        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN and event.button == 1:
                pygame.quit()
                exit()
