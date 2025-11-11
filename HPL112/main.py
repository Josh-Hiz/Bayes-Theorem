# bayes_movie.py
from manim import *
import numpy as np

# --------- Styling helpers (colors consistent across scenes) ----------
COLOR_POST = YELLOW_B
COLOR_LIKE = BLUE_B
COLOR_PRIOR = ORANGE
COLOR_EVID = PURPLE_B
BG = "#0e0e10"


# =========================== 1) Title Card ==============================
class TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Bayesianism", weight="BOLD").scale(1.5)
        title.set_color_by_gradient(BLUE_B, TEAL_A)
        subtitle = Text("Bayes’s theorem as the geometry of changing beliefs", font_size=36, color=TEAL_A)

        line1 = Text("Joshua Hizgiaev", font_size=40, color=TEAL_B)
        line2 = Text("HPL-112: Science and Metaphysics", font_size=36, color=TEAL_B)
        line3 = Text("A quick study of history, meaning, and visualization", font_size=32, color=TEAL_A)

        underline = Line(LEFT, RIGHT, color=TEAL_A).set_width(title.width * 1.06)

        top = VGroup(title, underline, subtitle).arrange(DOWN, buff=0.25)
        bottom = VGroup(line1, line2, line3).arrange(DOWN, buff=0.15)

        group = VGroup(top, bottom).arrange(DOWN, buff=0.6)
        group.move_to((0.0, 0.0, 0.0))

        self.play(Write(title), run_time=1.2)
        underline.next_to(title, DOWN, buff=0.18)
        self.play(Create(underline), run_time=0.6)
        self.play(FadeIn(subtitle, shift=0.2 * DOWN), run_time=0.8)
        self.wait(0.3)
        self.play(LaggedStart(
            FadeIn(line1, shift=0.2 * DOWN),
            FadeIn(line2, shift=0.2 * DOWN),
            FadeIn(line3, shift=0.2 * DOWN),
            lag_ratio=0.18, run_time=1.0
        ))
        self.wait(0.7)
        self.play(Flash(title, line_length=0.25, color=TEAL_C, time_width=0.6), run_time=0.6)
        self.wait(0.6)


# =========================== 2) History ================================
class History(Scene):
    def construct(self):
        self.camera.background_color = BG

        h = Text("A (very) short history", weight="BOLD", font_size=52).to_edge(UP)
        self.play(FadeIn(h, shift=0.2 * UP), run_time=0.6)

        # Cards for Bayes and Laplace
        bayes = VGroup(
            Text("Rev. Thomas Bayes (1701–1761)", font_size=40, color=GREY_E),
            Text("Essay posthumously published (1763).", font_size=32, color=GREY_C)
        ).arrange(DOWN, aligned_edge=LEFT).scale(1.0)

        laplace = VGroup(
            Text("Pierre-Simon Laplace (1749–1827)", font_size=40, color=GREY_E),
            Text("Generalized and popularized the method.", font_size=32, color=GREY_C)
        ).arrange(DOWN, aligned_edge=LEFT).scale(1.0)

        anno_b = SurroundingRectangle(bayes, color=TEAL_B, buff=0.25)
        anno_l = SurroundingRectangle(laplace, color=TEAL_B, buff=0.25)

        bayes_group = VGroup(bayes, anno_b).move_to((-3.5, 0.5, 0.0))
        laplace_group = VGroup(laplace, anno_l).move_to((3.5, 0.5, 0.0))

        self.play(FadeIn(bayes_group, shift=0.2 * RIGHT), run_time=0.8)
        self.play(FadeIn(laplace_group, shift=0.2 * LEFT), run_time=0.8)
        self.wait(0.4)

        # Bridge sentence
        bridge = Text(
            "From chance and inference to a general rule for learning from evidence.",
            font_size=34, color=GREY_E
        ).to_edge(DOWN).shift((0.0, 0.3, 0.0))
        self.play(Write(bridge), run_time=0.9)
        self.wait(1.2)


