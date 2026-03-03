from django.shortcuts import render
from .models import Job
from .forms import ResumeForm

def job_list(request):
    jobs = Job.objects.exclude(title="Post Resume")
    post_resume = Job.objects.filter(title="Post Resume")    # must be add upload resume model's title is:"Post Resume". {must use space}
    context = {'jobs': jobs , 'post_resume':post_resume }
    return render(request, 'job_portal/job_list.html', context)

# def submit_resume(request, job_id):
#     job = Job.objects.get(id=job_id)
#     if request.method == 'POST':
#         form = ResumeForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Save the resume to the job
#              resume_instance = form.save(commit=False)
#              resume_instance.job = job  # Associate the resume with the job
#              resume_instance.save()
#              return render(request, 'job_portal/resume_submitted.html')
#     else:
#         form = ResumeForm()
#     return render(request, 'job_portal/submit_resume.html', {'form': form, 'job': job})  


# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Job
# from .forms import ResumeForm

# def submit_resume(request, job_id):
#     job = get_object_or_404(Job, id=job_id)

#     # Check circular file type
#     circular_is_pdf = False
#     if job.circular:
#         circular_url = job.circular.url.lower()
#         if circular_url.endswith('.pdf'):
#             circular_is_pdf = True

#     if request.method == 'POST':
#         form = ResumeForm(request.POST, request.FILES)
#         if form.is_valid():
#             resume_instance = form.save(commit=False)
#             resume_instance.job = job  # Associate resume with the job
#             resume_instance.save()
#             # Redirect or render a success page
#             return render(request, 'job_portal/resume_submitted.html', {'job': job, 'resume': resume_instance})
#         else:
#             # Form invalid, show errors
#             return render(request, 'job_portal/submit_resume.html', {
#                 'form': form,
#                 'job': job,
#                 'circular_is_pdf': circular_is_pdf
#             })
#     else:
#         form = ResumeForm()

#     return render(request, 'job_portal/submit_resume.html', {
#         'form': form,
#         'job': job,
#         'circular_is_pdf': circular_is_pdf
#     })
#     # job done for this project



from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Job
from .forms import ResumeForm


