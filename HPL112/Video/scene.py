# bayes_movie.py
from manim import *
import numpy as np

# --------- Styling helpers (colors consistent across scenes) ----------
COLOR_POST = YELLOW_B
COLOR_LIKE = BLUE_B
COLOR_PRIOR = ORANGE
COLOR_EVID = PURPLE_B
BG = "#0e0e10"  # A dark background, as requested


# =========================== 1) Title Card ==============================
# Your original scene is great. Just adding a longer wait.
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
        group.move_to(ORIGIN)

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
        
        # Added longer wait for pacing
        self.wait(4)


# =========================== 2) History ================================
# Your original scene is good. Just adding a longer wait.
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
        self.wait(1.4)

        # Bridge sentence
        bridge = Text(
            "From chance and inference to a general rule for learning from evidence.",
            font_size=34, color=GREY_E
        ).to_edge(DOWN).shift((0.0, 0.3, 0.0))
        self.play(Write(bridge), run_time=1.5)
        
        # Added longer wait
        self.wait(4)


# ===================== 3) What is Bayesianism? (NEW) ====================
# This new scene provides the conceptual core.
class WhatIsBayesianism(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("The core idea: Updating beliefs", font_size=44).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)
        self.wait(1)

        # 1. Start with a Prior
        prior_txt = Text("Prior Belief: P(H)", color=COLOR_PRIOR).scale(0.9)
        prior_desc = Text("Our starting belief in Hypothesis H", color=GREY_C).scale(0.7)
        prior_group = VGroup(prior_txt, prior_desc).arrange(DOWN, buff=0.15)
        prior_group.move_to(LEFT * 4)

        self.play(Write(prior_txt), run_time=1)
        self.play(FadeIn(prior_desc, shift=0.1 * DOWN), run_time=0.7)
        self.wait(1.5)

        # 2. Add Evidence
        evidence_txt = Text("New Evidence: E", color=COLOR_EVID).scale(0.9)
        evidence_desc = Text("We observe some new data E", color=GREY_C).scale(0.7)
        evidence_group = VGroup(evidence_txt, evidence_desc).arrange(DOWN, buff=0.15)
        evidence_group.move_to(ORIGIN)
        
        plus = MathTex("+").scale(1.5).next_to(prior_group, RIGHT, buff=0.8)
        evidence_group.next_to(plus, RIGHT, buff=0.8)
        
        self.play(Write(plus), run_time=0.5)
        self.play(Write(evidence_txt), run_time=1)
        self.play(FadeIn(evidence_desc, shift=0.1 * DOWN), run_time=0.7)
        self.wait(1.5)

        # 3. Get a Posterior
        post_txt = Text("Posterior Belief: P(H|E)", color=COLOR_POST).scale(0.9)
        post_desc = Text("Our updated belief in H, *given* E", color=GREY_C).scale(0.7)
        post_group = VGroup(post_txt, post_desc).arrange(DOWN, buff=0.15)
        
        arrow = MathTex(r"\rightarrow").scale(1.5).next_to(evidence_group, RIGHT, buff=0.8)
        post_group.next_to(arrow, RIGHT, buff=0.8)

        self.play(Write(arrow), run_time=0.5)
        self.play(Write(post_txt), run_time=1)
        self.play(FadeIn(post_desc, shift=0.1 * DOWN), run_time=0.7)
        self.wait(2)

        # 4. State the question
        flow = VGroup(prior_group, plus, evidence_group, arrow, post_group).move_to(ORIGIN)
        self.play(flow.animate.shift(UP * 2))
        
        question = Text(
            "How do we *quantify* this update?",
            font_size=40,
            t2c={"quantify": YELLOW}
        ).next_to(flow, DOWN, buff=1.2)
        
        self.play(Write(question), run_time=1.2)
        self.wait(4)


