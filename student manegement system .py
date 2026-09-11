import gradio as gr


# ============================================================
# STUDENT CLASS
# ============================================================

class Student:

    def __init__(self):
        self.student_id = None

    # CREATE
    def Create(self, student_id):
        self.student_id = int(student_id)
        return f"Student Created Successfully!\nStudent ID: {self.student_id}"

    # READ
    def Read(self):
        if self.student_id is None:
            return "No Student Found."
        
        return f"Student ID: {self.student_id}"

    # UPDATE
    def Update(self, new_id):
        if self.student_id is None:
            return "No Student exists to update."

        self.student_id = int(new_id)
        return f"Student Updated Successfully!\nNew Student ID: {self.student_id}"

    # DELETE
    def Delete(self):
        if self.student_id is None:
            return "No Student Found."

        old_id = self.student_id
        self.student_id = None

        return f"Student Deleted Successfully!\nDeleted Student ID: {old_id}"

    # CHECK STATUS
    def check_status(self):
        if self.student_id is None:
            return "Student Status: Not Available / Deleted"

        return f"Student Status: Active\nStudent ID: {self.student_id}"


# ============================================================
# CREATE STUDENT OBJECT
# ============================================================

stu = Student()


# ============================================================
# GRADIO INTERFACE
# ============================================================

with gr.Blocks(title="Student Management System") as app:

    # Application title
    gr.Markdown(
        """
        # 🏢 Student Management System
        A beginner-friendly OOP + Gradio project
        """
    )

    # --------------------------------------------------------
    # STUDENT SECTION
    # --------------------------------------------------------

    gr.Markdown("## 👨‍🎓 Student")

    student_id = gr.Number(
        label="Student ID",
        value=11,
        precision=0
    )

    new_student_id = gr.Number(
        label="New Student ID",
        precision=0
    )

    # Output box
    output = gr.Textbox(
        label="Output",
        lines=5
    )

    # --------------------------------------------------------
    # BUTTONS
    # --------------------------------------------------------

    create_button = gr.Button("Create Student")
    read_button = gr.Button("Read Student")
    update_button = gr.Button("Update Student")
    delete_button = gr.Button("Delete Student")

    # --------------------------------------------------------
    # BUTTON FUNCTIONS
    # --------------------------------------------------------

    create_button.click(
        fn=stu.Create,
        inputs=student_id,
        outputs=output
    )

    read_button.click(
        fn=stu.Read,
        inputs=None,
        outputs=output
    )

    update_button.click(
        fn=stu.Update,
        inputs=new_student_id,
        outputs=output
    )

    delete_button.click(
        fn=stu.Delete,
        inputs=None,
        outputs=output
    )

    # --------------------------------------------------------
    # STATUS SECTION
    # --------------------------------------------------------

    gr.Markdown("## 🔍 Check Student Status")

    status_button = gr.Button("Check Status")

    status_output = gr.Textbox(
        label="Student Status",
        lines=5
    )

    status_button.click(
        fn=stu.check_status,
        inputs=None,
        outputs=status_output
    )


# ============================================================
# RUN APPLICATION
# ============================================================

app.launch()