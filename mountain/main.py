import pygame as pg
import moderngl as mgl
import struct
import sys
import numpy as np


class App:
    def __init__(self, win_size=(1600, 900)):
        # Pygame initialization
        pg.init()
        pg.mixer.init()  # Inicializar el mezclador de audio
        pg.display.set_mode(win_size, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        # Reproducir música de fondo
        pg.mixer.music.load('C:\\Users\\horby\\OneDrive\\Escritorio\\mountain\\waves.mp3')

  # Ruta al archivo de audio
        pg.mixer.music.play(-1)  # Reproducir en bucle infinito

        # Time objects
        self.clock = pg.time.Clock()

        # Load shaders
        with open('programs/vertex.glsl') as f:
            vertex = f.read()
        with open('programs/fragment.glsl') as f:
            fragment = f.read()
        self.program = self.ctx.program(vertex_shader=vertex, fragment_shader=fragment)

        # Quad screen vertices
        vertices = [(-1, -1), (1, -1), (1, 1), (-1, 1), (-1, -1), (1, 1)]
        vertex_data = struct.pack(f'{len(vertices) * len(vertices[0])}f', *sum(vertices, ()))
        self.vbo = self.ctx.buffer(vertex_data)
        self.vao = self.ctx.vertex_array(self.program, [(self.vbo, '2f', 'in_position')])

        # Uniforms
        self.set_uniform('u_resolution', win_size)

        # Camera attributes
        self.camera_pos = np.array([220.0, 50.0, 220.0], dtype=np.float32)
        self.camera_front = np.array([0.0, 0.0, -1.0], dtype=np.float32)
        self.camera_up = np.array([0.0, 1.0, 0.0], dtype=np.float32)
        self.camera_speed = 1.0  # Aumentar la velocidad de movimiento
        self.last_mouse_x, self.last_mouse_y = pg.mouse.get_pos()
        self.yaw, self.pitch = -90.0, 0.0
        pg.mouse.set_visible(False)
        pg.event.set_grab(True)

    def render(self):
        self.ctx.clear()
        self.vao.render()
        pg.display.flip()

    def update(self):
        self.set_uniform('u_time', pg.time.get_ticks() * 0.001)
        self.set_uniform('camera_pos', tuple(self.camera_pos))
        self.handle_keys()
        self.handle_mouse()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.render()
            self.clock.tick(60)
            fps = self.clock.get_fps()
            pg.display.set_caption(f'{fps:.1f} FPS')

    def set_uniform(self, u_name, u_value):
        try:
            self.program[u_name] = u_value
        except KeyError:
            pass

    def destroy(self):
        self.vbo.release()
        self.program.release()
        self.vao.release()
        pg.mixer.music.stop()  # Detener la música al salir

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.destroy()
                pg.quit()
                sys.exit()

    def handle_keys(self):
        keys = pg.key.get_pressed()
        camera_speed = self.camera_speed
        if keys[pg.K_w]:
            self.camera_pos += camera_speed * self.camera_front
        if keys[pg.K_s]:
            self.camera_pos -= camera_speed * self.camera_front
        if keys[pg.K_a]:
            self.camera_pos -= np.cross(self.camera_front, self.camera_up) * camera_speed
        if keys[pg.K_d]:
            self.camera_pos += np.cross(self.camera_front, self.camera_up) * camera_speed
        if keys[pg.K_UP]:
            self.camera_pos += camera_speed * self.camera_up
        if keys[pg.K_DOWN]:
            self.camera_pos -= camera_speed * self.camera_up

    def handle_mouse(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        x_offset = mouse_x - self.last_mouse_x
        y_offset = self.last_mouse_y - mouse_y  # Reversed since y-coordinates range from bottom to top
        self.last_mouse_x, self.last_mouse_y = mouse_x, mouse_y

        sensitivity = 0.1
        x_offset *= sensitivity
        y_offset *= sensitivity

        self.yaw += x_offset
        self.pitch += y_offset

        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0

        front = np.array([
            np.cos(np.radians(self.yaw)) * np.cos(np.radians(self.pitch)),
            np.sin(np.radians(self.pitch)),
            np.sin(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))
        ], dtype=np.float32)
        self.camera_front = front / np.linalg.norm(front)


if __name__ == '__main__':
    app = App()
    app.run()
