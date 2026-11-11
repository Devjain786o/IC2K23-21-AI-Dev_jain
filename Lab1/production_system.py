
"""
Experiment 2: Production Rule Based System
Author: Dev Jain
Roll No: IC2K23-21
"""


def run_production_rules():

    # Store the initial conditions in working memory
    memory = {
        "temperature": 32,
        "person_present": True,
        "fan_on": False,
        "window_open": False
    }

    # Define rules with their conditions and operations
    production_rules = [

        (
            "Switch ON the Fan",
            lambda data: (
                data["temperature"] > 28
                and data["person_present"] is True
                and data["fan_on"] is False
            ),
            lambda data: data.update({"fan_on": True})
        ),

        (
            "Open the Window",
            lambda data: (
                data["temperature"] > 30
                and data["window_open"] is False
            ),
            lambda data: data.update({"window_open": True})
        )

    ]

    print("PRODUCTION RULE SYSTEM")
    print("=" * 35)

    print("Initial Working Memory:", memory)

    # Execute rules until no condition is satisfied
    while True:

        executed = False

        for name, check, operation in production_rules:

            if check(memory):

                print("\nExecuting Rule:", name)

                operation(memory)

                executed = True
                break

        # Stop when no rule can be applied
        if executed is False:
            break

    print("\nUpdated Working Memory:", memory)


if __name__ == "__main__":
    run_production_rules()
