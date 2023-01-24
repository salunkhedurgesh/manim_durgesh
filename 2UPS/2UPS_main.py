from manim import *
from manim.opengl import *
from icra_supplementary import *
from icra_functions import *


class MakeTitle(Scene):
    def construct(self):
        title = Tex(r"Design optimization of a parallel manipulator for otological surgery").scale(0.8).shift(UP)
        authors = Tex(r"Durgesh Haribhau Salunkhe$^1$, Guillaume Michel$^2$, Elise Olivier$^2$ \\ Shivesh Kumar$^3$, "
                      r"Marcello Sanguineti$^4$, Damien Chablat$^1$").next_to(title, DOWN).scale(0.6)
        affiliations = Tex(r"$^1$ Laboratoire des Sciences du Numerique de Nantes, France\\"
                           r"$^2$ Centre Hospitalier Universitaire, Nantes, France \\"
                           r"$^3$ Robotics Innovation Center, DFKI GmbH, Bremen, Germany \\"
                           r"$^4$ Universita Degli Studi di Genova, Italy").next_to(authors, DOWN).scale(0.45)
        # icra_L = ImageMobject("icra_logo2.png").scale(0.1).move_to([-5, 2.5, 0])
        icra_L = ImageMobject("cfm_logo.png").scale(0.8).move_to([0, 2.5, 0])

        self.add(*[iter2 for iter2 in [title, authors, icra_L, affiliations]])
        self.wait(17)

        bottom_title = title.copy().scale(0.7).move_to([0, -3.7, 0])
        bottom_line = Line(start=[-7, -3.5, 0], end=[7, -3.5, 0], stroke_width=0.5)
        top_line = Line(start=[-7, 3.2, 0], end=[7, 3.2, 0], stroke_width=0.5)
        icra_L2 = icra_L.copy().scale(0.4).move_to([-6, 3.5, 0])
        self.play(*[FadeOut(k) for k in [authors, affiliations]])
        self.play(*[Transform(k, j) for k, j in zip([title, icra_L], [bottom_title, icra_L2])], Create(top_line),
                  Create(bottom_line))
        self.wait()
        self.clear()
        self.add(*get_Background("Table of Contents"))
        self.wait(2)


class Slide1(Scene):
    def construct(self):
        self.add(*get_Background("Table of Contents"))
        bullet_points = Tex(r"\begin{enumerate} \item Introduction \item Design Optimisation \item Results"
                            r"\item Conclusions and Future works \end{enumerate}")
        self.play(FadeIn(bullet_points.shift(LEFT * 3).scale(0.9)))
        self.wait(20)


class Results4(ThreeDScene):
    def construct(self):
        self.add_fixed_in_frame_mobjects(*get_Background("Results : structure comparison"))
        self.set_camera_orientation(theta=60 * DEGREES, phi=75 * DEGREES)
        first_robot = get_ParaRobot(
            [0.375, -1.75, 0.07, 0.75, -0.79, -0.06, 1.23, 1.26 + PI / 2, -0.15, 1.17, -0.24 + PI / 2, 0.19, 3.17],
            para_ext=False)
        second_robot = get_ParaRobot(
            [0.96, -1.38, 0.08, 0.82, 0.04, -0.05, 1, -0.96 + PI / 2, -0.14, 1, 0.6 + PI / 2, 0, 2.97], para_ext=False)
        third_robot = get_ParaRobot(
            [0.9, -0.51, 0.01, 1.07, -0.14, -0.02, 0.71, -0.55 + PI / 2, 0.08, 0.7, 0.98 + PI / 2, 0.08, 3.26],
            para_ext=False)
        self.add(first_robot.shift(LEFT * 4 + DOWN * 2), second_robot, third_robot.shift(RIGHT * 4 + DOWN * 2))


class Conclusions_Static(Scene):
    def construct(self):
        self.add(*get_Background("Conclusion and future work"))

        point1 = get_item("The optimisation algorithm is versatile in adapting to various constraints").shift(UP * 2.7)
        point2 = get_item("The surgeons feedback was useful to design reward strategies").next_to(point1, DOWN * 3)
        point3 = get_item("A collaborative effort between designers and surgeons from the design\\\\"
                          " phase is of paramount importance to avoid unnecessary delays at\\\\"
                          " later stages").next_to(point2, DOWN * 3)
        point4 = get_item("A physical prototype is in progress to assess the impact of \\\\feedback on design "
                          "efficiency")
        point4s = SurroundingRectangle(point4, stroke_color=YELLOW, stroke_width=1)
        p4g = Group(point4, point4s)

        self.add(point1)
        self.add(point2.shift(LEFT))
        self.add(point3.shift(LEFT * 0.25))
        self.add(p4g.shift(DOWN * 1.73, LEFT * 1.15))


