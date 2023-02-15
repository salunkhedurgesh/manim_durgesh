from manim import *
from manim.opengl import *
import math

"""
Note : The main difference between Transform and ReplacementTransform
Transform(A, B) : A becomes B
ReplacementTransform(A, B) : A stays separate from B
TransformFromCopy(A, B) : A's copy remains on the screen and A is transformed to B
                          It is hard to then make the copy disappear as we do not have a handle on it
"""


class FirstAnim(Scene):
    def construct(self):
        circle = Circle().set_fill(color=PINK, opacity=0.5)
        square = Square().flip(RIGHT).rotate(-3 * TAU / 8)
        square2 = square.copy().scale(2)
        self.play(Create(circle))
        self.play(ReplacementTransform(circle, square))
        self.wait()
        self.play(Transform(square, square2), time=2)
        self.play(TransformFromCopy(square2, square2.scale(0.5)))
        self.wait()


class SecondAnim(Scene):
    def construct(self):
        circle = Circle(radius=1, color=RED)
        dot = Dot()
        dot2 = dot.copy().move_to([1, 0, 0])
        line = Line([3, 0, 0], [5, 0, 0])

        # self.add(dot)
        self.add(line)
        self.play(GrowFromCenter(circle))
        self.play(FadeIn(dot2))
        self.wait(0.1)
        self.play(MoveAlongPath(dot2, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=np.array([2, 0, 0])), run_time=1.5)
        self.wait()


class OneJointOneLink(ThreeDScene):
    def construct(self):
        joint = OpenGLSurface(
            lambda u, v: (
                0.1 * np.cos(u),
                0.1 * np.sin(u),
                v),
            v_range=[-0.2, 0.2], u_range=[0, TAU], color=RED_D
        ).shift([0, 0, -1.5])

        link = OpenGLSurface(
            lambda u, v: (
                0.075 * np.cos(u),
                0.075 * np.sin(u),
                v),
            v_range=[-0.5, 0.5], u_range=[0, TAU], color=YELLOW_D
        ).shift([0, 0, -1.5])

        link2 = link.copy()
        joint2 = get_RobotJoint(np.array([0, 1, -1.5]), np.array([0, 1, 0]), joint_color=BLUE_D)
        link2.shift([0, 1, 0.5])
        link = link.rotate(PI / 2, axis=np.array([0.1, 0, 0])).shift([0, 0.5, 0])
        link3 = get_RobotLink(np.array([0, 0, 0]), np.array([0, 0, 2]))
        first_frame = get_Frame([0, 0, 0], [0, 0, 1])
        self.add(first_frame)
        self.play(self.camera.animate.set_euler_angles(phi=90 * DEGREES))
        self.play(self.camera.animate.scale(0.5))
        self.play(FadeIn(joint, link))
        self.play(self.camera.animate.set_euler_angles(theta=90 * DEGREES))
        self.play(FadeIn(joint, link, joint2, link2))
        self.wait()
        self.play(Create(link3))

        # for i in range(5):
        #     self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, zoom=2 * i / 10 + 0.1)
        #     self.wait(0.1)


class CheckFrame(ThreeDScene):
    def construct(self):
        x_axis = Arrow3D(start=[0, 0, 0], end=[1, 0, 0]).set_color(RED)
        y_axis = Arrow3D(start=[0, 0, 0], end=[0, 1, 0]).set_color(GREEN)
        z_axis = Arrow3D(start=[0, 0, 0], end=[0, 0, 1] / la.norm(np.array([0, 0, 1]))).set_color(BLUE)
        self.camera.set_euler_angles(theta=30 * DEGREES, phi=30 * DEGREES)
        k = Group(x_axis, y_axis, z_axis)
        m = get_Frame([0, 0, 0], np.eye(3, 3), scale=0.5)
        n = get_Frame([0, 0, 0], np.eye(3, 3), scale=2)
        self.add(k)
        self.play(FadeOut(k))
        self.wait()
        self.add(m)
        for i2 in range(2):
            self.play(self.camera.animate.set_euler_angles(theta=60 * DEGREES, phi=60 * DEGREES))
            self.play(self.camera.animate.set_euler_angles(theta=80 * DEGREES, phi=10 * DEGREES))
            if i2 == 0:
                self.play(ReplacementTransform(m, n))
                self.play(self.camera.animate.set_euler_angles(theta=10 * DEGREES, phi=750 * DEGREES))
                print(f"The frame height is {self.camera.frame_shape}")
                self.play(self.camera.animate.shift(UP * 3))
                print(f"The frame height after shifting up is {self.camera.frame_shape}")
                self.play(self.camera.animate.shift(DOWN * 3))
                print(f"The frame height after re-shifting is {self.camera.frame_shape}")

        self.wait()


