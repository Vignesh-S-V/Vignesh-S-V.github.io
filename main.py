from manim import *
import random

class LavatharRealistic(Scene):
    def construct(self):
        # 1. ஆரம்பத் தலைப்பு (Cinematic Intro)
        intro_text = Text("LAVATHAR", font_size=80, color=GOLD).set_glow_factor(1)
        self.play(Write(intro_text), run_time=2)
        self.play(intro_text.animate.scale(0.5).to_edge(UP), run_time=1)

        # 2. தத்ரூபமான சூரியன் (Realistic Sun Construction)
        # பல வண்ண அடுக்குகளைச் சேர்த்து ஒரு கோளம் போன்ற தோற்றம்
        layers = VGroup(*[
            Circle(radius=1.5 + (i * 0.1), color=color, fill_opacity=0.2 - (i * 0.02))
            for i, color in enumerate([YELLOW, ORANGE, RED, DARK_RED])
        ])
        core = Circle(radius=1.4, color=YELLOW, fill_opacity=1).set_glow_factor(2)
        sun = VGroup(layers, core)

        # பிளாஸ்மா அலைகள் (Plasma Filaments)
        filaments = VGroup(*[
            Arc(radius=2.5 + random.uniform(0, 0.5), start_angle=random.uniform(0, TAU), 
                angle=random.uniform(0.5, 1.5), color=ORANGE, stroke_width=2)
            for _ in range(20)
        ])

        self.play(FadeIn(sun), Create(filaments))

        # சூரியன் துடிப்பது மற்றும் பிளாஸ்மா சுழல்வது (Realistic Motion)
        def update_sun(m, dt):
            m.scale(1 + 0.01 * np.sin(TAU * dt))
        
        sun.add_updater(update_sun)
        self.play(Rotate(filaments, angle=PI, run_time=5, rate_func=linear))

        # 3. பேரழிவு - சூரியன் சிவப்பாதல் (The Unraveling)
        announcement = Text("STELLAR RECALIBRATION", color=RED, font_size=36).next_to(sun, DOWN)
        self.play(Write(announcement))
        self.play(
            sun.animate.set_color(RED_E).scale(1.5),
            filaments.animate.set_color(RED).scale(2).set_stroke(width=5),
            run_time=3
        )
        self.play(Flash(sun, color=RED, flash_radius=4, num_lines=40))

        # 4. தப்பிக்கும் விண்கலங்கள் (The Fleet as Particles)
        fleet = VGroup(*[
            Dot(point=[random.uniform(-1, 1), random.uniform(-3, -2), 0], color=WHITE)
            for _ in range(12)
        ])
        
        self.play(FadeIn(fleet))
        self.play(
            fleet.animate.shift(UP * 10).set_opacity(0),
            sun.animate.scale(2).set_opacity(0.1),
            run_time=4,
            rate_func=exponential_decay
        )

        # 5. முடிவு (The Return)
        self.play(FadeOut(sun), FadeOut(announcement))
        final_quote = Text("We all return to light.", font_size=40, color=GOLD)
        self.play(Write(final_quote))
        self.wait(2)