# ============ 4) Deriving the Equation (REPLACES BayesEquation) =============
# This scene builds the equation from scratch, giving it meaning.
class DerivingTheEquation(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Deriving the theorem", font_size=44).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)
        self.wait(1)

        # Start with the definition of conditional probability
        definition = MathTex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}").scale(1.2)
        def_label = Text("Definition of Conditional Probability", font_size=32, color=GREY_C)
        def_label.next_to(definition, DOWN, buff=0.4)
        
        self.play(Write(definition), run_time=1.2)
        self.play(FadeIn(def_label, shift=0.1 * DOWN), run_time=0.7)
        self.wait(2)

        # Apply it to our terms H and E
        eq1 = MathTex(r"P(H|E) = \frac{P(H \cap E)}{P(E)}").scale(1.2)
        eq1.move_to(definition.get_center())
        self.play(TransformMatchingTex(definition, eq1), FadeOut(def_label))
        self.wait(1.5)

        # Now, consider the other direction
        eq2_start = MathTex(r"P(E|H) = \frac{P(E \cap H)}{P(H)}").scale(1.2)
        eq2_start.next_to(eq1, DOWN, buff=1.0)
        self.play(Write(eq2_start), run_time=1.2)
        self.wait(1)

        # Rearrange it
        eq2_re = MathTex(r"P(E \cap H) = P(E|H) P(H)").scale(1.2)
        eq2_re.move_to(eq2_start.get_center())
        self.play(TransformMatchingTex(eq2_start, eq2_re))
        self.wait(1.5)

        # Note that P(H ∩ E) = P(E ∩ H)
        intersect_note = Text("Note: P(H ∩ E) is the same as P(E ∩ H)", font_size=28, color=GREY_B)
        intersect_note.next_to(VGroup(eq1, eq2_re), UP, buff=0.8)
        self.play(FadeIn(intersect_note, shift=0.1 * UP), run_time=0.7)
        self.wait(1)

        # Now, substitute!
        self.play(FadeOut(intersect_note))
        
        sub_line = Line(eq2_re.get_bottom(), eq1.get_part_by_tex("P(H \cap E)").get_top(), color=YELLOW)
        self.play(
            Create(sub_line),
            eq2_re.animate.set_color(COLOR_LIKE),
            eq1.get_part_by_tex("P(H \cap E)").animate.set_color(COLOR_LIKE),
            run_time=1.5
        )
        self.wait(0.5)

        # The final form
        final_eq = MathTex(r"P(H|E)", r"=", r"\frac{P(E|H) P(H)}{P(E)}").scale(1.4)
        final_eq.get_part_by_tex(r"P(H|E)").set_color(COLOR_POST)
        final_eq.get_part_by_tex(r"P(E|H) P(H)").set_color(COLOR_LIKE)
        # Manim needs a bit of help sometimes to color substrings
        final_eq[2][5:9].set_color(COLOR_PRIOR) # P(H)
        final_eq.get_part_by_tex(r"P(E)").set_color(COLOR_EVID)

        self.play(
            FadeOut(sub_line),
            TransformMatchingTex(VGroup(eq1, eq2_re), final_eq)
        )
        self.wait(2)

        # --- Add the labels ---
        # This is the part from your original BayesEquation scene, now it has context
        post  = final_eq.get_part_by_tex(r"P(H|E)")
        like  = final_eq.get_part_by_tex(r"P(E|H)")
        prior = final_eq[2][5:9] # P(H)
        evid  = final_eq.get_part_by_tex(r"P(E)")

        b_post = Brace(post, DOWN, color=GREY_A); t_post = b_post.get_text("Posterior").set_color(COLOR_POST)
        b_like = Brace(like, UP, color=GREY_A);   t_like = b_like.get_text("Likelihood").set_color(COLOR_LIKE)
        b_prio = Brace(prior, UP, color=GREY_A);  t_prio = b_prio.get_text("Prior").set_color(COLOR_PRIOR)
        b_evid = Brace(evid, DOWN, color=GREY_A); t_evid = b_evid.get_text("Evidence").set_color(COLOR_EVID)

        self.play(
            GrowFromCenter(b_post), FadeIn(t_post, shift=0.15 * DOWN),
            GrowFromCenter(b_prio), FadeIn(t_prio, shift=0.15 * UP),
            run_time=1
        )
        self.wait(1)
        self.play(
            GrowFromCenter(b_like), FadeIn(t_like, shift=0.15 * UP),
            GrowFromCenter(b_evid), FadeIn(t_evid, shift=0.15 * DOWN),
            run_time=1
        )
        self.wait(3)
        
        # Read-through
        self.play(
            Indicate(t_prio), Indicate(prior),
            run_time=1.5
        )
        self.play(
            Indicate(t_like), Indicate(like),
            run_time=1.5
        )
        self.play(
            Indicate(t_evid), Indicate(evid),
            run_time=1.5
        )
        self.play(
            Indicate(t_post), Indicate(post),
            run_time=1.5
        )
        self.wait(3)