class Slide2(Scene):
    def construct(self):
        self.add(*get_Background("Introduction : comparison of tools"))
        os = Tex("Otological Surgery", font_size=48).move_to([0, 2.8, 0])
        arrow1 = Arrow(start=os.get_bottom(), end=os.get_bottom() + LEFT * 2 + DOWN, stroke_width=1,
                       max_tip_length_to_length_ratio=0.1)
        arrow2 = Arrow(start=os.get_bottom(), end=os.get_bottom() + RIGHT * 2 + DOWN, stroke_width=1,
                       max_tip_length_to_length_ratio=0.1)
        endo = Tex("Endoscope", font_size=36).move_to(arrow1.get_end() + DOWN * 0.5)
        micro = Tex("Microscope", font_size=36).move_to(arrow2.get_end() + DOWN * 0.5)
        ## First Figure
        endo_img1 = ImageMobject("endo_proximity.png").scale(0.4).shift(LEFT * 2 + DOWN)
        endo_img1_cap = Tex(r"Better proximity to \\the operating area", font_size=28).move_to(
            endo_img1.get_bottom() + DOWN * 0.5)
        endo_img1F = Group(endo_img1_cap, endo_img1)
        micro_img1 = ImageMobject("micro_proximity.jpg").scale(0.18).shift(RIGHT * 2 + DOWN)
        micro_img1_cap = Tex(r"At least 25 cm\\from the operating area", font_size=28).move_to(
            micro_img1.get_bottom() + DOWN * 0.5)
        micro_img1F = Group(micro_img1, micro_img1_cap)

        ## Second Figure
        endo_img2 = ImageMobject("endo_view.png").scale(0.4).shift(LEFT * 2 + DOWN)
        endo_img2_cap = Tex(r"Close view to\\the operating area ", font_size=28).move_to(
            endo_img2.get_bottom() + DOWN * 0.5)
        endo_img2F = Group(endo_img2_cap, endo_img2)
        micro_img2 = ImageMobject("micro_view2.png").scale(1).shift(RIGHT * 2 + DOWN)
        micro_img2_cap = Tex(r"View through a funnel", font_size=28).move_to(
            micro_img2.get_bottom() + DOWN * 0.5)
        micro_img2F = Group(micro_img2, micro_img2_cap)

        ## Third Figure
        endo_img3 = ImageMobject("endo_proximity.png").scale(0.4).shift(LEFT * 2 + DOWN)
        endo_img3_cap = Tex(r"Limited to 1 instrument\\ at a time ", font_size=28).move_to(
            endo_img3.get_bottom() + DOWN * 0.5)
        endo_img3F = Group(endo_img3_cap, endo_img3)
        micro_img3 = ImageMobject("micro_2hands.png").scale(0.45).shift(RIGHT * 2 + DOWN)
        micro_img3_cap = Tex(r"Both hands available \\for operating", font_size=28).move_to(
            micro_img3.get_bottom() + DOWN * 0.5)
        micro_img3F = Group(micro_img3, micro_img3_cap)

        small_endo1 = endo_img1.copy().scale(0.6).move_to(endo.get_center() + LEFT * 3 + UP * 0.5)
        small_micro1 = micro_img1.copy().scale(0.6).move_to(micro.get_center() + RIGHT * 3.2 + UP * 0.5)
        small_endo2 = endo_img2.copy().scale(0.9).move_to(small_endo1.get_bottom() + DOWN)
        small_micro2 = micro_img2.copy().scale(0.7).move_to(small_micro1.get_bottom() + DOWN)
        small_endo3 = endo_img3.copy().scale(0.7).move_to(small_endo2.get_bottom() + DOWN)
        small_micro3 = micro_img3.copy().scale(0.8).move_to(small_micro2.get_bottom() + DOWN)

        endo_adv1 = Tex("Better proximity", font_size=36).next_to(endo, DOWN * 2)
        sea1 = SurroundingRectangle(endo_adv1, corner_radius=0.2).set_stroke(color=GREEN)
        endo_adv2 = Tex("Close view", font_size=36).next_to(endo_adv1, DOWN * 3)
        sea2 = SurroundingRectangle(endo_adv2, corner_radius=0.2).set_stroke(color=GREEN)
        endo_adv3 = Tex("1 instrument", font_size=36).next_to(endo_adv2, DOWN * 3)
        sea3 = SurroundingRectangle(endo_adv3, corner_radius=0.2).set_stroke(color=RED)
        micro_adv1 = Tex("25 cm distance", font_size=36).next_to(micro, DOWN * 2)
        sma1 = SurroundingRectangle(micro_adv1, corner_radius=0.2).set_stroke(RED)
        micro_adv2 = Tex("Tunnel view", font_size=36).next_to(micro_adv1, DOWN * 3)
        sma2 = SurroundingRectangle(micro_adv2, corner_radius=0.2).set_stroke(RED)
        micro_adv3 = Tex("2 instrument", font_size=36).next_to(micro_adv2, DOWN * 3)
        sma3 = SurroundingRectangle(micro_adv3, corner_radius=0.2).set_stroke(GREEN)

        self.add(os)
        self.wait()
        self.play(*[FadeIn(j) for j in [arrow1, arrow2, endo, micro]])
        self.wait(5)
        self.play(*[FadeIn(k) for k in [endo_img1, endo_img1_cap, micro_img1, micro_img1_cap]])
        self.wait(8)
        self.play(*[FadeOut(k) for k in [endo_img1_cap, micro_img1_cap]])
        self.play(*[Transform(j, k) for j, k in zip([endo_img1, micro_img1], [small_endo1, small_micro1])])
        self.add(endo_adv1, micro_adv1)
        self.play(*[Create(k) for k in [sea1, sma1]])
        self.wait(5)

        self.play(*[FadeIn(k) for k in [endo_img2, endo_img2_cap, micro_img2, micro_img2_cap]])
        self.wait(8)
        self.play(*[FadeOut(k) for k in [endo_img2_cap, micro_img2_cap]])
        self.play(*[Transform(j, k) for j, k in zip([endo_img2, micro_img2], [small_endo2, small_micro2])])
        self.add(endo_adv2, micro_adv2)
        self.play(*[Create(k) for k in [sea2, sma2]])
        self.wait(4)

        self.play(*[FadeIn(k) for k in [endo_img3, endo_img3_cap, micro_img3, micro_img3_cap]])
        self.wait(8)
        self.play(*[FadeOut(k) for k in [endo_img3_cap, micro_img3_cap]])
        self.play(*[Transform(j, k) for j, k in zip([endo_img3, micro_img3], [small_endo3, small_micro3])])
        self.add(endo_adv3, micro_adv3)
        self.play(*[Create(k) for k in [sea3, sma3]])
        self.wait(6)

        """
        Slide 3
        """
        self.clear()
        self.add(sea1, sea2, sea3, sma1, sma2, sma3, endo_adv1, endo_adv2, endo_adv3,
                 micro_adv1, micro_adv2, micro_adv3)
        self.play(*[Transform(j, k) for j, k in zip([*get_Background("Introduction : comparison of tools")],
                                                    [*get_Background("Introduction : the proposal")])])
        self.clear()
        micro3_g = Group(sma3, micro_adv3)
        micro3_g2 = micro3_g.copy().scale(2).move_to(ORIGIN)
        self.add(*get_Background("Introduction : the proposal"), sma3, micro_adv3)
        self.wait()
        self.play(Transform(micro3_g, micro3_g2))
        proposal = Tex(r"Design and optimise a mechanism \\that can act as an assistant to the surgeon \\"
                       r"in handling of the endoscope", font_size=36).next_to(micro3_g, DOWN * 1.5)
        self.play(FadeIn(proposal))
        self.wait(11)