class Covering(ThreeDScene):
    def construct(self):
        self.camera.set_euler_angles(theta=30 * DEGREES, phi=30 * DEGREES)
        covering1 = OpenGLSurface(
            lambda u, v: (
                v * np.cos(u),
                v * np.sin(u),
                0.2),
            u_range=[0, TAU], v_range=[0, 0.1], color=YELLOW_D
        )
        self.add(covering1)


class AnimateRobot2(ThreeDScene):
    def construct(self):
        d_list = [245, -150, -150, 540, 150, 160]
        a_list = [0, 710, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, PI / 2, -PI / 2, 0]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]
        theta_list = adapt_2Pi([-0.85, 2.3138080772012836773, -0.6781533894384433379,
                                -0.11433000418458210166, 0.15294147166034383606, 2.46])
        theta_list_inter1 = adapt_2Pi([-0.85, 2.71573821e-02, 6.81434159e-02, 8.35356126e-01, 4.31228851e-04, 2.46])
        theta_list_inter2 = adapt_2Pi([-0.85, -1.47772586e+00, 1.19056044e+00, -1.47537815e+00, -2.69837580e+00, 2.46])
        theta_list2 = adapt_2Pi([2.2888967063871344502, 0.82778457638851243458, 3.8197460430282402772,
                                 3.0272626494052111684, 0.15294147166034300337, 2.46])

        each_iteration = 50
        total_iterations = 100
        offset = 0
        key_points = [theta_list, theta_list_inter1, theta_list_inter2, theta_list2]

        # theta_list = [0, PI / 2, -PI / 3, PI, 0, 0]
        if key_points is None or len(key_points) < 2:
            raise ValueError("The key points are either empty or only 1 configuration is mentioned\n"
                             "Please mention least 2 arrays of length 6 that will act as the start and end point"
                             "of the trajectory to plot")

        if len(key_points) == 2:
            intermediate_theta = get_interpolation_vector(key_points[0], key_points[1],
                                                          total_iterations=total_iterations,
                                                          each_iteration=each_iteration)
        else:
            via_points = []
            for vi in range(1, len(key_points) - 1):
                via_points.append(key_points[vi])
            intermediate_theta = get_interpolation_vector(key_points[0], key_points[-1],
                                                          via_points=via_points, total_iterations=total_iterations)

        ee_point_vec = []
        ee_trace = Group()

        self.camera.scale(4)
        self.camera.set_euler_angles(theta=-45 * DEGREES, phi=90 * DEGREES)

        rob_ins = get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset)
        ee_point, ee_R = get_FrameMatrix(d_list, key_points[0], a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        self.add(rob_ins)
        self.add(get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset,
                                   opacity=0.25))
        for anim_iter in range(1, len(intermediate_theta)):
            ee_point, ee_R = get_FrameMatrix(d_list, intermediate_theta[anim_iter], a_list, alpha_list,
                                             6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(Line3D(start=ee_point_vec[-2], end=ee_point, color=WHITE, thickness=0.05, fill_opacity=1))

            self.play(Transform(rob_ins, get_RobotInstance(d_list, intermediate_theta[anim_iter], a_list,
                                                           alpha_list, offset=offset)),
                      run_time=0.05)
            self.add(ee_trace)
            if np.mod(anim_iter, 100 / 4) == 0:
                ghost_instance = get_RobotInstance(d_list, intermediate_theta[anim_iter], a_list,
                                                   alpha_list, offset=offset, opacity=0.25, show_frame=True)
                self.add(ghost_instance)

        self.wait()
        self.play(self.camera.animate.set_euler_angles(theta=360 * DEGREES, phi=90 * DEGREES), run_time=5)
        self.wait()


class TracedPathExample(Scene):
    def construct(self):
        circ = Circle(color=YELLOW_D).shift(4 * LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = Group(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.2))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8 * RIGHT), run_time=4, rate_func=linear)


