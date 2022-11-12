from datetime import datetime
from django.db import models

DEPARTMENT_CHOICES = (
    ("CSE", "Computer Science and Engineering"),
    ("ECE", "Electronics and Communication Engineering"),
    ("EE", "Electrical Engineering"),
    ("ME", "Mechanical Engineering"),
    ("CE", "Civil Engineering"),
    ("IT", "Information Technology"),
    ("BME", "Biomedical Engineering"),
    ("AIML", "Artificial Intelligence and Machine Learning"),
    ("BCA", "Bachelor of Computer Applications"),
    ("MCA", "Master of Computer Applications"),
    ("MBA", "Master of Business Administration"),
    ("MTECH", "Master of Technology"),
    ("BBA", "Bachelor of Business Administration"),
    ("BSCCS", "Bachelor of Science in Computer Science & Cyber Security"),
    ("CSBS", "Computer Science and Business Systems"),
)

SEX_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
)


def get_current_year():
    return datetime.now().year  # type: ignore


class Member(models.Model):
    name = models.CharField(max_length=254)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, null=True)
    email = models.EmailField(max_length=254, unique=True)

    whatsapp = models.BigIntegerField(null=True, blank=True)
    contact = models.BigIntegerField(null=True, blank=True)

    department = models.CharField(
        max_length=6, null=True, blank=True, choices=DEPARTMENT_CHOICES
    )

    graduation = models.IntegerField(default=get_current_year)
    section = models.CharField(max_length=10, null=True, blank=True)
    student_id = models.CharField(max_length=16, null=True, blank=True)
    avatar = models.ImageField(upload_to="member/avatar", null=True, blank=True)

    is_verified = models.BooleanField(default=False)
    payment_image = models.ImageField(upload_to="member/payment", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "phoenix_member"

    def __str__(self):
        return f"{self.name} : {self.graduation}"