class Slide4(ThreeDScene):
    def construct(self):
        self.add_fixed_in_frame_mobjects(*get_Background("Design of the mechanism"))
        self.set_camera_orientation(theta=60 * DEGREES, phi=75 * DEGREES)

        sph_joint = Sphere(radius=0.15, checkerboard_colors=[YELLOW, YELLOW], stroke_width=0.0001)
        a1 = a2 = 1
        b1 = b2 = 1.8
        h1 = h2 = 0
        h3 = h4 = 0.5
        t = 3.5
        theta1 = theta2 = phi1 = phi2 = 0
        offset = -3
        para_joint = -3

        # parameters = [a1, theta1, h1, a2, theta2, h2, b1, phi1, h3, b2, phi2, h4, t]
        rigid_link = get_ActiveLink([0, 0, offset], [a1 * np.cos(theta1), a1 * np.sin(theta1), offset + h1], radius=0.1)
        rigid_link2 = get_ActiveLink([0, 0, offset], [a2 * np.sin(theta2), a2 * np.cos(theta2), offset + h2],
                                     radius=0.1)
        sph_joint1 = sph_joint.copy().move_to([a1 * np.cos(theta1), a1 * np.sin(theta1), offset + h1])
        sph_joint2 = sph_joint.copy().move_to([a2 * np.sin(theta2), a2 * np.cos(theta2), offset + h2])

        active_leg = get_ActiveLink([a1 * np.cos(theta1), a1 * np.sin(theta1), offset + h1],
                                    [b1 * np.cos(phi1), b1 * np.sin(phi1), t + h3 + offset],
                                    link_color=[RED, RED], show_piston=True)
        active_leg2 = get_ActiveLink([a2 * np.sin(theta1), a2 * np.cos(theta1), offset + h2],
                                     [b2 * np.sin(phi1), b2 * np.cos(phi1), t + h4 + offset],
                                     link_color=[RED, RED], show_piston=True)

        rigid_link3 = get_ActiveLink([0, 0, offset + t + h3], [b1 * np.cos(phi1), b1 * np.sin(phi1), t + h3 + offset],
                                     radius=0.1)
        rigid_link4 = get_ActiveLink([0, 0, offset + t + h4], [b2 * np.sin(phi1), b2 * np.cos(phi1), t + h4 + offset],
                                     radius=0.1)

        sph_joint3 = sph_joint.copy().move_to([b1 * np.cos(phi1), b1 * np.sin(phi1), t + h3 + offset])
        sph_joint4 = sph_joint.copy().move_to([b2 * np.sin(phi1), b2 * np.cos(phi1), t + h4 + offset])

        mcg1 = get_ActiveLink([-0.4, 0, offset + t], [0.4, 0, offset + t], radius=0.15, link_color=[RED_B, RED_B])
        mcg2 = get_ActiveLink([0, -0.4, offset + t], [0, 0.4, offset + t], radius=0.15, link_color=[GREEN_C, GREEN_C])
        vert_link = get_ActiveLink([0, 0, offset], [0, 0, offset + t + max(h3, h4)], radius=0.1,
                                   link_color=[GOLD_D, GOLD_D])

        pj1 = get_ActiveLink([0, 0, offset + t + max(h3, h4)], [0, 0, offset + t + max(h3, h4) + 1], radius=0.05)
        pj2 = get_ActiveLink([0, 0, offset + t + max(h3, h4) + 1], [para_joint, 0, offset + t + max(h3, h4) + 1],
                             radius=0.05)
        pj3 = get_ActiveLink([0, 0, offset + t + max(h3, h4) + 0.5], [para_joint, 0, offset + t + max(h3, h4) + 0.5],
                             radius=0.05)
        tool = get_ActiveLink([para_joint, 0, offset + t + max(h3, h4) + 1], [para_joint, 0, offset + t], radius=0.05,
                              link_color=[LIGHT_PINK, LIGHT_PINK])

        robot = Group()
        robot.add(active_leg, active_leg2, rigid_link, rigid_link2, sph_joint1, sph_joint2)
        robot.add(rigid_link3, rigid_link4, sph_joint3, sph_joint4, mcg1, mcg2)
        robot.add(pj1, pj2, pj3, tool, vert_link)

        box1 = get_Box([a1 * np.cos(theta1), a1 * np.sin(theta1), offset + h1],
                       [b1 * np.cos(phi1), b1 * np.sin(phi1), t + h3 + offset], box_color=[YELLOW, YELLOW],
                       opacity=0.6, box_bre=0.8)
        box2 = get_Box([a2 * np.sin(theta2), a2 * np.cos(theta2), offset + h2],
                       [b2 * np.sin(phi2), b2 * np.cos(phi2), t + h4 + offset], box_color=[YELLOW, YELLOW],
                       opacity=0.6, box_bre=0.8)

        box3 = get_Box([0, 0, offset], [0, 0, t + max(h3, h4) + offset], box_color=[RED, RED],
                       opacity=0.6, box_bre=0.8)

        box4 = get_Box([0, 0, t + max(h3, h4) + offset + 0.25], [-3, 0, t + max(h3, h4) + offset + 0.25],
                       box_color=[TEAL_B, TEAL_B], opacity=0.6, box_bre=2, box_h=0.5)

        text1 = Tex(r"2U\underline{P}S - 1U mechanism \\~\\ U $\rightarrow$ Universal joint \\ P $\rightarrow$ "
                    r"Prismatic joint(actuated) \\ S $\rightarrow$ Spherical joint", font_size=30).shift(LEFT * 4)
        text2 = Tex(r"The motion constraint generator \\decides the type of degree of freedom \\ (2 orientations)",
                    font_size=30).move_to(text1.get_center() + LEFT * 0.5)
        text3 = Tex(r"A parallelogram joint is \\introduced to have a remote \\ center of rotation",
                    font_size=30).move_to(text1.get_center())
        text4 = Tex(r"The legs with actuated joints", font_size=30).shift(RIGHT * 4)
        text5 = Tex(r"The motion constraint generator", font_size=30).shift(RIGHT * 4)
        text6 = Tex(r"The parallelogram joint", font_size=30).shift(RIGHT * 4)

        connect_line = DashedLine(start=[0, 0, offset + t], end=[para_joint, 0, offset + t])

        self.play(*[FadeIn(k) for k in [rigid_link, rigid_link2, rigid_link3, rigid_link4]])
        self.wait()
        self.add_fixed_in_frame_mobjects(text1)
        self.play(*[FadeIn(k) for k in [sph_joint1, sph_joint2, sph_joint3, sph_joint4]])
        self.play(*[FadeIn(k) for k in [active_leg, active_leg2]])
        self.wait(16)
        self.play(FadeOut(text1))
        self.play(*[FadeIn(k) for k in [mcg1, mcg2, vert_link]])
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text2)
        self.wait(5)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.play(*[FadeIn(k) for k in [pj1, pj2, pj3, tool]])
        self.play(Create(connect_line))
        self.wait(5)

        self.play(FadeOut(text3), FadeOut(connect_line))

        self.play(*[FadeIn(k) for k in [box1, box2]])
        self.add_fixed_in_frame_mobjects(text4)
        self.wait(7)
        self.play(*[FadeOut(k) for k in [box1, box2, text4]])
        self.add_fixed_in_frame_mobjects(text5)
        self.play(*[FadeIn(k) for k in [box3]])
        self.wait(7)
        self.play(*[FadeOut(k) for k in [box3, text5]])
        self.add_fixed_in_frame_mobjects(text6)
        self.play(*[FadeIn(k) for k in [box4]])
        self.wait(7)


