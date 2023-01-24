from functions_durgesh.robot_functions import make_paths
from functions_durgesh.maple_functions import *
from functions_durgesh.icra_functions import *
import pandas as pd
from manim.utils.color import GREEN, GOLD_A


class MakeTitle(Scene):
    def construct(self):
        title = Tex(r"Trajectory planning problems in commercial cuspidal robots").scale(0.8).shift(UP)
        authors = Tex(r"Durgesh Haribhau Salunkhe$^1$, Damien Chablat$^1$ \\ "
                      r"Philippe Wenger$^1$").next_to(title, DOWN).scale(0.6)
        affiliations = Tex(r"$^1$ Laboratoire des Sciences du Numerique de Nantes, France").next_to(authors,
                                                                                                    DOWN).scale(0.45)
        icra_L = ImageMobject("pics/icra23_logo.png").scale(0.8).move_to([-2, 2.5, 0])
        ls2n = ImageMobject("pics/ls2n_logo.png").scale(0.2).move_to([2, 2.5, 0])

        self.add(*[iter2 for iter2 in [title, authors, icra_L, affiliations, ls2n]])
        self.wait()

        bottom_title = Tex(r"Trajectory planning problems in commercial cuspidal robots").scale(0.7).move_to(
            [0, -3.7, 0])
        bottom_line = Line(start=[-7, -3.5, 0], end=[7, -3.5, 0], stroke_width=0.5)
        top_line = Line(start=[-7, 3.2, 0], end=[7, 3.2, 0], stroke_width=0.5)
        icra_L2 = icra_L.copy().scale(0.4).move_to([-6, 3.5, 0])
        ls2n2 = ImageMobject("pics/ls2n_logo.png").scale(0.1).move_to([6, 3.5, 0])
        self.play(*[FadeOut(k) for k in [authors, affiliations]])
        self.play(*[Transform(k, j) for k, j in zip([title, icra_L, ls2n], [bottom_title, icra_L2, ls2n2])],
                  Create(top_line),
                  Create(bottom_line))
        self.wait()
        self.clear()
        self.add(*get_Background("Table of Contents"))
        self.wait(2)


class Contents(Scene):
    def construct(self):
        # object definition
        toc = Tex("\\begin{itemize} \\item Cuspidality analysis of JACO robot (Gen 2, no-wrist)\\end{itemize}",
                  "\\begin{itemize} \\item Nonsingular change of solutions in JACO robot\end{itemize}",
                  "\\begin{itemize} \\item Repeatable and non repeatable paths in JACO robot\\end{itemize}",
                  "\\begin{itemize} \\item Issues in trajectory planning of \\emph{cuspidal} serial robots\\"
                  "end{itemize}").scale(0.8).shift(UP * 1.5)

        # animations
        self.add(*get_Background("Table of Contents"))
        for i2 in range(4):
            new = toc[i2].copy().shift(LEFT + i2 * DOWN * 0.7)
            self.play(FadeIn(new))
            self.wait(3)


class Definition(Scene):
    def construct(self):
        # object definition
        toc = Tex("What is a cuspidal robot?").shift(UP * 2)
        ans = Tex(r"""\begin{minipage}{8 cm} \centering A robot that has multiple inverse kinematic solutions in an 
        \emph{aspect} is defined as a cuspidal robot \end{minipage}""", font_size=36).next_to(toc, DOWN * 1.5)

        assumption1 = Tex(
            r"""\begin{minipage}{8 cm} \centering $\rightarrow$ There are no joint limits \end{minipage}""",
            font_size=36).next_to(ans, DOWN)
        assumption2 = Tex(
            r"""\begin{minipage}{8 cm} \centering $\rightarrow$ Collision constraints are 
            not considered \end{minipage}""", font_size=36).next_to(assumption1, DOWN)

        # animations
        self.add(*get_Background("Definition"))
        self.play(FadeIn(toc))
        self.wait()
        self.play(FadeIn(ans))
        self.wait()
        self.play(FadeIn(assumption1))
        self.play(FadeIn(assumption2))
        self.wait()


def time_dot(year, y_str, direction=UP):
    mov_vec = -6 + 12 * (year - 1986) / (2022 - 1986)
    dot_ins = Dot(color=GREEN).move_to([mov_vec, 1, 0]).scale(2)
    ys = Tex(y_str).scale(0.8).next_to(dot_ins, direction)

    return Group(dot_ins, ys)


def BoxedText(istr):
    first_element = Tex(istr)
    second_element = SurroundingRectangle(first_element)

    return Group(first_element, second_element)


