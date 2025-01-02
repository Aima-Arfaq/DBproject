from django.db import models

# Create your models here.

from django.db import models

# Student Model
import datetime
from django.core.exceptions import ValidationError

from django.db import models

class Student(models.Model):
    DEPT_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('DS', 'Data Science'),
        ('SE', 'Software Engineering'),
        ('PharmD', 'D Pharmacy'),
        # Add other department choices here
    ]
    
    ALLOCATION_STATUS_CHOICES = [
        ('allocated', 'Allocated'),
        ('unallocated', 'Unallocated'),
    ]
    
    st_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    st_contactNumber = models.CharField(max_length=11)
    st_email = models.EmailField()
    emergency_contact = models.CharField(max_length=11)
    dept_name = models.CharField(max_length=6, choices=DEPT_CHOICES)
    room_id = models.ForeignKey(
        'Room',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,  # Allows the field to be left empty in forms
    )
    start_date = models.DateField()
    end_date = models.DateField()
    allocationStatus = models.CharField(max_length=20, choices=ALLOCATION_STATUS_CHOICES)
    
    def save(self, *args, **kwargs):
        if len(self.st_contactNumber) != 11 or not self.st_contactNumber.isdigit():
            raise ValueError("Contact number must be 11 digits long.")
        if len(self.emergency_contact) != 11 or not self.emergency_contact.isdigit():
            raise ValueError("Emergency contact must be 11 digits long.")
        if not self.st_email.endswith('@gmail.com'):
            raise ValueError("Email must end with '@gmail.com'.")
        if self.end_date <= self.start_date:
            raise ValueError("End date must be greater than start date.")
        
        # Handle room logic
        room = self.room_id
        if self.allocationStatus == 'allocated' and room:
            # Update room status and number of students
            if room.room_type == 'single':
                room.noOfStudents = 1
                room.room_status = 'occupied'
            elif room.room_type == 'double':
                if room.noOfStudents < 2:
                    room.noOfStudents += 1
                if room.noOfStudents == 2:
                    room.room_status = 'occupied'
                else:
                    room.room_status = 'available'
            
            room.save()
        elif self.allocationStatus == 'unallocated':
            # If the student is unallocated, clear room_id
            if room:
                if room.noOfStudents > 0:
                    room.noOfStudents -= 1
                if room.noOfStudents == 0:
                    room.room_status = 'available'
                room.save()
            self.room_id = None  # Clear the room assignment
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"




# Department Model
class Department(models.Model):
    dept_name = models.CharField(max_length=100, primary_key=True)
    dept_id = models.IntegerField() 
    degreeDuration = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    
    def save(self, *args, **kwargs):
        if self.degreeDuration < 1 or self.degreeDuration > 5:
            raise ValueError("Degree Duration must be between 1 and 5 years.")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.dept_name

# Visitors Model
from datetime import date
from django.core.exceptions import ValidationError

class Visitors(models.Model):
    st_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    visitor_id = models.AutoField(primary_key=True)
    visitorName = models.CharField(max_length=255)
    purposeOfVisit = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    dateOfVisit = models.DateField()


    def save(self, *args, **kwargs):
        # Call the clean method to perform validation
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Visitor {self.visitorName} for {self.st_id}"


# Menu Model
class Menu(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    day = models.CharField(max_length=9, choices=DAY_CHOICES, primary_key=True)
    breakfast = models.CharField(max_length=255)
    lunch = models.CharField(max_length=255)
    dinner = models.CharField(max_length=255)
    
    def __str__(self):
        return self.day


# Room Model
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=10, choices=[('single', 'Single'), ('double', 'Double')])
    room_status = models.CharField(max_length=10, choices=[('available', 'Available'), ('occupied', 'Occupied')])
    noOfStudents = models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2')])
    
    def __str__(self):
        return f"Room {self.room_id}"

# Room Allocation Model
class RoomAllocation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    st_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Room {self.room_id} allocated to Student {self.st_id.st_id}"

# Annual Dues Model
class AnnualDues(models.Model):
    Year = models.PositiveIntegerField()
    electricityCharges = models.DecimalField(max_digits=10, decimal_places=2, default=5000)
    water = models.DecimalField(max_digits=10, decimal_places=2, default=2000)
    roomAccomodation = models.DecimalField(max_digits=10, decimal_places=2, default=5000)
    gas = models.DecimalField(max_digits=10, decimal_places=2, default=2000)
    commonRoom = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    studyRoom = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    WiFi = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    others = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total = (self.electricityCharges + self.water + self.roomAccomodation + self.gas +
                      self.commonRoom + self.studyRoom + self.WiFi + self.others)
        if any(value < 0 for value in [self.electricityCharges, self.water, self.roomAccomodation, self.gas,
                                       self.commonRoom, self.studyRoom, self.WiFi, self.others]):
            raise ValueError("None of the charges can be negative.")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Annual Dues for Year {self.Year}"

# Annual Challan Model
class AnnualChallan(models.Model):
    challan_no = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    st_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    validUpto = models.DateField()
    
    def save(self, *args, **kwargs):
        self.validUpto = models.DateField.today() + models.timedelta(days=15)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Challan No {self.challan_no} for Student {self.st_id.st_id}"

# Annual Dues Status Model
class AnnualDuesStatus(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]
    
    st_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Year = models.PositiveIntegerField()
    paymentStatus = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    
    def __str__(self):
        return f"Dues Status for Student {self.st_id.st_id} in Year {self.Year}: {self.paymentStatus.capitalize()}"


# Monthly Meal Consumption Model
class MonthlyMealConsumption(models.Model):
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    
    st_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=10, choices=MONTH_CHOICES)
    year = models.PositiveIntegerField()
    daysConsumed = models.PositiveIntegerField()
    perDayCharges = models.DecimalField(max_digits=10, decimal_places=2)
    charges = models.DecimalField(max_digits=12, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if self.daysConsumed < 1 or self.daysConsumed > 31:
            raise ValueError("Days consumed must be between 1 and 31.")
        if self.perDayCharges < 0:
            raise ValueError("Per day charges cannot be negative.")
        self.charges = self.daysConsumed * self.perDayCharges
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Meal Consumption for Student {self.st_id.st_id} in {self.month} {self.year}"


# Monthly Dues Status Model
class MonthlyDuesStatus(models.Model):
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]
    
    st_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    month = models.CharField(max_length=10, choices=MONTH_CHOICES,  )
    payment_status = models.CharField(max_length=7, choices=PAYMENT_STATUS_CHOICES, default = 'unpaid')
    
    def __str__(self):
        return f"Monthly Dues Status for Student {self.st_id.st_id} in {self.month}/{self.year} - Status: {self.payment_status}"

# Hostel Staff Model
class HostelStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=255)
    staff_role = models.CharField(max_length=100)
    staff_contact = models.CharField(max_length=11)
    staff_salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if len(self.staff_contact) != 11 or not self.staff_contact.isdigit():
            raise ValueError("Staff contact number must be 11 digits long and cannot be negative.")
        if self.staff_salary < 0:
            raise ValueError("Salary cannot be negative.")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.staff_name} ({self.staff_role})"