class ImplicitExample(Scene):
    def construct(self):
        ax = Axes(x_range=[-PI, PI], y_range=[-PI, PI], x_length=6, y_length=6, tips=False)
        a = ax.plot_implicit_curve(
            lambda theta2, theta3: (np.cos(theta2) - 0.75) * (38 * np.cos(theta2) * np.sin(theta3) * np.cos(theta3) +
                                                              41 * np.cos(theta2) * np.cos(theta3) ** 2
                                                              - 8 * np.cos(theta2) * np.sin(theta3) + 44 * np.cos(
                        theta2) * np.cos(theta3) +
                                                              7 * np.sin(theta3) * np.cos(theta3) + 24 * np.cos(
                        theta3) ** 2 - 8 * np.cos(theta2) -
                                                              12 * np.sin(theta3) + 16 * np.cos(theta3) - 12),
            color=BLUE
        )
        b = ax.plot_implicit_curve(
            lambda theta2, theta3: (np.cos(theta2) - 0.3) * (3 * np.cos(theta3) + 4) * (
                    np.cos(theta2) * np.cos(theta3) - 2 * np.cos(theta2) * np.sin(theta3) - np.sin(theta3)),
            color=BLUE
        )

        a, a_prime, h, hk, t = [1, 1, 0, 0, 1]
        para_sing = ax.plot_implicit_curve(
            lambda alpha, beta: np.cos(beta) ** 2 * np.sin(alpha) ** 2 * a * h * hk * t - np.cos(beta) ** 2 *
                                np.sin(alpha)
                                * np.cos(alpha) * a_prime * h * t ** 2 + np.cos(beta) ** 2 * np.sin(alpha) * np.cos(
                alpha)
                                * h * hk * t ** 2 + np.sin(beta) * np.sin(alpha) * np.cos(alpha) * a * a_prime * h * t -
                                np.sin(beta) * np.sin(alpha) * np.cos(alpha) * a * h * hk * t - np.cos(beta) *
                                np.sin(beta) * np.cos(alpha) ** 2 * a * a_prime * hk * t + np.cos(beta) * np.sin(beta) *
                                np.sin(alpha) * a * a_prime * h * t + np.cos(beta) * np.sin(beta) * np.sin(alpha) * a *
                                h * hk * t - np.cos(beta) * np.sin(beta) * np.sin(alpha) ** 2 * a * a_prime * hk * t +
                                np.cos(beta) ** 2 * np.cos(alpha) * a ** 2 * h ** 2 + np.cos(beta) * np.cos(
                alpha) ** 2 *
                                a_prime ** 2 * t ** 2 - np.cos(beta) * np.cos(alpha) ** 2 * hk ** 2 * t ** 2 - np.sin(
                beta)
                                * np.sin(alpha) * a ** 2 * a_prime ** 2 - np.sin(beta) * np.cos(
                alpha) * a * a_prime ** 2
                                * t + np.sin(beta) * np.cos(alpha) ** 2 * a_prime * h * t ** 2 - np.sin(beta) *
                                np.cos(alpha) ** 2 * h * hk * t ** 2 + np.cos(beta) * np.sin(
                alpha) * a ** 2 * a_prime * h
                                - np.cos(beta) ** 2 * np.sin(alpha) * a * h ** 2 * t + np.sin(beta) ** 2 * np.cos(
                alpha) *
                                a ** 2 * a_prime * hk + np.cos(beta) ** 2 * np.cos(alpha) ** 2 * a * a_prime * h * t +
                                np.cos(beta) * np.sin(beta) * np.sin(alpha) ** 2 * a * h ** 2 * t + np.cos(beta) *
                                np.sin(beta) * np.cos(alpha) ** 2 * a * h ** 2 * t - np.sin(beta) ** 2 * np.sin(
                alpha) ** 2
                                * a * a_prime * h * t - np.sin(beta) ** 2 * np.sin(alpha) * np.cos(alpha) * a_prime * h
                                * t ** 2 + np.sin(beta) ** 2 * np.sin(alpha) * np.cos(alpha) * h * hk * t ** 2 -
                                np.sin(beta) ** 2 * np.cos(alpha) ** 2 * a * h * hk * t - np.cos(beta) * np.sin(beta) *
                                np.cos(alpha) * a ** 2 * a_prime * h - np.cos(beta) * np.sin(beta) * np.cos(alpha) *
                                a ** 2 * h * hk + np.cos(beta) * np.sin(alpha) * np.cos(alpha) * a * a_prime ** 2 * t -
                                np.cos(beta) * np.sin(alpha) * np.cos(alpha) * a * hk ** 2 * t - np.sin(beta) ** 2 *
                                np.sin(alpha) * a * a_prime * hk * t + np.cos(beta) * np.cos(alpha) * a * a_prime *
                                h * t,
            color=RED,
        ).set_fill(YELLOW)
        c = Rectangle(height=5.95, width=5.95, stroke_width=1.5, stroke_color=WHITE)
        self.add(ax)
        self.clear()
        self.add(para_sing, c)
        # self.play(Create(b), run_time=5)