def submit_resume(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    circular_is_pdf = False
    if job.circular:
        circular_url = job.circular.url.lower()
        if circular_url.endswith('.pdf'):
            circular_is_pdf = True

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume_instance = form.save(commit=False)
            resume_instance.job = job
            resume_instance.save()

            # =========================
            # 1️⃣ Admin Notification Mail
            # =========================
            subject_admin = f"New Resume Submitted for {job.title}"
            message_admin = f"""
            A new resume has been submitted.

            Job Title: {job.title}
            Name: {resume_instance.name}
            Email: {resume_instance.email}
            Contact: {resume_instance.contact}
            """

            send_mail(
                subject_admin,
                message_admin,
                settings.DEFAULT_FROM_EMAIL,
                ['jsbdltd@gmail.com'],  # your receiving email
                fail_silently=False,
            )

            # =========================
            # 2️⃣ Applicant Confirmation Mail
            # =========================
            if resume_instance.email:
                subject_user = "Application Received - JSBD Overseas Limited"
                message_user = f"""
                Dear {resume_instance.name},

                Thank you for applying for the position of {job.title}.
                We have successfully received your application.

                Our team will review your resume and contact you if shortlisted.

                Best Regards,
                JSBD Overseas Limited
                """

                send_mail(
                    subject_user,
                    message_user,
                    settings.DEFAULT_FROM_EMAIL,
                    [resume_instance.email],
                    fail_silently=False,
                )

            return render(request, 'job_portal/resume_submitted.html', {
                'job': job,
                'resume': resume_instance
            })

        else:
            return render(request, 'job_portal/submit_resume.html', {
                'form': form,
                'job': job,
                'circular_is_pdf': circular_is_pdf
            })

    else:
        form = ResumeForm()

    return render(request, 'job_portal/submit_resume.html', {
        'form': form,
        'job': job,
        'circular_is_pdf': circular_is_pdf
    })





# # views.py

# import pdfplumber
# import re
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Student, SemesterResult


# def upload_semester_pdf(request):

#     if request.method == "POST":

#         pdf_file = request.FILES.get("pdf_file")
#         semester_number = int(request.POST.get("semester"))

#         full_text = ""

#         with pdfplumber.open(pdf_file) as pdf:
#             for page in pdf.pages:
#                 text = page.extract_text()
#                 if text:
#                     full_text += text + "\n"

#         # Extract Batch
#         batch_match = re.search(r'Batch\s+(\d+)', full_text)
#         batch_number = batch_match.group(1) if batch_match else "Unknown"

#         # Extract student rows
#         pattern = re.findall(
#             r'\d+\s+([A-Z.\s]+?)\s+'
#             r'(CS-D-[\d\-A-Z]+)\s+'
#             r'2022-2023.*?'
#             r'(\d+\.\d+)\s+([A-Z+\-]+)\s+Passed\s+(\d+\.\d+)',
#             full_text,
#             re.DOTALL
#         )

#         for name, reg_no, sgpa, avg_grade, cgpa in pattern:

#             student, created = Student.objects.update_or_create(
#                 reg_no=reg_no.strip(),
#                 defaults={
#                     "name": name.strip(),
#                     "batch": batch_number,
#                     "final_cgpa": float(cgpa)
#                 }
#             )

#             SemesterResult.objects.update_or_create(
#                 student=student,
#                 semester=semester_number,
#                 defaults={
#                     "sgpa": float(sgpa),
#                     "average_grade": avg_grade,
#                     "cgpa": float(cgpa)
#                 }
#             )

#         return HttpResponse("✅ Semester Result Uploaded Successfully")

#     return render(request, "upload_semester.html")




# # views.py

# import pdfplumber
# import re
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Student, SemesterResult

# def upload_semester_pdf(request):
#     if request.method == "POST":
#         pdf_file = request.FILES.get("pdf_file")
#         semester_number = int(request.POST.get("semester"))

#         full_text = ""
#         with pdfplumber.open(pdf_file) as pdf:
#             for page in pdf.pages:
#                 text = page.extract_text()
#                 if text:
#                     full_text += text + "\n"

#         # Extract Batch
#         batch_match = re.search(r'Batch\s+(\d+)', full_text)
#         batch_number = batch_match.group(1) if batch_match else "Unknown"

#         # --- Extract all student lines ---
#         # Using old regex idea to capture CGPA/SGPA/Avg Grade if present
#         student_pattern = re.findall(
#             r'\d+\s+([A-Z.\s]+?)\s+'           # Name
#             r'(CS-D-[\d\-A-Z]+)\s+'            # Reg No
#             r'2022-2023.*?'                     # Session
#             r'(\d+\.\d+)?\s*([A-Z+\-]+)?\s*(Passed|Failed|Incomplete)?\s*(\d+\.\d+)?',  # SGPA, Avg Grade, Result, CGPA
#             full_text,
#             re.DOTALL | re.IGNORECASE
#         )

#         for name, reg_no, sgpa, avg_grade, result_status, cgpa in student_pattern:

#             # Clean values
#             name = name.strip()
#             reg_no = reg_no.strip()
#             sgpa_val = float(sgpa) if sgpa else 0
#             avg_grade_val = avg_grade if avg_grade else ""
#             cgpa_val = float(cgpa) if cgpa else 0

#             # --- Save Student ---
#             student, created = Student.objects.update_or_create(
#                 reg_no=reg_no,
#                 defaults={
#                     "name": name,
#                     "batch": batch_number,
#                     "final_cgpa": cgpa_val
#                 }
#             )

#             # --- Save SemesterResult ---
#             SemesterResult.objects.update_or_create(
#                 student=student,
#                 semester=semester_number,
#                 defaults={
#                     "sgpa": sgpa_val,
#                     "average_grade": avg_grade_val,
#                     "cgpa": cgpa_val
#                 }
#             )

#         return HttpResponse(f"✅ Semester {semester_number} Results Uploaded Successfully for Batch {batch_number}")

#     return render(request, "upload_semester.html")


# #ayta okey ase just last ar obj ta store kore pare nhh, tai block

# import pdfplumber
# import re
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Student, SemesterResult


# def upload_semester_pdf(request):

#     if request.method == "POST":

#         pdf_file = request.FILES.get("pdf_file")
#         semester_number = int(request.POST.get("semester"))

#         full_text = ""

#         with pdfplumber.open(pdf_file) as pdf:
#             for page in pdf.pages:
#                 text = page.extract_text()
#                 if text:
#                     full_text += text + "\n"

#         # -------- Extract Batch --------
#         batch_match = re.search(r'Batch\s+(\d+)', full_text)
#         batch_number = batch_match.group(1) if batch_match else "Unknown"

#         # -------- Clean Text --------
#         lines = full_text.split("\n")
#         cleaned_lines = []

#         for line in lines:
#             line = line.strip()
#             if line:
#                 cleaned_lines.append(line)

#         students = []
#         current_student = ""

#         # -------- Combine multi-line student rows --------
#         for line in cleaned_lines:

#             # Student row starts with roll number
#             if re.match(r'^\d+\s+', line):
#                 if current_student:
#                     students.append(current_student)
#                 current_student = line
#             else:
#                 current_student += " " + line

#         if current_student:
#             students.append(current_student)

#         # -------- Extract Data from each student --------
#         for row in students:

#             # Skip header rows
#             if "Roll Name" in row or "Credit" in row:
#                 continue

#             reg_match = re.search(r'(CS-D-[\d\-A-Z]+)', row)
#             if not reg_match:
#                 continue

#             reg_no = reg_match.group(1)

#             # Extract name (between roll and reg no)
#             name_match = re.search(r'^\d+\s+(.*?)\s+CS-D-', row)
#             name = name_match.group(1).strip() if name_match else "Unknown"

#             # Extract SGPA, Grade, Result, CGPA (শেষের অংশ থেকে)
#             tail_match = re.search(
#                 r'(\d+\.\d+|--)\s+([A-Z+\-]+|--)\s+(Passed|Incomplete|Readmision|Failed)\s+(\d+\.\d+|Incomplete|--)',
#                 row
#             )

#             sgpa = None
#             avg_grade = None
#             cgpa = None

#             if tail_match:
#                 sgpa_raw = tail_match.group(1)
#                 avg_grade = tail_match.group(2)
#                 cgpa_raw = tail_match.group(4)

#                 if sgpa_raw != "--":
#                     sgpa = float(sgpa_raw)

#                 if cgpa_raw not in ["--", "Incomplete"]:
#                     try:
#                         cgpa = float(cgpa_raw)
#                     except:
#                         cgpa = None

#             # -------- Save Student --------
#             student, created = Student.objects.update_or_create(
#                 reg_no=reg_no,
#                 defaults={
#                     "name": name,
#                     "batch": batch_number,
#                     "final_cgpa": cgpa
#                 }
#             )

#             # -------- Save Semester Result --------
#             SemesterResult.objects.update_or_create(
#                 student=student,
#                 semester=semester_number,
#                 defaults={
#                     "sgpa": sgpa,
#                     "average_grade": avg_grade,
#                     "cgpa": cgpa
#                 }
#             )

#         return HttpResponse(f"✅ Semester {semester_number} Uploaded Successfully for Batch {batch_number}")

#     return render(request, "upload_semester.html")