class Timeline(Scene):
    def construct(self):
        # object definition
        title = Tex("Timeline of cuspidal serial robots").scale(0.8).shift(UP * 2.5)
        line = Arrow([-7, 0, 0], [7, 0, 0]).shift(UP)
        # Borrel
        borrel_dot = time_dot(1986, "'86")
        borrel_cross = Cross().move_to(borrel_dot).scale(0.3).shift(DOWN * 0.3)
        assumption = BoxedText(r"""\begin{minipage}{8 cm} \centering It was assumed that all the inverse kinematic 
        solutions of a robot belong to separate aspects \end{minipage}""").shift(DOWN * 2)
        borrels_proof = BoxedText(r"""\begin{minipage}{8 cm} \centering Borrel and Liegeois presented a formal 
        proof of the same \end{minipage}""").shift(DOWN * 2)
        borrel_banner = Tex("\\emph{Borrel}").scale(0.8).next_to(borrel_dot, UP * 1.5)

        # Vincenzo-Parenti Castelli
        vpc_dot = time_dot(1988, "'88", DOWN)
        vpc_proof = BoxedText(r"""\begin{minipage}{8 cm} \centering Vincenzo Parenti-Castelli and Carlo Innocenti 
        presented a counterexample discrediting the existing proof \end{minipage}""").shift(DOWN * 2)
        # burdick_proof = BoxedText(r"""\begin{minipage}{8 cm} \centering Burdick presented results in 3R serial robots
        #         \end{minipage}""").shift(DOWN * 2)
        vpc_banner = Tex("\\emph{Parenti \\\\ Castelli}").scale(0.8).next_to(vpc_dot, DOWN * 1.5)

        # Philippe
        pw_dot = time_dot(1992, "'92")
        philippe_ud = BoxedText(r"""\begin{minipage}{8 cm} \centering Uniqueness domains and characteristic 
        surfaces are defined: Wenger. P. \end{minipage}""").shift(DOWN * 2)
        wenger_banner = Tex("\\emph{Wenger}").scale(0.8).next_to(pw_dot, UP * 1.5)
        pw_dot2 = time_dot(1995, "'95", DOWN)
        philippe_cr = BoxedText(r"""\begin{minipage}{8 cm} \centering Term 'cuspidal' robots is defined owing to the 
        existence of a cusp point in the workspace of such robots : Wenger et.al.\end{minipage}""").shift(DOWN * 2)
        omri_banner = Tex("\\emph{El Omri}").scale(0.8).next_to(pw_dot2, DOWN * 1.5)

        # Baili
        baili_dot = time_dot(2004, "'04")
        baili_contr = BoxedText(r"""\begin{minipage}{8 cm} \centering Extensive analysis and classification of 3R 
        'orthogonal' robots is presented: Baili. M. et al. \end{minipage}""").shift(DOWN * 2)
        baili_banner = Tex("\\emph{Baili}").scale(0.8).next_to(baili_dot, UP * 1.5)

        # Corvez
        corvez_dot = time_dot(2005, "'05", DOWN)
        corvez_contr = BoxedText(r"""\begin{minipage}{8 cm} \centering Cusp point as a sufficient condition 
        for a generic 3R serial robot is established : Corvez. S. et al.\end{minipage}""").shift(DOWN * 2)
        corvez_banner = Tex("\\emph{Corvez}").scale(0.8).next_to(corvez_dot, DOWN * 1.5)

        # Capco
        capco_dot = time_dot(2020, "'20")
        capco_contr = BoxedText(r"""\begin{minipage}{8 cm} \centering Non cuspidal properties of UR5 are 
        proven using computer algebraic tools : Capco et al. \end{minipage}""").shift(DOWN * 2)
        capco_banner = Tex("\\emph{Capco}").scale(0.8).next_to(capco_dot, UP * 1.5)

        # Salunkhe
        durghy_dot = time_dot(2021, "'22", DOWN)
        durghy_contr = BoxedText(r"""\begin{minipage}{8 cm} \centering Necessary and sufficient condition for generic 3R
                 serial robot was proved along with existence of reduced aspects : Salunkhe 
                 et al. \end{minipage}""").shift(DOWN * 2)
        durghy_banner = Tex("\\emph{Salunkhe}").scale(0.8).next_to(durghy_dot, DOWN * 1.5)

        # Prebet
        remi_contr = BoxedText(r"""\begin{minipage}{8 cm} \centering Certified algorithm to decide cuspidality of a nR 
                non-redundant serial robot was presented : Chablat et al. \end{minipage}""").shift(DOWN * 2)
        remi_banner = Tex("\\emph{Prebet}").scale(0.8).next_to(durghy_dot, DOWN * 3)

        # animations
        self.add(*get_Background("Introduction"))
        self.add(title)
        self.play(Create(line))
        self.wait()
        self.play(*[FadeIn(k) for k in [borrel_dot, assumption]])
        self.wait()
        self.play(FadeOut(assumption))
        self.wait()
        self.play(FadeIn(borrels_proof))
        self.wait()
        self.play(ReplacementTransform(borrels_proof, borrel_banner))

        self.play(*[FadeIn(k) for k in [vpc_dot, vpc_proof]])
        self.wait()
        self.play(Create(borrel_cross))
        self.wait()
        self.play(ReplacementTransform(vpc_proof, vpc_banner))

        self.play(*[FadeIn(k) for k in [pw_dot, philippe_ud]])
        self.wait()
        self.play(ReplacementTransform(philippe_ud, wenger_banner))
        self.play(*[FadeIn(k) for k in [pw_dot2, philippe_cr]])
        self.wait()
        self.play(ReplacementTransform(philippe_cr, omri_banner))
        self.play(FadeOut(title))

        self.play(*[FadeIn(k) for k in [baili_dot, baili_contr]])
        self.wait()
        self.play(ReplacementTransform(baili_contr, baili_banner))

        self.play(*[FadeIn(k) for k in [corvez_contr, corvez_dot]])
        self.wait()
        self.play(ReplacementTransform(corvez_contr, corvez_banner))

        self.play(*[FadeIn(k) for k in [capco_contr, capco_dot]])
        self.wait()
        self.play(ReplacementTransform(capco_contr, capco_banner))

        self.play(*[FadeIn(k) for k in [durghy_contr, durghy_dot]])
        self.wait()
        self.play(ReplacementTransform(durghy_contr, durghy_banner))

        self.play(FadeIn(remi_contr))
        self.wait()
        self.play(ReplacementTransform(remi_contr, remi_banner))

        self.wait()


class Fancy(Scene):
    def construct(self):
        # object definition
        text = Tex(r"""\begin{minipage}{12 cm} \centering This is not a fancy piece of imagination! 
        \end{minipage}""", font_size=68, color=RED_B)

        # animations
        self.add(*get_Background("Real world applications"))
        self.play(Write(text))
        self.wait(2)


class Achille(Scene):
    def construct(self):
        # object definition
        achille_caption = Tex(r"""\begin{minipage}{10 cm} \centering Trajectory planning failure in real world 
        applications \\ (Video Credits: Achille Verheyes, achille0.medium.com) \end{minipage}""",
                              font_size=36).shift(DOWN * 3)

        # animations
        self.add(*get_Background("Real world implementation"))
        self.add(achille_caption)