class StaticSlide(Scene):
    def construct(self):
        self.add(*get_Background("Nelder Mead : improvement"))
        # self.play(Write(Tex("Thank you", color=YELLOW).scale(3)), run_time=2)
        # self.wait(3)
        # self.play(Write(Tex("I am open to questions").shift(DOWN * 3)), run_time=2)
        # self.wait(5)


class Slide5(ThreeDScene):
    def construct(self):
        self.add(*get_Background("Optimisation : parameters"))
        # self.add_fixed_in_frame_mobjects(*get_Background("Design of the mechanism"))
        # self.set_camera_orientation(theta=60 * DEGREES, phi=75 * DEGREES)
        # self.add(get_ParaRobot())
        of = Tex(r"Objective function", font_size=36)
        ofs = SurroundingRectangle(of)
        obj_fun = Group(of, ofs).shift(UP * 2.5)
        obj_man = Tex(r"To maximize the global kinematic quality \\ \emph{and} \\ the total feasible workspace in the "
                      r"desired Regular Dextrous Workspace", font_size=30)

        sing_leg = Line(start=[0, 0, 0], end=[0.3, 0, 0], color=RED)
        sing_text = Tex(r"Singularities in the workspace \\ parameterized by $\alpha$ and $\beta$").next_to(sing_leg,
                                                                                                            RIGHT)
        leg_group = Group(sing_leg, sing_text)
        legend = Group(leg_group, SurroundingRectangle(leg_group, stroke_color=WHITE, stroke_width=1)).scale(0.6)
        self.play(FadeIn(obj_fun))
        self.play(FadeIn(obj_man.next_to(obj_fun, DOWN)))
        self.wait(6)
        sing_plot, circ1 = get_implicitplot(rdw="circ")
        sing_plot = sing_plot.scale(0.6).shift(DOWN)
        rdw_text = Tex(r"The regular dextrous \\workspace is a square \\ or a circle inside the workspace",
                       font_size=30).next_to(sing_plot, RIGHT)
        circ1 = circ1.scale(0.6).shift(DOWN)
        legend = legend.next_to(sing_plot, LEFT)
        self.play(FadeIn(sing_plot), FadeIn(legend))
        self.play(FadeIn(rdw_text))
        self.play(Create(circ1))
        rdw_rec = Square(side_length=1, stroke_width=1, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.6).move_to(
            circ1.get_center())
        self.wait(4)
        self.play(Transform(circ1, rdw_rec))
        self.wait(3)


