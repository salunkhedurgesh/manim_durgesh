from manim import *
from manimlib import TexturedSurface, SurfaceMesh


class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Surface(
            lambda u, v: np.array([
                2 * np.cos(u),
                2 * np.sin(u),
                v
            ]), v_range=[-2, 2], u_range=[0, TAU],)
        torus2 = Surface(
            lambda u, v: np.array([
                1 * np.cos(u),
                1 * np.sin(u),
                v
            ]), v_range=[-2, 2], u_range=[0, TAU],)
        sphere = Surface(
            lambda u, v: np.array([
                np.cos(v) * np.cos(u),
                np.cos(v) * np.sin(u),
                np.sin(v)
            ]), v_range=[0, TAU], u_range=[0, TAU],)
        # You can texture a surface with up to two images, which will
        # be interpreted as the side towards the light, and away from
        # the light.  These can be either urls, or paths to a local file
        # in whatever you've set as the image directory in
        # the custom_config.yml file

        day_texture = "EarthTextureMap"
        # night_texture = "NightEarthTextureMap" day_texture =
        # "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px
        # -Whole_world_-_land_and_oceans.jpg" night_texture =
        # "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night
        # .jpg"

        self.play(FadeIn(sphere))
        print(f"The type of sphere is {type(sphere)}")
        ts1 = TexturedSurface(sphere, day_texture)
        self.add(ts1)
        self.wait(2)

