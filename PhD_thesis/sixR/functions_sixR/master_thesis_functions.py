from manim import *
from manim.opengl import *


def get_mechline(base, u11vec, s12vec, u21vec, s22vec, tvec, zoom=1):
    base = base * zoom
    u11vec = u11vec * zoom
    s12vec = s12vec * zoom
    u21vec = u21vec * zoom
    s22vec = s22vec * zoom
    tvec = tvec * zoom
    max_s = np.maximum(s12vec[2], s22vec[2])

    tvecp1 = tvec + np.array([0.1, 0, 0]) * zoom
    tvecp2 = tvec - np.array([0.1, 0, 0]) * zoom
    tvecp3 = tvec + np.array([0, 0.1, 0]) * zoom
    tvecp4 = tvec - np.array([0, 0.1, 0]) * zoom

    first_leg = VGroup(Line(base, u11vec), Line(u11vec, s12vec),
                       Line(s12vec, np.array([0, 0, s12vec[2]])))
    second_leg = VGroup(Line(base, u21vec).set_color(BLUE),
                        Line(u21vec, s22vec).set_color(BLUE),
                        Line(s22vec, np.array([0, 0, s22vec[2]])).set_color(BLUE))
    third_leg = Line(base, np.array([tvec[0], tvec[1], max_s])).set_color(ORANGE)
    universal_joint = VGroup(Line(tvecp1, tvecp2).set_stroke(color=RED, width=3),
                             Line(tvecp3, tvecp4).set_stroke(color=RED, width=3))
    # All_dots = Group(u11, s12, u21, s22, t)
    return Group(first_leg, second_leg, third_leg, universal_joint)


def dTextbox(self, obj, width=10, font=18):
    self.width = width
    self.font = font
    self.wstr = str(self.width)
    self.text = obj

    if Tex(self.text).get_width() < self.width:
        return Tex(self.text, font=self.font, alignment="\\raggedright")
    else:
        return Tex("\\raggedright \\begin{minipage}{" + self.wstr + "cm}" + self.text + "\\end{minipage}",
                   font=self.font)


def get_sphere(vmin=0, vmax=TAU, radius=1, umin=0, umax=PI, color=None,
               tilt_axis=np.array([1, 0, 0]), tilt_angle=0):
    if color is None:
        color = [BLUE, GREEN]

    tmat = rodrigmat3_axis(tilt_angle=tilt_angle, tilt_axis=tilt_axis)
    class_sphere = Surface(
        lambda u, v: np.matmul(tmat, np.array(
            [radius * np.cos(v) * np.sin(u), radius * np.sin(v) * np.sin(u), radius * np.cos(u)])),
        resolution=(50, 50), checkerboard_colors=color, v_range=[vmin, vmax],
        u_range=[umin, umax], shade_in_3d=False,
    )
    return class_sphere


def get_cyl(vmin=0, vmax=3, radius=0.3, color=None, tilt_axis=np.array([1, 0, 0]), tilt_angle=0):
    if color is None:
        color = [RED, DARK_BLUE]
    radius = radius
    vmax = vmax
    vmin = vmin
    angle = tilt_angle
    axis = tilt_axis

    tmat = rodrigmat3_axis(tilt_angle=angle, tilt_axis=axis)
    my_cyl = Surface(
        lambda u, v: np.matmul(tmat, np.array([radius * np.cos(u), radius * np.sin(u), v])),
        resolution=(12, 12), checkerboard_colors=color, v_range=[vmin, vmax],
        u_range=[0, TAU], shade_in_3d=False,
    )
    return my_cyl


def rodrigmat3_axis(tilt_axis, tilt_angle):
    if np.linalg.norm(tilt_axis) == 0:
        return np.eye(3)
    else:
        axis = normalize(tilt_axis)
        angle = tilt_angle

        e11 = np.cos(angle) + axis[0] ** 2 * (1 - np.cos(angle))
        e12 = axis[0] * axis[1] * (1 - np.cos(angle)) - axis[2] * np.sin(angle)
        e13 = axis[1] * np.sin(angle) + axis[0] * axis[2] * (1 - np.cos(angle))

        e21 = axis[2] * np.sin(angle) + axis[0] * axis[1] * (1 - np.cos(angle))
        e22 = np.cos(angle) + axis[1] ** 2 * (1 - np.cos(angle))
        e23 = axis[1] * axis[2] * (1 - np.cos(angle)) - axis[0] * np.sin(angle)

        e31 = axis[0] * axis[2] * (1 - np.cos(angle)) - axis[1] * np.sin(angle)
        e32 = axis[0] * np.sin(angle) + axis[1] * axis[2] * (1 - np.cos(angle))
        e33 = np.cos(angle) + axis[2] ** 2 * (1 - np.cos(angle))

        return np.array([[e11, e12, e13], [e21, e22, e23], [e31, e32, e33]])
