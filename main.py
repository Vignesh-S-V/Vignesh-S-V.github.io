from manim import *
import os

# அனிமேஷன் வகுப்பு
class LavatharAnimation(Scene):
    def construct(self):
        # 1. பின்னணி மற்றும் ஆரம்பத் தலைப்பு
        self.camera.background_color = "#000000"
        
        title = Text("LAVATHAR", font_size=72, color=GOLD)
        subtitle = Text("The Sun's Children", font_size=36, color=WHITE).next_to(title, DOWN)
        
        # திரைக்கதை: காட்சி 1 - அறிமுகம் [cite: 7, 11]
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # 2. சூரியன் மற்றும் பிளாஸ்மா உருவாக்கம் [cite: 15, 23]
        # சூரியனின் மையப்பகுதி 15.7 மில்லியன் கெல்வின் வெப்பநிலையைக் குறிக்கிறது [cite: 37]
        sun = Circle(radius=2, color=YELLOW, fill_opacity=0.8)
        sun.set_glow_factor(1)
        
        # பிளாஸ்மா அலைகள் [cite: 15]
        plasma_waves = Annulus(inner_radius=2, outer_radius=2.4, color=ORANGE, fill_opacity=0.4)
        
        self.play(Create(sun))
        # rate_func இங்கே சீராக மாற்றப்பட்டுள்ளது (பிழையைத் தவிர்க்க)
        self.play(
            sun.animate.scale(1.2), 
            Create(plasma_waves),
            rate_func=smooth 
        )
        self.wait(1)

        # 3. தகவல் பலகை (Text info)
        description = Text(
            "Sol City Prime: 200,000 km below the surface", 
            font_size=25,
            color=WHITE
        ).to_edge(UP)
        
        # திரைக்கதை: 502-ம் ஆண்டின் விடியல் [cite: 14]
        self.play(Write(description))
        self.play(Indicate(sun, color=RED))
        self.wait(2)

        # 4. முடிவு
        final_text = Text("Act 1: Paradise in Fire", font_size=48, color=RED) # 
        self.play(ReplacementTransform(description, final_text))
        self.wait(2)
