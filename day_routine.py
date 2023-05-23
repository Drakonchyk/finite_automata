"""
FSM for daily routine
"""
import random
from queue import Queue

class State:
    """
    Represents a state in the daily routine automaton.
    """
    def __init__(self, name: str, durability: int, message: str) -> None:
        self.name = name
        self.durability = durability
        self.message = message
        self.transitions = []

    def add_transitions(self, transitions: list):
        """
        Adds transitions to the state.

        Args:
            transitions (list): A list of State objects representing the possible transitions.

        Returns:
            None
        """
        self.transitions = transitions

class Event(State):
    """
    Represents an event in the daily routine automaton.
    """
    def __init__(self, name: str, durability: int, message: str, state: object) -> None:
        """
        Initializes a new instance of the Event class.

        Args:
            name (str): The name of the event.
            durability (int): The durability of the event.
            message (str): The message associated with the event.
            state (object): The state that the event leads to.

        Returns:
            None
        """
        super().__init__(name, durability, message)
        self.state = state


# 5 states for daily routine
SLEEP = State("sleep", 4, "Zzzzzzz...")
STUDY = State("study", 1, "Studying... again")
EAT = State("eat", 1, "Mm, not that bad")
STRESS = State("stress", 1, "I can't do this anymore")
RELAX = State("relax", 1, "Procrastination?")

# connections between the states
SLEEP.add_transitions([STUDY, RELAX, SLEEP, EAT])
STUDY.add_transitions([SLEEP, EAT, STRESS, STUDY])
EAT.add_transitions([STUDY, RELAX])
STRESS.add_transitions([STUDY, STRESS, EAT])
RELAX.add_transitions([STRESS, SLEEP, RELAX])

# 4 random events that may occure
LECTURE = Event("lecture", 2, "One more lecture", STUDY)
RANDOM_DEADLINE = Event("random deadline", 3, "So tired of all this stuff", STUDY)
DAILY_SLEEP = Event("daily sleep", 2, "I want to sleep!", SLEEP)
SMOKING = Event("smoking", 1, "Bad habit, but so calming", RELAX)


class DailyRoutineAutomata:
    """
    Represents a daily routine automaton.
    """
    def __init__(self):
        """
        Initializes a new instance of the DailyRoutineAutomata class.

        Returns:
            None
        """
        self.current_state = STUDY
        self.event_queue = Queue()
        self.eat_counter = 0
        self.sleep_counter = 0


    def add_event(self):
        """
        Adds a random event to the event queue.

        Returns:
            None
        """
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
        """
        Simulates a day according to the daily routine automaton.

        Returns:
            None
        """
        hour = 0
        occurance_chance = 0.25
        while hour < 24:
            random_chance = random.uniform(0.0, 1.0)
            self.add_event()
            print(f"Hour {hour}")
            if 0 <= hour < 8:
                self.current_state = random.choice(self.current_state.transitions)
                while self.current_state == EAT:
                    self.current_state = random.choice(self.current_state.transitions)
                if 3 < hour < 8 and self.sleep_counter == 0:
                    print("Well, it's time to sleep already")
                    self.current_state = SLEEP
                hour += self.current_state.durability
            elif 8 <= hour <= 21 and random_chance <= occurance_chance:
                event = self.event_queue.get()
                print(f"Oh! It's time for {event.name}")
                print(event.message)
                self.current_state = event.state
                occurance_chance = 0.25
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
            occurance_chance += self.current_state.durability / 100
            if self.current_state == SLEEP:
                self.sleep_counter += 1
            elif self.current_state == EAT:
                self.eat_counter += 1
        print("The day is over!")

# Create an instance of the DailyRoutineAutomata class
automata = DailyRoutineAutomata()

# Simulate the daily routine
automata.simulate_day()
