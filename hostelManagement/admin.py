from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Department, Visitors, Menu, Room, RoomAllocation, AnnualDues, AnnualChallan
from .models import AnnualDuesStatus, MonthlyMealConsumption, MonthlyDuesStatus, HostelStaff

# Register Student model
class StudentAdmin(admin.ModelAdmin):
    list_display = ('st_id', 'firstName', 'lastName', 'st_email', 'dept_name', 'room_id', 'allocationStatus')
    search_fields = ('firstName', 'lastName', 'st_email','allocationStatus','room_id__room_id')
    list_filter = ('dept_name', 'allocationStatus')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "room_id":
            kwargs["queryset"] = Room.objects.filter(room_status="available")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Student, StudentAdmin)

# Register Department model
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'dept_id', 'degreeDuration')
    search_fields = ('dept_name',)

admin.site.register(Department, DepartmentAdmin)

# Register Visitors model
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('visitor_id', 'st_id', 'visitorName', 'purposeOfVisit','relation', 'dateOfVisit')
    search_fields = ('visitorName', 'purposeOfVisit')
    list_filter = ('dateOfVisit',)

admin.site.register(Visitors, VisitorsAdmin)

# Register Menu model
class MenuAdmin(admin.ModelAdmin):
    list_display = ('day', 'breakfast', 'lunch', 'dinner')
    search_fields = ('day',)

admin.site.register(Menu, MenuAdmin)

# Register Room model
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_type', 'room_status', 'noOfStudents')
    search_fields = ('room_id', 'room_type','room_status')
    list_filter = ('room_status',)

admin.site.register(Room, RoomAdmin)

# Register RoomAllocation model
class RoomAllocationAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'st_id')
    search_fields = ('room_id', 'st_id')

admin.site.register(RoomAllocation, RoomAllocationAdmin)

# Register AnnualDues model
class AnnualDuesAdmin(admin.ModelAdmin):
    readonly_fields = ('total',)
    list_display = ('Year', 'electricityCharges', 'water', 'roomAccomodation', 'gas','commonRoom', 'studyRoom', 'WiFi','others', 'total')
    search_fields = ('Year',)
    
admin.site.register(AnnualDues, AnnualDuesAdmin)

# Register AnnualChallan model
class AnnualChallanAdmin(admin.ModelAdmin):
    list_display = ('challan_no', 'room_id', 'st_id', 'validUpto')
    search_fields = ('challan_no', 'st_id')

admin.site.register(AnnualChallan, AnnualChallanAdmin)

# Register AnnualDuesStatus model
class AnnualDuesStatusAdmin(admin.ModelAdmin):
    list_display = ('st_id', 'Year', 'paymentStatus')
    search_fields = ('st_id', 'Year','paymentStatus')

admin.site.register(AnnualDuesStatus, AnnualDuesStatusAdmin)

# Register MonthlyMealConsumption model
class MonthlyMealConsumptionAdmin(admin.ModelAdmin):
    readonly_fields = ('charges',)
    list_display = ('st_id', 'month', 'year', 'daysConsumed', 'charges')
    search_fields = ('st_id', 'month', 'year')

admin.site.register(MonthlyMealConsumption, MonthlyMealConsumptionAdmin)

# Register MonthlyDuesStatus model
class MonthlyDuesStatusAdmin(admin.ModelAdmin):
    list_display = ('st_id', 'year', 'month', 'payment_status')
    search_fields = ('st_id', 'year', 'month')

admin.site.register(MonthlyDuesStatus, MonthlyDuesStatusAdmin)

# Register HostelStaff model
class HostelStaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'staff_name', 'staff_role', 'staff_salary')
    search_fields = ('staff_name', 'staff_role')
    list_filter = ('staff_role',)

admin.site.register(HostelStaff, HostelStaffAdmin)

