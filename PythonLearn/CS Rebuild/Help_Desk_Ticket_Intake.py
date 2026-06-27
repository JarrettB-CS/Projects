# CS Rebuild HQ – Support Ticket Summary Builder
# Collects customer, device, operating system, issue, and urgency details.
# Prints a clean support ticket summary without conditional logic.

customer_name = input("Enter your name: ")
device_type = input("Enter your device: ")
operating_system = input("Enter your device OS: ")
issue_category = input("Enter your type of issue: ")
issue_description = input("Enter your issue details: ")
urgency = input("Enter urgency 1-5: ")

print("--- Support Ticket ---")
print(f"Customer: {customer_name}")
print(f"Device: {device_type}")
print(f"Operating System: {operating_system}")
print(f"Category: {issue_category}")
print(f"Issue: {issue_description}")
print(f"Urgency: {urgency}")

# TODO:
# - [easy] Add spacing and separators to make the printed ticket easier to read.
# - [medium] Validate the urgency rating so it only accepts values from 1 to 5.
# - [hard] Add ticket IDs, timestamps, and support-priority labels.

# UPDATE LOG:
# 1.0.0 (2026-06-27) [init] – Initial working version. Collected support ticket details and printed a clean ticket summary without using if statements.
