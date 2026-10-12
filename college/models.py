from django.db import models


class Lecturer(models.Model):
    # ლექტორი
    full_name = models.CharField(max_length=150)
    academic_degree = models.CharField(max_length=100, default="Ph.D.")  # აკადემიური ხარისხი
    office_room = models.CharField(max_length=50, blank=True, null=True)  # აუდიტორიის/კაბინეტის ნომერი
    contact_email = models.EmailField(unique=True)

    class Meta:
        db_table = 'lecturers'

    def __str__(self):
        return f"{self.full_name} ({self.academic_degree})"


class Course(models.Model):
    # კურსი
    course_name = models.CharField(max_length=200)
    credit_points = models.IntegerField(default=5)  # ECTS კრედიტები
    syllabus_details = models.TextField(blank=True, null=True)  # სილაბუსის აღწერა
    
    # კურსები და ლექტორები (Many-to-One)
    # ერთ ლექტორი - რამდენიმე კურსი
    lead_lecturer = models.ForeignKey(
        Lecturer, 
        on_delete=models.CASCADE, 
        related_name='assigned_courses'
    )

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f"{self.course_name} [{self.credit_points} ECTS]"


class Student(models.Model):
    # სტუდენტი
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    student_id_code = models.CharField(max_length=20, unique=True)  # პირადი ნომერი ან უნივერსიტეტის ID
    current_semester = models.IntegerField(default=1)  # მიმდინარე სემესტრი
    
    # სტუდენტები და კურსები: Many-to-Many
    # ერთ სტუდენტი - ბევრი კურსი
    enrolled_courses = models.ManyToManyField(
        Course, 
        related_name='enrolled_students'
    )

    class Meta:
        db_table = 'students'
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.student_id_code})"