class Slide6(ThreeDScene):
    def construct(self):
        self.add_fixed_in_frame_mobjects(*get_Background("Optimisation : parameters"))
        of = Tex(r"Constraints", font_size=36)
        ofs = SurroundingRectangle(of)
        obj_fun = Group(of, ofs).shift(UP * 2.5)
        obj_man = Tex(r"A point should belong to the feasible workspace:", font_size=30).next_to(obj_fun, DOWN)
        no_col = Tex(r"No collision in the active legs", font_size=30).shift(RIGHT * 4.5)
        no_sing = Tex(r"RDW should be singularity free", font_size=30).shift(DOWN + RIGHT * 4.5)
        no_limits = Tex(r"Passive joint limits are respected", font_size=30).shift(DOWN * 2 + RIGHT * 4.5)
        self.add_fixed_in_frame_mobjects(obj_fun)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(obj_man)
        colliding_robot = get_ParaRobot([1, 0, 0, 1, 0, 0, 1.8, 75 * DEGREES, 0.5, 2.5, -PI / 4, 0, 3.5])
        colliding_robot = colliding_robot.scale(0.6)
        sing_plot, circ1 = get_implicitplot(rdw="circ")
        sing_plot = sing_plot.scale(0.6).shift(DOWN)
        circ1 = circ1.scale(0.6).shift(DOWN)
        sing_plot2, circ2 = get_implicitplot(paras=[1, 1, 0, 0, 4], rdw="circ")
        sing_plot2 = sing_plot2.scale(0.6).shift(DOWN)
        circ2 = circ2.scale(0.6).shift(DOWN)

        self.set_camera_orientation(theta=60 * DEGREES, phi=75 * DEGREES)
        self.play(FadeIn(colliding_robot))
        self.add_fixed_in_frame_mobjects(no_col)
        self.wait(6)
        self.play(FadeOut(colliding_robot))
        self.wait()
        self.add_fixed_in_frame_mobjects(sing_plot, circ1)
        self.add_fixed_in_frame_mobjects(no_sing)
        self.wait(3)
        self.play(*[Transform(j, k) for j, k in
                    zip([sing_plot, circ1], [sing_plot.copy().shift(LEFT * 4), circ1.copy().shift(LEFT * 4)])])
        self.wait(4)
        self.add_fixed_in_frame_mobjects(sing_plot2, circ2)
        self.wait(4)
        self.add_fixed_in_frame_mobjects(no_limits)
        self.wait(5)


class Slide7(Scene):
    def construct(self):
        self.add(*get_Background("Feedbacks from surgeons"))
        input_point0 = "The feedback from surgeons was taken in two phases"
        input_point = "A simulated CAD environment was presented to the surgeons"
        input_point2 = "The speed and size of the components were close to the reality"
        point0 = get_item(input_point0, 36).shift(UP * 2.8)
        point1 = get_item(input_point, 36).next_to(point0, DOWN * 1.5)
        point2 = get_item(input_point2, 36).next_to(point1, DOWN * 1.5)

        img1 = ImageMobject("mannequinendo2.png").scale(2).shift(DOWN + LEFT * 4)
        img2 = ImageMobject("renderings.png").scale(0.6).shift(DOWN + RIGHT * 4)

        self.play(FadeIn(point0))
        self.wait(2)
        self.play(FadeIn(point1))
        self.wait(2)
        self.play(FadeIn(img1))
        self.play(FadeIn(img2))
        self.wait(4)
        self.play(FadeIn(point2))
        self.wait(5)


