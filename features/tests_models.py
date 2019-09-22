from django.test import TestCase
from django.db import IntegrityError
from features.models import *


class ClientTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name='ClientA')

    def test_name_max_length(self):
        name_max_length = self.client._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 64)

    def test_contact_max_length(self):
        max_length = self.client._meta.get_field('contact').max_length
        self.assertEqual(max_length, 64)

    def test_street_max_length(self):
        max_length = self.client._meta.get_field('street').max_length
        self.assertEqual(max_length, 255)

    def test_city_max_length(self):
        max_length = self.client._meta.get_field('city').max_length
        self.assertEqual(max_length, 64)

    def test_state_max_length(self):
        max_length = self.client._meta.get_field('state').max_length
        self.assertEqual(max_length, 64)

    def test_zip_max_length(self):
        max_length = self.client._meta.get_field('zip').max_length
        self.assertEqual(max_length, 24)

    def test_phone_max_length(self):
        max_length = self.client._meta.get_field('phone').max_length
        self.assertEqual(max_length, 11)


class ProjectTestCase(TestCase):
    def setUp(self):
        self.project = Project(name="ProjectA")

    def test_name_max_length(self):
        max_length = self.project._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)


class FeatureRequestsTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name='ClientA')
        self.project = Project.objects.create(name='ProjectA')
        self.request = FeatureRequest.objects.create(client=self.client,
                                                     project=self.project,
                                                     title='RequestA',
                                                     description='This is a request for A',
                                                     priority=1,
                                                     )

    def test_title_max_length(self):
        max_length = self.request._meta.get_field('title').max_length
        self.assertEqual(max_length, 48)

    def test_unique_priority_fails(self):
        request2 = FeatureRequest(title="RequestB", priority=1)
        request2.client = self.client
        request2.project = self.project
        request2.description = 'This is a request for B'
        with self.assertRaises(IntegrityError):
            request2.save()

    def test_unique_priority_passes_when_different(self):
        request2 = FeatureRequest(title="RequestB", priority=2)
        request2.client = self.client
        request2.project = self.project
        request2.description = 'This is a request for B'
        with self.assertRaises(AssertionError):
            with self.assertRaises(IntegrityError):
                request2.save()

    def test_unique_priority_passes_when_different_project(self):
        project2 = Project(name="ProjectB")
        project2.save()

        request2 = FeatureRequest(title="RequestB", priority=1)
        request2.client = self.client
        request2.project = project2
        request2.description = 'This is a request for B'

        with self.assertRaises(AssertionError):
            with self.assertRaises(IntegrityError):
                request2.save()
