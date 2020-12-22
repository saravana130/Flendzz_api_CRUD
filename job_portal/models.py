from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    crated_by = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    salary_package = models.CharField(max_length=100, default='Not Disclosed', blank=True)

    def __str__(self):
        return self.title

class JobApplicant(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=50, null=False)
    applicant_email_id = models.EmailField(null=False)
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job_id', 'applicant_email_id',)

    def __str__(self):
        return self.applicant_name