class PosPlot(Scene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def construct(self):
        # object definition

        # Plotting the path
        path_length = 10
        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")
        df_n2 = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")

        plane2 = NumberPlane(x_range=[0, path_length], y_range=[-3.2, 3.2], x_length=path_length, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             })
        # plane2.y_axis.shift(LEFT * 3.2)
        plane2.x_axis.shift(DOWN * 3.2)
        plane2.add_coordinates(np.arange(0, path_length), range(-3, 4))
        plane2.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane2.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        x_label2 = Tex("path", font_size=30).next_to(plane2.x_axis, DOWN * 0.8)
        y_label2 = Tex("$\\theta_1 (radians)$", font_size=30).next_to(plane2.y_axis, LEFT * 0.8).rotate(np.pi / 2)
        plane2.add(x_label2, y_label2)
        # plane2.shift(LEFT*path_length/2)

        full_path2 = []
        paths = make_paths(df_n)

        first_x = (len(paths[2]) * path_length) / 724 - path_length / 2
        second_x = (len(paths[0]) * path_length) / 724 - path_length / 2
        third_x = ((len(paths[1]) - len(paths[4])) * path_length) / 724 - path_length / 2

        first_transition = DashedLine([first_x, -3.5, 0], [first_x, 3.5, 0])
        first_nom = Tex("$(8 \\rightarrow 6)$", font_size=24).move_to(first_transition.get_end()).shift(LEFT * 0.5)
        second_transition = DashedLine([second_x, -3.5, 0], [second_x, 3.5, 0])
        second_nom = Tex("$(6 \\rightarrow 4)$", font_size=24).move_to(second_transition.get_end()).shift(RIGHT * 0.5)
        third_transition = DashedLine([third_x, -3.5, 0], [third_x, 3.5, 0])
        third_nom = Tex("$(4 \\rightarrow 8)$", font_size=24).move_to(third_transition.get_end())

        point_plot = Dot().move_to(np.array([-path_length / 2, paths[2][1], 0]))
        point_plot2 = Dot().move_to(np.array([-path_length / 2, paths[0][1], 0]))
        point_plot3 = Dot(color=GREEN).move_to(np.array([-path_length / 2, paths[1][1], 0]))
        point_plot4 = Dot(color=GREEN).move_to(np.array([-path_length / 2, paths[3][1], 0]))

        point_plotb = Circle(color=BLUE_C, radius=0.1).move_to(np.array([-path_length / 2, paths[2][1], 0]))
        point_plot2b = Circle(color=BLUE_C, radius=0.1).move_to(np.array([-path_length / 2, paths[0][1], 0]))
        point_plot3b = Circle(color=BLUE_C, radius=0.1).move_to(np.array([-path_length / 2, paths[1][1], 0]))
        point_plot4b = Circle(color=BLUE_C, radius=0.1).move_to(np.array([-path_length / 2, paths[3][1], 0]))
        print(len(paths))

        for i2 in range(len(paths)):
            print(f"Length of path {i2} is {len(paths[i2])}")
            for i4 in np.arange(1, len(paths[i2]) - 1):
                i3 = paths[i2][0] - len(paths[i2]) + 1 + i4
                full_path2.append(Line(np.array([i3 * path_length / 724, paths[i2][i4], 0]),
                                       np.array([(i3 + 1) * path_length / 724, paths[i2][i4 + 1], 0]),
                                       stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6).shift(
                    LEFT * path_length / 2))

        full_path22 = []
        paths2 = make_paths(df_n2, thresh=0.2)
        print(len(paths2))

        for i2 in range(len(paths2)):
            print(f"Length of path2 {i2} is {len(paths2[i2])}")
            for i4 in np.arange(1, len(paths2[i2]) - 1):
                i3 = paths2[i2][0] - len(paths2[i2]) + 1 + i4
                full_path22.append(Line(np.array([i3 * path_length / 724, paths2[i2][i4], 0]),
                                        np.array([(i3 + 1) * path_length / 724, paths2[i2][i4 + 1], 0]),
                                        stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6).shift(
                    LEFT * path_length / 2))

        four_choices = Tex(
            r"""\begin{minipage}{7 cm}\centering We have 4 IKS in the same aspect and we can start the trajectory 
            from any one of them \end{minipage}""")
        first_choice = Tex(
            r"""\begin{minipage}{7 cm} \centering Let us start with IKS corresponding to $T_3$\end{minipage}""").shift(
            UP * 1.5)
        zeroth_problem = Tex(
            r"""\begin{minipage}{7 cm} \centering The path exits from a region with 8 IKS to enter a region with 
            6 IKS and thus lose 2 IKS (1 in each aspect) \end{minipage}""")
        zp_bkg = BackgroundRectangle(zeroth_problem, fill_opacity=1)
        zp_present = Group(zp_bkg, zeroth_problem)
        first_problem = Tex(
            r"""\begin{minipage}{7 cm}We do not have a continuous path beyond this point and a sudden jump 
            to any other paths in the same aspect will take place \end{minipage}""")
        fp_bkg = BackgroundRectangle(first_problem, fill_opacity=1)
        fp_present = Group(fp_bkg, first_problem)

        zeroth_problem2 = Tex(
            r"""\begin{minipage}{7 cm} \centering The path exits from a region with 6 IKS to enter a region with 4 
            IKS and further loses 2 IKS (1 in each aspect) \end{minipage}""")
        zp_bkg2 = BackgroundRectangle(zeroth_problem2, fill_opacity=1)
        zp_present2 = Group(zp_bkg2, zeroth_problem2)
        second_choice = Tex(
            r"""\begin{minipage}{7 cm} \centering Let us start with IKS corresponding to $T_7$\end{minipage}""").shift(
            UP * 1.5)
        second_problem = Tex(
            r"""\begin{minipage}{10 cm}Same problem is encountered at this point and a sudden jump 
            to any other paths with a solution at next instance will take place \end{minipage}""")
        sp_bkg = BackgroundRectangle(second_problem)
        sp_present = Group(sp_bkg, second_problem)

        third_choice = Tex(
            r"""\begin{minipage}{7 cm} \centering Trajectories  $T_2$ and $T_6$ lead to a continuous 
            path that can be \emph{repeated} \end{minipage}""").shift(UP * 2)
        third_problem = Tex(r"""\begin{minipage}{10 cm} \centering This path can be \emph{repeated} 
        because the trajectory ends with the same IKS it started with it \end{minipage}""")
        tp_bkg = BackgroundRectangle(third_problem, fill_opacity=1)
        tp_present = Group(tp_bkg, third_problem)
        zeroth_problem3 = Tex(r"""\begin{minipage}{7 cm} \centering The path exits from a region with 4 
        IKS to enter a region with 8 IKS and thus gains 4 IKS (2 in each aspect) \end{minipage}""")
        zp_bkg3 = BackgroundRectangle(zeroth_problem3, fill_opacity=1)
        zp_present3 = Group(zp_bkg3, zeroth_problem3)

        show_three = True

        # animations
        # self.add(*get_Background("Example trajectory of JACO robot"))
        self.add(plane2)
        self.play(*[FadeIn(k4) for k4 in full_path2])
        self.play(*[FadeIn(k4) for k4 in full_path22])

        self.FadeInFadeOut(four_choices)
        self.FadeIt(*full_path22)
        self.FadeInFadeOut(point_plotb, point_plot2b, point_plot3b, point_plot4b)

        self.wait()
        self.add(TracedPath(point_plot.get_center, stroke_width=5, stroke_color=GOLD_A))
        self.FadeInFadeOut(first_choice, wait_time=2)
        for i2 in np.arange(1, len(paths[2]) - 1, 2):
            self.play(Transform(point_plot, point_plot.move_to(
                np.array([(i2 * path_length / 724) - path_length / 2, paths[2][i2], 0])), run_time=0.2))
        self.play(Create(first_transition))
        self.play(FadeIn(first_nom))
        self.FadeInFadeOut(zp_present, wait_time=5)
        self.FadeInFadeOut(fp_present, wait_time=5)
        self.wait(2)

        self.add(TracedPath(point_plot2.get_center, stroke_width=5, stroke_color=GOLD_A))
        self.FadeInFadeOut(second_choice, wait_time=2)
        for i2 in np.arange(1, len(paths[0]) - 1, 4):
            self.play(Transform(point_plot2, point_plot2.move_to(
                np.array([(i2 * path_length / 724) - path_length / 2, paths[0][i2], 0])), run_time=0.2))
        self.play(Create(second_transition))
        self.play(FadeIn(second_nom))
        self.FadeInFadeOut(zp_present2, wait_time=5)
        self.FadeInFadeOut(sp_present, wait_time=5)
        self.wait(2)

        self.add(TracedPath(point_plot3.get_center, stroke_width=5, stroke_color=GREEN))
        self.add(TracedPath(point_plot4.get_center, stroke_width=5, stroke_color=GREEN))
        self.FadeInFadeOut(third_choice, wait_time=2)
        for i2 in np.arange(1, len(paths[1]) - 1, 8):
            if i2 > 724 - 74 and show_three:
                show_three = False
                self.wait()
                self.play(Create(third_transition))
                self.wait()
                self.play(FadeIn(third_nom))
                self.FadeInFadeOut(zp_present3, wait_time=5)
            self.play(Transform(point_plot3, point_plot3.move_to(
                np.array([(i2 * path_length / 724) - path_length / 2, paths[1][i2], 0])), run_time=0.05))
            self.play(Transform(point_plot4, point_plot4.move_to(
                np.array([(i2 * path_length / 724) - path_length / 2, paths[3][i2], 0])), run_time=0.05))
        self.wait()
        self.FadeInFadeOut(tp_present, wait_time=5)

        self.wait(2)
        # self.clear()
        # complete_set1 = Group(plane2, point_plot, point_plot2, *full_path2, first_transition, second_transition)
        # self.add(complete_set1)
        # self.play(Transform(complete_set1, complete_set1.copy().scale(0.5).shift(LEFT * 4 + UP)))
        # self.wait(3)

    def FadeInFadeOut(self, *inObject, wait_time=3):
        self.play(FadeIn(*inObject))
        self.wait(wait_time)
        self.play(FadeOut(*inObject))

    def FadeIt(self, *inObject):
        self.play(*[Transform(k2, k2.copy().set_opacity(0.2)) for k2 in inObject])


