from django.db import models

# -----------------------------------------------------------------
# Recursive m2m
# ------------------------------------------------------------------

class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=25)
    boss = models.BooleanField(default=False)
    supervisors = models.ManyToManyField("Employee", related_name="subordinates")

    class Meta:
        """ Default ordering of Employee objects"""
        ordering = ["lname"]

    def __str__(self):
        """ Return a string representation of the object """
        return f"{self.lname}, {self.fname}, is a boss: {self.boss}"
    
    def is_supervisor(self):
        """ Check if the employee has subordinates (is a supervisor) """
        return self.subordinates.exists()
    
    @classmethod
    def get_all_supervisors(cls):
        """ Return all employees who supervise others """
        return cls.objects.filter(subordinates__isnull=False).distinct()
    
    @classmethod
    def create_boss(cls, fname, lname):
        """ Create a new employee with boss status """
        return cls.objects.create(fname=fname, lname=lname, boss=True)
    
    