# ============ 5) Geometry of Belief (REFACTORED) =======================
# This scene is now the centerpiece, building the visual intuition
# that your original scene jumped right into.
class GeometryOfBelief(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Geometry of changing beliefs", font_size=44).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)

        # Trackers
        prior_val  = ValueTracker(0.30)  # P(H)
        lik_h_val  = ValueTracker(0.80)  # P(E|H)
        lik_nh_val = ValueTracker(0.20)  # P(E|¬H)

        # --- Step 1: The Canvas (Total Probability) ---
        W, Ht = 8.0, 4.6
        rect = Rectangle(width=W, height=Ht, stroke_color=GREY_D, stroke_width=2)
        rect.move_to((0.0, -0.1, 0.0))
        rect_label = Text("Space of all possibilities (Area = 1)", font_size=28, color=GREY_C)
        rect_label.next_to(rect, UP, buff=0.3)
        
        self.play(Create(rect), Write(rect_label), run_time=1)
        self.wait(1.5)

        # --- Step 2: The Prior ---
        def x_left()  : return rect.get_left()[0]
        def x_right() : return rect.get_right()[0]
        def y_top()   : return rect.get_top()[1]
        def y_bot()   : return rect.get_bottom()[1]
        def x_mid()   : return x_left() + prior_val.get_value() * W

        divider = always_redraw(lambda: Line(
            (x_mid(), y_bot(), 0.0), (x_mid(), y_top(), 0.0),
            color=COLOR_PRIOR, stroke_width=3
        ))
        
        # H region
        rect_H = always_redraw(lambda: Rectangle(
            width=prior_val.get_value() * W, height=Ht,
            fill_color=COLOR_PRIOR, fill_opacity=0.2, stroke_width=0
        ).align_to(rect, LEFT+DOWN))
        
        # not-H region
        rect_nH = always_redraw(lambda: Rectangle(
            width=(1 - prior_val.get_value()) * W, height=Ht,
            fill_color=GREY_E, fill_opacity=0.1, stroke_width=0
        ).align_to(rect, RIGHT+DOWN))
        
        lab_H  = always_redraw(lambda: Text("P(H)", font_size=30, color=COLOR_PRIOR).move_to(
            (x_left() + (x_mid() - x_left()) / 2, y_bot() - 0.3, 0)
        ))
        lab_nH = always_redraw(lambda: Text("P(¬H)", font_size=30, color=GREY_E).move_to(
            (x_mid() + (x_right() - x_mid()) / 2, y_bot() - 0.3, 0)
        ))
        
        prior_label = Text("Our Prior belief, P(H), splits the space.", font_size=28, color=COLOR_PRIOR)
        prior_label.next_to(rect, DOWN, buff=0.8)

        self.play(
            FadeOut(rect_label),
            FadeIn(rect_H), FadeIn(rect_nH),
            Create(divider),
            Write(lab_H), Write(lab_nH),
            Write(prior_label),
            run_time=1.5
        )
        self.wait(2)

        # --- Step 3: The Likelihoods ---
        def make_left_E():
            w = prior_val.get_value() * W
            h = lik_h_val.get_value() * Ht
            return Rectangle(width=w, height=h,
                             fill_color=COLOR_LIKE, fill_opacity=0.6,
                             stroke_color=COLOR_LIKE, stroke_opacity=0.9, stroke_width=2
                             ).align_to(rect, LEFT+UP)

        def make_right_E():
            w = (1.0 - prior_val.get_value()) * W
            h = lik_nh_val.get_value() * Ht
            return Rectangle(width=w, height=h,
                             fill_color=COLOR_LIKE, fill_opacity=0.3,
                             stroke_color=COLOR_LIKE, stroke_opacity=0.7, stroke_width=2
                             ).align_to(rect, RIGHT+UP)

        left_E  = always_redraw(make_left_E)
        right_E = always_redraw(make_right_E)
        
        like_label = Text("Likelihoods shade in the 'Evidence' (E)", font_size=28, color=COLOR_LIKE)
        like_label.next_to(prior_label, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(left_E), FadeIn(right_E), Write(like_label), run_time=1.2)
        self.wait(1)

        # Add likelihood braces
        brace_l = always_redraw(lambda: Brace(left_E, RIGHT, color=COLOR_LIKE))
        txt_l   = always_redraw(lambda: brace_l.get_text(r"P(E|H)").set_color(COLOR_LIKE))
        
        brace_r = always_redraw(lambda: Brace(right_E, LEFT, color=GREY_C))
        txt_r   = always_redraw(lambda: brace_r.get_text(r"P(E|¬H)").set_color(GREY_C))
        
        self.play(GrowFromCenter(brace_l), FadeIn(txt_l), GrowFromCenter(brace_r), FadeIn(txt_r), run_time=1)
        self.wait(2.5)

        # --- Step 4: The Posterior ---
        # The Posterior is the RATIO of the areas
        post_label_text = Text(
            "Posterior P(H|E) = \n'H-and-E' area / 'Total E' area",
            font_size=32, color=COLOR_POST
        ).to_edge(RIGHT).shift(LEFT * 0.5 + UP * 1.5)
        
        self.play(Write(post_label_text), run_time=1.5)
        self.wait(1)
        
        # Highlight the two components
        self.play(
            Indicate(left_E, color=COLOR_POST, scale_factor=1.05),
            run_time=1.5
        )
        self.play(
            Indicate(VGroup(left_E, right_E), color=COLOR_EVID, scale_factor=1.02),
            run_time=1.5
        )
        self.wait(2)
        
        # Add the equation card from your original
        eq = MathTex(r"P(H|E)=\frac{P(E|H)P(H)}{P(E|H)P(H) + P(E| \neg H)P(\neg H)}")
        eq.set_color_by_tex(r"P(H|E)", COLOR_POST)
        eq.set_color_by_tex(r"P(E|H)", COLOR_LIKE)
        eq.set_color_by_tex(r"P(H)", COLOR_PRIOR)
        eq.set_color_by_tex(r"P(E| \neg H)", GREY_C)
        eq.set_color_by_tex(r"P(\neg H)", GREY_E)
        eq.scale(0.7).next_to(post_label_text, DOWN, buff=0.4)
        
        self.play(Write(eq), run_time=1.5)
        self.wait(3)

        # --- Step 5: Animate it! ---
        # This is your original animation, now with full context.
        def posterior() -> float:
            p  = prior_val.get_value()
            lh = lik_h_val.get_value()
            ln = lik_nh_val.get_value()
            num = lh * p
            den = num + ln * (1.0 - p)
            return 0.0 if den == 0.0 else num / den

        post_num = always_redraw(lambda:
            DecimalNumber(posterior(), num_decimal_places=3)
            .set_color(COLOR_POST).scale(1.1)
            .next_to(eq, DOWN, buff=0.3)
        )
        post_label = Text("P(H | E) =", font_size=36, color=COLOR_POST)
        post_label.next_to(post_num, LEFT, buff=0.2)
        
        self.play(FadeIn(post_label), FadeIn(post_num), run_time=0.6)
        self.wait(1)

        # Animate two updates to show “geometry drives belief”
        self.play(
            prior_val.animate.set_value(0.55),
            lik_h_val.animate.set_value(0.65),
            lik_nh_val.animate.set_value(0.25),
            run_time=4.0, rate_func=smooth
        )
        self.wait(1.5)
        
        self.play(
            prior_val.animate.set_value(0.05), # Low prior
            lik_h_val.animate.set_value(0.95), # High likelihood
            lik_nh_val.animate.set_value(0.02), # Low false positive
            run_time=5.0, rate_func=smooth
        )
        self.wait(1.5)
        
        self.play(
            prior_val.animate.set_value(0.5),
            lik_h_val.animate.set_value(0.5),
            lik_nh_val.animate.set_value(0.5),
            run_time=4.0, rate_func=smooth
        )
        self.wait(4)


# =================== 6) Numerical Example (Test) =======================
# Refactored to be clearer and connect to the previous scene
class NumericalExample(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("A concrete example (diagnostic test)", font_size=44).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)

        # Parameters
        pH   = 0.01   # prevalence (H = "Has Disease")
        pEH  = 0.90   # sensitivity (E = "Tests Positive")
        pEnH = 0.05   # false positive rate

        # Show inputs
        t_H = Text("H = 'Patient has disease'", font_size=34, color=GREY_E)
        t_E = Text("E = 'Patient tests positive'", font_size=34, color=GREY_E)
        t_group = VGroup(t_H, t_E).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT).shift(UP * 2.0)
        self.play(FadeIn(t_group, shift=0.1 * RIGHT), run_time=0.8)
        self.wait(1)

        t1 = MathTex(r"P(H) = 0.01", r"\text{ (prevalence)}").set_color_by_tex("P(H)", COLOR_PRIOR)
        t2 = MathTex(r"P(E|H) = 0.90", r"\text{ (sensitivity)}").set_color_by_tex("P(E|H)", COLOR_LIKE)
        t3 = MathTex(r"P(E|\neg H) = 0.05", r"\text{ (false positive rate)}").set_color_by_tex(r"P(E|\neg H)", GREY_C)
        params = VGroup(t1, t2, t3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        params.next_to(t_group, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(LaggedStart(*[FadeIn(m, shift=0.1 * RIGHT) for m in params], lag_ratio=0.2, run_time=1.2))
        self.wait(2)

        # Compute P(E) and P(H|E)
        pE = pEH * pH + pEnH * (1 - pH)
        pHgivenE = (pEH * pH) / pE

        # Show Bayes formula with numbers
        eq_group = VGroup(
            MathTex(r"P(H|E) = \frac{P(E|H)P(H)}{P(E|H)P(H) + P(E|\neg H)P(\neg H)}"),
            MathTex(rf"P(H|E) = \frac{{{pEH:.2f} \cdot {pH:.2f}}}{{({pEH:.2f} \cdot {pH:.2f}) + ({pEnH:.2f} \cdot {1-pH:.2f})}}"),
            MathTex(rf"P(H|E) = \frac{{{pEH * pH:.4f}}}{{{pE:.4f}}}"),
            MathTex(rf"P(H|E) \approx {pHgivenE:.3f}")
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).to_edge(RIGHT).shift(LEFT * 0.5 + UP * 0.5)
        
        eq_group[0].set_color_by_tex("P(H|E)", COLOR_POST)
        eq_group[0].set_color_by_tex("P(E|H)", COLOR_LIKE)
        eq_group[0].set_color_by_tex("P(H)", COLOR_PRIOR)
        
        eq_group[3].set_color(COLOR_POST)

        self.play(Write(eq_group[0]), run_time=1.0)
        self.wait(1.5)
        self.play(Write(eq_group[1]), run_time=1.5)
        self.wait(1.0)
        self.play(Write(eq_group[2]), run_time=1.0)
        self.wait(1.0)
        self.play(Write(eq_group[3]), run_time=1.2)
        self.wait(2)

        # Area diagram to “explain” the low posterior
        caption = Text("Why so low? The geometry shows it.", font_size=32, color=GREY_E)
        caption.to_edge(DOWN).shift(UP * 2.5)
        self.play(FadeIn(caption, shift=0.15 * DOWN), run_time=0.6)
        self.wait(1)

        # Quick miniature geometry inset
        W, Ht = 7.0, 3.8
        rect = Rectangle(width=W, height=Ht, stroke_color=GREY_D, stroke_width=2).to_edge(DOWN).shift(UP * 0.4)
        
        x_left = rect.get_left()[0]
        x_mid = x_left + pH * W
        x_right = rect.get_right()[0]
        y_top = rect.get_top()[1]
        y_bot = rect.get_bottom()[1]

        # Draw the regions
        rect_H = Rectangle(width=pH * W, height=Ht, fill_color=COLOR_PRIOR, fill_opacity=0.2, stroke_width=0)
        rect_H.align_to(rect, LEFT+DOWN)
        lab_H = Text("P(H) = 1%", font_size=24, color=COLOR_PRIOR).move_to(rect_H)
        
        rect_nH = Rectangle(width=(1-pH)*W, height=Ht, fill_color=GREY_E, fill_opacity=0.1, stroke_width=0)
        rect_nH.align_to(rect, RIGHT+DOWN)
        lab_nH = Text("P(¬H) = 99%", font_size=24, color=GREY_E).move_to(rect_nH)

        self.play(Create(rect), FadeIn(rect_H), FadeIn(rect_nH), run_time=0.8)
        self.play(Write(lab_H), Write(lab_nH), run_time=0.8)
        self.wait(1.5)

        # Draw the E regions
        left_E = Rectangle(width=pH * W, height=pEH * Ht,
                           fill_color=COLOR_LIKE, fill_opacity=0.6, stroke_width=0)
        left_E.align_to(rect, LEFT+UP)
        area_l_label = Text("P(E ∩ H)\nTrue Positives", font_size=20, color=WHITE).move_to(left_E)

        right_E = Rectangle(width=(1 - pH) * W, height=pEnH * Ht,
                            fill_color=COLOR_LIKE, fill_opacity=0.3, stroke_width=0)
        right_E.align_to(rect, RIGHT+UP)
        area_r_label = Text("P(E ∩ ¬H)\nFalse Positives", font_size=20, color=WHITE).move_to(right_E)

        self.play(FadeIn(left_E), FadeIn(right_E), run_time=1.0)
        self.play(Write(area_l_label), Write(area_r_label), run_time=1.0)
        self.wait(2)

        # Highlight the final ratio
        callout = Text(
            "Posterior = (True Positives) / (All Positives)",
            font_size=30, color=COLOR_POST
        ).next_to(rect, UP, buff=0.2)
        
        self.play(Write(callout), run_time=1.0)
        
        # Flash the areas
        self.play(Indicate(left_E, color=COLOR_POST, scale_factor=1.1), run_time=1.2)
        self.play(Indicate(VGroup(left_E, right_E), color=COLOR_EVID, scale_factor=1.02), run_time=1.2)
        
        final_note = Text(
            "The 'False Positive' area is much larger than the 'True Positive' area!",
            font_size=28, color=YELLOW
        ).next_to(callout, UP, buff=0.2)
        self.play(FadeIn(final_note, shift=0.1*UP), run_time=0.8)
        
        self.wait(5)


# ========================== 7) Takeaway ================================
# Your original scene is perfect. Just adding a long wait.
class Takeaway(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Main takeaways", weight="BOLD", font_size=52).to_edge(UP)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.6)

        bullets = VGroup(
            Text("• Bayes’s theorem updates beliefs: prior × likelihood ÷ evidence.", font_size=36).set_color(GREY_E),
            Text("• Think geometrically: posterior is the share of E that lies in H.", font_size=36).set_color(GREY_E),
            Text("• Low base rates matter; strong tests can still yield modest P(H|E).", font_size=36).set_color(GREY_E),
            Text("• Modeling discipline (clear hypotheses) keeps ‘P(E)’ meaningful.", font_size=36).set_color(GREY_E),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).scale(0.9).set_x(0)

        self.play(LaggedStart(*[FadeIn(m, shift=0.1 * RIGHT) for m in bullets], lag_ratio=0.25, run_time=2.0))
        self.wait(4)

        end = Text("Thanks for watching!", font_size=48).set_color_by_gradient(BLUE_B, TEAL_A)
        self.play(Write(end.next_to(bullets, DOWN, buff=0.8)), run_time=0.8)
        
        # Long final wait
        self.wait(5)