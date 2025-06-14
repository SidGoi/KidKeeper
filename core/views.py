from django.shortcuts import render
from .models import Kid


# Home Page -
def home(request):
    data = Kid.objects.all()
    return render(request, "index.html", {"data": data})


# Add Kids Page -
from django.shortcuts import render, redirect
from .models import Kid, Attendance
from django.utils import timezone


def add(request):
    if request.method == "POST":
        kid_name = request.POST["kid_name"]
        father_name = request.POST["father_name"]
        surename = request.POST["surename"]
        standard = request.POST["standard"]
        birthdate = request.POST["birthdate"]
        mobile_number = request.POST["mobile_number"]

        Kid.objects.create(
            kid_name=kid_name,
            father_name=father_name,
            surename=surename,
            standard=standard,
            birthdate=birthdate,
            mobile_number=mobile_number,
        )
        return redirect("home")
    return render(request, "add.html")


def delete(request, id):
    kid = Kid.objects.get(id=id)
    kid.delete()
    return redirect("home")


from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, datetime
from .models import Kid


def edit(request, id):
    kid = get_object_or_404(Kid, id=id)

    if request.method == "POST":
        birthdate_str = request.POST["birthdate"]
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

        kid.kid_name = request.POST["kid_name"]
        kid.father_name = request.POST["father_name"]
        kid.surename = request.POST["surename"]
        kid.standard = request.POST["standard"]
        kid.birthdate = birthdate
        kid.mobile_number = request.POST["mobile_number"]

        kid.save()
        return redirect("home")

    return render(request, "edit.html", {"kid": kid})


from django.utils import timezone


def take_attendance(request):
    kids = Kid.objects.all()
    today = timezone.now().date().isoformat()  # YYYY-MM-DD format
    return render(request, "take_attendance.html", {"kids": kids, "today": today})


from django.utils import timezone
from datetime import datetime

from django.db import transaction


def submit_attendance(request):
    if request.method == "POST":
        date_input = request.POST.get("date")

        try:
            date_today = datetime.strptime(date_input, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            date_today = timezone.now().date()

        try:
            with transaction.atomic():
                for kid in Kid.objects.all():
                    is_present = request.POST.get(str(kid.id)) == "on"
                    Attendance.objects.create(
                        kid=kid, date=date_today, is_present=is_present
                    )
        except Exception as e:
            print("Something went wrong:", e)

        return redirect("home")


def view_attendance(request):
    from django.db.models import Count, Q

    attendance_summary = (
        Attendance.objects.values("date")
        .annotate(total_present=Count("id", filter=Q(is_present=True)))
        .order_by("-date")
    )

    return render(
        request, "view_attendance.html", {"attendance_summary": attendance_summary}
    )


def attendance_by_date(request, date):
    records = Attendance.objects.filter(date=date, is_present=True).select_related(
        "kid"
    )
    return render(
        request, "day.html", {"date": date, "records": records}
    )
