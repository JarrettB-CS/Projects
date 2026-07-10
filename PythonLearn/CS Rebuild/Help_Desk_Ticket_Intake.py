# CS Rebuild HQ – Support Ticket Summary Builder
# Collects customer, device, operating system, issue, and urgency details.
# Prints a clean support ticket summary without conditional logic.

customer_name = input("Enter your name: ")
device_type = input("Enter your device: ")
operating_system = input("Enter your device OS: ")
issue_category = input("Enter your type of issue: ")
issue_description = input("Enter your issue details: ")
urgency = int(input("Enter urgency 1-5: "))

print()
print("--- Support Ticket ---")
print(f"Customer: {customer_name}")
print(f"Device: {device_type}")
print(f"Operating System: {operating_system}")
print(f"Category: {issue_category}")
print(f"Issue: {issue_description}")
print(f"Urgency: {urgency}")

if customer_name == "":
    print("Missing customer name")
elif device_type == "":
    print("Missing device type")
elif urgency < 1 or urgency > 5:
    print("Invalid urgency rating")
elif urgency == 5 or issue_category == "security":
    print("Priority: Critical - escalate immediately")
elif urgency in [3, 4]:
    print("Priority: Medium - normal support queue")
else:
    print("Priority: Low - handle when available")

print("Ticket accepted")

# TODO:
# - [easy] Add a closing separator after the support ticket summary.
# - [medium] Validate the urgency rating so it only accepts values from 1 to 5.
# - [hard] Add ticket IDs, timestamps, and support-priority labels.

# UPDATE LOG:
# 1.1.0 (2026-07-09) [feature] [homework] [easy] – Completed TODO: Added spacing and separators to make the support ticket easier to read.
# 1.0.1 (2026-06-28) [homework] – Displayed priority messages based on urgency.
# 1.0.0 (2026-06-27) [init] – Initial working version. Collected support ticket details and printed a clean ticket summary without using if statements.
