import random
from queue import Queue

class State:
    def __init__(self, name: str, durability: int, message: str) -> None:
        self.name = name
        self.durability = durability
        self.message = message
        self.transitions = []

    def add_transitions(self, transitions: list):
        self.transitions = transitions

class Event(State):
    def __init__(self, name: str, durability: int, message: str, state: object) -> None:
        super().__init__(name, durability, message)
        self.state = state



SLEEP = State("sleep", 4, "Zzzzzzz...")
STUDY = State("study", 1, "Studying... again")
EAT = State("eat", 1, "Mm, not that bad")
STRESS = State("stress", 1, "I can't do this anymore")
RELAX = State("relax", 1, "Procrastination?")
SLEEP.add_transitions([STUDY, RELAX, SLEEP, EAT])
STUDY.add_transitions([SLEEP, EAT, STRESS, STUDY])
EAT.add_transitions([STUDY, RELAX])
STRESS.add_transitions([STUDY, STRESS, EAT])
RELAX.add_transitions([STRESS, SLEEP, RELAX])
LECTURE = Event("lecture", 2, "One more lecture", STUDY)
RANDOM_DEADLINE = Event("random deadline", 3, "So tired of all this stuff", STUDY)
DAILY_SLEEP = Event("daily sleep", 2, "I want to sleep!", SLEEP)
SMOKING = Event("smoking", 1, "Bad habit, but so calming", RELAX)


class DailyRoutineAutomata:
    def __init__(self):
        self.current_state = STUDY
        self.event_queue = Queue()
        self.eat_counter = 0
        self.sleep_counter = 0


    def add_event(self):
        random_choice = random.uniform(0.0, 1.0)
        if random_choice < 0.3:
            event = LECTURE
        elif 0.3 <= random_choice < 0.7:
            event = SMOKING
        elif 0.7 <= random_choice < 0.95:
            event = RANDOM_DEADLINE
        elif 0.95 <= random_choice <= 1:
            event = DAILY_SLEEP
        self.event_queue.put(event)

    def simulate_day(self):
        hour = 0
        occurance = 0.33
        while hour < 24:
            random_chance = random.uniform(0.0, 1.0)
            self.add_event()
            print(f"Hour {hour}")
            if 1 <= hour < 8:
                self.current_state = random.choice(self.current_state.transitions)
                while self.current_state not in (SLEEP, STUDY, STRESS):
                    self.current_state = random.choice(self.current_state.transitions)
                if 3 < hour < 8 and self.sleep_counter == 0:
                    print("Well, it's time to sleep already")
                    self.current_state = SLEEP
                hour += self.current_state.durability
            elif 8 <= hour <= 21 and random_chance <= occurance:
                event = self.event_queue.get()
                print(f"Oh! It's time for {event.name}")
                print(event.message)
                self.current_state = event.state
                occurance = 0.33
                hour += event.durability
            else:
                self.current_state = random.choice(self.current_state.transitions)
                if 17 < hour < 21 and self.eat_counter == 0:
                    print("I'm quite hungry now")
                    self.current_state = EAT
                elif self.eat_counter >= 3:
                    while self.current_state in (SLEEP, EAT):
                        self.current_state = random.choice(self.current_state.transitions)
                else:
                    while self.current_state == SLEEP:
                        self.current_state = random.choice(self.current_state.transitions)
                hour += self.current_state.durability
            print("Current state:", self.current_state.name)
            print(self.current_state.message)
            print('-----------------------------------------------')
            occurance += self.current_state.durability / 100
            if self.current_state == SLEEP:
                self.sleep_counter += 1
            elif self.current_state == EAT:
                self.eat_counter += 1


# Create an instance of the DailyRoutineAutomata class
automata = DailyRoutineAutomata()

# Simulate the daily routine
automata.simulate_day()
