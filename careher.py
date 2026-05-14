import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

root = tk.Tk()
root.title("CareHer")
root.geometry("500x600")
root.configure(bg="#FDF6F0")

# -────────────────────────────────────────────────────────────────────────────
#  REMEDIES DATA
# -────────────────────────────────────────────────────────────────────────────
Remedies = {
    "Menstrual": {
        "Cramps": {
            "title": "To ease pain ",
            "exercise": [
                ("Child's Pose (Balasana)",      "Relaxes lower back and reduces cramp intensity."),
                ("Knees-to-Chest (Apanasana)",   "Gently massages abdomen and eases pain."),
                ("Supine Twist",                   "Releases tension in lower body."),
                ("Legs Up the Wall",               "Improves blood flow and relaxation."),
                ("Deep Breathing",                 "Calms nervous system and reduces pain perception."),
            ],
            "food": [
                ("Ginger tea",           "Reduces inflammation and helps with cramps."),
                ("Dark chocolate (70%+)","Magnesium relaxes muscles and improves mood."),
                ("Salmon / flaxseeds",  "Omega-3 fatty acids reduce pain-causing hormones."),
                ("Spinach / leafy greens","Rich in iron and magnesium."),
                ("Bananas",             "Helps reduce muscle spasms."),
            ],
            "avoid_exercise": [
                ("HIIT",           "Too intense, can worsen cramps."),
                ("Heavy lifting", "Adds strain on body."),
                ("Core workouts",   "Increases abdominal pressure."),
            ],
            "avoid_food": [
                ("Caffeine",       "Can increase cramps and anxiety."),
                ("Fried foods",   "Increase inflammation."),
                ("Salty snacks",  "Cause bloating."),
                ("Sugary foods",  "Lead to energy crashes."),
            ],
            "note": "Keep movements slow, eat nourishing food, and rest when needed."
        },
        "Low Energy": {
            "title": "Restore energy ",
            "exercise": [
                ("Slow walking",        "Keeps body active without exhausting it."),
                ("Light yoga",          "Improves circulation and mood."),
                ("Breathing exercises", "Boosts oxygen and energy."),
            ],
            "food": [
                ("Oats",   "Provides steady energy."),
                ("Apples", "Natural sugar + fiber for quick boost."),
                ("Nuts",   "Healthy fats and protein."),
                ("Eggs",   "High protein for strength."),
                ("Honey",  "Quick natural energy source."),
            ],
            "avoid_exercise": [
                ("Running",         "Too demanding during low energy."),
                ("Long workouts",    "Drains energy further."),
                ("Intense training", "Leads to fatigue."),
            ],
            "avoid_food": [
                ("Junk food",      "Causes energy crashes."),
                ("Sugary drinks",  "Short-term boost, then fatigue."),
            ],
            "note": "Light movement + energy-rich foods work best."
        }
    }
}

# -────────────────────────────────────────────────────────────────────────────
#  NUTRITION DATA
# -────────────────────────────────────────────────────────────────────────────
NUTRITION_DATA = [
    {
        "title": "Energy (Calories)",
        "info": "You may need slightly more energy (approx. +100-300 kcal/day)\nReason: Body is working harder + fatigue",
        "sources": ["Rice, roti, oats", "Banana", "Nuts"],
        "tip": None,
        "bg": "#FFF0F3",
    },
    {
        "title": "Iron  (Most Important)",
        "info": "Helps replace blood loss & prevent weakness",
        "sources": ["Spinach", "Lentils", "Jaggery"],
        "tip": "Eat with Vitamin C for better absorption",
        "bg": "#FFE8ED",
    },
    {
        "title": "Vitamin C",
        "info": "Helps body absorb iron * Boosts immunity",
        "sources": ["Orange", "Lemon", "Tomato"],
        "tip": None,
        "bg": "#FFF0F3",
    },
    {
        "title": "Calcium",
        "info": "Reduces cramps & supports bones",
        "sources": ["Milk", "Paneer", "Green vegetables"],
        "tip": None,
        "bg": "#FFE8ED",
    },
    {
        "title": "Vitamin D",
        "info": "Helps calcium absorption * Improves mood",
        "sources": ["Sunlight", "Eggs"],
        "tip": None,
        "bg": "#FFF0F3",
    },
    {
        "title": "Magnesium",
        "info": "Helps reduce cramps & stress",
        "sources": ["Dark chocolate", "Nuts", "Banana"],
        "tip": None,
        "bg": "#FFE8ED",
    },
    {
        "title": "Vitamin B6 & B12",
        "info": "Helps with mood swings & energy",
        "sources": ["Eggs", "Fish", "Dairy"],
        "tip": None,
        "bg": "#FFF0F3",
    },
    {
        "title": "Omega-3 Fatty Acids",
        "info": "Reduce pain & inflammation",
        "sources": ["Fish", "Flaxseeds", "Walnuts"],
        "tip": None,
        "bg": "#FFE8ED",
    },
    {
        "title": "Water  (Very Important)",
        "info": "Drink 2-3 liters daily\nHelps reduce: Bloating * Headache * Fatigue",
        "sources": [],
        "tip": None,
        "bg": "#FFF0F3",
    },
]