# ====================== 3) Bayes Equation (Parts) ======================
class BayesEquation(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Bayes’s theorem (parts)", font_size=44).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)

        eq = MathTex(r"P(H|E)=\frac{P(E|H)\,P(H)}{P(E)}").scale(1.2)
        eq.set_color_by_tex(r"P(H|E)", COLOR_POST)
        eq.set_color_by_tex(r"P(E|H)", COLOR_LIKE)
        eq.set_color_by_tex(r"P(H)"  , COLOR_PRIOR)
        eq.set_color_by_tex(r"P(E)"  , COLOR_EVID)

        self.play(Write(eq), run_time=1.2)
        self.wait(0.2)

        post  = eq.get_part_by_tex(r"P(H|E)")
        like  = eq.get_part_by_tex(r"P(E|H)")
        prior = eq.get_part_by_tex(r"P(H)")
        evid  = eq.get_part_by_tex(r"P(E)")

        b_post = Brace(post, DOWN);  t_post = b_post.get_text("posterior").set_color(COLOR_POST)
        b_like = Brace(like, UP);    t_like = b_like.get_text("likelihood").set_color(COLOR_LIKE)
        b_prio = Brace(prior, DOWN); t_prio = b_prio.get_text("prior").set_color(COLOR_PRIOR)
        b_evid = Brace(evid, UP);    t_evid = b_evid.get_text("evidence / marginal").set_color(COLOR_EVID)

        self.play(GrowFromCenter(b_post), FadeIn(t_post, shift=0.15 * DOWN), run_time=0.5)
        self.play(GrowFromCenter(b_like), FadeIn(t_like, shift=0.15 * UP), run_time=0.5)
        self.play(GrowFromCenter(b_prio), FadeIn(t_prio, shift=0.15 * DOWN), run_time=0.5)
        self.play(GrowFromCenter(b_evid), FadeIn(t_evid, shift=0.15 * UP), run_time=0.5)
        self.wait(0.5)

        # Quick “read-through”
        self.play(
            Indicate(prior, color=COLOR_PRIOR),
            Indicate(like,  color=COLOR_LIKE),
            Indicate(evid,  color=COLOR_EVID),
            Indicate(post,  color=COLOR_POST),
            run_time=1.2
        )
        self.wait(0.6)


# ===================== 4) Evidence (Total Probability) ==================
class EvidenceExpansion(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Where does P(E) come from?", font_size=44).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)

        eq = MathTex(r"P(E)=\sum_{i}P(E|H_i)P(H_i)").scale(1.1)
        eq.set_color_by_tex(r"P(E)", COLOR_EVID)
        eq.set_color_by_tex(r"P(E|H_i)", COLOR_LIKE)
        eq.set_color_by_tex(r"P(H_i)", COLOR_PRIOR)

        self.play(Write(eq), run_time=1.0)
        self.wait(0.4)

        note = Text("Evidence = weighted average of likelihoods across all hypotheses.", font_size=34, color=GREY_E)
        note.next_to(eq, DOWN, buff=0.5)
        self.play(FadeIn(note, shift=0.2 * DOWN), run_time=0.7)
        self.wait(1.1)


# ============ 5) Geometry: “Bayes is the geometry of belief” ===========
class GeometryOfBelief(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Geometry of changing beliefs", font_size=44).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)

        # Trackers
        prior  = ValueTracker(0.30)  # P(H)
        lik_h  = ValueTracker(0.80)  # P(E|H)
        lik_nh = ValueTracker(0.20)  # P(E|¬H)

        # Canvas rectangle
        W, Ht = 8.0, 4.6
        rect = Rectangle(width=W, height=Ht, stroke_color=GREY_D, stroke_width=2)
        rect.move_to((0.0, -0.1, 0.0))
        self.play(Create(rect), run_time=0.6)

        def x_left()  -> float: return rect.get_left()[0]
        def x_right() -> float: return rect.get_right()[0]
        def y_top()   -> float: return rect.get_top()[1]
        def y_bot()   -> float: return rect.get_bottom()[1]
        def x_mid()   -> float: return x_left() + prior.get_value() * W

        divider = always_redraw(lambda: Line(
            (x_mid(), y_bot(), 0.0), (x_mid(), y_top(), 0.0),
            color=COLOR_PRIOR, stroke_width=3
        ))
        lab_H  = always_redraw(lambda: Text("H", font_size=30, color=COLOR_PRIOR).next_to(
            Line((x_left(), y_bot(), 0.0), (x_mid(), y_bot(), 0.0)), DOWN, buff=0.2))
        lab_nH = always_redraw(lambda: Text("¬H", font_size=30, color=GREY_E).next_to(
            Line((x_mid(), y_bot(), 0.0), (x_right(), y_bot(), 0.0)), DOWN, buff=0.2))

        self.play(Create(divider), FadeIn(lab_H), FadeIn(lab_nH), run_time=0.8)

        # E regions
        def make_left_E() -> Rectangle:
            w = prior.get_value() * W
            h = lik_h.get_value() * Ht
            r = Rectangle(width=w, height=h,
                          fill_color=TEAL_B, fill_opacity=0.55,
                          stroke_color=TEAL_B, stroke_opacity=0.8, stroke_width=2)
            r.move_to((x_left() + w / 2.0, y_top() - h / 2.0, 0.0))
            return r

        def make_right_E() -> Rectangle:
            w = (1.0 - prior.get_value()) * W
            h = lik_nh.get_value() * Ht
            r = Rectangle(width=w, height=h,
                          fill_color=TEAL_B, fill_opacity=0.35,
                          stroke_color=TEAL_B, stroke_opacity=0.6, stroke_width=2)
            r.move_to((x_mid() + w / 2.0, y_top() - h / 2.0, 0.0))
            return r

        left_E  = always_redraw(make_left_E)
        right_E = always_redraw(make_right_E)
        self.play(FadeIn(left_E), FadeIn(right_E), run_time=0.8)

        # Braces: heights are likelihoods
        brace_l = always_redraw(lambda: Brace(left_E, RIGHT, color=COLOR_LIKE))
        txt_l   = always_redraw(lambda: brace_l.get_text("P(E | H)"))
        brace_r = always_redraw(lambda: Brace(right_E, LEFT))
        txt_r   = always_redraw(lambda: brace_r.get_text("P(E | ¬H)"))
        self.play(GrowFromCenter(brace_l), FadeIn(txt_l), GrowFromCenter(brace_r), FadeIn(txt_r), run_time=0.8)

        # Posterior readout
        def posterior() -> float:
            p  = prior.get_value()
            lh = lik_h.get_value()
            ln = lik_nh.get_value()
            den = lh * p + ln * (1.0 - p)
            return 0.0 if den == 0.0 else (lh * p) / den

        post_num = always_redraw(lambda:
            DecimalNumber(posterior(), num_decimal_places=3)
            .set_color(COLOR_POST).scale(1.1)
            .next_to(rect, RIGHT, buff=0.6)
        )
        post_label = Text("P(H | E)", font_size=36, color=COLOR_POST).next_to(post_num, UP, buff=0.1)
        self.play(FadeIn(post_label), FadeIn(post_num), run_time=0.6)

        # Equation card
        eq = MathTex(r"P(H|E)=\frac{P(E|H)P(H)}{P(E)}").scale(0.9)
        eq.set_color_by_tex(r"P(H|E)", COLOR_POST)
        eq.set_color_by_tex(r"P(E|H)", COLOR_LIKE)
        eq.set_color_by_tex(r"P(H)", COLOR_PRIOR)
        eq.set_color_by_tex(r"P(E)", COLOR_EVID)
        eq.next_to(post_num, DOWN, buff=0.2)
        self.play(Write(eq), run_time=0.8)

        # Animate two updates to show “geometry drives belief”
        self.play(
            prior.animate.set_value(0.55),
            lik_h.animate.set_value(0.65),
            lik_nh.animate.set_value(0.25),
            run_time=2.0, rate_func=smooth
        )
        self.wait(0.5)
        self.play(
            prior.animate.set_value(0.20),
            lik_h.animate.set_value(0.85),
            lik_nh.animate.set_value(0.05),
            run_time=2.0, rate_func=smooth
        )
        self.wait(0.8)


# =================== 6) Numerical Example (Test) =======================
class NumericalExample(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("A concrete example (diagnostic test)", font_size=44).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)

        # Parameters
        pH   = 0.01   # prevalence
        pEH  = 0.90   # sensitivity
        pEnH = 0.05   # false positive rate

        # Show inputs
        t1 = Text("P(H) = 0.01 (prevalence)", font_size=34, color=COLOR_PRIOR)
        t2 = Text("P(E | H) = 0.90 (sensitivity)", font_size=34, color=COLOR_LIKE)
        t3 = Text("P(E | ¬H) = 0.05 (false positive rate)", font_size=34, color=COLOR_LIKE)
        params = VGroup(t1, t2, t3).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT).shift((0.2, 0.0, 0.0))
        self.play(LaggedStart(*[FadeIn(m, shift=0.1 * RIGHT) for m in params], lag_ratio=0.2, run_time=1.0))
        self.wait(0.3)

        # Compute P(E) and P(H|E)
        pE = pEH * pH + pEnH * (1 - pH)
        pHgivenE = (pEH * pH) / pE

        # Show Bayes formula with numbers
        eq = MathTex(r"P(H|E)=\frac{P(E|H)P(H)}{P(E)}").scale(0.95)
        eq.set_color_by_tex(r"P(H|E)", COLOR_POST)
        eq.set_color_by_tex(r"P(E|H)", COLOR_LIKE)
        eq.set_color_by_tex(r"P(H)", COLOR_PRIOR)
        eq.set_color_by_tex(r"P(E)", COLOR_EVID)

        nums = MathTex(
            rf"P(H|E)=\frac{{{pEH:.2f}\cdot{pH:.2f}}}{{{pE:.3f}}}\approx {pHgivenE:.3f}"
        ).scale(0.95)
        nums.set_color_by_tex(r"P(H|E)", COLOR_POST)

        eq_group = VGroup(eq, nums).arrange(DOWN, buff=0.35).to_edge(RIGHT).shift((-0.2, 0.0, 0.0))
        self.play(Write(eq), run_time=0.9)
        self.wait(0.2)
        self.play(Write(nums), run_time=0.9)
        self.wait(0.6)

        # Area diagram to “explain” the low posterior despite strong sensitivity
        caption = Text("Even with a strong test, low base rate keeps P(H|E) modest.", font_size=32, color=GREY_E)
        caption.next_to(eq_group, DOWN, buff=0.4)
        self.play(FadeIn(caption, shift=0.15 * DOWN), run_time=0.6)

        # Quick miniature geometry inset
        W, Ht = 6.4, 3.6
        rect = Rectangle(width=W, height=Ht, stroke_color=GREY_D, stroke_width=2).to_edge(DOWN).shift((0.0, 0.3, 0.0))
        self.play(Create(rect), run_time=0.5)

        # Columns
        x_left = rect.get_left()[0]
        x_mid = x_left + pH * W
        x_right = rect.get_right()[0]
        y_top = rect.get_top()[1]
        y_bot = rect.get_bottom()[1]

        divider = Line((x_mid, y_bot, 0.0), (x_mid, y_top, 0.0), color=COLOR_PRIOR, stroke_width=3)
        self.play(Create(divider), run_time=0.4)

        left_E = Rectangle(width=pH * W, height=pEH * Ht,
                           fill_color=TEAL_B, fill_opacity=0.55,
                           stroke_color=TEAL_B, stroke_opacity=0.9, stroke_width=2)
        left_E.move_to((x_left + (pH * W) / 2.0, y_top - (pEH * Ht) / 2.0, 0.0))

        right_E = Rectangle(width=(1 - pH) * W, height=pEnH * Ht,
                            fill_color=TEAL_B, fill_opacity=0.35,
                            stroke_color=TEAL_B, stroke_opacity=0.7, stroke_width=2)
        right_E.move_to((x_mid + ((1 - pH) * W) / 2.0, y_top - (pEnH * Ht) / 2.0, 0.0))

        self.play(FadeIn(left_E), FadeIn(right_E), run_time=0.6)

        callout = VGroup(
            Text("Posterior = left E-area ÷ total E-area", font_size=30, color=COLOR_POST)
        ).next_to(rect, UP, buff=0.2)
        self.play(FadeIn(callout), run_time=0.5)
        self.wait(1.0)


# ========================== 7) Takeaway ================================
class Takeaway(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Main takeaways", weight="BOLD", font_size=52).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)

        bullets = VGroup(
            Text("Bayes’s theorem updates beliefs: prior × likelihood ÷ evidence.", font_size=36).set_color(GREY_E),
            Text("Think geometrically: posterior is the share of E that lies in H.", font_size=36).set_color(GREY_E),
            Text("Low base rates matter; strong tests can still yield modest P(H|E).", font_size=36).set_color(GREY_E),
            Text("Modeling discipline (clear hypotheses) keeps ‘P(E)’ meaningful.", font_size=36).set_color(GREY_E),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).to_edge(LEFT).shift((0.2, 0.0, 0.0))

        self.play(LaggedStart(*[FadeIn(m, shift=0.1 * RIGHT) for m in bullets], lag_ratio=0.15, run_time=1.2))
        self.wait(1.2)

        end = Text("Thanks for watching!", font_size=48).set_color_by_gradient(BLUE_B, TEAL_A)
        self.play(Write(end.next_to(bullets, DOWN, buff=0.8)), run_time=0.8)
        self.wait(0.8)