class TempCheck(Scene):
    def construct(self):
        circ = Line(start=[0, 0, 0], end=[0, 1, 1])
        square = Square()
        self.add(circ, square)


class GenerateHyperboloid(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=-45 * DEGREES, theta=35.624 * DEGREES)
        self.add(Line(start=[-1, 0.5, -2], end=[1, 0.5, 2]))
        for gi in np.arange(0, 2 * PI, 0.1):
            self.add(Line(start=[-1, 0.5, -2], end=[1, 0.5, 2]).rotate(angle=gi, about_point=[0, 0, 0]))
            self.wait(0.1)


class TempCheck2(ThreeDScene):
    def construct(self):
        self.camera.set_euler_angles(phi=75 * DEGREES, theta=30 * DEGREES)
        a, c = 1, 1
        hyperboloid = OpenGLSurface(
            lambda u, v: np.array([
                a * math.sqrt(1 + u ** 2) * np.cos(v),
                a * math.sqrt(1 + u ** 2) * np.sin(v),
                c * u
            ]), u_range=[-1, 1], v_range=[0, TAU], color=BLUE_D, opacity=1, gloss=0.8
        )

        torus = Torus()
        self.play(Create(hyperboloid), run_time=4)
        self.play(FadeOut(hyperboloid))
        self.play(Create(torus))
        self.wait()

        circ = Circle(color=YELLOW_D).shift(4 * LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = Group(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.2))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8 * RIGHT), run_time=4, rate_func=linear)


