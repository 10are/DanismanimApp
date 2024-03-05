from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import WorkDay, Appointment
from django.contrib.auth.models import User
import datetime
from counselor.models import ConsultantProfile
from django.urls import reverse
from rest_framework.test import APIClient

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.counselor = ConsultantProfile.objects.create(name='Test Counselor')
        self.work_day = WorkDay.objects.create(
            counselor=self.counselor,
            start_date='2024-03-05',
            end_date='2024-03-05',
            start_time='09:00',
            end_time='17:00',
            session_duration=60,
            break_duration=15
        )
        self.appointment = Appointment.objects.create(
            counselor=self.counselor,
            work_day='2024-03-05',
            start_time='09:00',
            end_time='10:00'
        )

    def test_work_day_list_view(self):
        url = reverse('workday-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_appointment_list_view(self):
        url = reverse('appointment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_counselor_appointment_view(self):
        url = reverse('counselorappointment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