# -────────────────────────────────────────────────────────────────────────────
#  EXERCISE DATA
# -────────────────────────────────────────────────────────────────────────────
EXERCISE_DATA = [
    # -- Menstrual Phase ------------------------------------------------------
    {
        "phase": "Menstrual Phase",
        "phase_bg": "#F9D0D8",
        "phase_fg": "#6B1F35",
        "levels": [
            {
                "dot": "", "level": "1. High Pain",
                "subtitle": "Severe cramps, fatigue",
                "goal": "Relief + relaxation (almost rest mode)",
                "poses": [
                    "Child's Pose (Balasana)",
                    "Knees-to-Chest Pose (Apanasana)",
                    "Supine Twist (Supta Matsyendrasana)",
                    "Legs Up the Wall (Viparita Karani)",
                    "Corpse Pose (Savasana)",
                ],
                "intensity": "Very Low",
                "duration": "10-20 mins",
                "message": "Take rest. Focus on breathing and gentle stretches.",
                "card_bg": "#FFE5E5",
            },
            {
                "dot": "", "level": "2. Moderate Pain",
                "subtitle": "",
                "goal": "Light movement + reduce cramps",
                "poses": [
                    "Cat-Cow Stretch (Marjaryasana-Bitilasana)",
                    "Cobra Pose (Bhujangasana)",
                    "Child's Pose (Balasana)",
                    "Seated Forward Bend (Paschimottanasana)",
                    "Bridge Pose (Setu Bandhasana)",
                ],
                "intensity": "Low",
                "duration": "15-30 mins",
                "message": "Keep movements slow. Avoid intense workouts.",
                "card_bg": "#FFF0E0",
            },
            {
                "dot": "", "level": "3. Low Pain",
                "subtitle": "Mild or no cramps",
                "goal": "Gentle activity + maintain routine",
                "poses": [
                    "Downward Dog (Adho Mukha Svanasana)",
                    "Warrior I (Virabhadrasana I)",
                    "Warrior II (Virabhadrasana II)",
                    "Triangle Pose (Trikonasana)",
                    "Cat-Cow Stretch",
                ],
                "intensity": "Low-Moderate",
                "duration": "20-40 mins",
                "message": "You can stay active but avoid overexertion.",
                "card_bg": "#E8F5E9",
            },
        ],
    },
    # -- Pre-Menstrual / PMS Phase --------------------------------------------
    {
        "phase": "Pre-Menstrual / PMS Phase",
        "phase_bg": "#F2D0DC",
        "phase_fg": "#5A1528",
        "levels": [
            {
                "dot": "", "level": "1. High Discomfort",
                "subtitle": "PMS, fatigue, bloating",
                "goal": "Relaxation + reduce stress",
                "poses": [
                    "Child's Pose (Balasana)",
                    "Legs Up the Wall (Viparita Karani)",
                    "Supine Twist (Supta Matsyendrasana)",
                    "Deep breathing / meditation",
                    "Slow walking",
                ],
                "intensity": "Very Low",
                "duration": "10-20 mins",
                "message": "Focus on calming your body. Rest is okay.",
                "card_bg": "#FFE5E5",
            },
            {
                "dot": "", "level": "2. Moderate Discomfort",
                "subtitle": "",
                "goal": "Stay active without stressing the body",
                "poses": [
                    "Pilates (light core work)",
                    "Bodyweight training (light squats, wall push-ups)",
                    "Yoga flow (slow pace)",
                    "Cycling (easy pace)",
                    "Cat-Cow (Marjaryasana-Bitilasana)",
                    "Bridge Pose (Setu Bandhasana)",
                    "Cobra Pose (Bhujangasana)",
                    "Seated Forward Bend (Paschimottanasana)",
                ],
                "intensity": "Low-Moderate",
                "duration": "20-35 mins",
                "message": "Keep it light and controlled. Avoid intense sessions.",
                "card_bg": "#FFF0E0",
            },
            {
                "dot": "", "level": "3. Low Discomfort",
                "subtitle": "Feeling mostly normal",
                "goal": "Maintain fitness but don't overdo",
                "poses": [
                    "Strength training (moderate weights)",
                    "Light jogging",
                    "Dance workouts",
                    "Resistance band workouts",
                    "Warrior II (Virabhadrasana II)",
                    "Triangle Pose (Trikonasana)",
                    "Downward Dog (Adho Mukha Svanasana)",
                ],
                "intensity": "Moderate",
                "duration": "30-45 mins",
                "message": "You can stay active, but listen to your body.",
                "card_bg": "#E8F5E9",
            },
        ],
    },
    # -- Follicular Phase -----------------------------------------------------
    {
        "phase": "Follicular Phase  (Day ~6-14)",
        "phase_bg": "#D4F0D4",
        "phase_fg": "#1B5E20",
        "levels": [
            {
                "dot": "", "level": "Rising Energy",
                "subtitle": "Energy rising, mood improves, body feels lighter",
                "goal": "Explore + build consistency",
                "poses": [
                    "Light jogging or brisk walking",
                    "Dance / Zumba",
                    "Beginner strength training",
                    "Sun Salutation (Surya Namaskar)",
                    "Warrior I & II (Virabhadrasana I & II)",
                    "Downward Dog (Adho Mukha Svanasana)",
                ],
                "intensity": "Low-Moderate",
                "duration": "30-45 mins",
                "message": "This is the best phase to explore and build consistency.",
                "card_bg": "#E8F5E9",
            },
        ],
    },
    # -- Ovulation Phase ------------------------------------------------------
    {
        "phase": "Ovulation Phase  (Peak Energy)",
        "phase_bg": "#FFF9C4",
        "phase_fg": "#5D4037",
        "levels": [
            {
                "dot": "", "level": "Peak Energy Phase",
                "subtitle": "Ovulation day +/- 1 day - highest energy, strength & confidence",
                "goal": "Maximum performance",
                "poses": [
                    "HIIT (High-Intensity Interval Training)",
                    "Running / sprinting",
                    "Jump rope",
                    "Sports (badminton, basketball, etc.)",
                    "Heavy weight lifting - Squats, Deadlifts, Push-ups",
                    "Warrior III (Virabhadrasana III)",
                    "Plank Pose",
                    "Chaturanga (low plank)",
                    "Sun Salutation (Surya Namaskar)",
                ],
                "intensity": "High",
                "duration": "30-60 mins",
                "message": "This is your strongest phase - push your limits safely.",
                "card_bg": "#FFFDE7",
            },
        ],
    },
]