class Slide25(ThreeDScene):
    def construct(self):
        # self.camera.set_euler_angles(phi=PI / 2.5, theta=PI / 2 - np.deg2rad(30))
        self.set_camera_orientation(theta=PI / 2 - np.deg2rad(30))
        self.set_camera_orientation(phi=PI / 2.5)

        base = np.array([0, 0, -0.5])
        tvec = np.array([0, 0, 1 + base[2]])
        u11vec = np.array([0.25, -0.15, 0.05 + base[2]])
        s12vec = np.array([0.5, 0.2, 1.05 + base[2]])
        u21vec = np.array([0.1, 0.25, -0.05 + base[2]])
        s22vec = np.array([-0.1, 0.5, 0.9 + base[2]])

        u21short = np.array([0, 0.75, -1.5])
        u11short = np.array([0.75, 0, -1.5])
        u21long = np.array([0, 3.5, -1.5])
        u11long = np.array([3.5, 0, -1.5])

        u11vec2 = np.array([0.25, 0, base[2]])
        u21vec2 = np.array([0, 0.25, base[2]])
        s12vec2 = np.array([0.65, 0, 1.1 + base[2]])
        s22vec2 = np.array([0, 0.65, 1.1 + base[2]])
        mzoom = 3
        my_mech = get_mechline(base, u11vec, s12vec, u21vec, s22vec, tvec, 6)
        my_mech2 = get_mechline(base, u11vec, s12vec, u21vec, s22vec, tvec, zoom=mzoom)
        my_mech3 = get_mechline(base, u11vec2, s12vec2, u21vec2, s22vec2, tvec, zoom=mzoom)
        my_mech4 = get_mechline(base, u11vec, s12vec, u21vec2, s22vec, tvec, 3)
        my_mech5 = get_mechline(base, u11vec, s12vec, u21vec, s22vec2, tvec, 3)
        my_mech6 = get_mechline(base, u11vec2, s12vec2, u21vec2, s22vec2, tvec, 3)

        para13 = Tex("Total 13 parameters to define", width=6).to_edge(RIGHT)
        exp1 = Tex("3 $\\times$ 4 joints = 12", width=6).next_to(para13, DOWN)
        exp2 = Tex("+ 1 for the height of universal joint", width=6).next_to(exp1, DOWN)

        exp3 = Tex("We use human intuition to reduce the dimension of the optimisation space to 4",
                             width=4.5).to_edge(RIGHT).shift(UP * 1.5)
        exp4 = Tex("The extra constraints we imply are: \\begin{itemize} \\item Both the legs are identical "
                             "in dimensions \\item The legs are 90 degrees apart \\item The leg1 is along "
                        "x-axis\\end{itemize}",
                             width=4.5).next_to(exp3, DOWN)

        self.play(FadeIn(my_mech2), run_time=2)
        self.wait(2)

        sphere1 = get_sphere(radius=0.2).move_to(u11vec * mzoom)
        sphere2 = get_sphere(radius=0.2).move_to(s12vec * mzoom)
        sphere3 = get_sphere(radius=0.2).move_to(u21vec * mzoom)
        sphere4 = get_sphere(radius=0.2).move_to(s22vec * mzoom)
        cyl = get_cyl(vmin=base[2] * mzoom, vmax=tvec[2] * mzoom, radius=0.1)
        group = Group(my_mech2, sphere1, sphere2, sphere3, sphere4, cyl)

        sphere5 = get_sphere(radius=0.2).move_to(u11vec2 * mzoom)
        sphere6 = get_sphere(radius=0.2).move_to(s12vec2 * mzoom)
        sphere7 = get_sphere(radius=0.2).move_to(u21vec2 * mzoom)
        sphere8 = get_sphere(radius=0.2).move_to(s22vec2 * mzoom)
        cyl2 = get_cyl(vmin=base[2] * mzoom, vmax=tvec[2] * mzoom, radius=0.1)
        group2 = Group(my_mech3, sphere5, sphere6, sphere7, sphere8, cyl2)

        line1 = DashedLine(start=base * mzoom, end=np.array([5, 0, base[2] * mzoom]))
        line2 = DashedLine(start=base * mzoom, end=np.array([0, 5, base[2] * mzoom]))
        line3 = DashedLine(start=np.array([0, 0, s12vec2[2] * mzoom]), end=np.array([5, 0, s12vec2[2] * mzoom]))
        line4 = DashedLine(start=np.array([0, 0, s12vec2[2] * mzoom]), end=np.array([0, 5, s22vec2[2] * mzoom]))

        lf1 = Line(start=base * mzoom, end=u11vec2 * mzoom).set_stroke(width=7, color=RED)
        lf2 = Line(start=base * mzoom, end=u21vec2 * mzoom).set_stroke(width=7, color=RED)
        botgro = Group(lf1, lf2)
        lf3 = Line(start=np.array([0, 0, s12vec2[2]]) * mzoom, end=s12vec2 * mzoom).set_stroke(width=7, color=RED)
        lf4 = Line(start=np.array([0, 0, s22vec2[2]]) * mzoom, end=s22vec2 * mzoom).set_stroke(width=7, color=RED)
        topgro = Group(lf3, lf4)

        angle = Arc(
            radius=1,
            start_angle=line1.get_angle(),
            angle=line2.get_angle(),
            color=RED,
        )
        angle.move_to(base * mzoom)
        self.add_fixed_in_frame_mobjects(para13)
        for item in [sphere1, sphere2, sphere3, sphere4, cyl]:
            self.play(FadeIn(item))
            self.wait()
            if item == sphere1:
                self.add_fixed_in_frame_mobjects(exp1)
            elif item == sphere4:
                self.add_fixed_in_frame_mobjects(exp2)
        self.wait(2)

        self.remove(my_mech2, sphere1, sphere2, sphere3, sphere4, cyl, para13, exp1, exp2)
        self.add(group)
        self.play(Transform(group, group.copy().move_to(np.array([4, 0, 0]))))

        self.add_fixed_in_frame_mobjects(exp3)
        self.wait(2)
        self.play(FadeIn(my_mech3))
        for item in [sphere5, sphere6, sphere7, sphere8, cyl2]:
            self.play(FadeIn(item))
            self.wait()
            if item == sphere6:
                self.add_fixed_in_frame_mobjects(exp4)

        for item in [botgro, topgro]:
            self.play(FadeIn(item))
            self.wait()
            self.play(FadeOut(item))
            self.wait()

        for item in [line1, line2, line3, line4, angle]:
            self.play(Create(item))
            self.wait()

        self.wait(2)


