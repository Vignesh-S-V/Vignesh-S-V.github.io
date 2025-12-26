from manim import *
import random

class LavatharFullEpic(Scene):
    def construct(self):
        # 1. ஆரம்பத் தலைப்பு (Act 1: Paradise in Fire) [cite: 11]
        title = Text("LAVATHAR", font_size=72, color=GOLD).set_glow_factor(1)
        subtitle = Text("Act 1: Paradise in Fire", font_size=36, color=WHITE).next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # 2. சூரியனின் தத்ரூபமான அமைப்பு (Realistic Sun Structure) [cite: 15, 16]
        # சூரியனின் மையப்பகுதி மற்றும் ஒளிரும் அடுக்குகள்
        sun_layers = VGroup(*[
            Circle(radius=1.5 + (i * 0.15), color=c, fill_opacity=0.2 - (i * 0.04))
            for i, c in enumerate([YELLOW, ORANGE, RED, MAROON])
        ])
        sun_core = Circle(radius=1.4, color=YELLOW, fill_opacity=1).set_glow_factor(2)
        sun = VGroup(sun_layers, sun_core)

        # காந்தப்புல கோடுகள் (Magnetic Field Lines) 
        mag_lines = VGroup(*[
            Arc(radius=2.2 + random.uniform(0, 0.6), start_angle=random.uniform(0, TAU), 
                angle=random.uniform(0.6, 1.8), color=ORANGE, stroke_width=2)
            for _ in range(25)
        ])

        self.play(FadeIn(sun), Create(mag_lines))
        
        # சூரியன் துடிப்பது போன்ற அனிமேஷன் (Pulsing Effect) [cite: 9]
        sun.add_updater(lambda m, dt: m.scale(1 + 0.005 * np.sin(TAU * dt)))
        self.play(Rotate(mag_lines, angle=PI/2), run_time=4, rate_func=linear)

        # 3. பேரழிவு - சூரியன் சிவப்பாதல் (The Unraveling) [cite: 341]
        warning = Text("STELLAR RECALIBRATION", color=RED, font_size=40).to_edge(UP)
        self.play(Write(warning))
        self.play(
            sun.animate.set_color(RED_E).scale(1.4),
            mag_lines.animate.set_color(RED).scale(1.8).set_stroke(width=4),
            run_time=3
        )
        # சோலார் பிளாஷ் (Solar Flash) 
        self.play(Flash(sun, color=RED, flash_radius=4.5, num_lines=50))
        self.wait(1)

        # 4. தப்பிக்கும் விண்கலங்கள் (The 12 Evacuation Ships) 
        ships = VGroup(*[
            Triangle(color=WHITE).scale(0.1).move_to([random.uniform(-1, 1), random.uniform(-0.5, 0.5), 0])
            for _ in range(12)
        ])
        
        fleet_text = Text("The Return: 120,000 Souls", font_size=30).next_to(sun, DOWN)
        self.play(Write(fleet_text), FadeIn(ships))
        self.play(
            ships.animate.shift(UP * 12).set_opacity(0),
            sun.animate.scale(2).set_opacity(0.1),
            run_time=5,
            rate_func=exponential_decay
        )

        # 5. முடிவு - பூமியின் மறுமலர்ச்சி (The Return) [cite: 985, 1013]
        self.play(FadeOut(sun), FadeOut(warning), FadeOut(fleet_text))
        earth = Circle(radius=1.8, color=BLUE, fill_opacity=0.6)
        greenery = Annulus(inner_radius=0, outer_radius=1.8, color=GREEN, fill_opacity=0.3)
        final_quote = Text("We all return to light.", font_size=42, color=GOLD)
        
        self.play(Create(earth), FadeIn(greenery))
        self.wait(1)
        self.play(ReplacementTransform(VGroup(earth, greenery), final_quote))
        self.play(Indicate(final_quote))
        self.wait(3)