# -────────────────────────────────────────────────────────────────────────────
#  HELPERS
# -────────────────────────────────────────────────────────────────────────────
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def make_scrollable(parent):
    """Return (canvas, inner_frame) with vertical scrollbar attached to parent."""
    canvas = tk.Canvas(parent, bg="#FDF6F0", highlightthickness=0)
    sb = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    inner = tk.Frame(canvas, bg="#FDF6F0")
    cw = canvas.create_window((0, 0), window=inner, anchor="nw")
    inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(cw, width=e.width))
    canvas.bind_all("<MouseWheel>",
                    lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
    return canvas, inner


# -────────────────────────────────────────────────────────────────────────────
#  DASHBOARD
# -────────────────────────────────────────────────────────────────────────────
def show_dashboard(age="quote"):
    clear_window()

    messages = {
        "quote": "Hello, queen! Your wellness matters, let us nurture it together.",
    }

    tk.Label(root, text="CareHer", font=("Arial", 24, "bold"),
             bg="#FDF6F0", fg="#E75480").pack(pady=(15, 2))
    tk.Label(root, text=messages.get(age, "Welcome!"), font=("Arial", 12),
             bg="#FDF6F0", fg="#555555", wraplength=460, justify="center").pack(pady=(0, 10))

    container = tk.Frame(root, bg="#FDF6F0")
    container.pack(expand=True, fill="both", padx=15, pady=5)
    container.columnconfigure(0, weight=1)
    container.columnconfigure(1, weight=1)
    for r in range(3):
        container.rowconfigure(r, weight=1)

    COLORS = {
        "food":      {"bg": "#E8919A", "btn": "#FFF0F3", "sub": "#FFD6DC"},
        "exercise":  {"bg": "#C97B8A", "btn": "#FFF0F3", "sub": "#F7C6D0"},
        "remedies":  {"bg": "#D4A5B5", "btn": "#FFF0F3", "sub": "#F9E3EB"},
        "predictor": {"bg": "#B87D96", "btn": "#FFF0F3", "sub": "#F2D0DC"},
    }

    def create_block(parent, title_text, desc, color_key, command=None):
        c = COLORS[color_key]
        frame = tk.Frame(parent, bg=c["bg"], bd=0, relief="flat")
        tk.Label(frame, text=title_text, font=("Arial", 15, "bold"),
                 bg=c["bg"], fg="white").pack(pady=(18, 4))
        tk.Label(frame, text=desc, wraplength=200, justify="center",
                 font=("Arial", 10), bg=c["bg"], fg=c["sub"]).pack(expand=True, padx=10)
        tk.Button(frame, text="Click here", bg=c["btn"], fg="#C0496A",
                  bd=0, relief="flat", cursor="hand2",
                  font=("Arial", 10, "bold"), padx=10, pady=4,
                  command=command).pack(pady=12)
        return frame

    def create_wide_block(parent, title_text, desc, color_key, command=None):
        c = COLORS[color_key]
        frame = tk.Frame(parent, bg=c["bg"], bd=0, relief="flat")
        tk.Label(frame, text=title_text, font=("Arial", 15, "bold"),
                 bg=c["bg"], fg="white").pack(pady=(20, 4))
        tk.Label(frame, text=desc, wraplength=400, justify="center",
                 font=("Arial", 10), bg=c["bg"], fg=c["sub"]).pack(expand=True, padx=20)
        tk.Button(frame, text="Click here", bg=c["btn"], fg="#C0496A",
                  bd=0, relief="flat", cursor="hand2",
                  font=("Arial", 10, "bold"), padx=14, pady=4,
                  command=command).pack(pady=14)
        return frame

    food     = create_block(container, "Food",     "Healthy diet tips for better menstrual health.",
                            "food",     command=open_nutrition)
    exercise = create_block(container, "Exercise", "Light workouts and yoga for your comfort.",
                            "exercise", command=open_exercise)
    remedies = create_wide_block(container, "Remedies",
                                 "Simple home remedies to ease cramps and pain.",
                                 "remedies", command=open_remedies_categories)
    predictor = create_wide_block(container, "Predictor",
                                  "Track and predict your next menstrual cycle.",
                                  "predictor", command=open_predictor)

    food.grid    (row=0, column=0, padx=(0, 6), pady=(0, 10), sticky="nsew")
    exercise.grid(row=0, column=1, padx=(6, 0), pady=(0, 10), sticky="nsew")
    remedies.grid(row=1, column=0, columnspan=2, padx=0, pady=(0, 10), sticky="nsew")
    predictor.grid(row=2, column=0, columnspan=2, padx=0, pady=(0, 5),  sticky="nsew")


# -────────────────────────────────────────────────────────────────────────────
#  NUTRITION PAGE
# -────────────────────────────────────────────────────────────────────────────
def open_nutrition():
    clear_window()
    _, inner = make_scrollable(root)

    tk.Label(inner, text="Nutrition During Periods",
             font=("Arial", 20, "bold"), bg="#FDF6F0", fg="#E75480").pack(pady=(18, 14))

    for item in NUTRITION_DATA:
        card = tk.Frame(inner, bg=item["bg"], bd=0, relief="flat")
        card.pack(fill="x", padx=20, pady=5)

        hdr = tk.Frame(card, bg=item["bg"])
        hdr.pack(fill="x", padx=12, pady=(10, 4))
        tk.Label(hdr, text=item["title"], font=("Arial", 13, "bold"),
                 bg=item["bg"], fg="#6B1F35").pack(side="left")

        tk.Label(card, text=item["info"], font=("Arial", 10),
                 bg=item["bg"], fg="#555555", justify="left",
                 wraplength=420, anchor="w").pack(anchor="w", padx=14, pady=(0, 4))

        if item["sources"]:
            src_frame = tk.Frame(card, bg=item["bg"])
            src_frame.pack(anchor="w", padx=14, pady=(0, 4))
            tk.Label(src_frame, text="Good sources:", font=("Arial", 10, "italic"),
                     bg=item["bg"], fg="#888888").pack(anchor="w")
            for name in item["sources"]:
                tk.Label(src_frame, text=f"  {name}",
                         font=("Arial", 10), bg=item["bg"], fg="#555555").pack(anchor="w")

        if item["tip"]:
            tk.Label(card, text=item["tip"], font=("Arial", 10, "bold"),
                     bg=item["bg"], fg="#C0496A").pack(anchor="w", padx=14, pady=(2, 8))
        else:
            tk.Frame(card, bg=item["bg"], height=8).pack()

    tk.Button(inner, text="<- Back to Home",
              font=("Arial", 10), bg="#F5B8C4", fg="#6B1F35",
              bd=0, relief="flat", cursor="hand2", padx=12, pady=6,
              command=show_dashboard).pack(pady=(16, 24))


# -────────────────────────────────────────────────────────────────────────────
#  EXERCISE PAGE
# -────────────────────────────────────────────────────────────────────────────
def open_exercise():
    clear_window()
    _, inner = make_scrollable(root)

    tk.Label(inner, text="Exercise Guide",
             font=("Arial", 20, "bold"), bg="#FDF6F0", fg="#E75480").pack(pady=(18, 4))
    tk.Label(inner, text="Choose workouts based on your phase & pain level.",
             font=("Arial", 10), bg="#FDF6F0", fg="#888888").pack(pady=(0, 14))

    for phase_data in EXERCISE_DATA:
        ph_frame = tk.Frame(inner, bg=phase_data["phase_bg"], bd=0)
        ph_frame.pack(fill="x", padx=20, pady=(10, 0))
        tk.Label(ph_frame, text=phase_data["phase"],
                 font=("Arial", 14, "bold"),
                 bg=phase_data["phase_bg"], fg=phase_data["phase_fg"]).pack(
                     anchor="w", padx=14, pady=10)

        for lvl in phase_data["levels"]:
            card = tk.Frame(inner, bg=lvl["card_bg"], bd=0, relief="flat")
            card.pack(fill="x", padx=20, pady=(2, 6))

            tk.Label(card,
                     text=f"{lvl['dot']}  {lvl['level']}" +
                          (f"  -  {lvl['subtitle']}" if lvl["subtitle"] else ""),
                     font=("Arial", 12, "bold"),
                     bg=lvl["card_bg"], fg="#333333").pack(anchor="w", padx=12, pady=(10, 2))

            tk.Label(card, text=f" Goal: {lvl['goal']}",
                     font=("Arial", 10, "italic"),
                     bg=lvl["card_bg"], fg="#555555").pack(anchor="w", padx=12, pady=(0, 4))

            tk.Label(card, text="Recommended:",
                     font=("Arial", 10, "bold"),
                     bg=lvl["card_bg"], fg="#6B1F35").pack(anchor="w", padx=12)
            for pose in lvl["poses"]:
                tk.Label(card, text=f"   * {pose}",
                         font=("Arial", 10),
                         bg=lvl["card_bg"], fg="#444444").pack(anchor="w", padx=12)

            meta = tk.Frame(card, bg=lvl["card_bg"])
            meta.pack(anchor="w", padx=12, pady=(6, 2))
            tk.Label(meta, text=f"Intensity: {lvl['intensity']}",
                     font=("Arial", 10), bg=lvl["card_bg"], fg="#555555").pack(side="left", padx=(0, 18))
            tk.Label(meta, text=f" Duration: {lvl['duration']}",
                     font=("Arial", 10), bg=lvl["card_bg"], fg="#555555").pack(side="left")

            msg_frame = tk.Frame(card, bg="#F9D0D8", bd=0)
            msg_frame.pack(fill="x", padx=12, pady=(6, 10))
            tk.Label(msg_frame, text=f"   {lvl['message']}",
                     font=("Arial", 10, "italic"),
                     bg="#F9D0D8", fg="#6B1F35",
                     wraplength=400, justify="left").pack(padx=10, pady=6)

    tk.Button(inner, text="<- Back to Home",
              font=("Arial", 10), bg="#F5B8C4", fg="#6B1F35",
              bd=0, relief="flat", cursor="hand2", padx=12, pady=6,
              command=show_dashboard).pack(pady=(16, 24))


# -────────────────────────────────────────────────────────────────────────────
#  REMEDIES - CATEGORY SELECTOR
# -────────────────────────────────────────────────────────────────────────────
def open_remedies_categories():
    clear_window()

    tk.Label(root, text=" Remedies", font=("Arial", 22, "bold"),
             bg="#FDF6F0", fg="#E75480").pack(pady=(24, 6))
    tk.Label(root, text="What would you like help with?",
             font=("Arial", 12), bg="#FDF6F0", fg="#888888").pack(pady=(0, 20))

    btn_frame = tk.Frame(root, bg="#FDF6F0")
    btn_frame.pack(expand=True)

    for label, key in [("Cramps", "Cramps"), ("Low Energy", "Low Energy")]:
        tk.Button(btn_frame, text=label,
                  font=("Arial", 14, "bold"),
                  bg="#E8919A", fg="white",
                  activebackground="#C0496A", activeforeground="white",
                  bd=0, relief="flat", cursor="hand2",
                  width=22, pady=16,
                  command=lambda k=key: open_remedy_detail(k)).pack(pady=10)

    tk.Button(root, text="<- Back to Home",
              font=("Arial", 10), bg="#F5B8C4", fg="#6B1F35",
              bd=0, relief="flat", cursor="hand2", padx=12, pady=6,
              command=show_dashboard).pack(pady=(20, 10))


# -────────────────────────────────────────────────────────────────────────────
#  REMEDIES - DETAIL PAGE
# -────────────────────────────────────────────────────────────────────────────
def open_remedy_detail(condition_key):
    clear_window()
    data = Remedies["Menstrual"][condition_key]

    canvas, inner = make_scrollable(root)

    tk.Label(inner, text=data["title"], font=("Arial", 20, "bold"),
             bg="#FDF6F0", fg="#E75480").pack(pady=(18, 2))

    def section_label(text, color="#C0496A"):
        tk.Label(inner, text=text, font=("Arial", 13, "bold"),
                 bg="#FDF6F0", fg=color).pack(anchor="w", padx=20, pady=(14, 4))

    def card(parent, title, desc, bg="#FFF0F3"):
        f = tk.Frame(parent, bg=bg, bd=0, relief="flat")
        f.pack(fill="x", padx=20, pady=4)
        tk.Label(f, text=title, font=("Arial", 11, "bold"),
                 bg=bg, fg="#6B1F35", anchor="w").pack(anchor="w", padx=10, pady=(8, 2))
        tk.Label(f, text=desc, font=("Arial", 10),
                 bg=bg, fg="#555555", wraplength=420, justify="left",
                 anchor="w").pack(anchor="w", padx=10, pady=(0, 8))

    section_label("Recommended Exercises")
    for exercise_item in data["exercise"]:
        name = exercise_item[0]
        desc = exercise_item[1]
        card(inner, name, desc, bg="#FFF0F3")

    section_label("Recommended Foods")
    for (name, desc) in data["food"]:
        card(inner, name, desc, bg="#FFF0F3")

    section_label("Exercises to Avoid", color="#B5001E")
    for (name, desc) in data["avoid_exercise"]:
        card(inner, name, desc, bg="#FFE5E5")

    section_label("Foods to Avoid", color="#B5001E")
    for (name, desc) in data["avoid_food"]:
        card(inner, name, desc, bg="#FFE5E5")

    note_frame = tk.Frame(inner, bg="#F9D0D8", bd=0, relief="flat")
    note_frame.pack(fill="x", padx=20, pady=(16, 6))
    tk.Label(note_frame, text="  Note", font=("Arial", 11, "bold"),
             bg="#F9D0D8", fg="#6B1F35").pack(anchor="w", padx=12, pady=(8, 2))
    tk.Label(note_frame, text=data["note"], font=("Arial", 10),
             bg="#F9D0D8", fg="#6B1F35", wraplength=420, justify="left").pack(
             anchor="w", padx=12, pady=(0, 10))

    tk.Button(inner, text="<- Back to Remedies",
              font=("Arial", 10), bg="#F5B8C4", fg="#6B1F35",
              bd=0, relief="flat", cursor="hand2", padx=12, pady=6,
              command=open_remedies_categories).pack(pady=(10, 20))


# -────────────────────────────────────────────────────────────────────────────
#  PERIOD PREDICTOR
# -────────────────────────────────────────────────────────────────────────────
def open_predictor():
    win = tk.Toplevel(root)
    win.title("Period Predictor")
    win.geometry("520x700")
    win.configure(bg="#FDF6F0")
    win.resizable(False, False)

    canvas = tk.Canvas(win, bg="#FDF6F0", highlightthickness=0)
    sb = tk.Scrollbar(win, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    inner = tk.Frame(canvas, bg="#FDF6F0")
    cw = canvas.create_window((0, 0), window=inner, anchor="nw")
    inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>",  lambda e: canvas.itemconfig(cw, width=e.width))
    canvas.bind_all("<MouseWheel>",
                    lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

    tk.Label(inner, text="Period Predictor", font=("Arial", 18, "bold"),
             bg="#FDF6F0", fg="#E75480").pack(pady=(18, 4))
    tk.Label(inner, text="Enter your last 6 period start dates to get started.",
             font=("Arial", 10), bg="#FDF6F0", fg="#888888").pack(pady=(0, 12))

    def section_label(text):
        tk.Label(inner, text=text, font=("Arial", 12, "bold"),
                 bg="#FDF6F0", fg="#C0496A").pack(anchor="w", padx=24, pady=(12, 4))

    section_label("Last 6 Period Start Dates  (DD-MM-YYYY)")
    date_entries = []
    date_frame = tk.Frame(inner, bg="#FDF6F0")
    date_frame.pack(padx=24, fill="x")

    for i in range(6):
        row = tk.Frame(date_frame, bg="#FDF6F0")
        row.pack(fill="x", pady=3)
        tk.Label(row, text=f"Month {i+1}:", font=("Arial", 10),
                 bg="#FDF6F0", fg="#555555", width=10, anchor="w").pack(side="left")
        entry = tk.Entry(row, font=("Arial", 11), width=16,
                         relief="solid", bd=1, fg="#333333")
        entry.pack(side="left", padx=(4, 0))
        entry.insert(0, "DD-MM-YYYY")
        entry.config(fg="#aaaaaa")

        def on_focus_in(e, ent=entry):
            if ent.get() == "DD-MM-YYYY":
                ent.delete(0, tk.END); ent.config(fg="#333333")

        def on_focus_out(e, ent=entry):
            if ent.get().strip() == "":
                ent.insert(0, "DD-MM-YYYY"); ent.config(fg="#aaaaaa")

        entry.bind("<FocusIn>",  on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        date_entries.append(entry)

    # Only 4 symptoms: Cramps, Mood Swings, Fatigue, Back Pain
    section_label("Pre-Period Symptoms")
    symptom_vars = {}
    sym_frame = tk.Frame(inner, bg="#FDF6F0")
    sym_frame.pack(padx=24, fill="x")
    for i, sym in enumerate(["Cramps", "Mood Swings", "Fatigue", "Back Pain"]):
        var = tk.BooleanVar()
        symptom_vars[sym] = var
        tk.Checkbutton(sym_frame, text=sym, variable=var,
                       font=("Arial", 10), bg="#FDF6F0",
                       fg="#555555", activebackground="#FDF6F0",
                       selectcolor="#F9D0D8", anchor="w").grid(
                           row=i//2, column=i%2, sticky="w", padx=(0, 20), pady=2)

    section_label("Sleep Cycle Disturbance")
    sleep_var = tk.StringVar(value="Low")
    sleep_frame = tk.Frame(inner, bg="#FDF6F0")
    sleep_frame.pack(padx=24, anchor="w")
    for opt in ["Low", "Moderate", "High"]:
        tk.Radiobutton(sleep_frame, text=opt, variable=sleep_var, value=opt,
                       font=("Arial", 10), bg="#FDF6F0", fg="#555555",
                       activebackground="#FDF6F0", selectcolor="#F9D0D8").pack(side="left", padx=8)

    section_label("Stress Level")
    stress_var = tk.StringVar(value="Low")
    stress_frame = tk.Frame(inner, bg="#FDF6F0")
    stress_frame.pack(padx=24, anchor="w")
    for opt in ["Low", "Medium", "High"]:
        tk.Radiobutton(stress_frame, text=opt, variable=stress_var, value=opt,
                       font=("Arial", 10), bg="#FDF6F0", fg="#555555",
                       activebackground="#FDF6F0", selectcolor="#F9D0D8").pack(side="left", padx=8)

    result_frame = tk.Frame(inner, bg="#F9D0D8", bd=0, relief="flat")
    result_frame.pack(padx=24, pady=(18, 6), fill="x")
    result_label = tk.Label(result_frame, text="", font=("Arial", 11),
                            bg="#F9D0D8", fg="#6B1F35", wraplength=440, justify="left")
    result_label.pack(padx=14, pady=12)

    def calculate():
        dates = []
        for entry in date_entries:
            raw = entry.get().strip()
            if raw in ("DD-MM-YYYY", ""):
                continue
            try:
                dates.append(datetime.strptime(raw, "%d-%m-%Y"))
            except ValueError:
                messagebox.showerror("Invalid Date",
                    f"'{raw}' is not valid. Please use DD-MM-YYYY format.")
                return

        if len(dates) < 2:
            messagebox.showwarning("Not Enough Data",
                "Please enter at least 2 period start dates.")
            return

        dates.sort()
        gaps = [(dates[i+1]-dates[i]).days for i in range(len(dates)-1)]
        avg_cycle   = round(sum(gaps)/len(gaps))
        next_period = dates[-1] + timedelta(days=avg_cycle)

        insights = []
        selected_symptoms = [s for s, v in symptom_vars.items() if v.get()]
        stress = stress_var.get()
        sleep  = sleep_var.get()

        if stress == "High":
            insights.append("High stress can delay your cycle. Try relaxation techniques.")
        elif stress == "Medium":
            insights.append("Moderate stress detected. Consider light walks or journaling.")
        if sleep == "High":
            insights.append("Poor sleep strongly affects hormones. Aim for 7-8 hours.")
        elif sleep == "Moderate":
            insights.append("Try to maintain a consistent sleep schedule.")
        if len(selected_symptoms) >= 3:
            insights.append("Multiple symptoms detected. Consider consulting a gynecologist.")
        elif "Cramps" in selected_symptoms:
            insights.append("For cramps, try a warm compress, ginger tea, or light yoga.")
        if "Mood Swings" in selected_symptoms:
            insights.append("Mood swings are normal. Try mindfulness exercises.")
        if "Fatigue" in selected_symptoms:
            insights.append("Combat fatigue with iron-rich foods like spinach and dates.")
        if "Back Pain" in selected_symptoms:
            insights.append("For back pain, try gentle stretches like Child's Pose or a warm compress.")
        if not insights:
            insights.append("Everything looks balanced! Keep up your healthy habits.")

        result_label.config(text=(
            f"  Predicted Next Period:  {next_period.strftime('%d %B %Y')}\n"
            f" Average Cycle Length:   {avg_cycle} days\n\n"
            + "\n\n".join(insights)
        ))

    tk.Button(inner, text="Predict My Cycle",
              font=("Arial", 13, "bold"), bg="#E75480", fg="white",
              activebackground="#C0496A", activeforeground="white",
              bd=0, relief="flat", cursor="hand2", padx=20, pady=10,
              command=calculate).pack(pady=(16, 6))

    # ── Phase Predictor ──────────────────────────────────────────────────────
    section_label("Current Phase Predictor")
    tk.Label(inner, text="Enter today's date to find out your current cycle phase.",
             font=("Arial", 10), bg="#FDF6F0", fg="#888888").pack(anchor="w", padx=24, pady=(0, 6))

    today_row = tk.Frame(inner, bg="#FDF6F0")
    today_row.pack(padx=24, anchor="w")
    tk.Label(today_row, text="Today's Date:", font=("Arial", 10),
             bg="#FDF6F0", fg="#555555", width=13, anchor="w").pack(side="left")
    today_entry = tk.Entry(today_row, font=("Arial", 11), width=16,
                           relief="solid", bd=1, fg="#333333")
    today_entry.pack(side="left", padx=(4, 0))
    today_entry.insert(0, "DD-MM-YYYY")
    today_entry.config(fg="#aaaaaa")

    def today_focus_in(e):
        if today_entry.get() == "DD-MM-YYYY":
            today_entry.delete(0, tk.END); today_entry.config(fg="#333333")

    def today_focus_out(e):
        if today_entry.get().strip() == "":
            today_entry.insert(0, "DD-MM-YYYY"); today_entry.config(fg="#aaaaaa")

    today_entry.bind("<FocusIn>",  today_focus_in)
    today_entry.bind("<FocusOut>", today_focus_out)

    phase_result_frame = tk.Frame(inner, bg="#F2D0DC", bd=0, relief="flat")
    phase_result_frame.pack(padx=24, pady=(12, 6), fill="x")
    phase_result_label = tk.Label(phase_result_frame, text="", font=("Arial", 11),
                                  bg="#F2D0DC", fg="#6B1F35", wraplength=440, justify="left")
    phase_result_label.pack(padx=14, pady=12)

    PHASE_INFO = {
        "Menstrual": {
            "emoji": "🌸",
            "desc": "Your body is shedding the uterine lining. Rest, stay warm, and eat iron-rich foods.",
            "color": "#F9D0D8",
        },
        "Follicular": {
            "emoji": "🌱",
            "desc": "Estrogen is rising and energy is building. Great time to start new healthy habits.",
            "color": "#D4F0D4",
        },
        "Ovulation": {
            "emoji": "✨",
            "desc": "Peak energy and confidence! Your body is at its strongest — make the most of it.",
            "color": "#FFF9C4",
        },
        "Luteal": {
            "emoji": "🌙",
            "desc": "Progesterone rises. You may feel slower — prioritize rest, magnesium, and self-care.",
            "color": "#F2D0DC",
        },
    }

    def predict_phase():
        raw_today = today_entry.get().strip()
        if raw_today in ("DD-MM-YYYY", ""):
            messagebox.showwarning("Missing Date", "Please enter today's date.")
            return
        try:
            today_date = datetime.strptime(raw_today, "%d-%m-%Y")
        except ValueError:
            messagebox.showerror("Invalid Date",
                f"'{raw_today}' is not valid. Please use DD-MM-YYYY format.")
            return

        # Collect valid period start dates
        dates = []
        for entry in date_entries:
            raw = entry.get().strip()
            if raw in ("DD-MM-YYYY", ""):
                continue
            try:
                dates.append(datetime.strptime(raw, "%d-%m-%Y"))
            except ValueError:
                pass

        if len(dates) < 2:
            messagebox.showwarning("Not Enough Data",
                "Please enter at least 2 period start dates and run 'Predict My Cycle' first.")
            return

        dates.sort()
        gaps = [(dates[i+1]-dates[i]).days for i in range(len(dates)-1)]
        avg_cycle   = round(sum(gaps)/len(gaps))
        next_period = dates[-1] + timedelta(days=avg_cycle)
        last_period = dates[-1]

        days_to_next   = (next_period - today_date).days   # positive = next period is ahead
        days_from_last = (today_date - last_period).days   # positive = today is after last period

        # Phase logic
        if days_from_last >= 0 and days_from_last <= 5:
            phase = "Menstrual"
        elif days_to_next >= 1 and days_to_next <= 13:
            phase = "Luteal"
        elif days_to_next in (14, 15, 16):
            phase = "Ovulation"
        elif days_to_next > 16:
            phase = "Follicular"
        else:
            # today is past expected period date
            phase = "Menstrual"

        info = PHASE_INFO[phase]
        phase_result_frame.config(bg=info["color"])
        phase_result_label.config(
            bg=info["color"],
            text=(
                f"  {info['emoji']}  Current Phase:  {phase} Phase\n\n"
                f"  {info['desc']}\n\n"
                f"  Days until next period:  "
                + (f"{days_to_next} days" if days_to_next >= 0 else f"{abs(days_to_next)} days overdue")
            )
        )

    phase_btn_row = tk.Frame(inner, bg="#FDF6F0")
    phase_btn_row.pack(pady=(8, 16))

    tk.Button(phase_btn_row, text="Find My Phase",
              font=("Arial", 12, "bold"), bg="#C97B8A", fg="white",
              activebackground="#A0506A", activeforeground="white",
              bd=0, relief="flat", cursor="hand2", padx=18, pady=8,
              command=predict_phase).pack(side="left", padx=(0, 10))

    def reset_today():
        today_entry.delete(0, tk.END)
        today_entry.insert(0, "DD-MM-YYYY")
        today_entry.config(fg="#aaaaaa")
        phase_result_label.config(text="")
        phase_result_frame.config(bg="#F2D0DC")
        phase_result_label.config(bg="#F2D0DC")

    tk.Button(phase_btn_row, text="Reset Date",
              font=("Arial", 10), bg="#F5B8C4", fg="#6B1F35",
              bd=0, relief="flat", cursor="hand2", padx=12, pady=8,
              command=reset_today).pack(side="left")

    tk.Button(inner, text="Clear",
              font=("Arial", 10), bg="#F5B8C4", fg="#6B1F35",
              bd=0, relief="flat", cursor="hand2", padx=12, pady=6,
              command=lambda: [
                  [e.delete(0, tk.END) or e.insert(0, "DD-MM-YYYY") or e.config(fg="#aaaaaa")
                   for e in date_entries],
                  [v.set(False) for v in symptom_vars.values()],
                  sleep_var.set("Low"), stress_var.set("Low"),
                  result_label.config(text=""),
              ]).pack(pady=(0, 20))


# -- Launch -------------------------------------------------------------------
show_dashboard("quote")
root.mainloop()