class Slide25N(ThreeDScene):
    def construct(self):
        # self.camera.set_euler_angles(phi=PI / 2.5, theta=PI / 2 - np.deg2rad(30))
        self.set_camera_orientation(theta=PI / 2 - np.deg2rad(30))
        self.set_camera_orientation(phi=PI / 2.5)

        base = np.array([0, 0, -0.5])
        tvec = np.array([0, 0, 1 + base[2]])
        u11vec = np.array([0.25, -0.15, 0.05 + base[2]])
        s12vec = np.array([0.5, 0.2, 1.05 + base[2]])
        u21vec = np.array([0.1, 0.25, -0.05 + base[2]])
        s22vec = np.array([-0.1, 0.5, 0.9 + base[2]])

        u21short = np.array([0, 0.75, -1.5])
        u11short = np.array([0.75, 0, -1.5])
        u21long = np.array([0, 3.5, -1.5])
        u11long = np.array([3.5, 0, -1.5])

        u11vec2 = np.array([0.25, 0, base[2]])
        u21vec2 = np.array([0, 0.25, base[2]])
        s12vec2 = np.array([0.65, 0, 1.1 + base[2]])
        s22vec2 = np.array([0, 0.65, 1.1 + base[2]])
        mzoom = 3
        my_mech = get_mechline(base, u11vec, s12vec, u21vec, s22vec, tvec, 6)
        my_mech2 = get_mechline(base, u11vec, s12vec, u21vec, s22vec, tvec, zoom=mzoom)
        my_mech3 = get_mechline(base, u11vec2, s12vec2, u21vec2, s22vec2, tvec, zoom=mzoom)
        my_mech4 = get_mechline(base, u11vec, s12vec, u21vec2, s22vec, tvec, 3)
        my_mech5 = get_mechline(base, u11vec, s12vec, u21vec, s22vec2, tvec, 3)
        my_mech6 = get_mechline(base, u11vec2, s12vec2, u21vec2, s22vec2, tvec, 3)

        para13 = Tex("Total 13 parameters to define", width=6).to_edge(RIGHT)
        exp1 = Tex("3 $\\times$ 4 joints = 12", width=6).next_to(para13, DOWN)
        exp2 = Tex("+ 1 for the height of universal joint", width=6).next_to(exp1, DOWN)

        exp3 = Tex("We use human intuition to reduce the dimension of the optimisation space to 4",
                   width=4.5).to_edge(RIGHT).shift(UP * 1.5)
        exp4 = Tex("The extra constraints we imply are: \\begin{itemize} \\item Both the legs are identical "
                   "in dimensions \\item The legs are 90 degrees apart \\item The leg1 is along "
                   "x-axis\\end{itemize}",
                   width=4.5).next_to(exp3, DOWN)

        sphere1 = get_sphere(radius=0.2).move_to(u11vec * mzoom)
        sphere2 = get_sphere(radius=0.2).move_to(s12vec * mzoom)
        sphere3 = get_sphere(radius=0.2).move_to(u21vec * mzoom)
        sphere4 = get_sphere(radius=0.2).move_to(s22vec * mzoom)
        cyl = get_cyl(vmin=base[2] * mzoom, vmax=tvec[2] * mzoom, radius=0.1)
        group = Group(my_mech2, sphere1, sphere2, sphere3, sphere4, cyl)

        sphere5 = get_sphere(radius=0.2).move_to(u11vec2 * mzoom)
        sphere6 = get_sphere(radius=0.2).move_to(s12vec2 * mzoom)
        sphere7 = get_sphere(radius=0.2).move_to(u21vec2 * mzoom)
        sphere8 = get_sphere(radius=0.2).move_to(s22vec2 * mzoom)
        cyl2 = get_cyl(vmin=base[2] * mzoom, vmax=tvec[2] * mzoom, radius=0.1)
        group2 = Group(my_mech3, sphere5, sphere6, sphere7, sphere8, cyl2)


        self.add(my_mech)
        self.wait()
        self.remove(my_mech)
        self.play(FadeIn(group2))
        self.wait(3)


class justCheck(ThreeDScene):
    def construct(self):
        class_sphere = Surface(
            lambda u, v:  np.array([0.2 * np.cos(v) * np.sin(u), 0.2 * np.sin(v) * np.sin(u), 0.2 * np.cos(u)]),
            v_range=[0, TAU], u_range=[0, PI]
        )
        self.add(class_sphere)


class UseZoomedScene(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.2,
            zoomed_display_height=1,
            zoomed_display_width=12,
            image_frame_stroke_width=8,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs
        )

    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(1)

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(ORIGIN)
        frame.set_color(RED)

        zoomed_display_frame.set_color(RED)

        zoomed_display.to_edge(RIGHT).shift(DOWN*5)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        self.play(Create(frame))

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )
        self.play(dot.animate.shift(LEFT))
        self.wait(3)
        self.play(dot.animate.shift(RIGHT))
        self.wait(2)