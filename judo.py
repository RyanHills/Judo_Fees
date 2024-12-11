class Athlete:
    def __init__(self, name, training_plan, current_weight, competition_weight, competitions, private_coaching_hours):
        self.name = name
        self.training_plan = training_plan
        self.current_weight = current_weight
        self.competition_weight = competition_weight
        self.competitions = competitions
        self.private_coaching_hours = private_coaching_hours
        self.total_cost = 0

    def calculate_total_cost(self):
        # Costs (can be updated as needed)
        TRAINING_PLAN_COST = 50.0
        COMPETITION_COST = 20.0
        PRIVATE_COACHING_COST_PER_HOUR = 15.0

        self.total_cost = (
            TRAINING_PLAN_COST +
            self.competitions * COMPETITION_COST +
            self.private_coaching_hours * PRIVATE_COACHING_COST_PER_HOUR
        )

    def compare_weights(self):
        if self.current_weight > self.competition_weight:
            return f"{self.name} is {self.current_weight - self.competition_weight} kg over their competition weight."
        elif self.current_weight < self.competition_weight:
            return f"{self.name} is {self.competition_weight - self.current_weight} kg under their competition weight."
        else:
            return f"{self.name} is at their competition weight."

    def display_costs(self):
        print(f"Athlete Name: {self.name}")
        print("Itemized Costs:")
        print(f"- Training Plan: £50.00")
        print(f"- Competitions: £{self.competitions * 20.0:.2f}")
        print(f"- Private Coaching: £{self.private_coaching_hours * 15.0:.2f}")
        print(f"Total Cost: £{self.total_cost:.2f}")
        print(self.compare_weights())
        print("-" * 40)


def main():
    athletes = []

    print("North Sussex Judo - Monthly Fee Calculator")

    num_athletes = int(input("Enter the number of athletes to register: "))

    for i in range(num_athletes):
        print(f"\nRegistering athlete #{i + 1}")

        name = input("Enter athlete name: ")
        training_plan = input("Enter training plan: ")
        current_weight = float(input("Enter current weight (kg): "))
        competition_weight = float(input("Enter competition weight category (kg): "))
        competitions = int(input("Enter number of competitions entered this month: "))
        private_coaching_hours = int(input("Enter number of private coaching hours: "))

        athlete = Athlete(
            name, training_plan, current_weight, competition_weight, competitions, private_coaching_hours
        )
        athlete.calculate_total_cost()
        athletes.append(athlete)

    print("\nMonthly Report:")
    for athlete in athletes:
        athlete.display_costs()

    print("Program completed.")


if __name__ == "__main__":
    main()
