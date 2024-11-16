import random
import tkinter as tk
from tkinter import scrolledtext

# Word list for generating passphrases
word_list = [
    "abandon", "ability", "absent", "access", "accuse", "acid", "actor", "adapt", "adult", "advance",
    "beach", "beam", "before", "begin", "behind", "believe", "below", "bench", "benefit", "better",
    "cable", "camera", "camp", "cancel", "canyon", "carbon", "cargo", "carpet", "carry", "castle",
    "dance", "dark", "date", "day", "deal", "decide", "defend", "define", "demand", "depend",
    "eagle", "early", "earth", "east", "easy", "echo", "economy", "edge", "edit", "effort",
    "fabric", "face", "fact", "fail", "fair", "fall", "family", "famous", "fancy", "farm",
    "garden", "gas", "gate", "gather", "gear", "general", "genius", "gentle", "genuine", "gift",
    "habit", "hair", "half", "hand", "handle", "happy", "harvest", "head", "health", "heart",
    "icon", "idea", "ideal", "identify", "ignore", "image", "impact", "import", "improve", "include",
    "jacket", "jail", "jar", "jazz", "jelly", "jewel", "join", "joke", "journey", "joy",
    "keep", "key", "kick", "kid", "kind", "king", "kiss", "kitchen", "knee", "knife",
    "label", "labor", "lack", "lady", "lake", "land", "large", "last", "laugh", "launch",
    "magic", "major", "make", "manage", "market", "match", "material", "matter", "mean", "measure",
    "nail", "name", "narrow", "nation", "nature", "near", "neat", "neck", "need", "negative",
    "ocean", "offer", "office", "oil", "old", "olive", "open", "option", "orange", "orbit",
    "page", "pair", "panel", "paper", "park", "part", "party", "pass", "path", "pattern",
    "queen", "quick", "quiet", "quiz", "quote", "race", "radio", "rain", "raise", "range",
    "safe", "sail", "salad", "same", "sample", "sand", "save", "scale", "scan", "scene",
    "table", "tag", "tail", "take", "tall", "tank", "tape", "target", "task", "taste",
    "unique", "unit", "unity", "unknown", "update", "upgrade", "upset", "urban", "urge", "use",
    "vacant", "valid", "valley", "value", "van", "variety", "vast", "vault", "vessel", "village",
    "wait", "wake", "walk", "wall", "want", "warm", "wash", "waste", "watch", "wave",
    "yard", "year", "yellow", "yield", "young", "youth", "zero", "zone", "zoo"
]

class PassphraseTesterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Passphrase Tester")
        self.root.configure(bg="black")
        
        self.is_running = False
        self.attempt = 1
        self.delay = 100  # Delay in milliseconds (500 ms = 0.5 seconds)
        
        # Setup the frames and widgets
        self.setup_ui()
    
    def setup_ui(self):
        # Start and Stop buttons
        self.start_button = tk.Button(self.root, text="Start", command=self.start_testing, bg="red", fg="white")
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_testing, bg="red", fg="white")
        self.stop_button.pack(pady=10)
        
        # Log area for passphrases being tested
        self.log_area = scrolledtext.ScrolledText(self.root, width=50, height=10, bg="black", fg="red")
        self.log_area.pack(padx=10, pady=10)
        
        # Area for successful keys found
        self.success_area = scrolledtext.ScrolledText(self.root, width=50, height=10, bg="black", fg="green")
        self.success_area.pack(padx=10, pady=10)
    
    def generate_random_passphrase(self):
        """Generates a random 12-word passphrase from the word list."""
        return ' '.join(random.choice(word_list) for _ in range(12))
    
    def start_testing(self):
        self.is_running = True
        self.log_area.insert(tk.END, "Starting passphrase testing...\n")
        self.log_area.see(tk.END)
        self.simulate_passphrase_testing()  # Start testing
    
    def stop_testing(self):
        self.is_running = False
        self.log_area.insert(tk.END, "Stopping passphrase testing...\n")
        self.log_area.see(tk.END)
    
    def simulate_passphrase_testing(self):
        if self.is_running:
            passphrase = self.generate_random_passphrase()
            
            # Log the passphrase being tested
            self.log_area.insert(tk.END, f"Attempt {self.attempt}: Testing '{passphrase}'...\n")
            self.log_area.see(tk.END)
            
            # Simulate a random chance of finding a "wallet"
            if random.random() < 0.001: 
                crypto_amount = round(random.uniform(0.01, 10.0), 2)
                success_message = f"🔥 Found {crypto_amount} BTC with '{passphrase}' 🔥\n"
                self.success_area.insert(tk.END, success_message)
                self.success_area.see(tk.END)
            
            self.attempt += 1
            self.root.after(self.delay, self.simulate_passphrase_testing)  # Schedule the next attempt

# Initialize the application
root = tk.Tk()
app = PassphraseTesterApp(root)
root.mainloop()