class Slide8(Scene):
    def construct(self):
        self.add(*get_Background("Feedbacks from surgeons"))
        input_point0 = get_item("In the first phase, the surgeons were from only one Hospital", 36).shift(UP * 2.7)
        input_point = get_item("In the second phase, surgeons across various hospitals over \\\\ France  participated",
                               36).next_to(input_point0, DOWN * 2)
        input_point2 = Tex(r"\begin{flushleft} \begin{itemize} \item The questionnaire for second feedback: \begin{"
                           r"itemize} "
                           r" \item had surgeons from different level of expertise "
                           r"\item Used a System Usability Scale to assess the learnability \item Aimed at "
                           r"understanding priorities of surgeons \end{itemize} \end{itemize}\end{flushleft}",
                           font_size=36).next_to(
            input_point, DOWN * 2)

        option1 = Tex("Speed").next_to(input_point2, DOWN * 2).shift(LEFT * 5)
        option1s = SurroundingRectangle(option1, stroke_color=YELLOW, corner_radius=0.1)
        option2 = Tex("Size").next_to(option1, RIGHT * 3.5)
        option2s = SurroundingRectangle(option2, stroke_color=YELLOW, corner_radius=0.1)
        option3 = Tex("Multi purpose").next_to(option2, RIGHT * 3.5)
        option3s = SurroundingRectangle(option3, stroke_color=YELLOW, corner_radius=0.1)
        option4 = Tex("Learning curve").next_to(option3, RIGHT * 3.5)
        option4s = SurroundingRectangle(option4, stroke_color=YELLOW, corner_radius=0.1)

        for j_iter in [input_point0, input_point, input_point2]:
            self.play(FadeIn(j_iter))
            self.wait(2)
        self.wait(10)

        for j_iter, k_iter in zip([option1, option2, option3, option4], [option1s, option2s, option3s, option4s]):
            self.play(*[FadeIn(m_iter) for m_iter in [j_iter, k_iter]])
            self.wait(2)


class NM_layer(Scene):
    def construct(self):
        self.add(*get_Background("Nelder Mead : layered constraints"))


class Slide9(Scene):
    def construct(self):
        self.add(*get_Background("Rewarding strategies"))

        first_text = Tex("Based on the feedback, we used 3 different rewarding strategies:", font_size=36).shift(
            UP * 2.7)
        input_point1 = get_item("Binary reward strategy", 36).next_to(first_text, DOWN * 2)
        input_point2 = get_item("Center biased reward strategy", 36).next_to(input_point1, DOWN * 2)
        input_point3 = get_item("Minimum quality constraint reward strategy", 36).next_to(input_point2, DOWN * 2)

        self.play(FadeIn(first_text))
        self.wait()
        self.play(FadeIn(input_point1))
        self.wait(2)
        self.play(FadeIn(input_point2))
        self.wait(2)
        self.play(FadeIn(input_point3))
        self.wait(3)


class Results1(Scene):
    def construct(self):
        self.add(*get_Background("Results : rewarding strategies"))
        sub_t = Tex("Results for binary reward strategy").shift(UP * 2.7)
        img1 = ImageMobject("binary_results.png").scale(0.16).next_to(sub_t, DOWN)
        bg_fill = BackgroundRectangle(img1, fill_color=WHITE, fill_opacity=1)
        img1_cap = Tex(
            r"Blank space:", r" Feasible workspace\\", "Circle:", r" Desired RDW \\", "Colored points:",
            " constraint violations",
            font_size=30).next_to(img1, DOWN).shift(LEFT * 2.5)
        for j in [0, 2, 4]:
            img1_cap[j].color = BLUE
        img1_cap2 = Tex(
            r"Heat map for the global \\conditioning index", font_size=30).next_to(img1_cap, RIGHT * 4)

        self.play(FadeIn(sub_t))
        self.wait()
        self.play(*[FadeIn(j) for j in [bg_fill, img1, img1_cap, img1_cap2]])
        self.wait(15)


class Results2(Scene):
    def construct(self):
        self.add(*get_Background("Results : rewarding strategies"))
        sub_t = Tex("Results for center biased reward strategy").shift(UP * 2.7)
        img1 = ImageMobject("biased_results.png").scale(0.16).next_to(sub_t, DOWN)
        bg_fill = BackgroundRectangle(img1, fill_color=WHITE, fill_opacity=1)
        img1_cap = Tex(
            r"Blank space:", r" Feasible workspace\\", "Circle:", r" Desired RDW \\", "Colored points:",
            " constraint violations",
            font_size=30).next_to(img1, DOWN).shift(LEFT * 2.5)
        for j in [0, 2, 4]:
            img1_cap[j].color = BLUE
        img1_cap2 = Tex(
            r"Heat map for the global \\conditioning index", font_size=30).next_to(img1_cap, RIGHT * 4)

        self.play(FadeIn(sub_t))
        self.wait()
        self.play(*[FadeIn(j) for j in [bg_fill, img1, img1_cap, img1_cap2]])
        self.wait(15)


class Results3(Scene):
    def construct(self):
        self.add(*get_Background("Results : rewarding strategies"))
        sub_t = Tex("Results for minimum quality constraint reward strategy").shift(UP * 2.7)
        img1 = ImageMobject("minqual_results.png").scale(0.16).next_to(sub_t, DOWN)
        bg_fill = BackgroundRectangle(img1, fill_color=WHITE, fill_opacity=1)
        img1_cap = Tex(
            r"Blank space:", r" Feasible workspace\\", "Circle:", r" Desired RDW \\", "Colored points:",
            " constraint violations",
            font_size=30).next_to(img1, DOWN).shift(LEFT * 2.5)
        for j in [0, 2, 4]:
            img1_cap[j].color = BLUE
        img1_cap2 = Tex(
            r"Heat map for the global \\conditioning index", font_size=30).next_to(img1_cap, RIGHT * 4)

        self.play(FadeIn(sub_t))
        self.wait()
        self.play(*[FadeIn(j) for j in [bg_fill, img1, img1_cap, img1_cap2]])
        self.wait(15)