class Temp(Scene):
    def construct(self):
        # object definition
        a = Circle(fill_color=BLACK, radius=0.1).scale(2)
        b = Dot()

        # animations
        self.FadeInFadeOut(a, b, wait_time=5)
        # self.add(a, b)

    def FadeInFadeOut(self, *inObject, wait_time=3):
        self.play(FadeIn(*inObject))
        self.wait(wait_time)
        # self.play(FadeOut(*object))
        self.play(*[Transform(k2, k2.copy().set_opacity(0.2)) for k2 in inObject])


def my_det(t2, t3):
    inter_val = [0, t2, t3]
    # return -3 * (3 * cos(inter_val[2]) + 4) * (
    #             sin(inter_val[2]) * (2 + 4 * cos(inter_val[1])) - 2 * cos(inter_val[1]) * cos(inter_val[2]))

    return jac3R(inter_val, [0, 1, 0], [1, 2, 3 / 2], [np.pi / 2, np.pi / 2, 0]) * 8


def my_det6R(s, e, cur_iter=0, total_iter=50):
    point1_comp = [-3.1201, 0.7082, 1.4904, 2.62, -1.9637, -1.8817]
    point2_comp = [3.0675, 1.0545, 1.3090, 2.4283, -1.2305, -2.3002]
    point3_comp = [2.9132, 0.2824, 1.9297, -2.1648, -2.9685, -2.7165]
    point4_comp = [2.5338, 1.2022, 1.1149, 1.5839, 0.6030, 2.6322]
    point5_comp = [2.4730, 0.0943, 2.0281, -1.4916, -2.4244, 2.4362]
    point6_comp = [2.4335, 0.0936, 1.5741, 1.4311, 2.3452, 0.5391]
    point7_comp = [-0.8579, 3.0408, 1.5721, -1.5912, 2.1625, 0.5390]
    point8_comp = [-0.8046, 3.0466, 1.1135, 1.5103, -2.2697, 2.4394]
    point9_comp = [-0.7501, 1.9399, 2.0268, -1.4270, 0.6212, 2.6291]
    point10_comp = [-0.2812, 2.0346, 1.8631, -0.5833, -1.0917, -2.4130]
    point11_comp = [-0.2456, 2.8156, 1.3090, 0.4882, -2.8301, -2.3003]
    point12_comp = [-0.1583, 2.7025, 1.4699, -0.0656, -2.5402, -1.9078]

    point_record = [point1_comp, point2_comp, point3_comp, point4_comp, point5_comp, point6_comp, point7_comp,
                    point8_comp, point9_comp, point10_comp, point11_comp, point12_comp]
    # JACO
    d1s = 212
    d3s = -12
    d4s = -249.3
    d5s = -84.6
    d6s = -222.73
    a2s = 410

    # DH parameters of CRX-10ia/L robot are:
    d_list = [d1s, 0, d3s, d4s, d5s, d6s]
    a_list = [0, a2s, 0, 0, 0, 0]
    alpha_list = [PI / 2, PI, PI / 2, np.deg2rad(55), np.deg2rad(55), PI]
    d_list = [number / 100 for number in d_list]
    a_list = [number / 100 for number in a_list]

    theta_list = return_intermediate(np.array(point_record[s]), np.array(point_record[e]), cur_iter, total_iter)

    return static_pref_jacdet(theta_list, d_list, a_list, alpha_list)


