# ============================================================
# LEAVE MANAGEMENT SYSTEM
# OOP + GRADIO
# Beginner Project
# ============================================================

import gradio as gr


# ============================================================
# 1. EMPLOYEE CLASS
# ============================================================

class Employee:

    def __init__(self, emp_id, name, leave_balance=20):
        self.emp_id = emp_id
        self.name = name

        # Total leaves available
        self.leave_balance = leave_balance

        # Store leave requests
        self.leave_requests = []

    # --------------------------------------------------------
    # Employee applies for leave
    # --------------------------------------------------------

    def apply_leave(self, days):

        # Check whether number of days is valid
        if days <= 0:
            return "❌ Leave days must be greater than 0."

        # Check leave balance
        if days > self.leave_balance:
            return (
                f"❌ You have only {self.leave_balance} "
                f"leave(s) remaining."
            )

        # Create leave request
        request = LeaveRequest(self, days)

        # Store request
        self.leave_requests.append(request)

        return (
            f"✅ Leave request submitted successfully!\n\n"
            f"Employee: {self.name}\n"
            f"Days Requested: {days}\n"
            f"Status: Pending"
        )


# ============================================================
# 2. LEAVE REQUEST CLASS
# ============================================================

class LeaveRequest:

    def __init__(self, employee, days):

        self.employee = employee
        self.days = days

        # Initially Pending
        self.status = "Pending"

    # --------------------------------------------------------
    # Approve leave
    # --------------------------------------------------------

    def approve(self):

        # Only Pending requests can be approved
        if self.status != "Pending":
            return f"Request is already {self.status}."

        # Check leave balance
        if self.days > self.employee.leave_balance:

            self.status = "Rejected"

            return "❌ Leave rejected because of insufficient balance."

        # Deduct approved leaves
        self.employee.leave_balance -= self.days

        # Change status
        self.status = "Approved"

        return (
            f"✅ Leave approved!\n\n"
            f"Employee: {self.employee.name}\n"
            f"Days: {self.days}\n"
            f"Remaining Leaves: {self.employee.leave_balance}"
        )

    # --------------------------------------------------------
    # Reject leave
    # --------------------------------------------------------

    def reject(self):

        if self.status != "Pending":
            return f"Request is already {self.status}."

        self.status = "Rejected"

        return (
            f"❌ Leave rejected.\n\n"
            f"Employee: {self.employee.name}"
        )


# ============================================================
# 3. MANAGER CLASS
# ============================================================

class Manager:

    def __init__(self, name):
        self.name = name

    # Approve employee request
    def approve_request(self, request):
        return request.approve()

    # Reject employee request
    def reject_request(self, request):
        return request.reject()


# ============================================================
# 4. CREATE EMPLOYEES
# ============================================================

employees = {

    101: Employee(101, "Rahul", 20),

    102: Employee(102, "Priya", 15),

    103: Employee(103, "Amit", 18)
}


# ============================================================
# 5. CREATE MANAGER
# ============================================================

manager = Manager("Mr. Sharma")


# ============================================================
# 6. APPLY LEAVE FUNCTION
# ============================================================

def apply_leave(employee_id, days):

    # Convert Employee ID to integer
    try:
        employee_id = int(employee_id)
    except:
        return "❌ Please enter a valid Employee ID."

    # Check Employee ID
    if employee_id not in employees:
        return "❌ Employee ID not found."

    # Convert days to integer
    try:
        days = int(days)
    except:
        return "❌ Please enter a valid number of days."

    # Get employee object
    employee = employees[employee_id]

    # Call Employee method
    message = employee.apply_leave(days)

    return message


# ============================================================
# 7. GET EMPLOYEE STATUS
# ============================================================

def check_status(employee_id):

    try:
        employee_id = int(employee_id)
    except:
        return "❌ Please enter a valid Employee ID."

    if employee_id not in employees:
        return "❌ Employee ID not found."

    employee = employees[employee_id]

    # No requests
    if len(employee.leave_requests) == 0:

        return (
            f"Employee: {employee.name}\n"
            f"Remaining Leaves: {employee.leave_balance}\n\n"
            f"No leave requests found."
        )

    # Create status report
    result = (
        f"Employee: {employee.name}\n"
        f"Remaining Leaves: {employee.leave_balance}\n\n"
        f"Leave Requests:\n"
    )

    # Display requests
    for i, request in enumerate(employee.leave_requests, start=1):

        result += (
            f"\nRequest {i}: "
            f"{request.days} day(s) → "
            f"{request.status}"
        )

    return result


# ============================================================
# 8. MANAGER - APPROVE LEAVE
# ============================================================

def approve_leave(employee_id):

    try:
        employee_id = int(employee_id)
    except:
        return "❌ Please enter a valid Employee ID."

    if employee_id not in employees:
        return "❌ Employee ID not found."

    employee = employees[employee_id]

    # Check requests
    if len(employee.leave_requests) == 0:
        return "❌ No leave request found."

    # Get latest request
    request = employee.leave_requests[-1]

    # Manager approves
    return manager.approve_request(request)


# ============================================================
# 9. MANAGER - REJECT LEAVE
# ============================================================

def reject_leave(employee_id):

    try:
        employee_id = int(employee_id)
    except:
        return "❌ Please enter a valid Employee ID."

    if employee_id not in employees:
        return "❌ Employee ID not found."

    employee = employees[employee_id]

    if len(employee.leave_requests) == 0:
        return "❌ No leave request found."

    # Get latest request
    request = employee.leave_requests[-1]

    # Manager rejects
    return manager.reject_request(request)


# ============================================================
# 10. GRADIO USER INTERFACE
# ============================================================

with gr.Blocks(title="Leave Management System") as app:

    # Application title
    gr.Markdown(
        """
        # 🏢 Sakshi OWN Leave Management System

        A beginner-friendly OOP + Gradio project
        """
    )

    # --------------------------------------------------------
    # EMPLOYEE SECTION
    # --------------------------------------------------------

    gr.Markdown("## 👨‍💼 Employee")

    employee_id = gr.Number(
        label="Employee ID",
        value=101,
        precision=0
    )

    leave_days = gr.Number(
        label="Number of Leave Days",
        value=1,
        precision=0
    )

    apply_button = gr.Button("Apply Leave")
    apply_button = gr.Button("Save my leave")

    apply_output = gr.Textbox(
        label="Application Status",
        lines=5
    )

    apply_button.click(
        fn=apply_leave,
        inputs=[employee_id, leave_days],
        outputs=apply_output
    )

    # --------------------------------------------------------
    # STATUS SECTION
    # --------------------------------------------------------

    gr.Markdown("## 📋 Check Leave Status")

    status_button = gr.Button("Check Status")

    status_output = gr.Textbox(
        label="Leave Status",
        lines=8
    )

    status_button.click(
        fn=check_status,
        inputs=employee_id,
        outputs=status_output
    )

    # --------------------------------------------------------
    # MANAGER SECTION
    # --------------------------------------------------------

    gr.Markdown("## 👨‍💼 Manager Panel")

    approve_button = gr.Button("Approve Latest Request")

    reject_button = gr.Button("Reject Latest Request")

    manager_output = gr.Textbox(
        label="Manager Action",
        lines=5
    )

    # Approve button
    approve_button.click(
        fn=approve_leave,
        inputs=employee_id,
        outputs=manager_output
    )

    # Reject button
    reject_button.click(
        fn=reject_leave,
        inputs=employee_id,
        outputs=manager_output
    )


# ============================================================
# 11. RUN APPLICATION
# ============================================================

app.launch()