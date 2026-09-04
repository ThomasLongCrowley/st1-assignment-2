# AI Activity Card
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    # Validate all required fields
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")

    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    # Check for double-booking
    for appointment in appointments:
        if (
            appointment["practitioner"] == practitioner_name
            and appointment["time"] == appointment_time
        ):
            raise ValueError(
                "This practitioner already has an appointment at that time."
            )

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
# double booking
# book_appointment('Alice Smith1', 'Dr. John Doe1', '2024-07-20 11:00 AM')
# book_appointment('Bob Johnson', 'Dr. John Doe1', '2024-07-20 11:00 AM')
# no values
book_appointment('', '', '')
display_appointments()


# # Part D
# def create_appointment(patient_name, practitioner_name, appointment_time):
#     """
#     Store appointment details in a dictionary.

#     Note:
#     - Do NOT use a database.
#     - Do NOT use a GUI.
#     """

#     appointment = {
#         "patient_name": patient_name,
#         "practitioner_name": practitioner_name,
#         "appointment_time": appointment_time
#     }

#     return appointment


# # Example usage
# appointment = create_appointment(
#     "",
#     "Dr Brown",
#     "10:00 AM, 15 September 2026"
# )

# print(appointment)