class JacDetPlot(Scene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def construct(self):
        # object definition

        # NumberPlane 2
        point1_comp = [-3.1201, 0.7082, 1.4904, 2.62, -1.9637, -1.8817]
        point2_comp = [3.0675, 1.0545, 1.3090, 2.4283, -1.2305, -2.3002]
        point3_comp = [2.9132, 0.2824, 1.9297, -2.1648, -2.9685, -2.7165]
        point4_comp = [2.5338, 1.2022, 1.1149, 1.5839, 0.6030, 2.6322]
        point5_comp = [2.4730, 0.0943, 2.0281, -1.4916, -2.4244, 2.4362]
        point6_comp = [2.4335, 0.0936, 1.5741, 1.4311, 2.3452, 0.5391]
        point7_comp = [-0.8579, 3.0408, 1.5721, -1.5912, 2.1625, 0.5390]
        point8_comp = [-0.8046, 3.0466, 1.1135, 1.5103, -2.2697, 2.4394]
        point9_comp = [-0.7501, 1.9399, 2.0268, -1.4270, 0.6212, 2.6291]
        point10_comp = [-0.2812, 2.0346, 1.8631, -0.5833, -1.0917, -2.4130]
        point11_comp = [-0.2456, 2.8156, 1.3090, 0.4882, -2.8301, -2.3003]
        point12_comp = [-0.1583, 2.7025, 1.4699, -0.0656, -2.5402, -1.9078]

        point_record = [point1_comp, point2_comp, point3_comp, point4_comp, point5_comp, point6_comp, point7_comp,
                        point8_comp, point9_comp, point10_comp, point11_comp, point12_comp]
        # JACO
        d1s = 212
        d3s = -12
        d4s = -249.3
        d5s = -84.6
        d6s = -222.73
        a2s = 410

        # DH parameters of CRX-10ia/L robot are:
        d_list = [d1s, 0, d3s, d4s, d5s, d6s]
        a_list = [0, a2s, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, np.deg2rad(55), np.deg2rad(55), PI]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]
        start_index = 0
        end_index = 4
        print("Started the min det traj stuff")
        y_min = min(0,
                    min_dettraj(d_list, a_list, alpha_list, point_record[start_index], point_record[end_index], 50)[0])
        if y_min == 0:
            y_max = min_dettraj(d_list, a_list, alpha_list, point_record[start_index], point_record[end_index], 50)[1]
        else:
            y_max = 0
        print(f"Ended the min det traj stuff {y_min, y_max}")

        plane2 = NumberPlane(x_range=[0, 50], y_range=[y_min, y_max], x_length=6.4, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0
                             }, ).add_coordinates(np.arange(0, 51, 10), np.linspace(y_min, y_max, num=5)).shift(
            LEFT * 3).scale(0.6)
        print("Finished plane basic")
        plane2.coordinate_labels[1][0:len(plane2.coordinate_labels[1]) - 1].shift(LEFT * 0.35)
        plane2.coordinate_labels[1][len(plane2.coordinate_labels[1]) - 1].shift(LEFT * 0.25)
        plane2.coordinate_labels[0].shift(UP * 0.35)
        print("Finished plane advanced")
        x_label2 = Tex("path", font_size=30).next_to(plane2.x_axis, UP * 0.45)
        y_label2 = Tex("$\\det(\\mathbf{J})$", font_size=30).next_to(plane2.y_axis).rotate(np.pi / 2).shift(LEFT * 1.15)
        plane2.add(x_label2, y_label2)

        det_point = Dot(color=LIGHT_BROWN).move_to(
            plane2.c2p(0, my_det6R(start_index, end_index, cur_iter=0, total_iter=50)))


        jac_cusp = Tex(r"""\begin{minipage}{8cm}\centering JACO robot is a cuspidal robot\end{minipage}""",
                       font_size=36).to_edge(RIGHT).shift(UP)
        jac_cusp1 = Tex(r"""\begin{minipage}{8cm}\begin{itemize} \item Maximum 12 IKS have been found 
        \item The 12 IKS lie in 2 separate aspects \end{itemize}\end{minipage}""", font_size=36).next_to(jac_cusp, DOWN)

        title = Tex(r"""\begin{minipage}{12cm}\centering Example nonsingular change of solutions \\ 
        The robot changes configuration without the change of sign for $\det(\mathbf{J})$\end{minipage}""",
                    font_size=36).to_edge(DOWN, buff=0.5)

        # animations
        self.add(*get_Background("JACO robot is cuspidal"))
        self.add(plane2)
        self.play(FadeIn(jac_cusp))
        self.wait(2)
        self.play(FadeIn(jac_cusp1))

        self.clear()
        self.add(*get_Background("JACO robot is cuspidal"))
        self.add(plane2)
        self.play(FadeIn(title))
        self.add(TracedPath(det_point.get_center, stroke_width=4, stroke_color=LIGHT_BROWN))
        for k in np.arange(0, 51):
            self.play(ReplacementTransform(det_point,
                                           det_point.move_to(plane2.c2p(k, my_det6R(start_index, end_index, cur_iter=k,
                                                                                    total_iter=50))),
                                           run_time=0.05))
        self.wait()


