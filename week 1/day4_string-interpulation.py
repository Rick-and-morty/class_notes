mad_lib = """
dear {name},
i am {action}ing you to {other_action} you
to {action_three} your {noun}.
"""
print(mad_lib.format(name="joel", action="write",
                     other_action="inform",
                     action_three="get lost",
                     noun="face"))
marker_action = "erase"
print("markers are difficult to %s")