class Conclusions(Scene):
    def construct(self):
        self.add(*get_Background("Conclusion and future work"))

        point1 = get_item("The optimisation algorithm versatile in adapting to various constraints was developed"). \
            shift(UP * 2.7).align_on_border(LEFT * 2)
        point2 = get_item("The surgeons feedback was useful to design reward strategies").next_to(point1, DOWN * 3). \
            align_to(point1, LEFT)
        point3 = get_item("A collaborative effort between designers and surgeons from the design\\\\"
                          " phase is of paramount importance to avoid unnecessary delays at\\\\"
                          " later stages").next_to(point2, DOWN * 3).align_to(point2, LEFT)
        point4 = get_item("A physical prototype is required to get better insights on the speed "
                          "comfortable for surgery").next_to(point3, DOWN * 3).align_to(point3, LEFT)
        point4s = SurroundingRectangle(point4, stroke_color=YELLOW, stroke_width=1)
        p4g = Group(point4, point4s)

        self.play(FadeIn(point1))
        self.wait(10)
        self.play(FadeIn(point2))
        self.wait(10)
        self.play(FadeIn(point3))
        self.wait(15)
        self.play(FadeIn(p4g))
        self.wait(15)


class Feedback1(Scene):
    def construct(self):
        self.add(*get_Background("Feedback from surgeons : methodology"))
        point1 = get_item("In the second phase, we sent a questionnaire to various French hospitals").shift(UP * 2.7)
        point2 = get_item("25 ENT specialists answered : ").next_to(point1, DOWN * 3)
        point3 = get_item("8 novice surgeons (< 10 years of ENT surgery experience)").next_to(point2, DOWN * 3)
        point4 = get_item("17 experienced surgeons (> 10 years of ENT surgery experience)").next_to(point3, DOWN * 3)

        self.play(FadeIn(point1))
        self.wait(2)
        self.play(FadeIn(point2.shift(LEFT)))
        self.wait(2)
        self.play(FadeIn(point3.shift(LEFT * 0.25)))
        self.wait(2)
        self.play(FadeIn(point4.shift(DOWN * 1.73, LEFT * 1.15)))
        self.wait(5)


class Feedback2(Scene):
    def construct(self):
        self.add(*get_Background("Feedback from surgeons : methodology"))
        point1 = get_item("The questionnaire starts with a short context, followed by a short video").shift(UP * 2.7)
        point2 = get_item("Speed : \\\\ - 3 videos showing a surgery of the sinus and ear with the surgical robot  "
                          "\\\\~\\\\ "
                          "- Participants were asked to evaluate the speed on a 5-points Likert scale ").next_to(
            point1, DOWN * 3).align_to(point1).align_to(point1, LEFT)
        point3 = get_item("created two different questionnaires with different video orders to account for the "
                          "influence of the order").next_to(point2, DOWN * 3).align_to(point2, LEFT)
        point4 = get_item("Priority : \\\\ participants were asked to classify four features (size, speed, easy to use,"
                          "compatibility for different surgeries such as ear and sinus)").next_to(point3, DOWN). \
            align_to(point3, LEFT)

        self.play(FadeIn(point1))
        self.wait(5)
        self.play(FadeIn(point2))
        self.wait(12)
        self.play(FadeIn(point3))
        self.wait(7)
        self.play(FadeIn(point4))
        self.wait(15)


class Feedback3(Scene):
    def construct(self):
        self.add(*get_Background("Feedback from surgeons : methodology"))
        point1 = get_item(
            "Perceived usability  : \\\\ based on the System usability Scale (Brook, 1996)").align_on_border(
            LEFT + UP * 3)
        point2 = get_item(
            "5 questions were asked  : \\\\ -	I think that I would like to use this surgical robot frequently"
            "\\\\ -	I found the surgical robot unnecessarily \\underline{complex}"
            "\\\\ - I thought the surgical robot was \\underline{easy to use}"
            "\\\\ -	I think most surgeons would \\underline{learn} to use this surgical robot \\underline{easily}"
            "\\\\ -	I \\underline{need to learn a lot} of things before using the surgical robot"). \
            next_to(point1, DOWN * 3).align_to(point1, LEFT)

        self.play(FadeIn(point1))
        self.wait(7)
        self.play(FadeIn(point2))
        self.wait(30)


class Feedback_Result(Scene):
    def construct(self):
        self.add(*get_Background("Feedback from surgeons"))
        feedback_image = ImageMobject("priority.png").scale(0.6).shift(DOWN)
        point1 = Tex("Answers about priority features of the surgical robot").align_on_border(UP * 3)

        self.play(FadeIn(point1))
        self.wait()
        self.play(FadeIn(feedback_image))
        self.wait(20)


class Feedback_Result(Scene):
    def construct(self):
        self.add(*get_Background("Results : Feedback from surgeons"))
        feedback_image = ImageMobject("priority.png").scale(0.6).shift(DOWN)
        point1 = Tex("Answers about priority features of the surgical robot").align_on_border(UP * 3)

        self.play(FadeIn(point1))
        self.wait()
        self.play(FadeIn(feedback_image))
        self.wait(20)