class TotalPlot(ZoomedScene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.06,
            zoomed_display_height=6,
            zoomed_display_width=10,
            image_frame_stroke_width=0.002,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            zoomed_camera_frame_starting_position=[-4.8, 0.18, 0],
            **kwargs
        )

    def construct(self):
        # object definition

        # Plotting the path
        path_length = 10
        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")
        df_n2 = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")

        plane2 = NumberPlane(x_range=[0, path_length], y_range=[-3.2, 3.2], x_length=path_length, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             })
        # plane2.y_axis.shift(LEFT * 3.2)
        plane2.x_axis.shift(DOWN * 3.2)
        plane2.add_coordinates(np.arange(0, path_length), range(-3, 4))
        plane2.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane2.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        x_label2 = Tex("path", font_size=30).next_to(plane2.x_axis, DOWN * 0.8)
        y_label2 = Tex("$\\theta_1 (radians)$", font_size=30).next_to(plane2.y_axis).rotate(np.pi / 2).shift(
            LEFT * 1.7)
        plane2.add(x_label2, y_label2)
        # plane2.shift(LEFT*path_length/2)

        full_path = []
        full_path2 = []
        zoom_path = []
        zoom_path2 = []
        zoom_pathD = []
        zoom_pathD2 = []
        paths = make_paths(df_n, thresh=0.2)
        paths2 = make_paths(df_n2, thresh=0.1)
        print(len(paths))
        t_str = []
        t1 = []

        for i2 in range(len(paths) + len(paths2)):
            t_str.append("T" + str(i2 + 1))

        for i2 in range(len(paths)):
            print(f"Length of path {i2} is {len(paths[i2])}")
            for i4 in np.arange(1, len(paths[i2]) - 1):
                i3 = paths[i2][0] - len(paths[i2]) + 1 + i4
                if i2 == 2:
                    zoom_path2.append(Line(np.array([i3 * path_length / 724, paths[i2][i4], 0]),
                                           np.array([(i3 + 1) * path_length / 724, paths[i2][i4 + 1], 0]),
                                           stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
                    zoom_pathD2.append(Line(np.array([i3 * path_length / 724, paths[i2][i4], 0]),
                                            np.array([(i3 + 1) * path_length / 724, paths[i2][i4 + 1], 0]),
                                            stroke_color=RED_C, stroke_width=0.5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
                else:
                    full_path2.append(Line(np.array([i3 * path_length / 724, paths[i2][i4], 0]),
                                           np.array([(i3 + 1) * path_length / 724, paths[i2][i4 + 1], 0]),
                                           stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
            if i2 == 3:
                t1.append(Tex("$T_1$").move_to(full_path2[-1].get_end()).shift(RIGHT * 0.2))
            elif i2 == 1:
                t1.append(Tex("$T_5$").move_to(full_path2[-1].get_end()).shift(LEFT * 2 + UP * 0.5))

        for i2 in range(len(paths2)):
            print(f"Length of path2 {i2} is {len(paths2[i2])}")
            for i4 in np.arange(1, len(paths2[i2]) - 1):
                i3 = paths2[i2][0] - len(paths2[i2]) + 1 + i4
                if i2 == 2:
                    zoom_path.append(Line(np.array([i3 * path_length / 724, paths2[i2][i4], 0]),
                                          np.array([(i3 + 1) * path_length / 724, paths2[i2][i4 + 1], 0]),
                                          stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
                    zoom_pathD.append(Line(np.array([i3 * path_length / 724, paths2[i2][i4], 0]),
                                           np.array([(i3 + 1) * path_length / 724, paths2[i2][i4 + 1], 0]),
                                           stroke_color=BLUE_C, stroke_width=0.5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
                else:
                    full_path.append(Line(np.array([i3 * path_length / 724, paths2[i2][i4], 0]),
                                          np.array([(i3 + 1) * path_length / 724, paths2[i2][i4 + 1], 0]),
                                          stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
            if i2 == 2:
                t1.append(Tex("$T_3, T_4$").move_to(zoom_path[-1].get_end()).shift(RIGHT * 0.8))
            else:
                if i2 == 0:
                    t1.append(Tex("$T_7, T_8$").move_to(full_path[-1].get_end()).shift(RIGHT * 0.8 + UP * 0.2))
                if i2 == 1:
                    t1.append(Tex("$T_6$").move_to(full_path[-1].get_end()).shift(LEFT * 2 + DOWN * 0.5))
                if i2 == 3:
                    t1.append(Tex("$T_2$").move_to(full_path[-1].get_end()).shift(LEFT * 2 + DOWN * 0.5))

        point_plotc = Dot().move_to(np.array([-path_length / 2, paths[0][1], 0]))
        point_plot2c = Dot().move_to(np.array([-path_length / 2, paths[1][1], 0]))
        point_plot3c = Dot().move_to(np.array([-path_length / 2, paths[2][1], 0]))
        point_plot4c = Dot().move_to(np.array([-path_length / 2, paths[3][1], 0]))
        point_plot5c = Dot().move_to(np.array([-path_length / 2, paths2[0][1], 0]))
        point_plot6c = Dot().move_to(np.array([-path_length / 2, paths2[1][1], 0]))
        point_plot7c = Dot().move_to(np.array([-path_length / 2, paths2[2][1], 0]))
        point_plot8c = Dot().move_to(np.array([-path_length / 2, paths2[3][1], 0]))

        first_text = Tex(
            r"""\begin{minipage}{7 cm} \centering We evaluate the IKS at each discrete point along the closed 
            loop path \end{minipage}""").shift(
            UP * 1.5)
        second_text = Tex(
            r"""\begin{minipage}{7 cm} \centering The following graph shows the values of $\theta_1$ at each 
            instance along the path \end{minipage}""").shift(UP * 1.5)
        second_text2 = Tex(
            r"""\begin{minipage}{7 cm} \centering The blue paths correspond to Aspect 1 ($\det(\mathbf{J}) > 0$)  
            \\ The red paths correspond to Aspect 2 ($\det(\mathbf{J}) < 0$) \end{minipage}""").shift(UP)
        second_text3 = Tex(
            r"""\begin{minipage}{7 cm} \centering As the trajectory is a closed loop, the final IKS match the 
            initial IKS \end{minipage}""").shift(UP * 1.5)
        third_text = Tex(
            r"""\begin{minipage}{7 cm} \centering We begin from a pose with 8 IKS \\ 
            (4 IKS in each aspect) \end{minipage}""").shift(UP * 1.5)

        # animations

        self.FadeInFadeOut(first_text)
        self.play(Create(plane2))
        self.FadeInFadeOut(second_text, wait_time=2)
        self.FadeInFadeOut(second_text2, wait_time=2)
        self.wait()
        self.add(*zoom_path, *zoom_path2, *full_path, *full_path2)
        self.wait()
        self.add(point_plotc, point_plot2c, point_plot3c, point_plot4c)
        self.FadeInFadeOut(second_text3, wait_time=2)
        self.play(*[Transform(k, k.copy().shift(RIGHT * path_length), run_time=2) for k in
                    [point_plotc, point_plot2c, point_plot3c, point_plot4c, point_plot5c, point_plot6c, point_plot7c,
                     point_plot8c]])
        self.play(*[FadeOut(k) for k in
                    [point_plotc, point_plot2c, point_plot3c, point_plot4c, point_plot5c, point_plot6c, point_plot7c,
                     point_plot8c]])
        self.activate_zooming(animate=True)

        self.remove(*zoom_path2, *zoom_path)
        self.add(*zoom_pathD, *zoom_pathD2)
        self.wait(2)
        # self.remove(*zoom_pathd, *zoom_pathd2)
        # self.add(*zoom_path2, *zoom_path)
        self.clear()
        self.add(plane2, *zoom_path, *zoom_path2, *full_path, *full_path2)
        # self.wait(5)

        self.FadeInFadeOut(third_text, wait_time=2)
        for i2 in [1, 5, 4, 0, 3, 2]:
            self.play(FadeIn(t1[i2]))
            self.wait(0.3)
        # self.add(*t1)
        self.wait()

    def FadeInFadeOut(self, *object_to_process, wait_time=3):
        self.play(FadeIn(*object_to_process))
        self.wait(wait_time)
        self.play(FadeOut(*object_to_process))


class NegPlot(ZoomedScene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.06,
            zoomed_display_height=6,
            zoomed_display_width=10,
            image_frame_stroke_width=0.002,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            zoomed_camera_frame_starting_position=[-4.8, 0.18, 0],
            **kwargs
        )

    def construct(self):
        # object definition

        # Plotting the path
        path_length = 10
        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")
        df_n2 = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")

        plane2 = NumberPlane(x_range=[0, path_length], y_range=[-3.2, 3.2], x_length=path_length, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             })
        # plane2.y_axis.shift(LEFT * 3.2)
        plane2.x_axis.shift(DOWN * 3.2)
        plane2.add_coordinates(np.arange(0, path_length), range(-3, 4))
        plane2.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane2.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        x_label2 = Tex("path", font_size=30).next_to(plane2.x_axis, DOWN * 0.8)
        y_label2 = Tex("$\\theta_1 (radians)$", font_size=30).next_to(plane2.y_axis).rotate(np.pi / 2).shift(
            LEFT * 1.15)
        plane2.add(x_label2, y_label2)
        # plane2.shift(LEFT*path_length/2)

        full_path = []
        full_path2 = []
        zoom_path = []
        zoom_path2 = []
        zoom_pathd = []
        zoom_pathd2 = []
        paths = make_paths(df_n, thresh=0.2)
        paths2 = make_paths(df_n2, thresh=0.1)
        print(len(paths))
        t1 = []

        for i2 in range(len(paths)):
            print(f"Length of path {i2} is {len(paths[i2])}")
            for i4 in np.arange(1, len(paths[i2]) - 1):
                i3 = paths[i2][0] - len(paths[i2]) + 1 + i4
                if i2 == 2:
                    zoom_path2.append(Line(np.array([i3 * path_length / 724, paths[i2][i4], 0]),
                                           np.array([(i3 + 1) * path_length / 724, paths[i2][i4 + 1], 0]),
                                           stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
                    zoom_pathd2.append(Line(np.array([i3 * path_length / 724, paths[i2][i4], 0]),
                                            np.array([(i3 + 1) * path_length / 724, paths[i2][i4 + 1], 0]),
                                            stroke_color=RED_C, stroke_width=0.5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
                else:
                    full_path2.append(Line(np.array([i3 * path_length / 724, paths[i2][i4], 0]),
                                           np.array([(i3 + 1) * path_length / 724, paths[i2][i4 + 1], 0]),
                                           stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
            if i2 == 3:
                t1.append(Tex("$T_1$").move_to(full_path2[-1].get_end()).shift(RIGHT * 0.2))
            elif i2 == 1:
                t1.append(Tex("$T_5$").move_to(full_path2[-1].get_end()).shift(LEFT * 2 + UP * 0.5))

        for i2 in range(len(paths2)):
            print(f"Length of path2 {i2} is {len(paths2[i2])}")
            for i4 in np.arange(1, len(paths2[i2]) - 1):
                i3 = paths2[i2][0] - len(paths2[i2]) + 1 + i4
                if i2 == 2:
                    zoom_path.append(Line(np.array([i3 * path_length / 724, paths2[i2][i4], 0]),
                                          np.array([(i3 + 1) * path_length / 724, paths2[i2][i4 + 1], 0]),
                                          stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
                    zoom_pathd.append(Line(np.array([i3 * path_length / 724, paths2[i2][i4], 0]),
                                           np.array([(i3 + 1) * path_length / 724, paths2[i2][i4 + 1], 0]),
                                           stroke_color=BLUE_C, stroke_width=0.5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
                else:
                    full_path.append(Line(np.array([i3 * path_length / 724, paths2[i2][i4], 0]),
                                          np.array([(i3 + 1) * path_length / 724, paths2[i2][i4 + 1], 0]),
                                          stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6).shift(
                        LEFT * path_length / 2))
            if i2 == 2:
                t1.append(Tex("$T_3, T_4$").move_to(zoom_path[-1].get_end()).shift(RIGHT * 0.8))
            else:
                if i2 == 0:
                    t1.append(Tex("$T_7, T_8$").move_to(full_path[-1].get_end()).shift(RIGHT * 0.8 + UP * 0.2))
                if i2 == 1:
                    t1.append(Tex("$T_6$").move_to(full_path[-1].get_end()).shift(LEFT * 2 + DOWN * 0.5))
                if i2 == 3:
                    t1.append(Tex("$T_2$").move_to(full_path[-1].get_end()).shift(LEFT * 2 + DOWN * 0.5))

        point_plot = Dot(color=GREEN).move_to(np.array([-path_length / 2, paths[0][1], 0]))
        point_plot2 = Dot(color=GREEN).move_to(np.array([-path_length / 2, paths[1][1], 0]))

        third_choice = Tex(
            r"""\begin{minipage}{7 cm} \centering Trajectories  $T_1$ and $T_5$ lead to a continuous path 
            that CANNOT be \emph{repeated} \end{minipage}""").shift(
            UP * 1.5)
        third_problem = Tex(
            r"""\begin{minipage}{7 cm} \centering These paths CANNOT be \emph{repeated} because the 
            trajectory ends at the start point of another trajectory which is not repeatable IKS \end{minipage}""")
        tp_bkg = BackgroundRectangle(third_problem, fill_opacity=1)
        tp_present = Group(tp_bkg, third_problem)

        # animations

        self.add(plane2, *zoom_path, *zoom_path2, *full_path, *full_path2)
        self.FadeIt(*full_path)
        self.play(*[FadeIn(k) for k in [t1[0], t1[1]]])

        self.add(TracedPath(point_plot.get_center, stroke_width=5, stroke_color=PURPLE_C))
        self.add(TracedPath(point_plot2.get_center, stroke_width=5, stroke_color=PURPLE_C))
        self.FadeInFadeOut(third_choice, wait_time=2)
        complete_path_T1 = paths[3] + paths[4]
        for i2 in np.arange(1, min(len(complete_path_T1), len(paths[1])) - 1, 8):
            self.play(Transform(point_plot, point_plot.move_to(
                np.array([(i2 * path_length / 724) - path_length / 2, complete_path_T1[i2], 0])), run_time=0.05))
            self.play(Transform(point_plot2, point_plot2.move_to(
                np.array([(i2 * path_length / 724) - path_length / 2, paths[1][i2], 0])), run_time=0.05))
        self.wait()
        self.FadeInFadeOut(tp_present, wait_time=5)

    def FadeIt(self, *inObject):
        self.play(*[Transform(k2, k2.copy().set_opacity(0.2)) for k2 in inObject])

    def FadeInFadeOut(self, *object_to_process, wait_time=3):
        self.play(FadeIn(*object_to_process))
        self.wait(wait_time)
        self.play(FadeOut(*object_to_process))


class TempPlot(ZoomedScene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.06,
            zoomed_display_height=6,
            zoomed_display_width=10,
            image_frame_stroke_width=0.002,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            zoomed_camera_frame_starting_position=[-4.8, 0.18, 0],
            **kwargs
        )

    def construct(self):
        # object definition

        # Plotting the path
        path_length = 10
        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")
        df_n2 = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")

        plane2 = NumberPlane(x_range=[0, path_length], y_range=[-3.2, 3.2], x_length=path_length, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             }).scale(0.7).shift(LEFT * 2.5)

        plane2.x_axis.shift(DOWN * plane2.y_axis.get_length() / 2)
        plane2.add_coordinates(np.arange(0, path_length), range(-3, 4))
        plane2.coordinate_labels[1][0:3].shift(LEFT * 0.4)
        plane2.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        x_label2 = Tex("path", font_size=30).next_to(plane2.x_axis, DOWN * 0.4).scale(0.8)
        y_label2 = Tex("$\\theta_1 (radians)$", font_size=30).next_to(plane2.y_axis).rotate(np.pi / 2).shift(
            LEFT * 1.5).scale(0.8)
        plane2.add(x_label2, y_label2)

        full_path2 = []
        paths = make_paths(df_n)

        offset_axis = np.array([plane2.x_axis.get_length() / 2, 0, 0])

        point_plotc = Dot().move_to(plane2.c2p(-path_length / 2, paths[2][1]) + offset_axis)
        point_plot2c = Dot().move_to(plane2.c2p(-path_length / 2, paths[0][1]) + offset_axis)
        point_plot3c = Dot(color=GREEN).move_to(plane2.c2p(-path_length / 2, paths[1][1]) + offset_axis)
        point_plot4c = Dot(color=GREEN).move_to(plane2.c2p(-path_length / 2, paths[3][1]) + offset_axis)
        print(len(paths))

        for i2 in range(len(paths)):
            print(f"Length of path {i2} is {len(paths[i2])}")

            for i4 in np.arange(1, len(paths[i2]) - 1):
                i3 = paths[i2][0] - len(paths[i2]) + 1 + i4
                full_path2.append(Line(plane2.c2p((i3 * path_length / 724), paths[i2][i4]),
                                       plane2.c2p(((i3 + 1) * path_length / 724), paths[i2][i4 + 1]),
                                       stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6))

        full_path22 = []
        paths2 = make_paths(df_n2, thresh=0.2)
        print(len(paths2))

        for i2 in range(len(paths2)):
            print(f"Length of path2 {i2} is {len(paths2[i2])}")

            for i4 in np.arange(1, len(paths2[i2]) - 1):
                i3 = paths2[i2][0] - len(paths2[i2]) + 1 + i4
                full_path22.append(Line(plane2.c2p((i3 * path_length / 724), paths2[i2][i4]),
                                        plane2.c2p(((i3 + 1) * path_length / 724), paths2[i2][i4 + 1]),
                                        stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6))

        # animations
        self.add(plane2, *full_path2, *full_path22)
        self.add(point_plotc, point_plot2c, point_plot3c, point_plot4c)
        self.play(*[Transform(k, k.copy().shift(RIGHT * plane2.x_axis.get_length())) for k in
                    [point_plotc, point_plot2c, point_plot3c, point_plot4c]])
        self.wait(2)

    def FadeIt(self, *inObject):
        self.play(*[Transform(k2, k2.copy().set_opacity(0.2)) for k2 in inObject])

    def FadeInFadeOut(self, *object_to_process, wait_time=3):
        self.play(FadeIn(*object_to_process))
        self.wait(wait_time)
        self.play(FadeOut(*object_to_process))


class CreateBackground(Scene):
    def construct(self):
        self.add(*get_Background(r"""Real world problems"""))


class Check(Scene):
    def construct(self):
        self.add(Tex("Thank you", font_size=64, color=YELLOW))
